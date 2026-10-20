"""Generated typed Native resource navigation. Do not edit; run make generate."""

from __future__ import annotations

import datetime
from collections.abc import AsyncIterator
from contextlib import AbstractAsyncContextManager
from typing import Any, Literal

import httpx2

from .._resources import Resource, Result, pages
from . import models as wire
from .api.agents import (
    archive_agent,
    compare_agent_revisions,
    create_agent,
    create_agent_revision,
    define_toolsets,
    delete_agent_avatar,
    duplicate_agent,
    get_agent,
    get_agent_avatar,
    get_agent_revision,
    index_toolsets,
    list_agent_revisions,
    list_agents,
    list_toolsets,
    prepare_composer,
    put_agent_avatar,
    set_default_agent_revision,
    unarchive_agent,
    update_agent,
    validate_agent,
)
from .api.assets import create_asset, create_upload, get_asset, list_assets, read_asset_content, retire_asset
from .api.auth import (
    accept,
    auth_configuration,
    bootstrap_administrator,
    change_password,
    confirm_email_change,
    confirm_password_reset,
    create_user_key,
    delete_user_avatar,
    disable_account,
    get_profile,
    get_user_avatar,
    list_account_audit_events,
    list_login_sessions,
    list_user_keys,
    logout,
    password_login,
    put_user_avatar,
    request_password_reset,
    revoke_login_session,
    revoke_user_key,
    session_profile,
    update_profile,
)
from .api.connections import (
    authorize_connection,
    complete_authorization,
    create_connection,
    define_connection_tools,
    define_connector_actions,
    get_connection,
    get_connector_app,
    get_redirect_uri,
    index_connection_tools,
    index_connector_actions,
    list_connection_tools,
    list_connections,
    list_connector_actions,
    list_connector_apps,
    list_mcp_servers,
    revoke_connection,
    test_connection,
    update_connection,
)
from .api.default import health, ready
from .api.desktop_assistance import (
    complete_assistance,
    control_desktop,
    disconnect_desktop,
    get_assistance,
    get_control,
    open_control,
    request_control,
    view_desktop,
)
from .api.environments import (
    add_environment_mount,
    check_computer,
    create_environment,
    create_environment_template,
    delete_environment,
    get_environment,
    get_environment_template,
    list_environment_mounts,
    list_environment_templates,
    list_environments,
    remove_environment_mount,
    stop_environment,
    update_environment,
    update_environment_mount,
    update_environment_template,
)
from .api.findings import (
    create_finding,
    get_finding,
    list_finding_analyses,
    list_findings,
    prepare_finding_agent,
    start_analysis,
    update_finding,
)
from .api.memories import (
    add_memory_mount,
    add_record,
    create_file,
    create_memory,
    delete_file,
    delete_memory,
    delete_record,
    get_memory,
    get_memory_revision,
    list_files,
    list_memories,
    list_memory_mounts,
    list_memory_revisions,
    list_records,
    move_file,
    purge_history,
    read_file,
    remove_memory_mount,
    replace_file,
    restore_memory_revision,
    search_records,
    update_memory,
    update_memory_mount,
    update_record,
)
from .api.memory_spaces import (
    create_space,
    delete_space,
    get_space,
    get_space_organization,
    list_space_organizations,
    list_space_sessions,
    list_spaces,
    organize_space,
    update_space,
)
from .api.models import (
    create_model,
    get_media_defaults,
    get_model,
    get_model_catalog,
    list_models,
    replace_media_defaults,
    update_model,
)
from .api.providers import (
    authorize_model,
    complete_model_authorization,
    create_connector_provider,
    create_environment_provider,
    create_memory_provider,
    create_model_provider,
    create_web_provider,
    delete_environment_provider,
    disconnect_model_authorization,
    discover_model_provider_models,
    environment_provider_references,
    get_connector_provider,
    get_environment_provider,
    get_memory_provider,
    get_model_provider,
    get_web_provider,
    list_connector_providers,
    list_environment_providers,
    list_memory_providers,
    list_model_providers,
    list_provider_types,
    list_web_providers,
    model_authorization,
    test_connector_provider,
    test_environment_provider,
    test_memory_provider,
    test_model_provider,
    test_web_provider,
    update_connector_provider,
    update_environment_provider,
    update_memory_provider,
    update_model_provider,
    update_web_provider,
)
from .api.runs import (
    archive_thread,
    create_session,
    create_thread,
    edit_entry,
    fork_run,
    get_inbox_entry,
    get_message_authors,
    get_run,
    get_run_agent,
    get_run_attempt,
    get_run_content,
    get_run_lineage,
    get_session,
    get_thread,
    get_trace,
    get_trace_backend,
    interrupt_run,
    list_attempt_spans,
    list_inbox,
    list_run_attempts,
    list_run_items,
    list_runs,
    list_sessions,
    list_thread_runs,
    list_threads,
    list_trace_spans,
    list_traces,
    read_run_item_content,
    read_span_content,
    reorder_inbox,
    resume_run,
    run_image,
    session_stream,
    submit_message,
    thread_stream,
    update_run,
    update_session,
    update_thread,
    withdraw_entry,
)
from .api.schedules import (
    archive_schedule,
    create_schedule,
    dispatch_schedule,
    enable_schedule,
    get_schedule,
    get_schedule_occurrence,
    get_schedule_status,
    list_schedule_occurrences,
    list_schedules,
    pause_schedule,
    preview_schedule,
    update_schedule,
)
from .api.skills import (
    archive_skill,
    create_skill,
    create_skill_revision,
    get_skill,
    get_skill_revision,
    list_skill_revisions,
    list_skills,
    read_skill_archive,
    read_skill_file,
    set_default_skill_revision,
    unarchive_skill,
    update_skill,
    validate_skill,
)
from .api.subscriptions import (
    create_subscription,
    delete_subscription,
    get_subscription,
    list_deliveries,
    list_subscriptions,
    redeliver,
    update_subscription,
)
from .api.tenancy import (
    archive_workspace,
    change_organization_grant,
    change_workspace_grant,
    create_organization_grant,
    create_organization_invitation,
    create_service_account,
    create_service_account_key,
    create_workspace,
    create_workspace_grant,
    create_workspace_invitation,
    delete_organization_grant,
    delete_organization_icon,
    delete_service_account,
    delete_workspace_grant,
    delete_workspace_icon,
    get_organization,
    get_organization_icon,
    get_service_account,
    get_workspace,
    get_workspace_icon,
    list_members,
    list_organization_audit_events,
    list_organization_grants,
    list_organization_invitations,
    list_organization_workspaces,
    list_organizations,
    list_service_account_keys,
    list_service_accounts,
    list_workspace_audit_events,
    list_workspace_grants,
    list_workspace_invitations,
    list_workspace_keys,
    list_workspaces,
    put_organization_icon,
    put_workspace_icon,
    resend_organization_invitation,
    resend_workspace_invitation,
    revoke_organization_invitation,
    revoke_workspace_invitation,
    revoke_workspace_key,
    update_organization,
    update_service_account,
    update_workspace,
)
from .api.usage import context_usage, model_request_metrics, summarize_usage, usage_agents, usage_models, usage_overview
from .types import UNSET, File, Unset


class ServiceResources(Resource):
    """Bound Native resource: /api/v1."""

    async def agent_composer(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.Agent]:
        """Prepare Composer. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: prepare_composer.asyncio_detailed(client=client, x_workspace_id=x_workspace_id)
        )

    @property
    def agents(self) -> Agents:
        return Agents(self._client, self._bindings)

    @property
    def assets(self) -> Assets:
        return Assets(self._client, self._bindings)

    @property
    def auth(self) -> Auth:
        return Auth(self._client, self._bindings)

    @property
    def connections(self) -> Connections:
        return Connections(self._client, self._bindings)

    @property
    def connector_providers(self) -> ConnectorProviders:
        return ConnectorProviders(self._client, self._bindings)

    @property
    def desktop_assistance(self) -> DesktopAssistance:
        return DesktopAssistance(self._client, self._bindings)

    @property
    def environment_providers(self) -> EnvironmentProviders:
        return EnvironmentProviders(self._client, self._bindings)

    @property
    def environment_templates(self) -> EnvironmentTemplates:
        return EnvironmentTemplates(self._client, self._bindings)

    @property
    def environments(self) -> Environments:
        return Environments(self._client, self._bindings)

    async def finding_agent(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.Agent]:
        """Prepare Finding Agent. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: prepare_finding_agent.asyncio_detailed(client=client, x_workspace_id=x_workspace_id)
        )

    @property
    def finding_analyses(self) -> FindingAnalyses:
        return FindingAnalyses(self._client, self._bindings)

    @property
    def findings(self) -> Findings:
        return Findings(self._client, self._bindings)

    @property
    def invitations(self) -> Invitations:
        return Invitations(self._client, self._bindings)

    @property
    def mcp_servers(self) -> McpServers:
        return McpServers(self._client, self._bindings)

    @property
    def media_understanding_defaults(self) -> MediaUnderstandingDefaults:
        return MediaUnderstandingDefaults(self._client, self._bindings)

    @property
    def memories(self) -> Memories:
        return Memories(self._client, self._bindings)

    @property
    def memory_providers(self) -> MemoryProviders:
        return MemoryProviders(self._client, self._bindings)

    @property
    def memory_spaces(self) -> MemorySpaces:
        return MemorySpaces(self._client, self._bindings)

    @property
    def model_catalog(self) -> ModelCatalog:
        return ModelCatalog(self._client, self._bindings)

    @property
    def model_providers(self) -> ModelProviders:
        return ModelProviders(self._client, self._bindings)

    @property
    def models(self) -> Models:
        return Models(self._client, self._bindings)

    @property
    def organizations(self) -> Organizations:
        return Organizations(self._client, self._bindings)

    @property
    def provider_types(self) -> ProviderTypes:
        return ProviderTypes(self._client, self._bindings)

    @property
    def runs(self) -> Runs:
        return Runs(self._client, self._bindings)

    @property
    def schedules(self) -> Schedules:
        return Schedules(self._client, self._bindings)

    @property
    def sessions(self) -> Sessions:
        return Sessions(self._client, self._bindings)

    @property
    def skills(self) -> Skills:
        return Skills(self._client, self._bindings)

    @property
    def subscriptions(self) -> Subscriptions:
        return Subscriptions(self._client, self._bindings)

    @property
    def threads(self) -> Threads:
        return Threads(self._client, self._bindings)

    @property
    def toolsets(self) -> Toolsets:
        return Toolsets(self._client, self._bindings)

    @property
    def trace_backend(self) -> TraceBackend:
        return TraceBackend(self._client, self._bindings)

    @property
    def traces(self) -> Traces:
        return Traces(self._client, self._bindings)

    @property
    def uploads(self) -> Uploads:
        return Uploads(self._client, self._bindings)

    @property
    def usage(self) -> Usage:
        return Usage(self._client, self._bindings)

    @property
    def users(self) -> Users:
        return Users(self._client, self._bindings)

    @property
    def web_providers(self) -> WebProviders:
        return WebProviders(self._client, self._bindings)

    @property
    def workspaces(self) -> Workspaces:
        return Workspaces(self._client, self._bindings)

    @property
    def healthz(self) -> Healthz:
        return Healthz(self._client, self._bindings)

    @property
    def readyz(self) -> Readyz:
        return Readyz(self._client, self._bindings)


class Agents(Resource):
    """Bound Native resource: /agents."""

    async def list(
        self,
        *,
        label: list[str] | Unset | None = UNSET,
        q: str | Unset | None = UNSET,
        archived: bool | Unset | None = UNSET,
        source: wire.AgentSource | Unset | None = UNSET,
        preset_kind: wire.PresetKind | Unset | None = UNSET,
        skill_id: str | Unset | None = UNSET,
        skill_revision_id: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.AgentPage]:
        """List Agents. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_agents.asyncio_detailed(
                client=client,
                label=label,
                q=q,
                archived=archived,
                source=source,
                preset_kind=preset_kind,
                skill_id=skill_id,
                skill_revision_id=skill_revision_id,
                limit=limit,
                cursor=cursor,
                x_workspace_id=x_workspace_id,
            )
        )

    def pages(
        self,
        *,
        label: list[str] | Unset | None = UNSET,
        q: str | Unset | None = UNSET,
        archived: bool | Unset | None = UNSET,
        source: wire.AgentSource | Unset | None = UNSET,
        preset_kind: wire.PresetKind | Unset | None = UNSET,
        skill_id: str | Unset | None = UNSET,
        skill_revision_id: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.AgentPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        label = label.copy() if isinstance(label, list) else label
        return pages(
            lambda next_cursor: self.list(
                label=label,
                q=q,
                archived=archived,
                source=source,
                preset_kind=preset_kind,
                skill_id=skill_id,
                skill_revision_id=skill_revision_id,
                limit=limit,
                x_workspace_id=x_workspace_id,
                cursor=next_cursor,
            ),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        label: list[str] | Unset | None = UNSET,
        q: str | Unset | None = UNSET,
        archived: bool | Unset | None = UNSET,
        source: wire.AgentSource | Unset | None = UNSET,
        preset_kind: wire.PresetKind | Unset | None = UNSET,
        skill_id: str | Unset | None = UNSET,
        skill_revision_id: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.Agent]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(
                label=label,
                q=q,
                archived=archived,
                source=source,
                preset_kind=preset_kind,
                skill_id=skill_id,
                skill_revision_id=skill_revision_id,
                limit=limit,
                cursor=cursor,
                x_workspace_id=x_workspace_id,
            )
            for item in page.value.items
        )

    async def create(self, *, body: wire.AgentCreate, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.Agent]:
        """Create Agent. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_agent.asyncio_detailed(client=client, body=body, x_workspace_id=x_workspace_id)
        )

    async def validate(self, *, body: wire.AgentValidate, x_workspace_id: str | Unset | None = UNSET) -> Result[None]:
        """Validate Agent. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: validate_agent.asyncio_detailed(client=client, body=body, x_workspace_id=x_workspace_id)
        )

    def __call__(self, agent_id: str) -> Agent:
        return Agent(self._client, self._bind("agent_id", agent_id))


class Agent(Resource):
    """Bound Native resource: /agents / {agent_id}."""

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.Agent]:
        """Get Agent. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_agent.asyncio_detailed(
                client=client, agent_id=self._bindings["agent_id"], x_workspace_id=x_workspace_id
            )
        )

    async def update(
        self,
        *,
        body: wire.AgentUpdate,
        if_match: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.Agent]:
        """Update Agent. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_agent.asyncio_detailed(
                client=client,
                agent_id=self._bindings["agent_id"],
                body=body,
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )

    async def archive(
        self, *, if_match: str | Unset | None = UNSET, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.Agent]:
        """Archive Agent. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: archive_agent.asyncio_detailed(
                client=client, agent_id=self._bindings["agent_id"], if_match=if_match, x_workspace_id=x_workspace_id
            )
        )

    @property
    def avatar(self) -> AgentsAgentIdAvatar:
        return AgentsAgentIdAvatar(self._client, self._bindings)

    async def duplicate(
        self, *, body: wire.AgentDuplicate, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.Agent]:
        """Duplicate Agent. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: duplicate_agent.asyncio_detailed(
                client=client, agent_id=self._bindings["agent_id"], body=body, x_workspace_id=x_workspace_id
            )
        )

    @property
    def revisions(self) -> AgentsAgentIdRevisions:
        return AgentsAgentIdRevisions(self._client, self._bindings)

    async def unarchive(
        self, *, if_match: str | Unset | None = UNSET, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.Agent]:
        """Unarchive Agent. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: unarchive_agent.asyncio_detailed(
                client=client, agent_id=self._bindings["agent_id"], if_match=if_match, x_workspace_id=x_workspace_id
            )
        )


class AgentsAgentIdAvatar(Resource):
    """Bound Native resource: /agents / {agent_id} / avatar."""

    async def delete(
        self, *, if_match: str | Unset | None = UNSET, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.Agent]:
        """Delete Agent Avatar. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_agent_avatar.asyncio_detailed(
                client=client, agent_id=self._bindings["agent_id"], if_match=if_match, x_workspace_id=x_workspace_id
            )
        )

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[File]:
        """Get Agent Avatar. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_agent_avatar.asyncio_detailed(
                client=client, agent_id=self._bindings["agent_id"], x_workspace_id=x_workspace_id
            )
        )

    def get_stream(self, *, x_workspace_id: str | Unset | None = UNSET) -> AbstractAsyncContextManager[httpx2.Response]:
        """Unbuffered response; caller checks status and consumes within the context."""
        return self._stream(
            get_agent_avatar.build_request(agent_id=self._bindings["agent_id"], x_workspace_id=x_workspace_id)
        )

    async def replace(
        self, *, body: File, if_match: str | Unset | None = UNSET, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.Agent]:
        """Put Agent Avatar. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: put_agent_avatar.asyncio_detailed(
                client=client,
                agent_id=self._bindings["agent_id"],
                body=body,
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )


class AgentsAgentIdRevisions(Resource):
    """Bound Native resource: /agents / {agent_id} / revisions."""

    async def list(
        self,
        *,
        view: wire.ReadView | Unset = UNSET,
        limit: int | Unset | None = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.AgentRevisionPage | wire.RevisionSummaryPage]:
        """List Agent Revisions. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_agent_revisions.asyncio_detailed(
                client=client,
                agent_id=self._bindings["agent_id"],
                view=view,
                limit=limit,
                cursor=cursor,
                x_workspace_id=x_workspace_id,
            )
        )

    async def create(
        self,
        *,
        body: wire.AgentRevisionCreate,
        if_match: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.AgentRevision]:
        """Create Agent Revision. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_agent_revision.asyncio_detailed(
                client=client,
                agent_id=self._bindings["agent_id"],
                body=body,
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )

    def __call__(self, revision_id: str) -> AgentsAgentIdRevisionsRevisionId:
        return AgentsAgentIdRevisionsRevisionId(self._client, self._bind("revision_id", revision_id))


class AgentsAgentIdRevisionsRevisionId(Resource):
    """Bound Native resource: /agents / {agent_id} / revisions / {revision_id}."""

    async def get(
        self,
        *,
        view: wire.ReadView | Unset = UNSET,
        section: wire.ConfigSection | Unset | None = UNSET,
        offset: int | Unset = UNSET,
        limit: int | Unset = UNSET,
        version: str | Unset | None = UNSET,
        query: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.AgentRevision | wire.RevisionSummary | wire.TextRead]:
        """Get Agent Revision. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_agent_revision.asyncio_detailed(
                client=client,
                agent_id=self._bindings["agent_id"],
                revision_id=self._bindings["revision_id"],
                view=view,
                section=section,
                offset=offset,
                limit=limit,
                version=version,
                query=query,
                x_workspace_id=x_workspace_id,
            )
        )

    @property
    def compare(self) -> AgentsAgentIdRevisionsRevisionIdCompare:
        return AgentsAgentIdRevisionsRevisionIdCompare(self._client, self._bindings)

    async def set_default(
        self, *, if_match: str | Unset | None = UNSET, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.Agent]:
        """Set Default Agent Revision. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: set_default_agent_revision.asyncio_detailed(
                client=client,
                agent_id=self._bindings["agent_id"],
                revision_id=self._bindings["revision_id"],
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )


class AgentsAgentIdRevisionsRevisionIdCompare(Resource):
    """Bound Native resource: /agents / {agent_id} / revisions / {revision_id} / compare."""

    async def get(
        self,
        *,
        base_revision_id: str,
        section: wire.CompareAgentRevisionsSection | Unset = UNSET,
        offset: int | Unset = UNSET,
        limit: int | Unset = UNSET,
        version: str | Unset | None = UNSET,
        query: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.TextRead]:
        """Compare Agent Revisions. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: compare_agent_revisions.asyncio_detailed(
                client=client,
                agent_id=self._bindings["agent_id"],
                revision_id=self._bindings["revision_id"],
                base_revision_id=base_revision_id,
                section=section,
                offset=offset,
                limit=limit,
                version=version,
                query=query,
                x_workspace_id=x_workspace_id,
            )
        )


