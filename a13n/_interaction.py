"""Bounded conveniences over exact Service resource identities."""

from __future__ import annotations

import asyncio
from contextlib import AbstractAsyncContextManager
from dataclasses import dataclass
from typing import TYPE_CHECKING

from ._resources import Resource, Result
from .generated import models as wire
from .generated.api.agent_management import get_workspaces_workspace_agents_agent
from .generated.api.protocol_gateway import (
    get_queued_submissions_queued_submission_id,
    get_runs_run_id,
    post_runs_run_id_feedback,
    post_runs_run_id_fork,
    post_runs_run_id_retry,
    post_runs_source_run_id_continue,
    post_threads_thread_id_runs,
    post_workspaces_workspace_runs,
)
from .generated.types import UNSET, Unset

if TYPE_CHECKING:
    from collections.abc import AsyncIterator, Mapping

    from .client import Client
    from .generated.resources import QueuedSubmission, Run
    from .streaming import StreamObservation


SEALED_STATUSES = frozenset({"completed", "failed", "cancelled", "waiting"})


def text_input(text: str) -> wire.AgentInput:
    """Ordinary version-2 text input; structured content remains independent."""
    return wire.AgentInput(
        schema_version=wire.AgentInputSchemaVersion.VALUE_1,
        content=[wire.TextContent(text=text, type_="text")],
    )


def accepted_run(client: Client, receipt: Result[wire.RunAcceptanceReceipt]) -> Run:
    from .generated.resources import Run

    return Run(client, {"run_id": receipt.value.run_id}, acceptance=receipt)


@dataclass(frozen=True, repr=False)
class Submission:
    """Actual Thread submission disposition, not a new durable SDK resource."""

    receipt: Result[wire.ThreadRunSubmissionReceipt]
    resource: Run | QueuedSubmission


@dataclass(frozen=True, repr=False)
class QueueDisposition:
    snapshot: Result[wire.QueuedSubmission]
    run: Run | None


class AgentMethods(Resource):
    async def start(
        self,
        input: str | wire.AgentInput,
        *,
        idempotency_key: str,
        agent_revision_id: str | Unset | None = UNSET,
        expected_current_revision_id: str | Unset | None = UNSET,
        config_override: wire.AgentRunOverrideInput | Unset | None = UNSET,
        environment: wire.ExistingEnvironmentSelection | wire.NewEnvironmentSelection | Unset | None = UNSET,
        hook_subscription: wire.InlineHookSubscriptionInput | Unset | None = UNSET,
        labels: wire.StartRunRequestLabels | Unset = UNSET,
        session_id: str | Unset | None = UNSET,
        session_labels: wire.StartRunRequestSessionLabels | Unset = UNSET,
        thread_labels: wire.StartRunRequestThreadLabels | Unset = UNSET,
    ) -> Run:
        """Resolve this Agent selector, then start a root Thread and Run.

        Two requests: explicit Agent lookup and one non-replayed submission.
        Revision resolution and concurrency preconditions remain Service-owned.
        """
        agent = await self._call(
            lambda client: get_workspaces_workspace_agents_agent.asyncio_detailed(
                workspace=self._bindings["workspace"], agent=self._bindings["agent"], client=client
            )
        )
        body = wire.StartRunRequest(
            agent_id=agent.value.id,
            input_=text_input(input) if isinstance(input, str) else input,
            agent_revision_id=agent_revision_id,
            expected_current_revision_id=expected_current_revision_id,
            config_override=config_override,
            environment=environment,
            hook_subscription=hook_subscription,
            labels=labels,
            session_id=session_id,
            session_labels=session_labels,
            thread_labels=thread_labels,
        )
        receipt = await self._call(
            lambda client: post_workspaces_workspace_runs.asyncio_detailed(
                workspace=self._bindings["workspace"], client=client, body=body, idempotency_key=idempotency_key
            )
        )
        return accepted_run(self._client, receipt)


class ThreadMethods(Resource):
    async def submit(self, body: wire.ThreadRunSubmissionRequest, *, idempotency_key: str) -> Submission:
        """Submit once; preserve the accepted Run OR queued intent and queue version."""
        from .client import ProtocolError
        from .generated.resources import QueuedSubmission

        receipt = await self._call(
            lambda client: post_threads_thread_id_runs.asyncio_detailed(
                thread_id=self.id, client=client, body=body, idempotency_key=idempotency_key
            )
        )
        value = receipt.value
        if value.outcome == wire.ThreadRunSubmissionReceiptOutcome.RUN_ACCEPTED and isinstance(
            value.run, wire.RunAcceptanceReceipt
        ):
            evidence = Result(value.run, receipt.status, receipt.headers, receipt.content)
            return Submission(receipt, accepted_run(self._client, evidence))
        if value.outcome == wire.ThreadRunSubmissionReceiptOutcome.QUEUED and isinstance(
            value.queued_submission, wire.QueuedSubmission
        ):
            return Submission(
                receipt,
                QueuedSubmission(self._client, {"queued_submission_id": value.queued_submission.queued_submission_id}),
            )
        raise ProtocolError("Thread submission has no matching resource receipt")


