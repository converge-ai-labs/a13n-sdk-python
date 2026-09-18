"""Bounded conveniences over exact Service resource identities."""

from __future__ import annotations

import asyncio
import math
from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal, cast

from ._resources import Resource, Result
from .generated import models as wire
from .generated.api.agent_management import get_workspaces_workspace_agents_agent
from .generated.api.protocol_gateway import (
    get_queued_submissions_queued_submission_id,
    get_runs_run_id,
    post_runs_run_id_feedback,
    post_runs_run_id_fork,
    post_runs_run_id_interrupt,
    post_runs_run_id_retry,
    post_runs_run_id_steer,
    post_runs_source_run_id_continue,
    post_threads_thread_id_runs,
    post_workspaces_workspace_runs,
)
from .generated.types import UNSET, Unset

if TYPE_CHECKING:
    from collections.abc import Mapping

    from .client import Client
    from .generated.resources import QueuedSubmission, Run, Session, Thread
    from .streaming import RunStream

SEALED_STATUSES = frozenset({"completed", "failed", "cancelled", "waiting"})


def text_input(text: str) -> wire.AgentInput:
    """Build the ordinary version-2 text input without changing structured input semantics."""
    return wire.AgentInput(
        schema_version=wire.AgentInputSchemaVersion.VALUE_1,
        content=[wire.TextContent(text=text, type_="text")],
    )


def _normalize_input(value: str | wire.AgentInput) -> wire.AgentInput:
    if isinstance(value, str):
        return text_input(value)
    if isinstance(value, wire.AgentInput):
        return value
    raise ValueError("input must be a string or AgentInput")


@dataclass(frozen=True, repr=False)
class RunAccepted[ReceiptT]:
    outcome: Literal["run_accepted"]
    run: Run
    thread: Thread
    session: Session
    receipt: Result[ReceiptT]


@dataclass(frozen=True, repr=False)
class SubmissionQueued:
    outcome: Literal["queued"]
    queued_submission: QueuedSubmission
    thread: Thread
    receipt: Result[wire.ThreadRunSubmissionReceipt]


type ThreadSubmission = RunAccepted[wire.ThreadRunSubmissionReceipt] | SubmissionQueued


def _accepted[ReceiptT](
    client: Client, receipt: Result[ReceiptT], value: wire.RunAcceptanceReceipt, *, source_run_id: str | None = None
) -> RunAccepted[ReceiptT]:
    from .client import ProtocolError
    from .generated.resources import Run, Session, Thread

    if not all(
        isinstance(identifier, str) and identifier for identifier in (value.run_id, value.thread_id, value.session_id)
    ):
        raise ProtocolError("Run acceptance has incomplete resource identities")
    if value.run_id == source_run_id:
        raise ProtocolError("Successor acceptance must identify a new Run")
    return RunAccepted(
        "run_accepted",
        Run(client, {"run_id": value.run_id}),
        Thread(client, {"thread_id": value.thread_id}),
        Session(client, {"session_id": value.session_id}),
        receipt,
    )


def _validate_wait(timeout: float, poll_interval: float) -> None:
    if not math.isfinite(timeout) or timeout <= 0:
        raise ValueError("timeout must be a finite positive number")
    if not math.isfinite(poll_interval) or poll_interval <= 0:
        raise ValueError("poll_interval must be a finite positive number")