class Assets(Resource):
    """Bound Native resource: /assets."""

    async def list(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.AssetPage]:
        """List Assets. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_assets.asyncio_detailed(
                client=client, limit=limit, cursor=cursor, x_workspace_id=x_workspace_id
            )
        )

    def pages(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.AssetPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, x_workspace_id=x_workspace_id, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.Asset]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(limit=limit, cursor=cursor, x_workspace_id=x_workspace_id)
            for item in page.value.items
        )

    async def create(self, *, body: wire.AssetCreate, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.Asset]:
        """Create Asset. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_asset.asyncio_detailed(client=client, body=body, x_workspace_id=x_workspace_id)
        )

    def __call__(self, asset_id: str) -> AssetsAssetId:
        return AssetsAssetId(self._client, self._bind("asset_id", asset_id))


class AssetsAssetId(Resource):
    """Bound Native resource: /assets / {asset_id}."""

    async def delete(
        self, *, if_match: str | Unset | None = UNSET, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.Asset]:
        """Retire Asset. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: retire_asset.asyncio_detailed(
                client=client, asset_id=self._bindings["asset_id"], if_match=if_match, x_workspace_id=x_workspace_id
            )
        )

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.Asset]:
        """Get Asset. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_asset.asyncio_detailed(
                client=client, asset_id=self._bindings["asset_id"], x_workspace_id=x_workspace_id
            )
        )

    @property
    def content(self) -> AssetsAssetIdContent:
        return AssetsAssetIdContent(self._client, self._bindings)


class AssetsAssetIdContent(Resource):
    """Bound Native resource: /assets / {asset_id} / content."""

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[File]:
        """Read Asset Content. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: read_asset_content.asyncio_detailed(
                client=client, asset_id=self._bindings["asset_id"], x_workspace_id=x_workspace_id
            )
        )

    def get_stream(self, *, x_workspace_id: str | Unset | None = UNSET) -> AbstractAsyncContextManager[httpx2.Response]:
        """Unbuffered response; caller checks status and consumes within the context."""
        return self._stream(
            read_asset_content.build_request(asset_id=self._bindings["asset_id"], x_workspace_id=x_workspace_id)
        )


class Auth(Resource):
    """Bound Native resource: /auth."""

    async def bootstrap(self, *, body: wire.BootstrapInput) -> Result[wire.LoginOutput]:
        """Bootstrap Administrator. One HTTP request; no automatic replay."""
        return await self._call(lambda client: bootstrap_administrator.asyncio_detailed(client=client, body=body))

    @property
    def configuration(self) -> AuthConfiguration:
        return AuthConfiguration(self._client, self._bindings)

    @property
    def email_change(self) -> AuthEmailChange:
        return AuthEmailChange(self._client, self._bindings)

    async def login(self, *, body: wire.LoginInput) -> Result[wire.LoginOutput]:
        """Password Login. One HTTP request; no automatic replay."""
        return await self._call(lambda client: password_login.asyncio_detailed(client=client, body=body))

    async def logout(self) -> Result[None]:
        """Logout. One HTTP request; no automatic replay."""
        return await self._call(lambda client: logout.asyncio_detailed(client=client))

    @property
    def password_reset(self) -> AuthPasswordReset:
        return AuthPasswordReset(self._client, self._bindings)

    @property
    def session(self) -> AuthSession:
        return AuthSession(self._client, self._bindings)


class AuthConfiguration(Resource):
    """Bound Native resource: /auth / configuration."""

    async def get(self) -> Result[wire.AuthConfiguration]:
        """Auth Configuration. One HTTP request; no automatic replay."""
        return await self._call(lambda client: auth_configuration.asyncio_detailed(client=client))


class AuthEmailChange(Resource):
    """Bound Native resource: /auth / email-change."""

    async def confirm(self, *, body: wire.EmailChangeConfirm) -> Result[None]:
        """Confirm Email Change. One HTTP request; no automatic replay."""
        return await self._call(lambda client: confirm_email_change.asyncio_detailed(client=client, body=body))


class AuthPasswordReset(Resource):
    """Bound Native resource: /auth / password-reset."""

    async def create(self, *, body: wire.PasswordReset) -> Result[None]:
        """Request Password Reset. One HTTP request; no automatic replay."""
        return await self._call(lambda client: request_password_reset.asyncio_detailed(client=client, body=body))

    async def confirm(self, *, body: wire.PasswordResetConfirm) -> Result[None]:
        """Confirm Password Reset. One HTTP request; no automatic replay."""
        return await self._call(lambda client: confirm_password_reset.asyncio_detailed(client=client, body=body))


class AuthSession(Resource):
    """Bound Native resource: /auth / session."""

    async def get(self) -> Result[wire.SessionProfile]:
        """Session Profile. One HTTP request; no automatic replay."""
        return await self._call(lambda client: session_profile.asyncio_detailed(client=client))


class Connections(Resource):
    """Bound Native resource: /connections."""

    async def list(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.ConnectionPage]:
        """List Connections. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_connections.asyncio_detailed(
                client=client, limit=limit, cursor=cursor, x_workspace_id=x_workspace_id
            )
        )

    def pages(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.ConnectionPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, x_workspace_id=x_workspace_id, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.Connection]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(limit=limit, cursor=cursor, x_workspace_id=x_workspace_id)
            for item in page.value.items
        )

    async def create(
        self, *, body: wire.ConnectionCreate, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.Connection]:
        """Create Connection. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_connection.asyncio_detailed(client=client, body=body, x_workspace_id=x_workspace_id)
        )

    @property
    def callback(self) -> ConnectionsCallback:
        return ConnectionsCallback(self._client, self._bindings)

    @property
    def redirect_uri(self) -> ConnectionsRedirectUri:
        return ConnectionsRedirectUri(self._client, self._bindings)

    def __call__(self, connection_id: str) -> ConnectionsConnectionId:
        return ConnectionsConnectionId(self._client, self._bind("connection_id", connection_id))


class ConnectionsCallback(Resource):
    """Bound Native resource: /connections / callback."""

    async def get(
        self,
        *,
        state: str,
        code: str | Unset | None = UNSET,
        error: str | Unset | None = UNSET,
        iss: str | Unset | None = UNSET,
        session_uri: str | Unset | None = UNSET,
    ) -> Result[Any | wire.CallbackOutcome]:
        """Complete Authorization. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: complete_authorization.asyncio_detailed(
                client=client, state=state, code=code, error=error, iss=iss, session_uri=session_uri
            )
        )


class ConnectionsRedirectUri(Resource):
    """Bound Native resource: /connections / redirect-uri."""

    async def get(self) -> Result[wire.OAuthRedirect]:
        """Get Redirect Uri. One HTTP request; no automatic replay."""
        return await self._call(lambda client: get_redirect_uri.asyncio_detailed(client=client))


class ConnectionsConnectionId(Resource):
    """Bound Native resource: /connections / {connection_id}."""

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.Connection]:
        """Get Connection. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_connection.asyncio_detailed(
                client=client, connection_id=self._bindings["connection_id"], x_workspace_id=x_workspace_id
            )
        )

    async def update(
        self,
        *,
        body: wire.ConnectionUpdate,
        if_match: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.Connection]:
        """Update Connection. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_connection.asyncio_detailed(
                client=client,
                connection_id=self._bindings["connection_id"],
                body=body,
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )

    async def authorize(
        self,
        *,
        body: wire.AuthorizationRequest,
        if_match: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.AuthorizationResult]:
        """Authorize Connection. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: authorize_connection.asyncio_detailed(
                client=client,
                connection_id=self._bindings["connection_id"],
                body=body,
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )

    async def revoke(
        self, *, if_match: str | Unset | None = UNSET, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.RevokedConnection]:
        """Revoke Connection. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: revoke_connection.asyncio_detailed(
                client=client,
                connection_id=self._bindings["connection_id"],
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )

    async def test(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.ConnectionTest]:
        """Test Connection. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: test_connection.asyncio_detailed(
                client=client, connection_id=self._bindings["connection_id"], x_workspace_id=x_workspace_id
            )
        )

    @property
    def tools(self) -> ConnectionsConnectionIdTools:
        return ConnectionsConnectionIdTools(self._client, self._bindings)


class ConnectionsConnectionIdTools(Resource):
    """Bound Native resource: /connections / {connection_id} / tools."""

    async def list(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.ToolPage]:
        """List Connection Tools. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_connection_tools.asyncio_detailed(
                client=client, connection_id=self._bindings["connection_id"], x_workspace_id=x_workspace_id
            )
        )

    @property
    def definitions(self) -> ConnectionsConnectionIdToolsDefinitions:
        return ConnectionsConnectionIdToolsDefinitions(self._client, self._bindings)

    @property
    def index(self) -> ConnectionsConnectionIdToolsIndex:
        return ConnectionsConnectionIdToolsIndex(self._client, self._bindings)


class ConnectionsConnectionIdToolsDefinitions(Resource):
    """Bound Native resource: /connections / {connection_id} / tools / definitions."""

    async def get(
        self,
        *,
        name: list[str],
        offset: int | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        version: str | Unset | None = UNSET,
        query: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.Definitions | wire.TextRead]:
        """Define Connection Tools. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: define_connection_tools.asyncio_detailed(
                client=client,
                connection_id=self._bindings["connection_id"],
                name=name,
                offset=offset,
                limit=limit,
                version=version,
                query=query,
                x_workspace_id=x_workspace_id,
            )
        )


class ConnectionsConnectionIdToolsIndex(Resource):
    """Bound Native resource: /connections / {connection_id} / tools / index."""

    async def get(
        self,
        *,
        query: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.CatalogIndex]:
        """Index Connection Tools. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: index_connection_tools.asyncio_detailed(
                client=client,
                connection_id=self._bindings["connection_id"],
                query=query,
                limit=limit,
                cursor=cursor,
                x_workspace_id=x_workspace_id,
            )
        )


class ConnectorProviders(Resource):
    """Bound Native resource: /connector-providers."""

    async def list(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.ProviderPage]:
        """List connector providers. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_connector_providers.asyncio_detailed(
                client=client, limit=limit, cursor=cursor, x_workspace_id=x_workspace_id
            )
        )

    def pages(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.ProviderPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, x_workspace_id=x_workspace_id, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.Provider]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(limit=limit, cursor=cursor, x_workspace_id=x_workspace_id)
            for item in page.value.items
        )

    async def create(
        self, *, body: wire.ProviderCreate, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.Provider]:
        """Create connector provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_connector_provider.asyncio_detailed(
                client=client, body=body, x_workspace_id=x_workspace_id
            )
        )

    def __call__(self, provider_id: str) -> ConnectorProvidersProviderId:
        return ConnectorProvidersProviderId(self._client, self._bind("provider_id", provider_id))


class ConnectorProvidersProviderId(Resource):
    """Bound Native resource: /connector-providers / {provider_id}."""

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.Provider]:
        """Get connector provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_connector_provider.asyncio_detailed(
                client=client, provider_id=self._bindings["provider_id"], x_workspace_id=x_workspace_id
            )
        )

    async def update(
        self,
        *,
        body: wire.ProviderUpdate,
        if_match: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.Provider]:
        """Update connector provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_connector_provider.asyncio_detailed(
                client=client,
                provider_id=self._bindings["provider_id"],
                body=body,
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )

    @property
    def apps(self) -> ConnectorProvidersProviderIdApps:
        return ConnectorProvidersProviderIdApps(self._client, self._bindings)

    async def test(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.ProviderTest]:
        """Test connector provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: test_connector_provider.asyncio_detailed(
                client=client, provider_id=self._bindings["provider_id"], x_workspace_id=x_workspace_id
            )
        )


class ConnectorProvidersProviderIdApps(Resource):
    """Bound Native resource: /connector-providers / {provider_id} / apps."""

    async def list(
        self,
        *,
        query: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        refresh: bool | Unset = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.ConnectorAppPage]:
        """List Connector Apps. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_connector_apps.asyncio_detailed(
                client=client,
                provider_id=self._bindings["provider_id"],
                query=query,
                limit=limit,
                cursor=cursor,
                refresh=refresh,
                x_workspace_id=x_workspace_id,
            )
        )

    def pages(
        self,
        *,
        query: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        refresh: bool | Unset = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.ConnectorAppPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(
                query=query, limit=limit, refresh=refresh, x_workspace_id=x_workspace_id, cursor=next_cursor
            ),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        query: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        refresh: bool | Unset = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.ConnectorApp]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(
                query=query, limit=limit, cursor=cursor, refresh=refresh, x_workspace_id=x_workspace_id
            )
            for item in page.value.items
        )

    def __call__(self, app: str) -> ConnectorProvidersProviderIdAppsApp:
        return ConnectorProvidersProviderIdAppsApp(self._client, self._bind("app", app))


class ConnectorProvidersProviderIdAppsApp(Resource):
    """Bound Native resource: /connector-providers / {provider_id} / apps / {app}."""

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.ConnectorApp]:
        """Get Connector App. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_connector_app.asyncio_detailed(
                client=client,
                provider_id=self._bindings["provider_id"],
                app=self._bindings["app"],
                x_workspace_id=x_workspace_id,
            )
        )

    @property
    def actions(self) -> ConnectorProvidersProviderIdAppsAppActions:
        return ConnectorProvidersProviderIdAppsAppActions(self._client, self._bindings)


class ConnectorProvidersProviderIdAppsAppActions(Resource):
    """Bound Native resource: /connector-providers / {provider_id} / apps / {app} / actions."""

    async def list(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.ConnectorActionPage]:
        """List Connector Actions. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_connector_actions.asyncio_detailed(
                client=client,
                provider_id=self._bindings["provider_id"],
                app=self._bindings["app"],
                x_workspace_id=x_workspace_id,
            )
        )

    @property
    def definitions(self) -> ConnectorProvidersProviderIdAppsAppActionsDefinitions:
        return ConnectorProvidersProviderIdAppsAppActionsDefinitions(self._client, self._bindings)

    @property
    def index(self) -> ConnectorProvidersProviderIdAppsAppActionsIndex:
        return ConnectorProvidersProviderIdAppsAppActionsIndex(self._client, self._bindings)


class ConnectorProvidersProviderIdAppsAppActionsDefinitions(Resource):
    """Bound Native resource: /connector-providers / {provider_id} / apps / {app} / actions / definitions."""

    async def get(
        self,
        *,
        name: list[str],
        offset: int | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        version: str | Unset | None = UNSET,
        query: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.Definitions | wire.TextRead]:
        """Define Connector Actions. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: define_connector_actions.asyncio_detailed(
                client=client,
                provider_id=self._bindings["provider_id"],
                app=self._bindings["app"],
                name=name,
                offset=offset,
                limit=limit,
                version=version,
                query=query,
                x_workspace_id=x_workspace_id,
            )
        )


class ConnectorProvidersProviderIdAppsAppActionsIndex(Resource):
    """Bound Native resource: /connector-providers / {provider_id} / apps / {app} / actions / index."""

    async def get(
        self,
        *,
        query: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.CatalogIndex]:
        """Index Connector Actions. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: index_connector_actions.asyncio_detailed(
                client=client,
                provider_id=self._bindings["provider_id"],
                app=self._bindings["app"],
                query=query,
                limit=limit,
                cursor=cursor,
                x_workspace_id=x_workspace_id,
            )
        )


class DesktopAssistance(Resource):
    """Bound Native resource: /desktop-assistance."""

    def __call__(self, assistance_id: str) -> DesktopAssistanceAssistanceId:
        return DesktopAssistanceAssistanceId(self._client, self._bind("assistance_id", assistance_id))


class DesktopAssistanceAssistanceId(Resource):
    """Bound Native resource: /desktop-assistance / {assistance_id}."""

    async def complete(self, *, body: wire.Completion, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.View]:
        """Complete Assistance. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: complete_assistance.asyncio_detailed(
                client=client, assistance_id=self._bindings["assistance_id"], body=body, x_workspace_id=x_workspace_id
            )
        )

    async def control(
        self, *, body: wire.Control, renew: bool | Unset = UNSET, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.Access]:
        """Control Desktop. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: control_desktop.asyncio_detailed(
                client=client,
                assistance_id=self._bindings["assistance_id"],
                body=body,
                renew=renew,
                x_workspace_id=x_workspace_id,
            )
        )

    async def disconnect(self, *, body: wire.Control, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.View]:
        """Disconnect Desktop. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: disconnect_desktop.asyncio_detailed(
                client=client, assistance_id=self._bindings["assistance_id"], body=body, x_workspace_id=x_workspace_id
            )
        )

    async def request_control(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.View]:
        """Request Control. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: request_control.asyncio_detailed(
                client=client, assistance_id=self._bindings["assistance_id"], x_workspace_id=x_workspace_id
            )
        )

    async def view(
        self, *, body: wire.Control, renew: bool | Unset = UNSET, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.Access]:
        """View Desktop. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: view_desktop.asyncio_detailed(
                client=client,
                assistance_id=self._bindings["assistance_id"],
                body=body,
                renew=renew,
                x_workspace_id=x_workspace_id,
            )
        )


class EnvironmentProviders(Resource):
    """Bound Native resource: /environment-providers."""

    async def list(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.ProviderPage]:
        """List environment providers. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_environment_providers.asyncio_detailed(
                client=client, limit=limit, cursor=cursor, x_workspace_id=x_workspace_id
            )
        )

    def pages(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.ProviderPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, x_workspace_id=x_workspace_id, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.Provider]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(limit=limit, cursor=cursor, x_workspace_id=x_workspace_id)
            for item in page.value.items
        )

    async def create(
        self, *, body: wire.ProviderCreate, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.Provider]:
        """Create environment provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_environment_provider.asyncio_detailed(
                client=client, body=body, x_workspace_id=x_workspace_id
            )
        )

    def __call__(self, provider_id: str) -> EnvironmentProvidersProviderId:
        return EnvironmentProvidersProviderId(self._client, self._bind("provider_id", provider_id))


class EnvironmentProvidersProviderId(Resource):
    """Bound Native resource: /environment-providers / {provider_id}."""

    async def delete(
        self, *, if_match: str | Unset | None = UNSET, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[None]:
        """Delete Environment Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_environment_provider.asyncio_detailed(
                client=client,
                provider_id=self._bindings["provider_id"],
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.Provider]:
        """Get environment provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_environment_provider.asyncio_detailed(
                client=client, provider_id=self._bindings["provider_id"], x_workspace_id=x_workspace_id
            )
        )

    async def update(
        self,
        *,
        body: wire.ProviderUpdate,
        if_match: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.Provider]:
        """Update environment provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_environment_provider.asyncio_detailed(
                client=client,
                provider_id=self._bindings["provider_id"],
                body=body,
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )

    @property
    def references(self) -> EnvironmentProvidersProviderIdReferences:
        return EnvironmentProvidersProviderIdReferences(self._client, self._bindings)

    async def test(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.ProviderTest]:
        """Test environment provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: test_environment_provider.asyncio_detailed(
                client=client, provider_id=self._bindings["provider_id"], x_workspace_id=x_workspace_id
            )
        )


class EnvironmentProvidersProviderIdReferences(Resource):
    """Bound Native resource: /environment-providers / {provider_id} / references."""

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.EnvironmentProviderReferences]:
        """Environment Provider References. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: environment_provider_references.asyncio_detailed(
                client=client, provider_id=self._bindings["provider_id"], x_workspace_id=x_workspace_id
            )
        )