class RunMethods(Resource):
    def __init__(
        self,
        client: Client,
        bindings: Mapping[str, str] | None = None,
        *,
        acceptance: Result[wire.RunAcceptanceReceipt] | None = None,
    ) -> None:
        super().__init__(client, bindings)
        self._acceptance = acceptance

    @property
    def acceptance(self) -> Result[wire.RunAcceptanceReceipt] | None:
        """Original acceptance evidence, if this handle came from a submission."""
        return self._acceptance

    async def wait(self, *, timeout: float = 300, poll_interval: float = 0.5) -> Result[wire.RunResource]:
        """Observe only this Run until sealed. Timeout/cancellation is local only."""
        if timeout <= 0 or poll_interval <= 0:
            raise ValueError("timeout and poll_interval must be positive")
        async with asyncio.timeout(timeout):
            while True:
                result = await self._call(
                    lambda client: get_runs_run_id.asyncio_detailed(run_id=self.id, client=client)
                )
                if result.value.status in SEALED_STATUSES:
                    return result
                await asyncio.sleep(poll_interval)

    async def feedback(self, body: wire.WaitingRunFeedbackRequest, *, idempotency_key: str) -> Run:
        """Explicitly resolve the complete pending set; return the successor Run."""
        receipt = await self._call(
            lambda client: post_runs_run_id_feedback.asyncio_detailed(
                run_id=self.id, client=client, body=body, idempotency_key=idempotency_key
            )
        )
        return accepted_run(self._client, receipt)

    async def retry(self, body: wire.RetryRunRequest, *, idempotency_key: str) -> Run:
        """Request a new Run; this is not RunAttempt recovery."""
        receipt = await self._call(
            lambda client: post_runs_run_id_retry.asyncio_detailed(
                run_id=self.id, client=client, body=body, idempotency_key=idempotency_key
            )
        )
        return accepted_run(self._client, receipt)

    async def fork(self, body: wire.ForkRunRequest, *, idempotency_key: str) -> Run:
        """Create a child Thread and its Run in the existing Session."""
        receipt = await self._call(
            lambda client: post_runs_run_id_fork.asyncio_detailed(
                run_id=self.id, client=client, body=body, idempotency_key=idempotency_key
            )
        )
        return accepted_run(self._client, receipt)

    async def continue_(self, body: wire.ContinueRunRequest, *, idempotency_key: str) -> Run:
        """Continue from this exact historical source, not the latest observed Run."""
        receipt = await self._call(
            lambda client: post_runs_source_run_id_continue.asyncio_detailed(
                source_run_id=self.id, client=client, body=body, idempotency_key=idempotency_key
            )
        )
        return accepted_run(self._client, receipt)

    def stream(
        self, *, after: str | None = None, max_event_bytes: int = 1_048_576
    ) -> AbstractAsyncContextManager[AsyncIterator[StreamObservation]]:
        """Attach once after a caller-applied cursor; never advance a checkpoint."""
        from .streaming import run_stream

        return run_stream(self._client, self.id, after=after, max_event_bytes=max_event_bytes)


class QueueMethods(Resource):
    async def wait(self, *, timeout: float = 300, poll_interval: float = 0.5) -> QueueDisposition:
        """Observe disposition without consuming input. Withdrawal surfaces as 404."""
        from .client import ProtocolError
        from .generated.resources import Run

        if timeout <= 0 or poll_interval <= 0:
            raise ValueError("timeout and poll_interval must be positive")
        async with asyncio.timeout(timeout):
            while True:
                snapshot = await self._call(
                    lambda client: get_queued_submissions_queued_submission_id.asyncio_detailed(
                        queued_submission_id=self.id, client=client
                    )
                )
                value = snapshot.value
                if value.state == wire.QueuedSubmissionState.CONSUMED:
                    if not isinstance(value.consumed_run_id, str) or not value.consumed_run_id:
                        raise ProtocolError("Consumed queue entry has no Run identity")
                    return QueueDisposition(snapshot, Run(self._client, {"run_id": value.consumed_run_id}))
                if value.state == wire.QueuedSubmissionState.FAILED:
                    return QueueDisposition(snapshot, None)
                await asyncio.sleep(poll_interval)