class AgentMethods(Resource):
    async def start(
        self,
        input: str | wire.AgentInput,
        *,
        idempotency_key: str,
        agent_revision_id: str | Unset | None = UNSET,
        expected_default_revision_id: str | Unset | None = UNSET,
        config_override: wire.AgentRunOverrideInput | Unset | None = UNSET,
        environment: wire.ExistingEnvironmentSelection | wire.NewEnvironmentSelection | Unset | None = UNSET,
        hook_subscription: wire.InlineHookSubscriptionInput | Unset | None = UNSET,
        labels: wire.StartRunRequestLabels | Unset = UNSET,
        session_id: str | Unset | None = UNSET,
        session_labels: wire.StartRunRequestSessionLabels | Unset = UNSET,
        thread_labels: wire.StartRunRequestThreadLabels | Unset = UNSET,
    ) -> RunAccepted[wire.RunAcceptanceReceipt]:
        input = _normalize_input(input)
        agent = await self._call(
            lambda client: get_workspaces_workspace_agents_agent.asyncio_detailed(
                workspace=self._bindings["workspace"], agent=self._bindings["agent"], client=client
            )
        )
        body = wire.StartRunRequest(
            agent_id=agent.value.id,
            input_=input,
            agent_revision_id=agent_revision_id,
            expected_default_revision_id=expected_default_revision_id,
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
        return _accepted(self._client, receipt, receipt.value)


class ThreadMethods(Resource):
    async def submit(
        self,
        input: str | wire.AgentInput,
        *,
        expected_thread_version: int,
        idempotency_key: str,
        agent_id: str | Unset | None = UNSET,
        agent_revision_id: str | Unset | None = UNSET,
        expected_default_revision_id: str | Unset | None = UNSET,
        config_override: wire.AgentRunOverrideInput | Unset | None = UNSET,
        environment: wire.ExistingEnvironmentSelection | wire.NewEnvironmentSelection | Unset | None = UNSET,
        hook_subscription: wire.InlineHookSubscriptionInput | Unset | None = UNSET,
        labels: wire.ThreadRunSubmissionRequestLabels | Unset = UNSET,
        waiting_resolution: Unset | wire.WaitingResolutionDefaults | None = UNSET,
    ) -> ThreadSubmission:
        from .client import ProtocolError
        from .generated.resources import QueuedSubmission, Thread

        body = wire.ThreadRunSubmissionRequest(
            expected_thread_version=expected_thread_version,
            input_=_normalize_input(input),
            agent_id=agent_id,
            agent_revision_id=agent_revision_id,
            expected_default_revision_id=expected_default_revision_id,
            config_override=config_override,
            environment=environment,
            hook_subscription=hook_subscription,
            labels=labels,
            waiting_resolution=waiting_resolution,
        )
        receipt = await self._call(
            lambda client: post_threads_thread_id_runs.asyncio_detailed(
                thread_id=self.id, client=client, body=body, idempotency_key=idempotency_key
            )
        )
        value = receipt.value
        if (
            value.outcome == wire.ThreadRunSubmissionReceiptOutcome.RUN_ACCEPTED
            and isinstance(value.run, wire.RunAcceptanceReceipt)
            and (value.queued_submission is None or isinstance(value.queued_submission, Unset))
        ):
            if value.run.thread_id != self.id:
                raise ProtocolError("Accepted Run does not belong to the bound Thread")
            return _accepted(self._client, receipt, value.run)
        if (
            value.outcome == wire.ThreadRunSubmissionReceiptOutcome.QUEUED
            and isinstance(value.queued_submission, wire.QueuedSubmission)
            and (value.run is None or isinstance(value.run, Unset))
        ):
            if value.queued_submission.thread_id != self.id:
                raise ProtocolError("Queued submission does not belong to the bound Thread")
            if (
                not isinstance(value.queued_submission.queued_submission_id, str)
                or not value.queued_submission.queued_submission_id
            ):
                raise ProtocolError("Queued submission has no resource identity")
            return SubmissionQueued(
                "queued",
                QueuedSubmission(self._client, {"queued_submission_id": value.queued_submission.queued_submission_id}),
                Thread(self._client, {"thread_id": value.queued_submission.thread_id}),
                receipt,
            )
        raise ProtocolError("Thread submission has no matching resource disposition")


class RunMethods(Resource):
    def __init__(self, client: Client, bindings: Mapping[str, str] | None = None) -> None:
        super().__init__(client, bindings)

    async def wait(self, *, timeout: float, poll_interval: float) -> Result[wire.RunResource]:
        _validate_wait(timeout, poll_interval)
        async with asyncio.timeout(timeout):
            while True:
                result = await self._call(
                    lambda client: get_runs_run_id.asyncio_detailed(run_id=self.id, client=client)
                )
                if result.value.status in SEALED_STATUSES:
                    return result
                await asyncio.sleep(poll_interval)

    async def steer(self, input: str | wire.AgentInput, *, idempotency_key: str) -> Result[wire.SteerReceipt]:
        body = _normalize_input(input)
        return await self._call(
            lambda client: post_runs_run_id_steer.asyncio_detailed(
                run_id=self.id, client=client, body=body, idempotency_key=idempotency_key
            )
        )

    async def cancel(
        self,
        *,
        expected_run_version: int,
        expected_thread_version: int,
        idempotency_key: str,
    ) -> Result[wire.InterruptReceipt]:
        body = wire.InterruptRequest(
            expected_run_version=expected_run_version,
            expected_thread_version=expected_thread_version,
        )
        return await self._call(
            lambda client: post_runs_run_id_interrupt.asyncio_detailed(
                run_id=self.id, client=client, body=body, idempotency_key=idempotency_key
            )
        )

    async def feedback(
        self, body: wire.WaitingRunFeedbackRequest, *, idempotency_key: str
    ) -> RunAccepted[wire.RunAcceptanceReceipt]:
        receipt = await self._call(
            lambda client: post_runs_run_id_feedback.asyncio_detailed(
                run_id=self.id, client=client, body=body, idempotency_key=idempotency_key
            )
        )
        return _accepted(self._client, receipt, receipt.value, source_run_id=self.id)

    async def retry(
        self, body: wire.RetryRunRequest, *, idempotency_key: str
    ) -> RunAccepted[wire.RunAcceptanceReceipt]:
        receipt = await self._call(
            lambda client: post_runs_run_id_retry.asyncio_detailed(
                run_id=self.id, client=client, body=body, idempotency_key=idempotency_key
            )
        )
        return _accepted(self._client, receipt, receipt.value, source_run_id=self.id)

    async def continue_from(
        self, body: wire.ContinueRunRequest, *, idempotency_key: str
    ) -> RunAccepted[wire.RunAcceptanceReceipt]:
        receipt = await self._call(
            lambda client: post_runs_source_run_id_continue.asyncio_detailed(
                source_run_id=self.id, client=client, body=body, idempotency_key=idempotency_key
            )
        )
        return _accepted(self._client, receipt, receipt.value, source_run_id=self.id)

    async def fork(self, body: wire.ForkRunRequest, *, idempotency_key: str) -> RunAccepted[wire.RunAcceptanceReceipt]:
        receipt = await self._call(
            lambda client: post_runs_run_id_fork.asyncio_detailed(
                run_id=self.id, client=client, body=body, idempotency_key=idempotency_key
            )
        )
        return _accepted(self._client, receipt, receipt.value, source_run_id=self.id)

    def stream(
        self,
        *,
        after: str | None = None,
        reconnect: bool = True,
        max_reconnects: int = 5,
        max_event_bytes: int = 1_048_576,
    ) -> RunStream:
        from .streaming import RunStream

        return RunStream(
            cast("Run", self),
            after=after,
            reconnect=reconnect,
            max_reconnects=max_reconnects,
            max_event_bytes=max_event_bytes,
        )


class QueueMethods(Resource):
    async def wait(self, *, timeout: float, poll_interval: float) -> Result[wire.QueuedSubmission]:
        _validate_wait(timeout, poll_interval)
        async with asyncio.timeout(timeout):
            while True:
                snapshot = await self._call(
                    lambda client: get_queued_submissions_queued_submission_id.asyncio_detailed(
                        queued_submission_id=self.id, client=client
                    )
                )
                if snapshot.value.state in {
                    wire.QueuedSubmissionState.CONSUMED,
                    wire.QueuedSubmissionState.FAILED,
                }:
                    return snapshot
                await asyncio.sleep(poll_interval)