class EnvironmentTemplates(Resource):
    """Bound Native resource: /environment-templates."""

    async def list(
        self,
        *,
        label: list[str] | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.TemplatePage]:
        """List Environment Templates. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_environment_templates.asyncio_detailed(
                client=client, label=label, limit=limit, cursor=cursor, x_workspace_id=x_workspace_id
            )
        )

    def pages(
        self,
        *,
        label: list[str] | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.TemplatePage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        label = label.copy() if isinstance(label, list) else label
        return pages(
            lambda next_cursor: self.list(label=label, limit=limit, x_workspace_id=x_workspace_id, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        label: list[str] | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.Template]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(label=label, limit=limit, cursor=cursor, x_workspace_id=x_workspace_id)
            for item in page.value.items
        )

    async def create(
        self, *, body: wire.TemplateCreate, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.Template]:
        """Create Environment Template. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_environment_template.asyncio_detailed(
                client=client, body=body, x_workspace_id=x_workspace_id
            )
        )

    def __call__(self, template_id: str) -> EnvironmentTemplatesTemplateId:
        return EnvironmentTemplatesTemplateId(self._client, self._bind("template_id", template_id))


class EnvironmentTemplatesTemplateId(Resource):
    """Bound Native resource: /environment-templates / {template_id}."""

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.Template]:
        """Get Environment Template. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_environment_template.asyncio_detailed(
                client=client, template_id=self._bindings["template_id"], x_workspace_id=x_workspace_id
            )
        )

    async def update(
        self,
        *,
        body: wire.TemplateUpdate,
        if_match: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.Template]:
        """Update Environment Template. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_environment_template.asyncio_detailed(
                client=client,
                template_id=self._bindings["template_id"],
                body=body,
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )


class Environments(Resource):
    """Bound Native resource: /environments."""

    async def list(
        self,
        *,
        status: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.EnvironmentPage]:
        """List Environments. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_environments.asyncio_detailed(
                client=client, status=status, limit=limit, cursor=cursor, x_workspace_id=x_workspace_id
            )
        )

    def pages(
        self,
        *,
        status: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.EnvironmentPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(
                status=status, limit=limit, x_workspace_id=x_workspace_id, cursor=next_cursor
            ),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        status: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.EnvironmentView]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(status=status, limit=limit, cursor=cursor, x_workspace_id=x_workspace_id)
            for item in page.value.items
        )

    async def create(
        self,
        *,
        body: wire.ExternalTargetCreate | wire.ManagedEnvironmentCreate,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.EnvironmentView]:
        """Create Environment. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_environment.asyncio_detailed(client=client, body=body, x_workspace_id=x_workspace_id)
        )

    def __call__(self, environment_id: str) -> EnvironmentsEnvironmentId:
        return EnvironmentsEnvironmentId(self._client, self._bind("environment_id", environment_id))


class EnvironmentsEnvironmentId(Resource):
    """Bound Native resource: /environments / {environment_id}."""

    async def delete(
        self, *, if_match: str | Unset | None = UNSET, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.EnvironmentView]:
        """Delete Environment. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_environment.asyncio_detailed(
                client=client,
                environment_id=self._bindings["environment_id"],
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.EnvironmentView]:
        """Get Environment. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_environment.asyncio_detailed(
                client=client, environment_id=self._bindings["environment_id"], x_workspace_id=x_workspace_id
            )
        )

    async def update(
        self,
        *,
        body: wire.EnvironmentUpdate,
        if_match: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.EnvironmentView]:
        """Update Environment. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_environment.asyncio_detailed(
                client=client,
                environment_id=self._bindings["environment_id"],
                body=body,
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )

    @property
    def computer(self) -> EnvironmentsEnvironmentIdComputer:
        return EnvironmentsEnvironmentIdComputer(self._client, self._bindings)

    async def stop(
        self, *, if_match: str | Unset | None = UNSET, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.EnvironmentView]:
        """Stop Environment. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: stop_environment.asyncio_detailed(
                client=client,
                environment_id=self._bindings["environment_id"],
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )


class EnvironmentsEnvironmentIdComputer(Resource):
    """Bound Native resource: /environments / {environment_id} / computer."""

    async def check(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.ComputerCheck]:
        """Check Computer. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: check_computer.asyncio_detailed(
                client=client, environment_id=self._bindings["environment_id"], x_workspace_id=x_workspace_id
            )
        )


class FindingAnalyses(Resource):
    """Bound Native resource: /finding-analyses."""

    async def list(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.AnalysisPage]:
        """List Finding Analyses. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_finding_analyses.asyncio_detailed(
                client=client, limit=limit, cursor=cursor, x_workspace_id=x_workspace_id
            )
        )

    def pages(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.AnalysisPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, x_workspace_id=x_workspace_id, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.Analysis]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(limit=limit, cursor=cursor, x_workspace_id=x_workspace_id)
            for item in page.value.items
        )

    async def create(
        self, *, body: wire.AnalysisCreate, idempotency_key: str, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.Analysis]:
        """Start Analysis. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: start_analysis.asyncio_detailed(
                client=client, body=body, idempotency_key=idempotency_key, x_workspace_id=x_workspace_id
            )
        )


class Findings(Resource):
    """Bound Native resource: /findings."""

    async def list(
        self,
        *,
        agent_id: str | Unset | None = UNSET,
        category: wire.Category | Unset | None = UNSET,
        severity: wire.Severity | Unset | None = UNSET,
        assessment: wire.Assessment | Unset | None = UNSET,
        closed: bool | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.FindingPage]:
        """List Findings. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_findings.asyncio_detailed(
                client=client,
                agent_id=agent_id,
                category=category,
                severity=severity,
                assessment=assessment,
                closed=closed,
                limit=limit,
                cursor=cursor,
                x_workspace_id=x_workspace_id,
            )
        )

    def pages(
        self,
        *,
        agent_id: str | Unset | None = UNSET,
        category: wire.Category | Unset | None = UNSET,
        severity: wire.Severity | Unset | None = UNSET,
        assessment: wire.Assessment | Unset | None = UNSET,
        closed: bool | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.FindingPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(
                agent_id=agent_id,
                category=category,
                severity=severity,
                assessment=assessment,
                closed=closed,
                limit=limit,
                x_workspace_id=x_workspace_id,
                cursor=next_cursor,
            ),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        agent_id: str | Unset | None = UNSET,
        category: wire.Category | Unset | None = UNSET,
        severity: wire.Severity | Unset | None = UNSET,
        assessment: wire.Assessment | Unset | None = UNSET,
        closed: bool | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.Finding]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(
                agent_id=agent_id,
                category=category,
                severity=severity,
                assessment=assessment,
                closed=closed,
                limit=limit,
                cursor=cursor,
                x_workspace_id=x_workspace_id,
            )
            for item in page.value.items
        )

    async def create(
        self, *, body: wire.FindingCreate, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.Finding]:
        """Create Finding. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_finding.asyncio_detailed(client=client, body=body, x_workspace_id=x_workspace_id)
        )

    def __call__(self, finding_id: str) -> FindingsFindingId:
        return FindingsFindingId(self._client, self._bind("finding_id", finding_id))


class FindingsFindingId(Resource):
    """Bound Native resource: /findings / {finding_id}."""

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.Finding]:
        """Get Finding. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_finding.asyncio_detailed(
                client=client, finding_id=self._bindings["finding_id"], x_workspace_id=x_workspace_id
            )
        )

    async def update(
        self,
        *,
        body: wire.FindingUpdate,
        if_match: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.Finding]:
        """Update Finding. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_finding.asyncio_detailed(
                client=client,
                finding_id=self._bindings["finding_id"],
                body=body,
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )


class Invitations(Resource):
    """Bound Native resource: /invitations."""

    def __call__(self, invitation_id: str) -> InvitationsInvitationId:
        return InvitationsInvitationId(self._client, self._bind("invitation_id", invitation_id))


class InvitationsInvitationId(Resource):
    """Bound Native resource: /invitations / {invitation_id}."""

    async def accept(self, *, body: wire.InvitationAccept) -> Result[wire.LoginOutput]:
        """Accept. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: accept.asyncio_detailed(
                client=client, invitation_id=self._bindings["invitation_id"], body=body
            )
        )


class McpServers(Resource):
    """Bound Native resource: /mcp-servers."""

    async def list(
        self, *, query: str | Unset | None = UNSET, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.McpServerPage]:
        """List Mcp Servers. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_mcp_servers.asyncio_detailed(client=client, query=query, limit=limit, cursor=cursor)
        )

    def pages(
        self, *, query: str | Unset | None = UNSET, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.McpServerPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(query=query, limit=limit, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self, *, query: str | Unset | None = UNSET, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.McpServer]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(query=query, limit=limit, cursor=cursor) for item in page.value.items)


class MediaUnderstandingDefaults(Resource):
    """Bound Native resource: /media-understanding-defaults."""

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.MediaDefaults]:
        """Get Media Defaults. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_media_defaults.asyncio_detailed(client=client, x_workspace_id=x_workspace_id)
        )

    async def replace(
        self,
        *,
        body: wire.MediaUnderstandingSelection,
        if_match: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.MediaDefaults]:
        """Replace Media Defaults. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: replace_media_defaults.asyncio_detailed(
                client=client, body=body, if_match=if_match, x_workspace_id=x_workspace_id
            )
        )


class Memories(Resource):
    """Bound Native resource: /memories."""

    async def list(
        self,
        *,
        label: list[str] | Unset | None = UNSET,
        kind: wire.MemoryKind | Unset | None = UNSET,
        type_: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.MemoryPage]:
        """List Memories. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_memories.asyncio_detailed(
                client=client,
                label=label,
                kind=kind,
                type_=type_,
                limit=limit,
                cursor=cursor,
                x_workspace_id=x_workspace_id,
            )
        )

    def pages(
        self,
        *,
        label: list[str] | Unset | None = UNSET,
        kind: wire.MemoryKind | Unset | None = UNSET,
        type_: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.MemoryPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        label = label.copy() if isinstance(label, list) else label
        return pages(
            lambda next_cursor: self.list(
                label=label, kind=kind, type_=type_, limit=limit, x_workspace_id=x_workspace_id, cursor=next_cursor
            ),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        label: list[str] | Unset | None = UNSET,
        kind: wire.MemoryKind | Unset | None = UNSET,
        type_: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.Memory]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(
                label=label, kind=kind, type_=type_, limit=limit, cursor=cursor, x_workspace_id=x_workspace_id
            )
            for item in page.value.items
        )

    async def create(
        self, *, body: wire.MemoryCreate, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.Memory]:
        """Create Memory. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_memory.asyncio_detailed(client=client, body=body, x_workspace_id=x_workspace_id)
        )

    def __call__(self, memory_id: str) -> MemoriesMemoryId:
        return MemoriesMemoryId(self._client, self._bind("memory_id", memory_id))


class MemoriesMemoryId(Resource):
    """Bound Native resource: /memories / {memory_id}."""

    async def delete(
        self, *, if_match: str | Unset | None = UNSET, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[None]:
        """Delete Memory. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_memory.asyncio_detailed(
                client=client, memory_id=self._bindings["memory_id"], if_match=if_match, x_workspace_id=x_workspace_id
            )
        )

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.Memory]:
        """Get Memory. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_memory.asyncio_detailed(
                client=client, memory_id=self._bindings["memory_id"], x_workspace_id=x_workspace_id
            )
        )

    async def update(
        self,
        *,
        body: wire.MemoryUpdate,
        if_match: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.Memory]:
        """Update Memory. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_memory.asyncio_detailed(
                client=client,
                memory_id=self._bindings["memory_id"],
                body=body,
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )

    @property
    def files(self) -> MemoriesMemoryIdFiles:
        return MemoriesMemoryIdFiles(self._client, self._bindings)

    @property
    def records(self) -> MemoriesMemoryIdRecords:
        return MemoriesMemoryIdRecords(self._client, self._bindings)

    @property
    def revisions(self) -> MemoriesMemoryIdRevisions:
        return MemoriesMemoryIdRevisions(self._client, self._bindings)


class MemoriesMemoryIdFiles(Resource):
    """Bound Native resource: /memories / {memory_id} / files."""

    async def list(
        self,
        *,
        prefix: str | Unset = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.MemoryFilePage]:
        """List Files. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_files.asyncio_detailed(
                client=client,
                memory_id=self._bindings["memory_id"],
                prefix=prefix,
                limit=limit,
                cursor=cursor,
                x_workspace_id=x_workspace_id,
            )
        )

    def pages(
        self,
        *,
        prefix: str | Unset = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.MemoryFilePage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(
                prefix=prefix, limit=limit, x_workspace_id=x_workspace_id, cursor=next_cursor
            ),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        prefix: str | Unset = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.MemoryFileEntry]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(prefix=prefix, limit=limit, cursor=cursor, x_workspace_id=x_workspace_id)
            for item in page.value.items
        )

    async def create(
        self, *, body: wire.MemoryFileCreate, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.MemoryFile]:
        """Create File. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_file.asyncio_detailed(
                client=client, memory_id=self._bindings["memory_id"], body=body, x_workspace_id=x_workspace_id
            )
        )

    async def move(
        self,
        *,
        body: wire.MemoryFileMove,
        if_match: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.MemoryFile]:
        """Move File. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: move_file.asyncio_detailed(
                client=client,
                memory_id=self._bindings["memory_id"],
                body=body,
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )

    def __call__(self, path: str) -> MemoriesMemoryIdFilesPath:
        return MemoriesMemoryIdFilesPath(self._client, self._bind("path", path))


class MemoriesMemoryIdFilesPath(Resource):
    """Bound Native resource: /memories / {memory_id} / files / {path}."""

    async def delete(
        self, *, if_match: str | Unset | None = UNSET, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[None]:
        """Delete File. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_file.asyncio_detailed(
                client=client,
                memory_id=self._bindings["memory_id"],
                path=self._bindings["path"],
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.MemoryFile]:
        """Read File. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: read_file.asyncio_detailed(
                client=client,
                memory_id=self._bindings["memory_id"],
                path=self._bindings["path"],
                x_workspace_id=x_workspace_id,
            )
        )

    async def replace(
        self,
        *,
        body: wire.MemoryFileReplace,
        if_match: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.MemoryFile]:
        """Replace File. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: replace_file.asyncio_detailed(
                client=client,
                memory_id=self._bindings["memory_id"],
                path=self._bindings["path"],
                body=body,
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )


class MemoriesMemoryIdRecords(Resource):
    """Bound Native resource: /memories / {memory_id} / records."""

    async def list(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.MemoryRecordPage]:
        """List Records. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_records.asyncio_detailed(
                client=client,
                memory_id=self._bindings["memory_id"],
                limit=limit,
                cursor=cursor,
                x_workspace_id=x_workspace_id,
            )
        )

    def pages(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.MemoryRecordPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, x_workspace_id=x_workspace_id, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.MemoryRecordView]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(limit=limit, cursor=cursor, x_workspace_id=x_workspace_id)
            for item in page.value.items
        )

    async def create(
        self, *, body: wire.MemoryRecordText, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.MemoryRecordView]:
        """Add Record. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: add_record.asyncio_detailed(
                client=client, memory_id=self._bindings["memory_id"], body=body, x_workspace_id=x_workspace_id
            )
        )

    async def search(
        self, *, body: wire.MemoryRecordSearch, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.MemoryRecordPage]:
        """Search Records. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: search_records.asyncio_detailed(
                client=client, memory_id=self._bindings["memory_id"], body=body, x_workspace_id=x_workspace_id
            )
        )

    def __call__(self, record_id: str) -> MemoriesMemoryIdRecordsRecordId:
        return MemoriesMemoryIdRecordsRecordId(self._client, self._bind("record_id", record_id))


class MemoriesMemoryIdRecordsRecordId(Resource):
    """Bound Native resource: /memories / {memory_id} / records / {record_id}."""

    async def delete(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[None]:
        """Delete Record. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_record.asyncio_detailed(
                client=client,
                memory_id=self._bindings["memory_id"],
                record_id=self._bindings["record_id"],
                x_workspace_id=x_workspace_id,
            )
        )

    async def replace(
        self, *, body: wire.MemoryRecordText, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.MemoryRecordView]:
        """Update Record. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_record.asyncio_detailed(
                client=client,
                memory_id=self._bindings["memory_id"],
                record_id=self._bindings["record_id"],
                body=body,
                x_workspace_id=x_workspace_id,
            )
        )


class MemoriesMemoryIdRevisions(Resource):
    """Bound Native resource: /memories / {memory_id} / revisions."""

    async def delete(self, *, path: str, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.HistoryPurge]:
        """Purge History. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: purge_history.asyncio_detailed(
                client=client, memory_id=self._bindings["memory_id"], path=path, x_workspace_id=x_workspace_id
            )
        )

    async def list(
        self,
        *,
        path: str | Unset | None = UNSET,
        run_id: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.MemoryRevisionPage]:
        """List Memory Revisions. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_memory_revisions.asyncio_detailed(
                client=client,
                memory_id=self._bindings["memory_id"],
                path=path,
                run_id=run_id,
                limit=limit,
                cursor=cursor,
                x_workspace_id=x_workspace_id,
            )
        )

    def pages(
        self,
        *,
        path: str | Unset | None = UNSET,
        run_id: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.MemoryRevisionPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(
                path=path, run_id=run_id, limit=limit, x_workspace_id=x_workspace_id, cursor=next_cursor
            ),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        path: str | Unset | None = UNSET,
        run_id: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.MemoryRevision]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(
                path=path, run_id=run_id, limit=limit, cursor=cursor, x_workspace_id=x_workspace_id
            )
            for item in page.value.items
        )

    def __call__(self, seq: int) -> MemoriesMemoryIdRevisionsSeq:
        return MemoriesMemoryIdRevisionsSeq(self._client, self._bind("seq", str(seq)))


class MemoriesMemoryIdRevisionsSeq(Resource):
    """Bound Native resource: /memories / {memory_id} / revisions / {seq}."""

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.MemoryRevisionDetail]:
        """Get Memory Revision. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_memory_revision.asyncio_detailed(
                client=client,
                memory_id=self._bindings["memory_id"],
                seq=int(self._bindings["seq"]),
                x_workspace_id=x_workspace_id,
            )
        )

    async def restore(
        self, *, if_match: str | Unset | None = UNSET, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.MemoryFileState]:
        """Restore Memory Revision. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: restore_memory_revision.asyncio_detailed(
                client=client,
                memory_id=self._bindings["memory_id"],
                seq=int(self._bindings["seq"]),
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )


class MemoryProviders(Resource):
    """Bound Native resource: /memory-providers."""

    async def list(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.ProviderPage]:
        """List memory providers. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_memory_providers.asyncio_detailed(
                client=client, limit=limit, cursor=cursor, x_workspace_id=x_workspace_id
            )
        )

    def pages(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.ProviderPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, x_workspace_id=x_workspace_id, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.Provider]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(limit=limit, cursor=cursor, x_workspace_id=x_workspace_id)
            for item in page.value.items
        )

    async def create(
        self, *, body: wire.ProviderCreate, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.Provider]:
        """Create memory provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_memory_provider.asyncio_detailed(
                client=client, body=body, x_workspace_id=x_workspace_id
            )
        )

    def __call__(self, provider_id: str) -> MemoryProvidersProviderId:
        return MemoryProvidersProviderId(self._client, self._bind("provider_id", provider_id))


class MemoryProvidersProviderId(Resource):
    """Bound Native resource: /memory-providers / {provider_id}."""

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.Provider]:
        """Get memory provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_memory_provider.asyncio_detailed(
                client=client, provider_id=self._bindings["provider_id"], x_workspace_id=x_workspace_id
            )
        )

    async def update(
        self,
        *,
        body: wire.ProviderUpdate,
        if_match: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.Provider]:
        """Update memory provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_memory_provider.asyncio_detailed(
                client=client,
                provider_id=self._bindings["provider_id"],
                body=body,
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )

    async def test(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.ProviderTest]:
        """Test memory provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: test_memory_provider.asyncio_detailed(
                client=client, provider_id=self._bindings["provider_id"], x_workspace_id=x_workspace_id
            )
        )


class MemorySpaces(Resource):
    """Bound Native resource: /memory-spaces."""

    async def list(
        self,
        *,
        label: list[str] | Unset | None = UNSET,
        enabled: bool | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.MemorySpacePage]:
        """List Spaces. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_spaces.asyncio_detailed(
                client=client, label=label, enabled=enabled, limit=limit, cursor=cursor, x_workspace_id=x_workspace_id
            )
        )

    def pages(
        self,
        *,
        label: list[str] | Unset | None = UNSET,
        enabled: bool | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.MemorySpacePage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        label = label.copy() if isinstance(label, list) else label
        return pages(
            lambda next_cursor: self.list(
                label=label, enabled=enabled, limit=limit, x_workspace_id=x_workspace_id, cursor=next_cursor
            ),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        label: list[str] | Unset | None = UNSET,
        enabled: bool | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.MemorySpace]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(
                label=label, enabled=enabled, limit=limit, cursor=cursor, x_workspace_id=x_workspace_id
            )
            for item in page.value.items
        )

    async def create(
        self, *, body: wire.MemorySpaceCreate, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.MemorySpace]:
        """Create Space. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_space.asyncio_detailed(client=client, body=body, x_workspace_id=x_workspace_id)
        )

    def __call__(self, space_id: str) -> MemorySpacesSpaceId:
        return MemorySpacesSpaceId(self._client, self._bind("space_id", space_id))


class MemorySpacesSpaceId(Resource):
    """Bound Native resource: /memory-spaces / {space_id}."""

    async def delete(
        self, *, if_match: str | Unset | None = UNSET, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[None]:
        """Delete Space. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_space.asyncio_detailed(
                client=client, space_id=self._bindings["space_id"], if_match=if_match, x_workspace_id=x_workspace_id
            )
        )

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.MemorySpace]:
        """Get Space. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_space.asyncio_detailed(
                client=client, space_id=self._bindings["space_id"], x_workspace_id=x_workspace_id
            )
        )

    async def update(
        self,
        *,
        body: wire.MemorySpaceUpdate,
        if_match: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.MemorySpace]:
        """Update Space. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_space.asyncio_detailed(
                client=client,
                space_id=self._bindings["space_id"],
                body=body,
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )

    @property
    def organization(self) -> MemorySpacesSpaceIdOrganization:
        return MemorySpacesSpaceIdOrganization(self._client, self._bindings)

    @property
    def organizations(self) -> MemorySpacesSpaceIdOrganizations:
        return MemorySpacesSpaceIdOrganizations(self._client, self._bindings)

    @property
    def sessions(self) -> MemorySpacesSpaceIdSessions:
        return MemorySpacesSpaceIdSessions(self._client, self._bindings)


class MemorySpacesSpaceIdOrganization(Resource):
    """Bound Native resource: /memory-spaces / {space_id} / organization."""

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.SpaceOrganizationStatus]:
        """Get Space Organization. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_space_organization.asyncio_detailed(
                client=client, space_id=self._bindings["space_id"], x_workspace_id=x_workspace_id
            )
        )


class MemorySpacesSpaceIdOrganizations(Resource):
    """Bound Native resource: /memory-spaces / {space_id} / organizations."""

    async def list(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.RunPage]:
        """List Space Organizations. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_space_organizations.asyncio_detailed(
                client=client,
                space_id=self._bindings["space_id"],
                limit=limit,
                cursor=cursor,
                x_workspace_id=x_workspace_id,
            )
        )

    def pages(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.RunPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, x_workspace_id=x_workspace_id, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.RunView]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(limit=limit, cursor=cursor, x_workspace_id=x_workspace_id)
            for item in page.value.items
        )

    async def create(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.SpaceOrganizationStatus]:
        """Organize Space. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: organize_space.asyncio_detailed(
                client=client, space_id=self._bindings["space_id"], x_workspace_id=x_workspace_id
            )
        )


class MemorySpacesSpaceIdSessions(Resource):
    """Bound Native resource: /memory-spaces / {space_id} / sessions."""

    async def list(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.SessionPage]:
        """List Space Sessions. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_space_sessions.asyncio_detailed(
                client=client,
                space_id=self._bindings["space_id"],
                limit=limit,
                cursor=cursor,
                x_workspace_id=x_workspace_id,
            )
        )

    def pages(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.SessionPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, x_workspace_id=x_workspace_id, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.SessionView]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(limit=limit, cursor=cursor, x_workspace_id=x_workspace_id)
            for item in page.value.items
        )


class ModelCatalog(Resource):
    """Bound Native resource: /model-catalog."""

    async def list(
        self,
        *,
        provider: str | Unset | None = UNSET,
        model: str | Unset | None = UNSET,
        view: wire.ReadView | Unset = UNSET,
        query: str | Unset | None = UNSET,
        capability: str | Unset | None = UNSET,
        limit: int | Unset | None = UNSET,
        cursor: str | Unset | None = UNSET,
        section: wire.GetModelCatalogSectionType0 | Unset | None = UNSET,
        offset: int | Unset = UNSET,
        text_limit: int | Unset = UNSET,
        version: str | Unset | None = UNSET,
    ) -> Result[wire.ModelCatalog | wire.ModelCatalogPage | wire.TextRead]:
        """Get Model Catalog. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_model_catalog.asyncio_detailed(
                client=client,
                provider=provider,
                model=model,
                view=view,
                query=query,
                capability=capability,
                limit=limit,
                cursor=cursor,
                section=section,
                offset=offset,
                text_limit=text_limit,
                version=version,
            )
        )


class ModelProviders(Resource):
    """Bound Native resource: /model-providers."""

    async def list(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.ProviderPage]:
        """List model providers. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_model_providers.asyncio_detailed(
                client=client, limit=limit, cursor=cursor, x_workspace_id=x_workspace_id
            )
        )

    def pages(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.ProviderPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, x_workspace_id=x_workspace_id, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.Provider]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(limit=limit, cursor=cursor, x_workspace_id=x_workspace_id)
            for item in page.value.items
        )

    async def create(
        self, *, body: wire.ProviderCreate, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.Provider]:
        """Create model provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_model_provider.asyncio_detailed(
                client=client, body=body, x_workspace_id=x_workspace_id
            )
        )

    def __call__(self, provider_id: str) -> ModelProvidersProviderId:
        return ModelProvidersProviderId(self._client, self._bind("provider_id", provider_id))


class ModelProvidersProviderId(Resource):
    """Bound Native resource: /model-providers / {provider_id}."""

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.Provider]:
        """Get model provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_model_provider.asyncio_detailed(
                client=client, provider_id=self._bindings["provider_id"], x_workspace_id=x_workspace_id
            )
        )

    async def update(
        self,
        *,
        body: wire.ProviderUpdate,
        if_match: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.Provider]:
        """Update model provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_model_provider.asyncio_detailed(
                client=client,
                provider_id=self._bindings["provider_id"],
                body=body,
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )

    @property
    def authorization(self) -> ModelProvidersProviderIdAuthorization:
        return ModelProvidersProviderIdAuthorization(self._client, self._bindings)

    async def authorize(
        self, *, body: wire.ProviderAuthorizationRequest, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.AuthorizationStart]:
        """Authorize Model. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: authorize_model.asyncio_detailed(
                client=client, provider_id=self._bindings["provider_id"], body=body, x_workspace_id=x_workspace_id
            )
        )

    @property
    def models(self) -> ModelProvidersProviderIdModels:
        return ModelProvidersProviderIdModels(self._client, self._bindings)

    async def test(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.ProviderTest]:
        """Test model provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: test_model_provider.asyncio_detailed(
                client=client, provider_id=self._bindings["provider_id"], x_workspace_id=x_workspace_id
            )
        )


class ModelProvidersProviderIdAuthorization(Resource):
    """Bound Native resource: /model-providers / {provider_id} / authorization."""

    async def delete(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.AuthorizationDisconnect]:
        """Disconnect Model Authorization. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: disconnect_model_authorization.asyncio_detailed(
                client=client, provider_id=self._bindings["provider_id"], x_workspace_id=x_workspace_id
            )
        )

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.AuthorizationStatus]:
        """Model Authorization. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: model_authorization.asyncio_detailed(
                client=client, provider_id=self._bindings["provider_id"], x_workspace_id=x_workspace_id
            )
        )

    async def callback(
        self, *, body: wire.AuthorizationCallback, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.AuthorizationStatus]:
        """Complete Model Authorization. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: complete_model_authorization.asyncio_detailed(
                client=client, provider_id=self._bindings["provider_id"], body=body, x_workspace_id=x_workspace_id
            )
        )


class ModelProvidersProviderIdModels(Resource):
    """Bound Native resource: /model-providers / {provider_id} / models."""

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[list[wire.ProviderModel]]:
        """Discover Model Provider Models. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: discover_model_provider_models.asyncio_detailed(
                client=client, provider_id=self._bindings["provider_id"], x_workspace_id=x_workspace_id
            )
        )


class Models(Resource):
    """Bound Native resource: /models."""

    async def list(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.ModelPage]:
        """List Models. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_models.asyncio_detailed(
                client=client, limit=limit, cursor=cursor, x_workspace_id=x_workspace_id
            )
        )

    def pages(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.ModelPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, x_workspace_id=x_workspace_id, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.Model]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(limit=limit, cursor=cursor, x_workspace_id=x_workspace_id)
            for item in page.value.items
        )

    async def create(self, *, body: wire.ModelCreate, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.Model]:
        """Create Model. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_model.asyncio_detailed(client=client, body=body, x_workspace_id=x_workspace_id)
        )

    def __call__(self, key: str) -> ModelsKey:
        return ModelsKey(self._client, self._bind("key", key))


class ModelsKey(Resource):
    """Bound Native resource: /models / {key}."""

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.Model]:
        """Get Model. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_model.asyncio_detailed(
                client=client, key=self._bindings["key"], x_workspace_id=x_workspace_id
            )
        )

    async def update(
        self,
        *,
        body: wire.ModelUpdate,
        if_match: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.Model]:
        """Update Model. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_model.asyncio_detailed(
                client=client, key=self._bindings["key"], body=body, if_match=if_match, x_workspace_id=x_workspace_id
            )
        )


class Organizations(Resource):
    """Bound Native resource: /organizations."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.OrganizationPage]:
        """List Organizations. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_organizations.asyncio_detailed(client=client, limit=limit, cursor=cursor)
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.OrganizationPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.Organization]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    def __call__(self, organization_id: str) -> Organization:
        return Organization(self._client, self._bind("organization_id", organization_id))


class Organization(Resource):
    """Bound Native resource: /organizations / {organization_id}."""

    async def get(self) -> Result[wire.Organization]:
        """Get Organization. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_organization.asyncio_detailed(
                client=client, organization_id=self._bindings["organization_id"]
            )
        )

    async def update(
        self, *, body: wire.OrganizationUpdate, if_match: str | Unset | None = UNSET
    ) -> Result[wire.Organization]:
        """Update Organization. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_organization.asyncio_detailed(
                client=client, organization_id=self._bindings["organization_id"], body=body, if_match=if_match
            )
        )

    @property
    def audit_events(self) -> OrganizationsOrganizationIdAuditEvents:
        return OrganizationsOrganizationIdAuditEvents(self._client, self._bindings)

    @property
    def grants(self) -> OrganizationsOrganizationIdGrants:
        return OrganizationsOrganizationIdGrants(self._client, self._bindings)

    @property
    def icon(self) -> OrganizationsOrganizationIdIcon:
        return OrganizationsOrganizationIdIcon(self._client, self._bindings)

    @property
    def invitations(self) -> OrganizationsOrganizationIdInvitations:
        return OrganizationsOrganizationIdInvitations(self._client, self._bindings)

    @property
    def members(self) -> OrganizationsOrganizationIdMembers:
        return OrganizationsOrganizationIdMembers(self._client, self._bindings)

    @property
    def workspaces(self) -> OrganizationsOrganizationIdWorkspaces:
        return OrganizationsOrganizationIdWorkspaces(self._client, self._bindings)


class OrganizationsOrganizationIdAuditEvents(Resource):
    """Bound Native resource: /organizations / {organization_id} / audit-events."""

    async def list(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> Result[wire.AuditPage]:
        """List Organization Audit Events. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_organization_audit_events.asyncio_detailed(
                client=client, organization_id=self._bindings["organization_id"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.AuditPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> AsyncIterator[wire.AuditEvent]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)


class OrganizationsOrganizationIdGrants(Resource):
    """Bound Native resource: /organizations / {organization_id} / grants."""

    async def list(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> Result[wire.GrantPage]:
        """List Organization Grants. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_organization_grants.asyncio_detailed(
                client=client, organization_id=self._bindings["organization_id"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.GrantPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> AsyncIterator[wire.GrantView]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    async def create(self, *, body: wire.GrantCreate) -> Result[wire.GrantView]:
        """Create Organization Grant. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_organization_grant.asyncio_detailed(
                client=client, organization_id=self._bindings["organization_id"], body=body
            )
        )

    def __call__(self, grant_id: str) -> OrganizationsOrganizationIdGrantsGrantId:
        return OrganizationsOrganizationIdGrantsGrantId(self._client, self._bind("grant_id", grant_id))


class OrganizationsOrganizationIdGrantsGrantId(Resource):
    """Bound Native resource: /organizations / {organization_id} / grants / {grant_id}."""

    async def delete(self) -> Result[None]:
        """Delete Organization Grant. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_organization_grant.asyncio_detailed(
                client=client, organization_id=self._bindings["organization_id"], grant_id=self._bindings["grant_id"]
            )
        )

    async def update(self, *, body: wire.GrantUpdate) -> Result[wire.GrantView]:
        """Change Organization Grant. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: change_organization_grant.asyncio_detailed(
                client=client,
                organization_id=self._bindings["organization_id"],
                grant_id=self._bindings["grant_id"],
                body=body,
            )
        )


class OrganizationsOrganizationIdIcon(Resource):
    """Bound Native resource: /organizations / {organization_id} / icon."""

    async def delete(self, *, if_match: str | Unset | None = UNSET) -> Result[wire.Organization]:
        """Delete Organization Icon. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_organization_icon.asyncio_detailed(
                client=client, organization_id=self._bindings["organization_id"], if_match=if_match
            )
        )

    async def get(self) -> Result[File]:
        """Get Organization Icon. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_organization_icon.asyncio_detailed(
                client=client, organization_id=self._bindings["organization_id"]
            )
        )

    def get_stream(self) -> AbstractAsyncContextManager[httpx2.Response]:
        """Unbuffered response; caller checks status and consumes within the context."""
        return self._stream(get_organization_icon.build_request(organization_id=self._bindings["organization_id"]))

    async def replace(self, *, body: File, if_match: str | Unset | None = UNSET) -> Result[wire.Organization]:
        """Put Organization Icon. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: put_organization_icon.asyncio_detailed(
                client=client, organization_id=self._bindings["organization_id"], body=body, if_match=if_match
            )
        )


class OrganizationsOrganizationIdInvitations(Resource):
    """Bound Native resource: /organizations / {organization_id} / invitations."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.InvitationPage]:
        """List Organization Invitations. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_organization_invitations.asyncio_detailed(
                client=client, organization_id=self._bindings["organization_id"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.InvitationPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> AsyncIterator[wire.Invitation]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    async def create(self, *, body: wire.InvitationCreate) -> Result[wire.InvitationReceipt]:
        """Create Organization Invitation. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_organization_invitation.asyncio_detailed(
                client=client, organization_id=self._bindings["organization_id"], body=body
            )
        )

    def __call__(self, invitation_id: str) -> OrganizationsOrganizationIdInvitationsInvitationId:
        return OrganizationsOrganizationIdInvitationsInvitationId(
            self._client, self._bind("invitation_id", invitation_id)
        )


class OrganizationsOrganizationIdInvitationsInvitationId(Resource):
    """Bound Native resource: /organizations / {organization_id} / invitations / {invitation_id}."""

    async def resend(self, *, if_match: str | Unset | None = UNSET) -> Result[wire.InvitationReceipt]:
        """Resend Organization Invitation. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: resend_organization_invitation.asyncio_detailed(
                client=client,
                organization_id=self._bindings["organization_id"],
                invitation_id=self._bindings["invitation_id"],
                if_match=if_match,
            )
        )

    async def revoke(self, *, if_match: str | Unset | None = UNSET) -> Result[wire.Invitation]:
        """Revoke Organization Invitation. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: revoke_organization_invitation.asyncio_detailed(
                client=client,
                organization_id=self._bindings["organization_id"],
                invitation_id=self._bindings["invitation_id"],
                if_match=if_match,
            )
        )


class OrganizationsOrganizationIdMembers(Resource):
    """Bound Native resource: /organizations / {organization_id} / members."""

    async def list(
        self,
        *,
        kind: wire.ListMembersKindType0 | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> Result[wire.MemberPage]:
        """List Members. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_members.asyncio_detailed(
                client=client, organization_id=self._bindings["organization_id"], kind=kind, limit=limit, cursor=cursor
            )
        )

    def pages(
        self,
        *,
        kind: wire.ListMembersKindType0 | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.MemberPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(kind=kind, limit=limit, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        kind: wire.ListMembersKindType0 | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.PrincipalSummary]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(kind=kind, limit=limit, cursor=cursor) for item in page.value.items)


class OrganizationsOrganizationIdWorkspaces(Resource):
    """Bound Native resource: /organizations / {organization_id} / workspaces."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.WorkspacePage]:
        """List Organization Workspaces. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_organization_workspaces.asyncio_detailed(
                client=client, organization_id=self._bindings["organization_id"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.WorkspacePage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> AsyncIterator[wire.Workspace]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    async def create(self, *, body: wire.WorkspaceCreate) -> Result[wire.Workspace]:
        """Create Workspace. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_workspace.asyncio_detailed(
                client=client, organization_id=self._bindings["organization_id"], body=body
            )
        )


class ProviderTypes(Resource):
    """Bound Native resource: /provider-types."""

    def __call__(self, kind: wire.ListProviderTypesKind) -> ProviderTypesKind:
        return ProviderTypesKind(self._client, self._bind("kind", str(kind)))


class ProviderTypesKind(Resource):
    """Bound Native resource: /provider-types / {kind}."""

    async def list(self) -> Result[wire.ProviderTypePage]:
        """List Provider Types. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_provider_types.asyncio_detailed(
                client=client, kind=wire.ListProviderTypesKind(self._bindings["kind"])
            )
        )


class Runs(Resource):
    """Bound Native resource: /runs."""

    async def list(
        self,
        *,
        text_query: str | Unset | None = UNSET,
        agent_id: str | Unset | None = UNSET,
        session_id: str | Unset | None = UNSET,
        thread_id: str | Unset | None = UNSET,
        principal_id: str | Unset | None = UNSET,
        status: wire.ListRunsStatusType0 | Unset | None = UNSET,
        created_after: datetime.datetime | Unset | None = UNSET,
        created_before: datetime.datetime | Unset | None = UNSET,
        view: wire.ListRunsView | Unset = UNSET,
        limit: int | Unset | None = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.RunPage | wire.RunSummaryPage]:
        """List Runs. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_runs.asyncio_detailed(
                client=client,
                text_query=text_query,
                agent_id=agent_id,
                session_id=session_id,
                thread_id=thread_id,
                principal_id=principal_id,
                status=status,
                created_after=created_after,
                created_before=created_before,
                view=view,
                limit=limit,
                cursor=cursor,
                x_workspace_id=x_workspace_id,
            )
        )

    def __call__(self, run_id: str) -> Run:
        return Run(self._client, self._bind("run_id", run_id))


class Run(Resource):
    """Bound Native resource: /runs / {run_id}."""

    async def get(
        self,
        *,
        view: wire.ReadView | Unset = UNSET,
        section: wire.GetRunSectionType0 | Unset | None = UNSET,
        offset: int | Unset = UNSET,
        limit: int | Unset = UNSET,
        version: str | Unset | None = UNSET,
        query: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.RunSummary | wire.RunView | wire.TextRead]:
        """Get Run. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_run.asyncio_detailed(
                client=client,
                run_id=self._bindings["run_id"],
                view=view,
                section=section,
                offset=offset,
                limit=limit,
                version=version,
                query=query,
                x_workspace_id=x_workspace_id,
            )
        )

    async def update(
        self, *, body: wire.RunLabels, if_match: str | Unset | None = UNSET, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.RunView]:
        """Update Run. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_run.asyncio_detailed(
                client=client,
                run_id=self._bindings["run_id"],
                body=body,
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )

    @property
    def agent(self) -> RunsRunIdAgent:
        return RunsRunIdAgent(self._client, self._bindings)

    @property
    def attempts(self) -> RunsRunIdAttempts:
        return RunsRunIdAttempts(self._client, self._bindings)

    @property
    def contents(self) -> RunsRunIdContents:
        return RunsRunIdContents(self._client, self._bindings)

    @property
    def desktop_assistance(self) -> RunsRunIdDesktopAssistance:
        return RunsRunIdDesktopAssistance(self._client, self._bindings)

    @property
    def desktop_control(self) -> RunsRunIdDesktopControl:
        return RunsRunIdDesktopControl(self._client, self._bindings)

    async def fork(
        self, *, body: wire.Fork, idempotency_key: str, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.Submitted]:
        """Fork Run. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: fork_run.asyncio_detailed(
                client=client,
                run_id=self._bindings["run_id"],
                body=body,
                idempotency_key=idempotency_key,
                x_workspace_id=x_workspace_id,
            )
        )

    @property
    def images(self) -> RunsRunIdImages:
        return RunsRunIdImages(self._client, self._bindings)

    async def interrupt(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.RunView]:
        """Interrupt Run. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: interrupt_run.asyncio_detailed(
                client=client, run_id=self._bindings["run_id"], x_workspace_id=x_workspace_id
            )
        )

    @property
    def items(self) -> RunsRunIdItems:
        return RunsRunIdItems(self._client, self._bindings)

    @property
    def lineage(self) -> RunsRunIdLineage:
        return RunsRunIdLineage(self._client, self._bindings)

    async def resume(
        self, *, body: wire.Resume, idempotency_key: str, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.RunView]:
        """Resume Run. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: resume_run.asyncio_detailed(
                client=client,
                run_id=self._bindings["run_id"],
                body=body,
                idempotency_key=idempotency_key,
                x_workspace_id=x_workspace_id,
            )
        )


class RunsRunIdAgent(Resource):
    """Bound Native resource: /runs / {run_id} / agent."""

    async def get(
        self,
        *,
        view: wire.ReadView | Unset = UNSET,
        section: wire.GetRunAgentSectionType0 | Unset | None = UNSET,
        part: wire.GetRunAgentPart | Unset = UNSET,
        offset: int | Unset = UNSET,
        limit: int | Unset = UNSET,
        version: str | Unset | None = UNSET,
        query: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.RunAgent | wire.RunAgentSummary | wire.TextRead]:
        """Get Run Agent. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_run_agent.asyncio_detailed(
                client=client,
                run_id=self._bindings["run_id"],
                view=view,
                section=section,
                part=part,
                offset=offset,
                limit=limit,
                version=version,
                query=query,
                x_workspace_id=x_workspace_id,
            )
        )


class RunsRunIdAttempts(Resource):
    """Bound Native resource: /runs / {run_id} / attempts."""

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.Attempts]:
        """List Run Attempts. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_run_attempts.asyncio_detailed(
                client=client, run_id=self._bindings["run_id"], x_workspace_id=x_workspace_id
            )
        )

    def __call__(self, attempt_id: str) -> RunsRunIdAttemptsAttemptId:
        return RunsRunIdAttemptsAttemptId(self._client, self._bind("attempt_id", attempt_id))


class RunsRunIdAttemptsAttemptId(Resource):
    """Bound Native resource: /runs / {run_id} / attempts / {attempt_id}."""

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.AttemptView]:
        """Get Run Attempt. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_run_attempt.asyncio_detailed(
                client=client,
                run_id=self._bindings["run_id"],
                attempt_id=self._bindings["attempt_id"],
                x_workspace_id=x_workspace_id,
            )
        )

    @property
    def trace(self) -> RunsRunIdAttemptsAttemptIdTrace:
        return RunsRunIdAttemptsAttemptIdTrace(self._client, self._bindings)


class RunsRunIdAttemptsAttemptIdTrace(Resource):
    """Bound Native resource: /runs / {run_id} / attempts / {attempt_id} / trace."""

    async def list(
        self,
        *,
        view: wire.ReadView | Unset = UNSET,
        status: wire.ListAttemptSpansStatusType0 | Unset | None = UNSET,
        kind: str | Unset | None = UNSET,
        tool_name: str | Unset | None = UNSET,
        limit: int | Unset | None = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.SpanPage | wire.SpanReadPage]:
        """List Attempt Spans. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_attempt_spans.asyncio_detailed(
                client=client,
                run_id=self._bindings["run_id"],
                attempt_id=self._bindings["attempt_id"],
                view=view,
                status=status,
                kind=kind,
                tool_name=tool_name,
                limit=limit,
                cursor=cursor,
                x_workspace_id=x_workspace_id,
            )
        )


class RunsRunIdContents(Resource):
    """Bound Native resource: /runs / {run_id} / contents."""

    def __call__(self, content_id: str) -> RunsRunIdContentsContentId:
        return RunsRunIdContentsContentId(self._client, self._bind("content_id", content_id))


class RunsRunIdContentsContentId(Resource):
    """Bound Native resource: /runs / {run_id} / contents / {content_id}."""

    async def get(
        self,
        *,
        view: wire.ReadView | Unset = UNSET,
        offset: int | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        version: str | Unset | None = UNSET,
        query: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.ContentSummary | wire.RunContent | wire.TextRead]:
        """Get Run Content. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_run_content.asyncio_detailed(
                client=client,
                run_id=self._bindings["run_id"],
                content_id=self._bindings["content_id"],
                view=view,
                offset=offset,
                limit=limit,
                version=version,
                query=query,
                x_workspace_id=x_workspace_id,
            )
        )


class RunsRunIdDesktopAssistance(Resource):
    """Bound Native resource: /runs / {run_id} / desktop-assistance."""

    def __call__(self, call_id: str) -> RunsRunIdDesktopAssistanceCallId:
        return RunsRunIdDesktopAssistanceCallId(self._client, self._bind("call_id", call_id))


class RunsRunIdDesktopAssistanceCallId(Resource):
    """Bound Native resource: /runs / {run_id} / desktop-assistance / {call_id}."""

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.View]:
        """Get Assistance. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_assistance.asyncio_detailed(
                client=client,
                run_id=self._bindings["run_id"],
                call_id=self._bindings["call_id"],
                x_workspace_id=x_workspace_id,
            )
        )


class RunsRunIdDesktopControl(Resource):
    """Bound Native resource: /runs / {run_id} / desktop-control."""

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.View | None]:
        """Get Control. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_control.asyncio_detailed(
                client=client, run_id=self._bindings["run_id"], x_workspace_id=x_workspace_id
            )
        )

    async def create(self, *, body: wire.Request, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.View]:
        """Open Control. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: open_control.asyncio_detailed(
                client=client, run_id=self._bindings["run_id"], body=body, x_workspace_id=x_workspace_id
            )
        )


class RunsRunIdImages(Resource):
    """Bound Native resource: /runs / {run_id} / images."""

    def __call__(self, image_id: str) -> RunsRunIdImagesImageId:
        return RunsRunIdImagesImageId(self._client, self._bind("image_id", image_id))


class RunsRunIdImagesImageId(Resource):
    """Bound Native resource: /runs / {run_id} / images / {image_id}."""

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[File]:
        """Run Image. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: run_image.asyncio_detailed(
                client=client,
                run_id=self._bindings["run_id"],
                image_id=self._bindings["image_id"],
                x_workspace_id=x_workspace_id,
            )
        )

    def get_stream(self, *, x_workspace_id: str | Unset | None = UNSET) -> AbstractAsyncContextManager[httpx2.Response]:
        """Unbuffered response; caller checks status and consumes within the context."""
        return self._stream(
            run_image.build_request(
                run_id=self._bindings["run_id"], image_id=self._bindings["image_id"], x_workspace_id=x_workspace_id
            )
        )


class RunsRunIdItems(Resource):
    """Bound Native resource: /runs / {run_id} / items."""

    async def list(
        self,
        *,
        before: int | Unset | None = UNSET,
        after: int | Unset | None = UNSET,
        limit: int | Unset | None = UNSET,
        view: wire.ReadView | Unset = UNSET,
        kind: wire.ItemKind | Unset | None = UNSET,
        state: wire.ItemState | Unset | None = UNSET,
        tool_name: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.ItemPage | wire.RunItems]:
        """List Run Items. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_run_items.asyncio_detailed(
                client=client,
                run_id=self._bindings["run_id"],
                before=before,
                after=after,
                limit=limit,
                view=view,
                kind=kind,
                state=state,
                tool_name=tool_name,
                x_workspace_id=x_workspace_id,
            )
        )

    def __call__(self, item_id: str) -> RunsRunIdItemsItemId:
        return RunsRunIdItemsItemId(self._client, self._bind("item_id", item_id))


class RunsRunIdItemsItemId(Resource):
    """Bound Native resource: /runs / {run_id} / items / {item_id}."""

    @property
    def content(self) -> RunsRunIdItemsItemIdContent:
        return RunsRunIdItemsItemIdContent(self._client, self._bindings)


class RunsRunIdItemsItemIdContent(Resource):
    """Bound Native resource: /runs / {run_id} / items / {item_id} / content."""

    async def get(
        self,
        *,
        ordinal: int,
        field: wire.ReadRunItemContentField | Unset = UNSET,
        offset: int | Unset = UNSET,
        limit: int | Unset = UNSET,
        version: str | Unset | None = UNSET,
        query: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.TextRead]:
        """Read Run Item Content. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: read_run_item_content.asyncio_detailed(
                client=client,
                run_id=self._bindings["run_id"],
                item_id=self._bindings["item_id"],
                ordinal=ordinal,
                field=field,
                offset=offset,
                limit=limit,
                version=version,
                query=query,
                x_workspace_id=x_workspace_id,
            )
        )


class RunsRunIdLineage(Resource):
    """Bound Native resource: /runs / {run_id} / lineage."""

    async def list(
        self,
        *,
        cursor: str | Unset | None = UNSET,
        view: wire.ReadView | Unset = UNSET,
        limit: int | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.RunPage | wire.RunSummaryPage]:
        """Get Run Lineage. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_run_lineage.asyncio_detailed(
                client=client,
                run_id=self._bindings["run_id"],
                cursor=cursor,
                view=view,
                limit=limit,
                x_workspace_id=x_workspace_id,
            )
        )


class Schedules(Resource):
    """Bound Native resource: /schedules."""

    async def list(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        state: wire.ScheduleState | Unset | None = UNSET,
        agent_id: str | Unset | None = UNSET,
        principal_id: str | Unset | None = UNSET,
        label: list[str] | Unset = UNSET,
        q: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.SchedulePage]:
        """List Schedules. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_schedules.asyncio_detailed(
                client=client,
                limit=limit,
                cursor=cursor,
                state=state,
                agent_id=agent_id,
                principal_id=principal_id,
                label=label,
                q=q,
                x_workspace_id=x_workspace_id,
            )
        )

    def pages(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        state: wire.ScheduleState | Unset | None = UNSET,
        agent_id: str | Unset | None = UNSET,
        principal_id: str | Unset | None = UNSET,
        label: list[str] | Unset = UNSET,
        q: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.SchedulePage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        label = label.copy() if isinstance(label, list) else label
        return pages(
            lambda next_cursor: self.list(
                limit=limit,
                state=state,
                agent_id=agent_id,
                principal_id=principal_id,
                label=label,
                q=q,
                x_workspace_id=x_workspace_id,
                cursor=next_cursor,
            ),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        state: wire.ScheduleState | Unset | None = UNSET,
        agent_id: str | Unset | None = UNSET,
        principal_id: str | Unset | None = UNSET,
        label: list[str] | Unset = UNSET,
        q: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.Schedule]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(
                limit=limit,
                cursor=cursor,
                state=state,
                agent_id=agent_id,
                principal_id=principal_id,
                label=label,
                q=q,
                x_workspace_id=x_workspace_id,
            )
            for item in page.value.items
        )

    async def create(
        self, *, body: wire.ScheduleCreate, idempotency_key: str, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.Schedule]:
        """Create Schedule. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_schedule.asyncio_detailed(
                client=client, body=body, idempotency_key=idempotency_key, x_workspace_id=x_workspace_id
            )
        )

    async def preview(
        self, *, body: wire.SchedulePreviewRequest, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.SchedulePreview]:
        """Preview Schedule. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: preview_schedule.asyncio_detailed(client=client, body=body, x_workspace_id=x_workspace_id)
        )

    def __call__(self, schedule_id: str) -> SchedulesScheduleId:
        return SchedulesScheduleId(self._client, self._bind("schedule_id", schedule_id))


class SchedulesScheduleId(Resource):
    """Bound Native resource: /schedules / {schedule_id}."""

    async def delete(
        self, *, if_match: str | Unset | None = UNSET, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[None]:
        """Archive Schedule. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: archive_schedule.asyncio_detailed(
                client=client,
                schedule_id=self._bindings["schedule_id"],
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.Schedule]:
        """Get Schedule. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_schedule.asyncio_detailed(
                client=client, schedule_id=self._bindings["schedule_id"], x_workspace_id=x_workspace_id
            )
        )

    async def update(
        self,
        *,
        body: wire.ScheduleUpdate,
        if_match: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.Schedule]:
        """Update Schedule. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_schedule.asyncio_detailed(
                client=client,
                schedule_id=self._bindings["schedule_id"],
                body=body,
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )

    async def dispatch(
        self,
        *,
        body: wire.ScheduleCommand,
        idempotency_key: str,
        if_match: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.Occurrence]:
        """Dispatch Schedule. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: dispatch_schedule.asyncio_detailed(
                client=client,
                schedule_id=self._bindings["schedule_id"],
                body=body,
                idempotency_key=idempotency_key,
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )

    async def enable(
        self,
        *,
        body: wire.ScheduleCommand,
        if_match: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.Schedule]:
        """Enable Schedule. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: enable_schedule.asyncio_detailed(
                client=client,
                schedule_id=self._bindings["schedule_id"],
                body=body,
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )

    @property
    def occurrences(self) -> SchedulesScheduleIdOccurrences:
        return SchedulesScheduleIdOccurrences(self._client, self._bindings)

    async def pause(
        self,
        *,
        body: wire.ScheduleCommand,
        if_match: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.Schedule]:
        """Pause Schedule. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: pause_schedule.asyncio_detailed(
                client=client,
                schedule_id=self._bindings["schedule_id"],
                body=body,
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )

    @property
    def status(self) -> SchedulesScheduleIdStatus:
        return SchedulesScheduleIdStatus(self._client, self._bindings)


class SchedulesScheduleIdOccurrences(Resource):
    """Bound Native resource: /schedules / {schedule_id} / occurrences."""

    async def list(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        status: wire.OccurrenceStatus | Unset | None = UNSET,
        trigger: wire.ScheduleTrigger | Unset | None = UNSET,
        created_after: datetime.datetime | Unset | None = UNSET,
        created_before: datetime.datetime | Unset | None = UNSET,
        unfinished: bool | Unset | None = UNSET,
        include: Literal["execution"] | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.OccurrencePage]:
        """List Schedule Occurrences. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_schedule_occurrences.asyncio_detailed(
                client=client,
                schedule_id=self._bindings["schedule_id"],
                limit=limit,
                cursor=cursor,
                status=status,
                trigger=trigger,
                created_after=created_after,
                created_before=created_before,
                unfinished=unfinished,
                include=include,
                x_workspace_id=x_workspace_id,
            )
        )

    def pages(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        status: wire.OccurrenceStatus | Unset | None = UNSET,
        trigger: wire.ScheduleTrigger | Unset | None = UNSET,
        created_after: datetime.datetime | Unset | None = UNSET,
        created_before: datetime.datetime | Unset | None = UNSET,
        unfinished: bool | Unset | None = UNSET,
        include: Literal["execution"] | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.OccurrencePage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(
                limit=limit,
                status=status,
                trigger=trigger,
                created_after=created_after,
                created_before=created_before,
                unfinished=unfinished,
                include=include,
                x_workspace_id=x_workspace_id,
                cursor=next_cursor,
            ),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        status: wire.OccurrenceStatus | Unset | None = UNSET,
        trigger: wire.ScheduleTrigger | Unset | None = UNSET,
        created_after: datetime.datetime | Unset | None = UNSET,
        created_before: datetime.datetime | Unset | None = UNSET,
        unfinished: bool | Unset | None = UNSET,
        include: Literal["execution"] | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.OccurrenceSummary]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(
                limit=limit,
                cursor=cursor,
                status=status,
                trigger=trigger,
                created_after=created_after,
                created_before=created_before,
                unfinished=unfinished,
                include=include,
                x_workspace_id=x_workspace_id,
            )
            for item in page.value.items
        )

    def __call__(self, occurrence_id: str) -> SchedulesScheduleIdOccurrencesOccurrenceId:
        return SchedulesScheduleIdOccurrencesOccurrenceId(self._client, self._bind("occurrence_id", occurrence_id))


class SchedulesScheduleIdOccurrencesOccurrenceId(Resource):
    """Bound Native resource: /schedules / {schedule_id} / occurrences / {occurrence_id}."""

    async def get(
        self, *, include: Literal["execution"] | Unset | None = UNSET, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.Occurrence]:
        """Get Schedule Occurrence. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_schedule_occurrence.asyncio_detailed(
                client=client,
                schedule_id=self._bindings["schedule_id"],
                occurrence_id=self._bindings["occurrence_id"],
                include=include,
                x_workspace_id=x_workspace_id,
            )
        )


class SchedulesScheduleIdStatus(Resource):
    """Bound Native resource: /schedules / {schedule_id} / status."""

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.ScheduleStatus]:
        """Get Schedule Status. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_schedule_status.asyncio_detailed(
                client=client, schedule_id=self._bindings["schedule_id"], x_workspace_id=x_workspace_id
            )
        )


class Sessions(Resource):
    """Bound Native resource: /sessions."""

    async def list(
        self,
        *,
        text_query: str | Unset | None = UNSET,
        q: str | Unset | None = UNSET,
        agent_id: str | Unset | None = UNSET,
        status: list[wire.RunStatus] | Unset = UNSET,
        trigger: list[wire.Trigger] | Unset = UNSET,
        updated_after: datetime.datetime | Unset | None = UNSET,
        updated_before: datetime.datetime | Unset | None = UNSET,
        label: list[str] | Unset = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.SessionPage]:
        """List Sessions. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_sessions.asyncio_detailed(
                client=client,
                text_query=text_query,
                q=q,
                agent_id=agent_id,
                status=status,
                trigger=trigger,
                updated_after=updated_after,
                updated_before=updated_before,
                label=label,
                limit=limit,
                cursor=cursor,
                x_workspace_id=x_workspace_id,
            )
        )

    def pages(
        self,
        *,
        text_query: str | Unset | None = UNSET,
        q: str | Unset | None = UNSET,
        agent_id: str | Unset | None = UNSET,
        status: list[wire.RunStatus] | Unset = UNSET,
        trigger: list[wire.Trigger] | Unset = UNSET,
        updated_after: datetime.datetime | Unset | None = UNSET,
        updated_before: datetime.datetime | Unset | None = UNSET,
        label: list[str] | Unset = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.SessionPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        status = status.copy() if isinstance(status, list) else status
        trigger = trigger.copy() if isinstance(trigger, list) else trigger
        label = label.copy() if isinstance(label, list) else label
        return pages(
            lambda next_cursor: self.list(
                text_query=text_query,
                q=q,
                agent_id=agent_id,
                status=status,
                trigger=trigger,
                updated_after=updated_after,
                updated_before=updated_before,
                label=label,
                limit=limit,
                x_workspace_id=x_workspace_id,
                cursor=next_cursor,
            ),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        text_query: str | Unset | None = UNSET,
        q: str | Unset | None = UNSET,
        agent_id: str | Unset | None = UNSET,
        status: list[wire.RunStatus] | Unset = UNSET,
        trigger: list[wire.Trigger] | Unset = UNSET,
        updated_after: datetime.datetime | Unset | None = UNSET,
        updated_before: datetime.datetime | Unset | None = UNSET,
        label: list[str] | Unset = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.SessionView]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(
                text_query=text_query,
                q=q,
                agent_id=agent_id,
                status=status,
                trigger=trigger,
                updated_after=updated_after,
                updated_before=updated_before,
                label=label,
                limit=limit,
                cursor=cursor,
                x_workspace_id=x_workspace_id,
            )
            for item in page.value.items
        )

    async def create(
        self, *, body: wire.SessionCreate, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.SessionView]:
        """Create Session. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_session.asyncio_detailed(client=client, body=body, x_workspace_id=x_workspace_id)
        )

    def __call__(self, session_id: str) -> Session:
        return Session(self._client, self._bind("session_id", session_id))


class Session(Resource):
    """Bound Native resource: /sessions / {session_id}."""

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.SessionView]:
        """Get Session. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_session.asyncio_detailed(
                client=client, session_id=self._bindings["session_id"], x_workspace_id=x_workspace_id
            )
        )

    async def update(
        self,
        *,
        body: wire.SessionUpdate,
        if_match: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.SessionView]:
        """Update Session. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_session.asyncio_detailed(
                client=client,
                session_id=self._bindings["session_id"],
                body=body,
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )

    @property
    def message_authors(self) -> SessionsSessionIdMessageAuthors:
        return SessionsSessionIdMessageAuthors(self._client, self._bindings)

    @property
    def stream(self) -> SessionsSessionIdStream:
        return SessionsSessionIdStream(self._client, self._bindings)


class SessionsSessionIdMessageAuthors(Resource):
    """Bound Native resource: /sessions / {session_id} / message-authors."""

    async def get(
        self, *, entry_id: list[str], x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.MessageAuthors]:
        """Get Message Authors. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_message_authors.asyncio_detailed(
                client=client, session_id=self._bindings["session_id"], entry_id=entry_id, x_workspace_id=x_workspace_id
            )
        )


class SessionsSessionIdStream(Resource):
    """Bound Native resource: /sessions / {session_id} / stream."""

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[Any]:
        """Session Stream. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: session_stream.asyncio_detailed(
                client=client, session_id=self._bindings["session_id"], x_workspace_id=x_workspace_id
            )
        )

    def get_stream(self, *, x_workspace_id: str | Unset | None = UNSET) -> AbstractAsyncContextManager[httpx2.Response]:
        """Unbuffered response; caller checks status and consumes within the context."""
        return self._stream(
            session_stream.build_request(session_id=self._bindings["session_id"], x_workspace_id=x_workspace_id)
        )


class Skills(Resource):
    """Bound Native resource: /skills."""

    async def list(
        self,
        *,
        label: list[str] | Unset | None = UNSET,
        q: str | Unset | None = UNSET,
        source: wire.ListSkillsSourceType0 | Unset | None = UNSET,
        archived: bool | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.SkillPage]:
        """List Skills. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_skills.asyncio_detailed(
                client=client,
                label=label,
                q=q,
                source=source,
                archived=archived,
                limit=limit,
                cursor=cursor,
                x_workspace_id=x_workspace_id,
            )
        )

    def pages(
        self,
        *,
        label: list[str] | Unset | None = UNSET,
        q: str | Unset | None = UNSET,
        source: wire.ListSkillsSourceType0 | Unset | None = UNSET,
        archived: bool | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.SkillPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        label = label.copy() if isinstance(label, list) else label
        return pages(
            lambda next_cursor: self.list(
                label=label,
                q=q,
                source=source,
                archived=archived,
                limit=limit,
                x_workspace_id=x_workspace_id,
                cursor=next_cursor,
            ),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        label: list[str] | Unset | None = UNSET,
        q: str | Unset | None = UNSET,
        source: wire.ListSkillsSourceType0 | Unset | None = UNSET,
        archived: bool | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.Skill]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(
                label=label,
                q=q,
                source=source,
                archived=archived,
                limit=limit,
                cursor=cursor,
                x_workspace_id=x_workspace_id,
            )
            for item in page.value.items
        )

    async def create(self, *, body: wire.SkillCreate, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.Skill]:
        """Create Skill. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_skill.asyncio_detailed(client=client, body=body, x_workspace_id=x_workspace_id)
        )

    async def validate(
        self, *, body: wire.SkillValidate, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.SkillManifest]:
        """Validate Skill. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: validate_skill.asyncio_detailed(client=client, body=body, x_workspace_id=x_workspace_id)
        )

    def __call__(self, skill_id: str) -> SkillsSkillId:
        return SkillsSkillId(self._client, self._bind("skill_id", skill_id))


class SkillsSkillId(Resource):
    """Bound Native resource: /skills / {skill_id}."""

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.Skill]:
        """Get Skill. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_skill.asyncio_detailed(
                client=client, skill_id=self._bindings["skill_id"], x_workspace_id=x_workspace_id
            )
        )

    async def update(
        self,
        *,
        body: wire.SkillUpdate,
        if_match: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.Skill]:
        """Update Skill. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_skill.asyncio_detailed(
                client=client,
                skill_id=self._bindings["skill_id"],
                body=body,
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )

    async def archive(
        self, *, if_match: str | Unset | None = UNSET, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.Skill]:
        """Archive Skill. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: archive_skill.asyncio_detailed(
                client=client, skill_id=self._bindings["skill_id"], if_match=if_match, x_workspace_id=x_workspace_id
            )
        )

    @property
    def revisions(self) -> SkillsSkillIdRevisions:
        return SkillsSkillIdRevisions(self._client, self._bindings)

    async def unarchive(
        self, *, if_match: str | Unset | None = UNSET, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.Skill]:
        """Unarchive Skill. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: unarchive_skill.asyncio_detailed(
                client=client, skill_id=self._bindings["skill_id"], if_match=if_match, x_workspace_id=x_workspace_id
            )
        )


class SkillsSkillIdRevisions(Resource):
    """Bound Native resource: /skills / {skill_id} / revisions."""

    async def list(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.SkillRevisionPage]:
        """List Skill Revisions. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_skill_revisions.asyncio_detailed(
                client=client,
                skill_id=self._bindings["skill_id"],
                limit=limit,
                cursor=cursor,
                x_workspace_id=x_workspace_id,
            )
        )

    def pages(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.SkillRevisionPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, x_workspace_id=x_workspace_id, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.SkillRevision]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(limit=limit, cursor=cursor, x_workspace_id=x_workspace_id)
            for item in page.value.items
        )

    async def create(
        self,
        *,
        body: wire.SkillRevisionCreate,
        if_match: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.SkillRevision]:
        """Create Skill Revision. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_skill_revision.asyncio_detailed(
                client=client,
                skill_id=self._bindings["skill_id"],
                body=body,
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )

    def __call__(self, revision_id: str) -> SkillsSkillIdRevisionsRevisionId:
        return SkillsSkillIdRevisionsRevisionId(self._client, self._bind("revision_id", revision_id))


class SkillsSkillIdRevisionsRevisionId(Resource):
    """Bound Native resource: /skills / {skill_id} / revisions / {revision_id}."""

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.SkillRevision]:
        """Get Skill Revision. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_skill_revision.asyncio_detailed(
                client=client,
                skill_id=self._bindings["skill_id"],
                revision_id=self._bindings["revision_id"],
                x_workspace_id=x_workspace_id,
            )
        )

    @property
    def content(self) -> SkillsSkillIdRevisionsRevisionIdContent:
        return SkillsSkillIdRevisionsRevisionIdContent(self._client, self._bindings)

    @property
    def files(self) -> SkillsSkillIdRevisionsRevisionIdFiles:
        return SkillsSkillIdRevisionsRevisionIdFiles(self._client, self._bindings)

    async def set_default(
        self, *, if_match: str | Unset | None = UNSET, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.Skill]:
        """Set Default Skill Revision. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: set_default_skill_revision.asyncio_detailed(
                client=client,
                skill_id=self._bindings["skill_id"],
                revision_id=self._bindings["revision_id"],
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )


class SkillsSkillIdRevisionsRevisionIdContent(Resource):
    """Bound Native resource: /skills / {skill_id} / revisions / {revision_id} / content."""

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[File]:
        """Read Skill Archive. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: read_skill_archive.asyncio_detailed(
                client=client,
                skill_id=self._bindings["skill_id"],
                revision_id=self._bindings["revision_id"],
                x_workspace_id=x_workspace_id,
            )
        )

    def get_stream(self, *, x_workspace_id: str | Unset | None = UNSET) -> AbstractAsyncContextManager[httpx2.Response]:
        """Unbuffered response; caller checks status and consumes within the context."""
        return self._stream(
            read_skill_archive.build_request(
                skill_id=self._bindings["skill_id"],
                revision_id=self._bindings["revision_id"],
                x_workspace_id=x_workspace_id,
            )
        )


class SkillsSkillIdRevisionsRevisionIdFiles(Resource):
    """Bound Native resource: /skills / {skill_id} / revisions / {revision_id} / files."""

    def __call__(self, path: str) -> SkillsSkillIdRevisionsRevisionIdFilesPath:
        return SkillsSkillIdRevisionsRevisionIdFilesPath(self._client, self._bind("path", path))


class SkillsSkillIdRevisionsRevisionIdFilesPath(Resource):
    """Bound Native resource: /skills / {skill_id} / revisions / {revision_id} / files / {path}."""

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[File]:
        """Read Skill File. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: read_skill_file.asyncio_detailed(
                client=client,
                skill_id=self._bindings["skill_id"],
                revision_id=self._bindings["revision_id"],
                path=self._bindings["path"],
                x_workspace_id=x_workspace_id,
            )
        )

    def get_stream(self, *, x_workspace_id: str | Unset | None = UNSET) -> AbstractAsyncContextManager[httpx2.Response]:
        """Unbuffered response; caller checks status and consumes within the context."""
        return self._stream(
            read_skill_file.build_request(
                skill_id=self._bindings["skill_id"],
                revision_id=self._bindings["revision_id"],
                path=self._bindings["path"],
                x_workspace_id=x_workspace_id,
            )
        )


class Subscriptions(Resource):
    """Bound Native resource: /subscriptions."""

    async def list(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.SubscriptionPage]:
        """List Subscriptions. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_subscriptions.asyncio_detailed(
                client=client, limit=limit, cursor=cursor, x_workspace_id=x_workspace_id
            )
        )

    def pages(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.SubscriptionPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, x_workspace_id=x_workspace_id, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.Subscription]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(limit=limit, cursor=cursor, x_workspace_id=x_workspace_id)
            for item in page.value.items
        )

    async def create(
        self, *, body: wire.SubscriptionCreate, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.CreatedSubscription]:
        """Create Subscription. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_subscription.asyncio_detailed(client=client, body=body, x_workspace_id=x_workspace_id)
        )

    def __call__(self, subscription_id: str) -> SubscriptionsSubscriptionId:
        return SubscriptionsSubscriptionId(self._client, self._bind("subscription_id", subscription_id))


class SubscriptionsSubscriptionId(Resource):
    """Bound Native resource: /subscriptions / {subscription_id}."""

    async def delete(
        self, *, if_match: str | Unset | None = UNSET, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[None]:
        """Delete Subscription. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_subscription.asyncio_detailed(
                client=client,
                subscription_id=self._bindings["subscription_id"],
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.Subscription]:
        """Get Subscription. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_subscription.asyncio_detailed(
                client=client, subscription_id=self._bindings["subscription_id"], x_workspace_id=x_workspace_id
            )
        )

    async def update(
        self,
        *,
        body: wire.SubscriptionUpdate,
        if_match: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.Subscription]:
        """Update Subscription. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_subscription.asyncio_detailed(
                client=client,
                subscription_id=self._bindings["subscription_id"],
                body=body,
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )

    @property
    def deliveries(self) -> SubscriptionsSubscriptionIdDeliveries:
        return SubscriptionsSubscriptionIdDeliveries(self._client, self._bindings)


class SubscriptionsSubscriptionIdDeliveries(Resource):
    """Bound Native resource: /subscriptions / {subscription_id} / deliveries."""

    async def list(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.DeliveryPage]:
        """List Deliveries. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_deliveries.asyncio_detailed(
                client=client,
                subscription_id=self._bindings["subscription_id"],
                limit=limit,
                cursor=cursor,
                x_workspace_id=x_workspace_id,
            )
        )

    def pages(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.DeliveryPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, x_workspace_id=x_workspace_id, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.WebhookDelivery]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(limit=limit, cursor=cursor, x_workspace_id=x_workspace_id)
            for item in page.value.items
        )

    def __call__(self, delivery_id: str) -> SubscriptionsSubscriptionIdDeliveriesDeliveryId:
        return SubscriptionsSubscriptionIdDeliveriesDeliveryId(self._client, self._bind("delivery_id", delivery_id))


class SubscriptionsSubscriptionIdDeliveriesDeliveryId(Resource):
    """Bound Native resource: /subscriptions / {subscription_id} / deliveries / {delivery_id}."""

    async def redeliver(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.WebhookDelivery]:
        """Redeliver. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: redeliver.asyncio_detailed(
                client=client,
                subscription_id=self._bindings["subscription_id"],
                delivery_id=self._bindings["delivery_id"],
                x_workspace_id=x_workspace_id,
            )
        )


class Threads(Resource):
    """Bound Native resource: /threads."""

    async def list(
        self,
        *,
        session_id: str | Unset | None = UNSET,
        occurrence_id: str | Unset | None = UNSET,
        text_query: str | Unset | None = UNSET,
        label: list[str] | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.ThreadPage]:
        """List Threads. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_threads.asyncio_detailed(
                client=client,
                session_id=session_id,
                occurrence_id=occurrence_id,
                text_query=text_query,
                label=label,
                limit=limit,
                cursor=cursor,
                x_workspace_id=x_workspace_id,
            )
        )

    def pages(
        self,
        *,
        session_id: str | Unset | None = UNSET,
        occurrence_id: str | Unset | None = UNSET,
        text_query: str | Unset | None = UNSET,
        label: list[str] | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.ThreadPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        label = label.copy() if isinstance(label, list) else label
        return pages(
            lambda next_cursor: self.list(
                session_id=session_id,
                occurrence_id=occurrence_id,
                text_query=text_query,
                label=label,
                limit=limit,
                x_workspace_id=x_workspace_id,
                cursor=next_cursor,
            ),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        session_id: str | Unset | None = UNSET,
        occurrence_id: str | Unset | None = UNSET,
        text_query: str | Unset | None = UNSET,
        label: list[str] | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.ThreadView]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(
                session_id=session_id,
                occurrence_id=occurrence_id,
                text_query=text_query,
                label=label,
                limit=limit,
                cursor=cursor,
                x_workspace_id=x_workspace_id,
            )
            for item in page.value.items
        )

    async def create(
        self, *, body: wire.NewThread, idempotency_key: str, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.Submitted]:
        """Create Thread. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_thread.asyncio_detailed(
                client=client, body=body, idempotency_key=idempotency_key, x_workspace_id=x_workspace_id
            )
        )

    def __call__(self, thread_id: str) -> Thread:
        return Thread(self._client, self._bind("thread_id", thread_id))


class Thread(Resource):
    """Bound Native resource: /threads / {thread_id}."""

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.ThreadView]:
        """Get Thread. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_thread.asyncio_detailed(
                client=client, thread_id=self._bindings["thread_id"], x_workspace_id=x_workspace_id
            )
        )

    async def update(
        self,
        *,
        body: wire.ThreadUpdate,
        if_match: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.ThreadView]:
        """Update Thread. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_thread.asyncio_detailed(
                client=client,
                thread_id=self._bindings["thread_id"],
                body=body,
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )

    async def archive(
        self, *, if_match: str | Unset | None = UNSET, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.ThreadView]:
        """Archive Thread. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: archive_thread.asyncio_detailed(
                client=client, thread_id=self._bindings["thread_id"], if_match=if_match, x_workspace_id=x_workspace_id
            )
        )

    @property
    def environments(self) -> ThreadsThreadIdEnvironments:
        return ThreadsThreadIdEnvironments(self._client, self._bindings)

    @property
    def inbox_entries(self) -> ThreadsThreadIdInbox:
        return ThreadsThreadIdInbox(self._client, self._bindings)

    @property
    def memories(self) -> ThreadsThreadIdMemories:
        return ThreadsThreadIdMemories(self._client, self._bindings)

    @property
    def runs(self) -> ThreadsThreadIdRuns:
        return ThreadsThreadIdRuns(self._client, self._bindings)

    @property
    def stream(self) -> ThreadsThreadIdStream:
        return ThreadsThreadIdStream(self._client, self._bindings)


class ThreadsThreadIdEnvironments(Resource):
    """Bound Native resource: /threads / {thread_id} / environments."""

    async def list(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.MountPage]:
        """List Environment Mounts. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_environment_mounts.asyncio_detailed(
                client=client, thread_id=self._bindings["thread_id"], x_workspace_id=x_workspace_id
            )
        )

    async def create(
        self,
        *,
        body: wire.MountCreate,
        if_match: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.MountView]:
        """Add Environment Mount. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: add_environment_mount.asyncio_detailed(
                client=client,
                thread_id=self._bindings["thread_id"],
                body=body,
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )

    def __call__(self, name: str) -> ThreadsThreadIdEnvironmentsName:
        return ThreadsThreadIdEnvironmentsName(self._client, self._bind("name", name))


class ThreadsThreadIdEnvironmentsName(Resource):
    """Bound Native resource: /threads / {thread_id} / environments / {name}."""

    async def delete(
        self, *, if_match: str | Unset | None = UNSET, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[None]:
        """Remove Environment Mount. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: remove_environment_mount.asyncio_detailed(
                client=client,
                thread_id=self._bindings["thread_id"],
                name=self._bindings["name"],
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )

    async def update(
        self,
        *,
        body: wire.MountUpdate,
        if_match: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.MountView]:
        """Update Environment Mount. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_environment_mount.asyncio_detailed(
                client=client,
                thread_id=self._bindings["thread_id"],
                name=self._bindings["name"],
                body=body,
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )


class ThreadsThreadIdInbox(Resource):
    """Bound Native resource: /threads / {thread_id} / inbox."""

    async def list(
        self,
        *,
        status: list[wire.EntryStatus] | Unset | None = UNSET,
        view: wire.ReadView | Unset = UNSET,
        kind: wire.ListInboxKindType0 | Unset | None = UNSET,
        limit: int | Unset | None = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.EntryPage | wire.EntrySummaryPage]:
        """List Inbox. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_inbox.asyncio_detailed(
                client=client,
                thread_id=self._bindings["thread_id"],
                status=status,
                view=view,
                kind=kind,
                limit=limit,
                cursor=cursor,
                x_workspace_id=x_workspace_id,
            )
        )

    async def create(
        self, *, body: wire.Message, idempotency_key: str, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.Submitted]:
        """Submit Message. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: submit_message.asyncio_detailed(
                client=client,
                thread_id=self._bindings["thread_id"],
                body=body,
                idempotency_key=idempotency_key,
                x_workspace_id=x_workspace_id,
            )
        )

    @property
    def order(self) -> ThreadsThreadIdInboxOrder:
        return ThreadsThreadIdInboxOrder(self._client, self._bindings)

    def __call__(self, entry_id: str) -> InboxEntry:
        return InboxEntry(self._client, self._bind("entry_id", entry_id))


class ThreadsThreadIdInboxOrder(Resource):
    """Bound Native resource: /threads / {thread_id} / inbox / order."""

    async def replace(
        self, *, body: wire.InboxOrder, if_match: str | Unset | None = UNSET, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.ThreadView]:
        """Reorder Inbox. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: reorder_inbox.asyncio_detailed(
                client=client,
                thread_id=self._bindings["thread_id"],
                body=body,
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )


class InboxEntry(Resource):
    """Bound Native resource: /threads / {thread_id} / inbox / {entry_id}."""

    async def delete(
        self, *, if_match: str | Unset | None = UNSET, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.Submitted]:
        """Withdraw Entry. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: withdraw_entry.asyncio_detailed(
                client=client,
                thread_id=self._bindings["thread_id"],
                entry_id=self._bindings["entry_id"],
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )

    async def get(
        self,
        *,
        view: wire.ReadView | Unset = UNSET,
        section: wire.GetInboxEntrySectionType0 | Unset | None = UNSET,
        offset: int | Unset = UNSET,
        limit: int | Unset = UNSET,
        version: str | Unset | None = UNSET,
        query: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.EntrySummary | wire.EntryView | wire.TextRead]:
        """Get Inbox Entry. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_inbox_entry.asyncio_detailed(
                client=client,
                thread_id=self._bindings["thread_id"],
                entry_id=self._bindings["entry_id"],
                view=view,
                section=section,
                offset=offset,
                limit=limit,
                version=version,
                query=query,
                x_workspace_id=x_workspace_id,
            )
        )

    async def update(
        self,
        *,
        body: wire.EntryUpdate,
        if_match: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.Submitted]:
        """Edit Entry. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: edit_entry.asyncio_detailed(
                client=client,
                thread_id=self._bindings["thread_id"],
                entry_id=self._bindings["entry_id"],
                body=body,
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )


class ThreadsThreadIdMemories(Resource):
    """Bound Native resource: /threads / {thread_id} / memories."""

    async def list(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.MemoryMountPage]:
        """List Memory Mounts. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_memory_mounts.asyncio_detailed(
                client=client, thread_id=self._bindings["thread_id"], x_workspace_id=x_workspace_id
            )
        )

    async def create(
        self,
        *,
        body: wire.MemoryMount,
        if_match: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.MemoryMount]:
        """Add Memory Mount. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: add_memory_mount.asyncio_detailed(
                client=client,
                thread_id=self._bindings["thread_id"],
                body=body,
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )

    def __call__(self, name: str) -> ThreadsThreadIdMemoriesName:
        return ThreadsThreadIdMemoriesName(self._client, self._bind("name", name))


class ThreadsThreadIdMemoriesName(Resource):
    """Bound Native resource: /threads / {thread_id} / memories / {name}."""

    async def delete(
        self, *, if_match: str | Unset | None = UNSET, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[None]:
        """Remove Memory Mount. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: remove_memory_mount.asyncio_detailed(
                client=client,
                thread_id=self._bindings["thread_id"],
                name=self._bindings["name"],
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )

    async def update(
        self,
        *,
        body: wire.MemoryMountUpdate,
        if_match: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.MemoryMount]:
        """Update Memory Mount. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_memory_mount.asyncio_detailed(
                client=client,
                thread_id=self._bindings["thread_id"],
                name=self._bindings["name"],
                body=body,
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )


class ThreadsThreadIdRuns(Resource):
    """Bound Native resource: /threads / {thread_id} / runs."""

    async def list(
        self,
        *,
        view: wire.ReadView | Unset = UNSET,
        limit: int | Unset | None = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.RunPage | wire.RunSummaryPage]:
        """List Thread Runs. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_thread_runs.asyncio_detailed(
                client=client,
                thread_id=self._bindings["thread_id"],
                view=view,
                limit=limit,
                cursor=cursor,
                x_workspace_id=x_workspace_id,
            )
        )


class ThreadsThreadIdStream(Resource):
    """Bound Native resource: /threads / {thread_id} / stream."""

    async def get(
        self,
        *,
        run: str | Unset | None = UNSET,
        position: str | Unset | None = UNSET,
        last_event_id: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[Any]:
        """Thread Stream. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: thread_stream.asyncio_detailed(
                client=client,
                thread_id=self._bindings["thread_id"],
                run=run,
                position=position,
                last_event_id=last_event_id,
                x_workspace_id=x_workspace_id,
            )
        )

    def get_stream(
        self,
        *,
        run: str | Unset | None = UNSET,
        position: str | Unset | None = UNSET,
        last_event_id: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AbstractAsyncContextManager[httpx2.Response]:
        """Unbuffered response; caller checks status and consumes within the context."""
        return self._stream(
            thread_stream.build_request(
                thread_id=self._bindings["thread_id"],
                run=run,
                position=position,
                last_event_id=last_event_id,
                x_workspace_id=x_workspace_id,
            )
        )


class Toolsets(Resource):
    """Bound Native resource: /toolsets."""

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.ToolsetCatalog]:
        """List Toolsets. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_toolsets.asyncio_detailed(client=client, x_workspace_id=x_workspace_id)
        )

    @property
    def definitions(self) -> ToolsetsDefinitions:
        return ToolsetsDefinitions(self._client, self._bindings)

    @property
    def index(self) -> ToolsetsIndex:
        return ToolsetsIndex(self._client, self._bindings)


class ToolsetsDefinitions(Resource):
    """Bound Native resource: /toolsets / definitions."""

    async def get(
        self,
        *,
        name: list[str],
        offset: int | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        version: str | Unset | None = UNSET,
        query: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.Definitions | wire.TextRead]:
        """Define Toolsets. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: define_toolsets.asyncio_detailed(
                client=client,
                name=name,
                offset=offset,
                limit=limit,
                version=version,
                query=query,
                x_workspace_id=x_workspace_id,
            )
        )


class ToolsetsIndex(Resource):
    """Bound Native resource: /toolsets / index."""

    async def get(
        self,
        *,
        query: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.CatalogIndex]:
        """Index Toolsets. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: index_toolsets.asyncio_detailed(
                client=client, query=query, limit=limit, cursor=cursor, x_workspace_id=x_workspace_id
            )
        )


class TraceBackend(Resource):
    """Bound Native resource: /trace-backend."""

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.TraceBackend]:
        """Get Trace Backend. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_trace_backend.asyncio_detailed(client=client, x_workspace_id=x_workspace_id)
        )


class Traces(Resource):
    """Bound Native resource: /traces."""

    async def list(
        self,
        *,
        session_id: str | Unset | None = UNSET,
        thread_id: str | Unset | None = UNSET,
        run_id: str | Unset | None = UNSET,
        attribute: list[str] | Unset | None = UNSET,
        started_after: datetime.datetime | Unset | None = UNSET,
        started_before: datetime.datetime | Unset | None = UNSET,
        view: wire.ReadView | Unset = UNSET,
        status: wire.ListTracesStatusType0 | Unset | None = UNSET,
        kind: str | Unset | None = UNSET,
        tool_name: str | Unset | None = UNSET,
        limit: int | Unset | None = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.SpanPage | wire.SpanReadPage]:
        """List Traces. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_traces.asyncio_detailed(
                client=client,
                session_id=session_id,
                thread_id=thread_id,
                run_id=run_id,
                attribute=attribute,
                started_after=started_after,
                started_before=started_before,
                view=view,
                status=status,
                kind=kind,
                tool_name=tool_name,
                limit=limit,
                cursor=cursor,
                x_workspace_id=x_workspace_id,
            )
        )

    def __call__(self, trace_id: str) -> TracesTraceId:
        return TracesTraceId(self._client, self._bind("trace_id", trace_id))


class TracesTraceId(Resource):
    """Bound Native resource: /traces / {trace_id}."""

    async def get(
        self,
        *,
        view: wire.ReadView | Unset = UNSET,
        section: wire.GetTraceSectionType0 | Unset | None = UNSET,
        offset: int | Unset = UNSET,
        limit: int | Unset = UNSET,
        version: str | Unset | None = UNSET,
        query: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.Span | wire.SpanSummary | wire.TextRead]:
        """Get Trace. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_trace.asyncio_detailed(
                client=client,
                trace_id=self._bindings["trace_id"],
                view=view,
                section=section,
                offset=offset,
                limit=limit,
                version=version,
                query=query,
                x_workspace_id=x_workspace_id,
            )
        )

    @property
    def spans(self) -> TracesTraceIdSpans:
        return TracesTraceIdSpans(self._client, self._bindings)


class TracesTraceIdSpans(Resource):
    """Bound Native resource: /traces / {trace_id} / spans."""

    async def list(
        self,
        *,
        view: wire.ReadView | Unset = UNSET,
        status: wire.ListTraceSpansStatusType0 | Unset | None = UNSET,
        kind: str | Unset | None = UNSET,
        tool_name: str | Unset | None = UNSET,
        limit: int | Unset | None = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.SpanPage | wire.SpanReadPage]:
        """List Trace Spans. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_trace_spans.asyncio_detailed(
                client=client,
                trace_id=self._bindings["trace_id"],
                view=view,
                status=status,
                kind=kind,
                tool_name=tool_name,
                limit=limit,
                cursor=cursor,
                x_workspace_id=x_workspace_id,
            )
        )

    def __call__(self, span_id: str) -> TracesTraceIdSpansSpanId:
        return TracesTraceIdSpansSpanId(self._client, self._bind("span_id", span_id))


class TracesTraceIdSpansSpanId(Resource):
    """Bound Native resource: /traces / {trace_id} / spans / {span_id}."""

    @property
    def content(self) -> TracesTraceIdSpansSpanIdContent:
        return TracesTraceIdSpansSpanIdContent(self._client, self._bindings)


class TracesTraceIdSpansSpanIdContent(Resource):
    """Bound Native resource: /traces / {trace_id} / spans / {span_id} / content."""

    async def list(
        self,
        *,
        section: wire.ReadSpanContentSection | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        offset: int | Unset = UNSET,
        limit: int | Unset = UNSET,
        version: str | Unset | None = UNSET,
        query: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.SpanContentPage]:
        """Read Span Content. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: read_span_content.asyncio_detailed(
                client=client,
                trace_id=self._bindings["trace_id"],
                span_id=self._bindings["span_id"],
                section=section,
                cursor=cursor,
                offset=offset,
                limit=limit,
                version=version,
                query=query,
                x_workspace_id=x_workspace_id,
            )
        )

    def pages(
        self,
        *,
        section: wire.ReadSpanContentSection | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        offset: int | Unset = UNSET,
        limit: int | Unset = UNSET,
        version: str | Unset | None = UNSET,
        query: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.SpanContentPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(
                section=section,
                offset=offset,
                limit=limit,
                version=version,
                query=query,
                x_workspace_id=x_workspace_id,
                cursor=next_cursor,
            ),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        section: wire.ReadSpanContentSection | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        offset: int | Unset = UNSET,
        limit: int | Unset = UNSET,
        version: str | Unset | None = UNSET,
        query: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.TextRead]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(
                section=section,
                cursor=cursor,
                offset=offset,
                limit=limit,
                version=version,
                query=query,
                x_workspace_id=x_workspace_id,
            )
            for item in page.value.items
        )


class Uploads(Resource):
    """Bound Native resource: /uploads."""

    async def create(
        self, *, body: wire.UploadCreate, idempotency_key: str, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.Upload]:
        """Create Upload. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_upload.asyncio_detailed(
                client=client, body=body, idempotency_key=idempotency_key, x_workspace_id=x_workspace_id
            )
        )


class Usage(Resource):
    """Bound Native resource: /usage."""

    async def get(
        self,
        *,
        run_id: str | Unset | None = UNSET,
        thread_id: str | Unset | None = UNSET,
        session_id: str | Unset | None = UNSET,
        ingested_after: datetime.datetime | Unset | None = UNSET,
        ingested_before: datetime.datetime | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.UsageSummary]:
        """Summarize Usage. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: summarize_usage.asyncio_detailed(
                client=client,
                run_id=run_id,
                thread_id=thread_id,
                session_id=session_id,
                ingested_after=ingested_after,
                ingested_before=ingested_before,
                x_workspace_id=x_workspace_id,
            )
        )

    @property
    def agents(self) -> UsageAgents:
        return UsageAgents(self._client, self._bindings)

    @property
    def context(self) -> UsageContext:
        return UsageContext(self._client, self._bindings)

    @property
    def models(self) -> UsageModels:
        return UsageModels(self._client, self._bindings)

    @property
    def overview(self) -> UsageOverview:
        return UsageOverview(self._client, self._bindings)

    @property
    def records(self) -> UsageRecords:
        return UsageRecords(self._client, self._bindings)


class UsageAgents(Resource):
    """Bound Native resource: /usage / agents."""

    async def list(
        self,
        *,
        start: datetime.datetime,
        end: datetime.datetime,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.AgentUsagePage]:
        """Usage Agents. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: usage_agents.asyncio_detailed(
                client=client, start=start, end=end, limit=limit, cursor=cursor, x_workspace_id=x_workspace_id
            )
        )

    def pages(
        self,
        *,
        start: datetime.datetime,
        end: datetime.datetime,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.AgentUsagePage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(
                start=start, end=end, limit=limit, x_workspace_id=x_workspace_id, cursor=next_cursor
            ),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        start: datetime.datetime,
        end: datetime.datetime,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.AgentUsage]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(
                start=start, end=end, limit=limit, cursor=cursor, x_workspace_id=x_workspace_id
            )
            for item in page.value.items
        )


class UsageContext(Resource):
    """Bound Native resource: /usage / context."""

    async def get(
        self,
        *,
        thread_id: str | Unset | None = UNSET,
        run_id: str | Unset | None = UNSET,
        record_id: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.ContextUsage | None]:
        """Context Usage. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: context_usage.asyncio_detailed(
                client=client, thread_id=thread_id, run_id=run_id, record_id=record_id, x_workspace_id=x_workspace_id
            )
        )


class UsageModels(Resource):
    """Bound Native resource: /usage / models."""

    async def list(
        self,
        *,
        start: datetime.datetime,
        end: datetime.datetime,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.ModelUsagePage]:
        """Usage Models. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: usage_models.asyncio_detailed(
                client=client, start=start, end=end, limit=limit, cursor=cursor, x_workspace_id=x_workspace_id
            )
        )

    def pages(
        self,
        *,
        start: datetime.datetime,
        end: datetime.datetime,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.ModelUsagePage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(
                start=start, end=end, limit=limit, x_workspace_id=x_workspace_id, cursor=next_cursor
            ),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        start: datetime.datetime,
        end: datetime.datetime,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.ModelUsageGroup]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(
                start=start, end=end, limit=limit, cursor=cursor, x_workspace_id=x_workspace_id
            )
            for item in page.value.items
        )


class UsageOverview(Resource):
    """Bound Native resource: /usage / overview."""

    async def get(
        self,
        *,
        start: datetime.datetime,
        end: datetime.datetime,
        timezone: str | Unset = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.UsageOverview]:
        """Usage Overview. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: usage_overview.asyncio_detailed(
                client=client, start=start, end=end, timezone=timezone, x_workspace_id=x_workspace_id
            )
        )


class UsageRecords(Resource):
    """Bound Native resource: /usage / records."""

    def __call__(self, record_id: str) -> UsageRecordsRecordId:
        return UsageRecordsRecordId(self._client, self._bind("record_id", record_id))


class UsageRecordsRecordId(Resource):
    """Bound Native resource: /usage / records / {record_id}."""

    @property
    def metrics(self) -> UsageRecordsRecordIdMetrics:
        return UsageRecordsRecordIdMetrics(self._client, self._bindings)


class UsageRecordsRecordIdMetrics(Resource):
    """Bound Native resource: /usage / records / {record_id} / metrics."""

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.ModelRequestMetrics]:
        """Model Request Metrics. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: model_request_metrics.asyncio_detailed(
                client=client, record_id=self._bindings["record_id"], x_workspace_id=x_workspace_id
            )
        )


class Users(Resource):
    """Bound Native resource: /users."""

    @property
    def me(self) -> UsersMe:
        return UsersMe(self._client, self._bindings)

    def __call__(self, user_id: str) -> UsersUserId:
        return UsersUserId(self._client, self._bind("user_id", user_id))


class UsersMe(Resource):
    """Bound Native resource: /users / me."""

    async def get(self) -> Result[wire.Profile]:
        """Get Profile. One HTTP request; no automatic replay."""
        return await self._call(lambda client: get_profile.asyncio_detailed(client=client))

    async def update(self, *, body: wire.ProfileUpdate, if_match: str | Unset | None = UNSET) -> Result[wire.Profile]:
        """Update Profile. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_profile.asyncio_detailed(client=client, body=body, if_match=if_match)
        )

    @property
    def audit_events(self) -> UsersMeAuditEvents:
        return UsersMeAuditEvents(self._client, self._bindings)

    @property
    def avatar(self) -> UsersMeAvatar:
        return UsersMeAvatar(self._client, self._bindings)

    async def disable(self, *, body: wire.AccountDisable) -> Result[None]:
        """Disable Account. One HTTP request; no automatic replay."""
        return await self._call(lambda client: disable_account.asyncio_detailed(client=client, body=body))

    @property
    def keys(self) -> UsersMeKeys:
        return UsersMeKeys(self._client, self._bindings)

    @property
    def login_sessions(self) -> UsersMeLoginSessions:
        return UsersMeLoginSessions(self._client, self._bindings)

    async def password(self, *, body: wire.PasswordChange) -> Result[None]:
        """Change Password. One HTTP request; no automatic replay."""
        return await self._call(lambda client: change_password.asyncio_detailed(client=client, body=body))


class UsersMeAuditEvents(Resource):
    """Bound Native resource: /users / me / audit-events."""

    async def list(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> Result[wire.AuditPage]:
        """List Account Audit Events. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_account_audit_events.asyncio_detailed(client=client, limit=limit, cursor=cursor)
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.AuditPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> AsyncIterator[wire.AuditEvent]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)


class UsersMeAvatar(Resource):
    """Bound Native resource: /users / me / avatar."""

    async def delete(self, *, if_match: str | Unset | None = UNSET) -> Result[wire.Profile]:
        """Delete User Avatar. One HTTP request; no automatic replay."""
        return await self._call(lambda client: delete_user_avatar.asyncio_detailed(client=client, if_match=if_match))

    async def replace(self, *, body: File, if_match: str | Unset | None = UNSET) -> Result[wire.Profile]:
        """Put User Avatar. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: put_user_avatar.asyncio_detailed(client=client, body=body, if_match=if_match)
        )


class UsersMeKeys(Resource):
    """Bound Native resource: /users / me / keys."""

    async def list(
        self,
        *,
        workspace_id: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> Result[wire.ApiKeyPage]:
        """List User Keys. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_user_keys.asyncio_detailed(
                client=client, workspace_id=workspace_id, limit=limit, cursor=cursor
            )
        )

    def pages(
        self,
        *,
        workspace_id: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.ApiKeyPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(workspace_id=workspace_id, limit=limit, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        workspace_id: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.ApiKey]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(workspace_id=workspace_id, limit=limit, cursor=cursor)
            for item in page.value.items
        )

    async def create(self, *, body: wire.UserKeyCreate) -> Result[wire.IssuedKey]:
        """Create User Key. One HTTP request; no automatic replay."""
        return await self._call(lambda client: create_user_key.asyncio_detailed(client=client, body=body))

    def __call__(self, key_id: str) -> UsersMeKeysKeyId:
        return UsersMeKeysKeyId(self._client, self._bind("key_id", key_id))


class UsersMeKeysKeyId(Resource):
    """Bound Native resource: /users / me / keys / {key_id}."""

    async def delete(self, *, if_match: str | Unset | None = UNSET) -> Result[wire.ApiKey]:
        """Revoke User Key. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: revoke_user_key.asyncio_detailed(
                client=client, key_id=self._bindings["key_id"], if_match=if_match
            )
        )


class UsersMeLoginSessions(Resource):
    """Bound Native resource: /users / me / login-sessions."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.LoginSessionPage]:
        """List Login Sessions. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_login_sessions.asyncio_detailed(client=client, limit=limit, cursor=cursor)
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.LoginSessionPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.LoginSession]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    def __call__(self, session_id: str) -> UsersMeLoginSessionsSessionId:
        return UsersMeLoginSessionsSessionId(self._client, self._bind("session_id", session_id))


class UsersMeLoginSessionsSessionId(Resource):
    """Bound Native resource: /users / me / login-sessions / {session_id}."""

    async def delete(self) -> Result[None]:
        """Revoke Login Session. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: revoke_login_session.asyncio_detailed(client=client, session_id=self._bindings["session_id"])
        )


class UsersUserId(Resource):
    """Bound Native resource: /users / {user_id}."""

    @property
    def avatar(self) -> UsersUserIdAvatar:
        return UsersUserIdAvatar(self._client, self._bindings)


class UsersUserIdAvatar(Resource):
    """Bound Native resource: /users / {user_id} / avatar."""

    async def get(self) -> Result[File]:
        """Get User Avatar. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_user_avatar.asyncio_detailed(client=client, user_id=self._bindings["user_id"])
        )

    def get_stream(self) -> AbstractAsyncContextManager[httpx2.Response]:
        """Unbuffered response; caller checks status and consumes within the context."""
        return self._stream(get_user_avatar.build_request(user_id=self._bindings["user_id"]))


class WebProviders(Resource):
    """Bound Native resource: /web-providers."""

    async def list(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.ProviderPage]:
        """List web providers. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_web_providers.asyncio_detailed(
                client=client, limit=limit, cursor=cursor, x_workspace_id=x_workspace_id
            )
        )

    def pages(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.ProviderPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, x_workspace_id=x_workspace_id, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.Provider]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(limit=limit, cursor=cursor, x_workspace_id=x_workspace_id)
            for item in page.value.items
        )

    async def create(
        self, *, body: wire.ProviderCreate, x_workspace_id: str | Unset | None = UNSET
    ) -> Result[wire.Provider]:
        """Create web provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_web_provider.asyncio_detailed(client=client, body=body, x_workspace_id=x_workspace_id)
        )

    def __call__(self, provider_id: str) -> WebProvidersProviderId:
        return WebProvidersProviderId(self._client, self._bind("provider_id", provider_id))


class WebProvidersProviderId(Resource):
    """Bound Native resource: /web-providers / {provider_id}."""

    async def get(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.Provider]:
        """Get web provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_web_provider.asyncio_detailed(
                client=client, provider_id=self._bindings["provider_id"], x_workspace_id=x_workspace_id
            )
        )

    async def update(
        self,
        *,
        body: wire.ProviderUpdate,
        if_match: str | Unset | None = UNSET,
        x_workspace_id: str | Unset | None = UNSET,
    ) -> Result[wire.Provider]:
        """Update web provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_web_provider.asyncio_detailed(
                client=client,
                provider_id=self._bindings["provider_id"],
                body=body,
                if_match=if_match,
                x_workspace_id=x_workspace_id,
            )
        )

    async def test(self, *, x_workspace_id: str | Unset | None = UNSET) -> Result[wire.ProviderTest]:
        """Test web provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: test_web_provider.asyncio_detailed(
                client=client, provider_id=self._bindings["provider_id"], x_workspace_id=x_workspace_id
            )
        )


class Workspaces(Resource):
    """Bound Native resource: /workspaces."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.WorkspacePage]:
        """List Workspaces. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_workspaces.asyncio_detailed(client=client, limit=limit, cursor=cursor)
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.WorkspacePage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> AsyncIterator[wire.Workspace]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    def __call__(self, workspace_id: str) -> Workspace:
        return Workspace(self._client, self._bind("workspace_id", workspace_id))


class Workspace(Resource):
    """Bound Native resource: /workspaces / {workspace_id}."""

    async def get(self) -> Result[wire.Workspace]:
        """Get Workspace. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspace.asyncio_detailed(client=client, workspace_id=self._bindings["workspace_id"])
        )

    async def update(
        self, *, body: wire.WorkspaceUpdate, if_match: str | Unset | None = UNSET
    ) -> Result[wire.Workspace]:
        """Update Workspace. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_workspace.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], body=body, if_match=if_match
            )
        )

    async def archive(self, *, if_match: str | Unset | None = UNSET) -> Result[wire.Workspace]:
        """Archive Workspace. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: archive_workspace.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], if_match=if_match
            )
        )

    @property
    def audit_events(self) -> WorkspacesWorkspaceIdAuditEvents:
        return WorkspacesWorkspaceIdAuditEvents(self._client, self._bindings)

    @property
    def grants(self) -> WorkspacesWorkspaceIdGrants:
        return WorkspacesWorkspaceIdGrants(self._client, self._bindings)

    @property
    def icon(self) -> WorkspacesWorkspaceIdIcon:
        return WorkspacesWorkspaceIdIcon(self._client, self._bindings)

    @property
    def invitations(self) -> WorkspacesWorkspaceIdInvitations:
        return WorkspacesWorkspaceIdInvitations(self._client, self._bindings)

    @property
    def keys(self) -> WorkspacesWorkspaceIdKeys:
        return WorkspacesWorkspaceIdKeys(self._client, self._bindings)

    @property
    def service_accounts(self) -> WorkspacesWorkspaceIdServiceAccounts:
        return WorkspacesWorkspaceIdServiceAccounts(self._client, self._bindings)


class WorkspacesWorkspaceIdAuditEvents(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / audit-events."""

    async def list(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> Result[wire.AuditPage]:
        """List Workspace Audit Events. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_workspace_audit_events.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.AuditPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> AsyncIterator[wire.AuditEvent]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)


class WorkspacesWorkspaceIdGrants(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / grants."""

    async def list(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> Result[wire.GrantPage]:
        """List Workspace Grants. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_workspace_grants.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.GrantPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> AsyncIterator[wire.GrantView]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    async def create(self, *, body: wire.GrantCreate) -> Result[wire.GrantView]:
        """Create Workspace Grant. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_workspace_grant.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], body=body
            )
        )

    def __call__(self, grant_id: str) -> WorkspacesWorkspaceIdGrantsGrantId:
        return WorkspacesWorkspaceIdGrantsGrantId(self._client, self._bind("grant_id", grant_id))


class WorkspacesWorkspaceIdGrantsGrantId(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / grants / {grant_id}."""

    async def delete(self) -> Result[None]:
        """Delete Workspace Grant. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_workspace_grant.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], grant_id=self._bindings["grant_id"]
            )
        )

    async def update(self, *, body: wire.GrantUpdate) -> Result[wire.GrantView]:
        """Change Workspace Grant. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: change_workspace_grant.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                grant_id=self._bindings["grant_id"],
                body=body,
            )
        )


class WorkspacesWorkspaceIdIcon(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / icon."""

    async def delete(self, *, if_match: str | Unset | None = UNSET) -> Result[wire.Workspace]:
        """Delete Workspace Icon. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_workspace_icon.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], if_match=if_match
            )
        )

    async def get(self) -> Result[File]:
        """Get Workspace Icon. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspace_icon.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"]
            )
        )

    def get_stream(self) -> AbstractAsyncContextManager[httpx2.Response]:
        """Unbuffered response; caller checks status and consumes within the context."""
        return self._stream(get_workspace_icon.build_request(workspace_id=self._bindings["workspace_id"]))

    async def replace(self, *, body: File, if_match: str | Unset | None = UNSET) -> Result[wire.Workspace]:
        """Put Workspace Icon. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: put_workspace_icon.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], body=body, if_match=if_match
            )
        )


class WorkspacesWorkspaceIdInvitations(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / invitations."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.InvitationPage]:
        """List Workspace Invitations. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_workspace_invitations.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.InvitationPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> AsyncIterator[wire.Invitation]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    async def create(self, *, body: wire.InvitationCreate) -> Result[wire.InvitationReceipt]:
        """Create Workspace Invitation. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_workspace_invitation.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], body=body
            )
        )

    def __call__(self, invitation_id: str) -> WorkspacesWorkspaceIdInvitationsInvitationId:
        return WorkspacesWorkspaceIdInvitationsInvitationId(self._client, self._bind("invitation_id", invitation_id))


class WorkspacesWorkspaceIdInvitationsInvitationId(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / invitations / {invitation_id}."""

    async def resend(self, *, if_match: str | Unset | None = UNSET) -> Result[wire.InvitationReceipt]:
        """Resend Workspace Invitation. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: resend_workspace_invitation.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                invitation_id=self._bindings["invitation_id"],
                if_match=if_match,
            )
        )

    async def revoke(self, *, if_match: str | Unset | None = UNSET) -> Result[wire.Invitation]:
        """Revoke Workspace Invitation. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: revoke_workspace_invitation.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                invitation_id=self._bindings["invitation_id"],
                if_match=if_match,
            )
        )


class WorkspacesWorkspaceIdKeys(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / keys."""

    async def list(
        self,
        *,
        principal_id: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> Result[wire.ApiKeyPage]:
        """List Workspace Keys. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_workspace_keys.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                principal_id=principal_id,
                limit=limit,
                cursor=cursor,
            )
        )

    def pages(
        self,
        *,
        principal_id: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.ApiKeyPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(principal_id=principal_id, limit=limit, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        principal_id: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.ApiKey]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(principal_id=principal_id, limit=limit, cursor=cursor)
            for item in page.value.items
        )

    def __call__(self, key_id: str) -> WorkspacesWorkspaceIdKeysKeyId:
        return WorkspacesWorkspaceIdKeysKeyId(self._client, self._bind("key_id", key_id))


class WorkspacesWorkspaceIdKeysKeyId(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / keys / {key_id}."""

    async def delete(self, *, if_match: str | Unset | None = UNSET) -> Result[wire.ApiKey]:
        """Revoke Workspace Key. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: revoke_workspace_key.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                key_id=self._bindings["key_id"],
                if_match=if_match,
            )
        )


class WorkspacesWorkspaceIdServiceAccounts(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / service-accounts."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.ServiceAccountPage]:
        """List Service Accounts. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_service_accounts.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.ServiceAccountPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.ServiceAccount]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    async def create(self, *, body: wire.ServiceAccountCreate) -> Result[wire.ServiceAccount]:
        """Create Service Account. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_service_account.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], body=body
            )
        )

    def __call__(self, account_id: str) -> WorkspacesWorkspaceIdServiceAccountsAccountId:
        return WorkspacesWorkspaceIdServiceAccountsAccountId(self._client, self._bind("account_id", account_id))


class WorkspacesWorkspaceIdServiceAccountsAccountId(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / service-accounts / {account_id}."""

    async def delete(self, *, if_match: str | Unset | None = UNSET) -> Result[wire.ServiceAccount]:
        """Delete Service Account. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_service_account.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                account_id=self._bindings["account_id"],
                if_match=if_match,
            )
        )

    async def get(self) -> Result[wire.ServiceAccount]:
        """Get Service Account. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_service_account.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], account_id=self._bindings["account_id"]
            )
        )

    async def update(
        self, *, body: wire.ServiceAccountUpdate, if_match: str | Unset | None = UNSET
    ) -> Result[wire.ServiceAccount]:
        """Update Service Account. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_service_account.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                account_id=self._bindings["account_id"],
                body=body,
                if_match=if_match,
            )
        )

    @property
    def keys(self) -> WorkspacesWorkspaceIdServiceAccountsAccountIdKeys:
        return WorkspacesWorkspaceIdServiceAccountsAccountIdKeys(self._client, self._bindings)


class WorkspacesWorkspaceIdServiceAccountsAccountIdKeys(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / service-accounts / {account_id} / keys."""

    async def list(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> Result[wire.ApiKeyPage]:
        """List Service Account Keys. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_service_account_keys.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                account_id=self._bindings["account_id"],
                limit=limit,
                cursor=cursor,
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.ApiKeyPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> AsyncIterator[wire.ApiKey]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    async def create(self, *, body: wire.KeyCreate) -> Result[wire.IssuedKey]:
        """Create Service Account Key. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_service_account_key.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                account_id=self._bindings["account_id"],
                body=body,
            )
        )


class Healthz(Resource):
    """Bound Native resource: /healthz."""

    async def get(self) -> Result[wire.HealthResponseHealth]:
        """Health. One HTTP request; no automatic replay."""
        return await self._call(lambda client: health.asyncio_detailed(client=client))


class Readyz(Resource):
    """Bound Native resource: /readyz."""

    async def get(self) -> Result[Any]:
        """Ready. One HTTP request; no automatic replay."""
        return await self._call(lambda client: ready.asyncio_detailed(client=client))
