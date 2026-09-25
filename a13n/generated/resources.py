"""Generated typed Native resource navigation. Do not edit; run make generate."""

from __future__ import annotations

import datetime
from collections.abc import AsyncIterator
from contextlib import AbstractAsyncContextManager
from typing import Any

import httpx2

from .._interaction import InboxEntryMethods, RunMethods, ThreadMethods, WorkspaceMethods
from .._resources import Resource, Result, pages
from . import models as wire
from .api.agents import (
    archive_agent_api_v1_workspaces_workspace_id_agents_agent_id_archive_post,
    create_agent_api_v1_workspaces_workspace_id_agents_post,
    create_revision_api_v1_workspaces_workspace_id_agents_agent_id_revisions_post,
    delete_avatar_api_v1_workspaces_workspace_id_agents_agent_id_avatar_delete,
    duplicate_agent_api_v1_workspaces_workspace_id_agents_agent_id_duplicate_post,
    get_agent_api_v1_workspaces_workspace_id_agents_agent_id_get,
    get_avatar_api_v1_workspaces_workspace_id_agents_agent_id_avatar_get,
    get_revision_api_v1_workspaces_workspace_id_agents_agent_id_revisions_revision_id_get,
    list_agents_api_v1_workspaces_workspace_id_agents_get,
    list_revisions_api_v1_workspaces_workspace_id_agents_agent_id_revisions_get,
    list_toolsets_api_v1_workspaces_workspace_id_toolsets_get,
    prepare_assistant_api_v1_workspaces_workspace_id_configuration_assistant_post,
    put_avatar_api_v1_workspaces_workspace_id_agents_agent_id_avatar_put,
    set_default_api_v1_workspaces_workspace_id_agents_agent_id_revisions_revision_id_set_default_post,
    unarchive_agent_api_v1_workspaces_workspace_id_agents_agent_id_unarchive_post,
    update_agent_api_v1_workspaces_workspace_id_agents_agent_id_patch,
    validate_revision_api_v1_workspaces_workspace_id_agents_validate_post,
)
from .api.assets import (
    create_asset_api_v1_workspaces_workspace_id_assets_post,
    create_upload_api_v1_workspaces_workspace_id_uploads_post,
    get_asset_api_v1_workspaces_workspace_id_assets_asset_id_get,
    list_assets_api_v1_workspaces_workspace_id_assets_get,
    read_asset_content_api_v1_workspaces_workspace_id_assets_asset_id_content_get,
    retire_asset_api_v1_workspaces_workspace_id_assets_asset_id_delete,
)
from .api.auth import (
    accept_api_v1_invitations_invitation_id_accept_post,
    auth_configuration_api_v1_auth_configuration_get,
    bootstrap_administrator_api_v1_auth_bootstrap_post,
    change_password_api_v1_users_me_password_post,
    confirm_email_change_api_v1_auth_email_change_confirm_post,
    confirm_password_reset_api_v1_auth_password_reset_confirm_post,
    create_user_key_api_v1_users_me_keys_post,
    delete_avatar_api_v1_users_me_avatar_delete,
    disable_account_api_v1_users_me_disable_post,
    get_avatar_api_v1_users_user_id_avatar_get,
    get_profile_api_v1_users_me_get,
    list_account_audit_events_api_v1_users_me_audit_events_get,
    list_login_sessions_api_v1_users_me_login_sessions_get,
    list_user_keys_api_v1_users_me_keys_get,
    logout_api_v1_auth_logout_post,
    password_login_api_v1_auth_login_post,
    put_avatar_api_v1_users_me_avatar_put,
    request_password_reset_api_v1_auth_password_reset_post,
    revoke_login_session_api_v1_users_me_login_sessions_session_id_delete,
    revoke_user_key_api_v1_users_me_keys_key_id_delete,
    session_profile_api_v1_auth_session_get,
    update_profile_api_v1_users_me_patch,
)
from .api.connections import (
    authorize_connection_api_v1_workspaces_workspace_id_connections_connection_id_authorize_post,
    complete_authorization_api_v1_connections_callback_get,
    create_connection_api_v1_workspaces_workspace_id_connections_post,
    get_app_api_v1_workspaces_workspace_id_connector_providers_provider_id_apps_app_get,
    get_connection_api_v1_workspaces_workspace_id_connections_connection_id_get,
    get_redirect_uri_api_v1_connections_redirect_uri_get,
    list_actions_api_v1_workspaces_workspace_id_connector_providers_provider_id_apps_app_actions_get,
    list_apps_api_v1_workspaces_workspace_id_connector_providers_provider_id_apps_get,
    list_connections_api_v1_workspaces_workspace_id_connections_get,
    list_mcp_servers_api_v1_mcp_servers_get,
    list_tools_api_v1_workspaces_workspace_id_connections_connection_id_tools_get,
    revoke_connection_api_v1_workspaces_workspace_id_connections_connection_id_revoke_post,
    test_connection_api_v1_workspaces_workspace_id_connections_connection_id_test_post,
    update_connection_api_v1_workspaces_workspace_id_connections_connection_id_patch,
)
from .api.default import health_healthz_get, ready_readyz_get
from .api.environments import (
    add_mount_api_v1_workspaces_workspace_id_threads_thread_id_environments_post,
    create_environment_api_v1_workspaces_workspace_id_environments_post,
    create_template_api_v1_workspaces_workspace_id_environment_templates_post,
    delete_environment_api_v1_workspaces_workspace_id_environments_environment_id_delete,
    get_environment_api_v1_workspaces_workspace_id_environments_environment_id_get,
    get_template_api_v1_workspaces_workspace_id_environment_templates_template_id_get,
    list_environments_api_v1_workspaces_workspace_id_environments_get,
    list_mounts_api_v1_workspaces_workspace_id_threads_thread_id_environments_get,
    list_templates_api_v1_workspaces_workspace_id_environment_templates_get,
    remove_mount_api_v1_workspaces_workspace_id_threads_thread_id_environments_name_delete,
    stop_environment_api_v1_workspaces_workspace_id_environments_environment_id_stop_post,
    update_environment_api_v1_workspaces_workspace_id_environments_environment_id_patch,
    update_template_api_v1_workspaces_workspace_id_environment_templates_template_id_patch,
)
from .api.memories import (
    add_mount_api_v1_workspaces_workspace_id_threads_thread_id_memories_post,
    add_record_api_v1_workspaces_workspace_id_memories_memory_id_records_post,
    create_file_api_v1_workspaces_workspace_id_memories_memory_id_files_post,
    create_memory_api_v1_workspaces_workspace_id_memories_post,
    delete_file_api_v1_workspaces_workspace_id_memories_memory_id_files_path_delete,
    delete_memory_api_v1_workspaces_workspace_id_memories_memory_id_delete,
    delete_record_api_v1_workspaces_workspace_id_memories_memory_id_records_record_id_delete,
    get_memory_api_v1_workspaces_workspace_id_memories_memory_id_get,
    get_revision_api_v1_workspaces_workspace_id_memories_memory_id_revisions_seq_get,
    list_files_api_v1_workspaces_workspace_id_memories_memory_id_files_get,
    list_memories_api_v1_workspaces_workspace_id_memories_get,
    list_mounts_api_v1_workspaces_workspace_id_threads_thread_id_memories_get,
    list_records_api_v1_workspaces_workspace_id_memories_memory_id_records_get,
    list_revisions_api_v1_workspaces_workspace_id_memories_memory_id_revisions_get,
    move_file_api_v1_workspaces_workspace_id_memories_memory_id_files_move_post,
    purge_history_api_v1_workspaces_workspace_id_memories_memory_id_revisions_delete,
    read_file_api_v1_workspaces_workspace_id_memories_memory_id_files_path_get,
    remove_mount_api_v1_workspaces_workspace_id_threads_thread_id_memories_name_delete,
    replace_file_api_v1_workspaces_workspace_id_memories_memory_id_files_path_put,
    restore_revision_api_v1_workspaces_workspace_id_memories_memory_id_revisions_seq_restore_post,
    search_records_api_v1_workspaces_workspace_id_memories_memory_id_records_search_post,
    update_memory_api_v1_workspaces_workspace_id_memories_memory_id_patch,
    update_mount_api_v1_workspaces_workspace_id_threads_thread_id_memories_name_patch,
    update_record_api_v1_workspaces_workspace_id_memories_memory_id_records_record_id_put,
)
from .api.models import (
    create_model_api_v1_organizations_organization_id_models_post,
    get_media_defaults_api_v1_workspaces_workspace_id_media_understanding_defaults_get,
    get_model_api_v1_organizations_organization_id_models_model_id_get,
    get_model_catalog_api_v1_model_catalog_get,
    list_models_api_v1_organizations_organization_id_models_get,
    replace_media_defaults_api_v1_workspaces_workspace_id_media_understanding_defaults_put,
    update_model_api_v1_organizations_organization_id_models_model_id_patch,
)
from .api.providers import (
    create_provider_api_v1_organizations_organization_id_connector_providers_post,
    create_provider_api_v1_organizations_organization_id_environment_providers_post,
    create_provider_api_v1_organizations_organization_id_memory_providers_post,
    create_provider_api_v1_organizations_organization_id_model_providers_post,
    create_provider_api_v1_organizations_organization_id_web_providers_post,
    get_provider_api_v1_organizations_organization_id_connector_providers_provider_id_get,
    get_provider_api_v1_organizations_organization_id_environment_providers_provider_id_get,
    get_provider_api_v1_organizations_organization_id_memory_providers_provider_id_get,
    get_provider_api_v1_organizations_organization_id_model_providers_provider_id_get,
    get_provider_api_v1_organizations_organization_id_web_providers_provider_id_get,
    list_provider_types_api_v1_provider_types_kind_get,
    list_providers_api_v1_organizations_organization_id_connector_providers_get,
    list_providers_api_v1_organizations_organization_id_environment_providers_get,
    list_providers_api_v1_organizations_organization_id_memory_providers_get,
    list_providers_api_v1_organizations_organization_id_model_providers_get,
    list_providers_api_v1_organizations_organization_id_web_providers_get,
    test_provider_api_v1_organizations_organization_id_connector_providers_provider_id_test_post,
    test_provider_api_v1_organizations_organization_id_environment_providers_provider_id_test_post,
    test_provider_api_v1_organizations_organization_id_memory_providers_provider_id_test_post,
    test_provider_api_v1_organizations_organization_id_model_providers_provider_id_test_post,
    test_provider_api_v1_organizations_organization_id_web_providers_provider_id_test_post,
    update_provider_api_v1_organizations_organization_id_connector_providers_provider_id_patch,
    update_provider_api_v1_organizations_organization_id_environment_providers_provider_id_patch,
    update_provider_api_v1_organizations_organization_id_memory_providers_provider_id_patch,
    update_provider_api_v1_organizations_organization_id_model_providers_provider_id_patch,
    update_provider_api_v1_organizations_organization_id_web_providers_provider_id_patch,
)
from .api.runs import (
    archive_thread_api_v1_workspaces_workspace_id_threads_thread_id_archive_post,
    create_session_api_v1_workspaces_workspace_id_sessions_post,
    create_thread_api_v1_workspaces_workspace_id_threads_post,
    edit_entry_api_v1_workspaces_workspace_id_threads_thread_id_inbox_entry_id_patch,
    fork_run_api_v1_workspaces_workspace_id_runs_run_id_fork_post,
    get_entry_api_v1_workspaces_workspace_id_threads_thread_id_inbox_entry_id_get,
    get_run_api_v1_workspaces_workspace_id_runs_run_id_get,
    get_session_api_v1_workspaces_workspace_id_sessions_session_id_get,
    get_thread_api_v1_workspaces_workspace_id_threads_thread_id_get,
    get_trace_api_v1_workspaces_workspace_id_traces_trace_id_get,
    get_trace_backend_api_v1_workspaces_workspace_id_trace_backend_get,
    interrupt_run_api_v1_workspaces_workspace_id_runs_run_id_interrupt_post,
    list_attempt_spans_api_v1_workspaces_workspace_id_runs_run_id_attempts_attempt_id_trace_get,
    list_inbox_api_v1_workspaces_workspace_id_threads_thread_id_inbox_get,
    list_sessions_api_v1_workspaces_workspace_id_sessions_get,
    list_thread_runs_api_v1_workspaces_workspace_id_threads_thread_id_runs_get,
    list_threads_api_v1_workspaces_workspace_id_threads_get,
    list_trace_spans_api_v1_workspaces_workspace_id_traces_trace_id_spans_get,
    list_traces_api_v1_workspaces_workspace_id_traces_get,
    reorder_inbox_api_v1_workspaces_workspace_id_threads_thread_id_inbox_order_put,
    resume_run_api_v1_workspaces_workspace_id_runs_run_id_resume_post,
    run_attempts_api_v1_workspaces_workspace_id_runs_run_id_attempts_get,
    run_items_api_v1_workspaces_workspace_id_runs_run_id_items_get,
    run_lineage_api_v1_workspaces_workspace_id_runs_run_id_lineage_get,
    submit_message_api_v1_workspaces_workspace_id_threads_thread_id_inbox_post,
    summarize_usage_api_v1_workspaces_workspace_id_usage_get,
    thread_stream_api_v1_workspaces_workspace_id_threads_thread_id_stream_get,
    update_run_api_v1_workspaces_workspace_id_runs_run_id_patch,
    update_session_api_v1_workspaces_workspace_id_sessions_session_id_patch,
    update_thread_api_v1_workspaces_workspace_id_threads_thread_id_patch,
    withdraw_entry_api_v1_workspaces_workspace_id_threads_thread_id_inbox_entry_id_delete,
)
from .api.secrets import (
    create_secret_api_v1_workspaces_workspace_id_secrets_post,
    delete_secret_api_v1_workspaces_workspace_id_secrets_secret_id_delete,
    get_secret_api_v1_workspaces_workspace_id_secrets_secret_id_get,
    list_secrets_api_v1_workspaces_workspace_id_secrets_get,
    replace_secret_api_v1_workspaces_workspace_id_secrets_secret_id_put,
)
from .api.skills import (
    archive_skill_api_v1_workspaces_workspace_id_skills_skill_id_archive_post,
    create_revision_api_v1_workspaces_workspace_id_skills_skill_id_revisions_post,
    create_skill_api_v1_workspaces_workspace_id_skills_post,
    get_revision_api_v1_workspaces_workspace_id_skills_skill_id_revisions_revision_id_get,
    get_skill_api_v1_workspaces_workspace_id_skills_skill_id_get,
    list_revisions_api_v1_workspaces_workspace_id_skills_skill_id_revisions_get,
    list_skills_api_v1_workspaces_workspace_id_skills_get,
    read_archive_api_v1_workspaces_workspace_id_skills_skill_id_revisions_revision_id_content_get,
    read_file_api_v1_workspaces_workspace_id_skills_skill_id_revisions_revision_id_files_path_get,
    set_default_revision_api_v1_workspaces_workspace_id_skills_skill_id_revisions_revision_id_set_default_post,
    unarchive_skill_api_v1_workspaces_workspace_id_skills_skill_id_unarchive_post,
    update_skill_api_v1_workspaces_workspace_id_skills_skill_id_patch,
    validate_package_api_v1_workspaces_workspace_id_skills_validate_post,
)
from .api.subscriptions import (
    create_subscription_api_v1_workspaces_workspace_id_subscriptions_post,
    delete_subscription_api_v1_workspaces_workspace_id_subscriptions_subscription_id_delete,
    get_subscription_api_v1_workspaces_workspace_id_subscriptions_subscription_id_get,
    list_deliveries_api_v1_workspaces_workspace_id_subscriptions_subscription_id_deliveries_get,
    list_subscriptions_api_v1_workspaces_workspace_id_subscriptions_get,
    redeliver_api_v1_workspaces_workspace_id_subscriptions_subscription_id_deliveries_delivery_id_redeliver_post,
    update_subscription_api_v1_workspaces_workspace_id_subscriptions_subscription_id_patch,
)
from .api.tenancy import (
    archive_workspace_api_v1_workspaces_workspace_id_archive_post,
    change_organization_grant_api_v1_organizations_organization_id_grants_grant_id_patch,
    change_workspace_grant_api_v1_workspaces_workspace_id_grants_grant_id_patch,
    create_organization_grant_api_v1_organizations_organization_id_grants_post,
    create_organization_invitation_api_v1_organizations_organization_id_invitations_post,
    create_service_account_api_v1_workspaces_workspace_id_service_accounts_post,
    create_service_account_key_api_v1_workspaces_workspace_id_service_accounts_account_id_keys_post,
    create_workspace_api_v1_organizations_organization_id_workspaces_post,
    create_workspace_grant_api_v1_workspaces_workspace_id_grants_post,
    create_workspace_invitation_api_v1_workspaces_workspace_id_invitations_post,
    delete_organization_grant_api_v1_organizations_organization_id_grants_grant_id_delete,
    delete_organization_icon_api_v1_organizations_organization_id_icon_delete,
    delete_service_account_api_v1_workspaces_workspace_id_service_accounts_account_id_delete,
    delete_workspace_grant_api_v1_workspaces_workspace_id_grants_grant_id_delete,
    delete_workspace_icon_api_v1_workspaces_workspace_id_icon_delete,
    get_organization_api_v1_organizations_organization_id_get,
    get_organization_icon_api_v1_organizations_organization_id_icon_get,
    get_service_account_api_v1_workspaces_workspace_id_service_accounts_account_id_get,
    get_workspace_api_v1_workspaces_workspace_id_get,
    get_workspace_icon_api_v1_workspaces_workspace_id_icon_get,
    list_members_api_v1_organizations_organization_id_members_get,
    list_organization_audit_events_api_v1_organizations_organization_id_audit_events_get,
    list_organization_grants_api_v1_organizations_organization_id_grants_get,
    list_organization_invitations_api_v1_organizations_organization_id_invitations_get,
    list_organization_workspaces_api_v1_organizations_organization_id_workspaces_get,
    list_organizations_api_v1_organizations_get,
    list_service_account_keys_api_v1_workspaces_workspace_id_service_accounts_account_id_keys_get,
    list_service_accounts_api_v1_workspaces_workspace_id_service_accounts_get,
    list_workspace_audit_events_api_v1_workspaces_workspace_id_audit_events_get,
    list_workspace_grants_api_v1_workspaces_workspace_id_grants_get,
    list_workspace_invitations_api_v1_workspaces_workspace_id_invitations_get,
    list_workspace_keys_api_v1_workspaces_workspace_id_keys_get,
    list_workspaces_api_v1_workspaces_get,
    put_organization_icon_api_v1_organizations_organization_id_icon_put,
    put_workspace_icon_api_v1_workspaces_workspace_id_icon_put,
    resend_organization_invitation_api_v1_organizations_organization_id_invitations_invitation_id_resend_post,
    resend_workspace_invitation_api_v1_workspaces_workspace_id_invitations_invitation_id_resend_post,
    revoke_organization_invitation_api_v1_organizations_organization_id_invitations_invitation_id_revoke_post,
    revoke_workspace_invitation_api_v1_workspaces_workspace_id_invitations_invitation_id_revoke_post,
    revoke_workspace_key_api_v1_workspaces_workspace_id_keys_key_id_delete,
    update_organization_api_v1_organizations_organization_id_patch,
    update_service_account_api_v1_workspaces_workspace_id_service_accounts_account_id_patch,
    update_workspace_api_v1_workspaces_workspace_id_patch,
)
from .types import UNSET, File, Unset


class ServiceResources(Resource):
    """Bound Native resource: /api/v1."""

    @property
    def auth(self) -> Auth:
        return Auth(self._client, self._bindings)

    @property
    def connections(self) -> Connections:
        return Connections(self._client, self._bindings)

    @property
    def invitations(self) -> Invitations:
        return Invitations(self._client, self._bindings)

    @property
    def mcp_servers(self) -> McpServers:
        return McpServers(self._client, self._bindings)

    @property
    def model_catalog(self) -> ModelCatalog:
        return ModelCatalog(self._client, self._bindings)

    @property
    def organizations(self) -> Organizations:
        return Organizations(self._client, self._bindings)

    @property
    def provider_types(self) -> ProviderTypes:
        return ProviderTypes(self._client, self._bindings)

    @property
    def users(self) -> Users:
        return Users(self._client, self._bindings)

    @property
    def workspaces(self) -> Workspaces:
        return Workspaces(self._client, self._bindings)

    @property
    def healthz(self) -> Healthz:
        return Healthz(self._client, self._bindings)

    @property
    def readyz(self) -> Readyz:
        return Readyz(self._client, self._bindings)


class Auth(Resource):
    """Bound Native resource: /auth."""

    async def bootstrap(self, *, body: wire.BootstrapInput) -> Result[wire.LoginOutput]:
        """Bootstrap Administrator. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: bootstrap_administrator_api_v1_auth_bootstrap_post.asyncio_detailed(client=client, body=body)
        )

    @property
    def configuration(self) -> AuthConfiguration:
        return AuthConfiguration(self._client, self._bindings)

    @property
    def email_change(self) -> AuthEmailChange:
        return AuthEmailChange(self._client, self._bindings)

    async def login(self, *, body: wire.LoginInput) -> Result[wire.LoginOutput]:
        """Password Login. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: password_login_api_v1_auth_login_post.asyncio_detailed(client=client, body=body)
        )

    async def logout(self) -> Result[None]:
        """Logout. One HTTP request; no automatic replay."""
        return await self._call(lambda client: logout_api_v1_auth_logout_post.asyncio_detailed(client=client))

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
        return await self._call(
            lambda client: auth_configuration_api_v1_auth_configuration_get.asyncio_detailed(client=client)
        )


class AuthEmailChange(Resource):
    """Bound Native resource: /auth / email-change."""

    async def confirm(self, *, body: wire.EmailChangeConfirm) -> Result[None]:
        """Confirm Email Change. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: confirm_email_change_api_v1_auth_email_change_confirm_post.asyncio_detailed(
                client=client, body=body
            )
        )


class AuthPasswordReset(Resource):
    """Bound Native resource: /auth / password-reset."""

    async def create(self, *, body: wire.PasswordReset) -> Result[None]:
        """Request Password Reset. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: request_password_reset_api_v1_auth_password_reset_post.asyncio_detailed(
                client=client, body=body
            )
        )

    async def confirm(self, *, body: wire.PasswordResetConfirm) -> Result[None]:
        """Confirm Password Reset. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: confirm_password_reset_api_v1_auth_password_reset_confirm_post.asyncio_detailed(
                client=client, body=body
            )
        )


class AuthSession(Resource):
    """Bound Native resource: /auth / session."""

    async def get(self) -> Result[wire.SessionProfile]:
        """Session Profile. One HTTP request; no automatic replay."""
        return await self._call(lambda client: session_profile_api_v1_auth_session_get.asyncio_detailed(client=client))


class Connections(Resource):
    """Bound Native resource: /connections."""

    @property
    def callback(self) -> ConnectionsCallback:
        return ConnectionsCallback(self._client, self._bindings)

    @property
    def redirect_uri(self) -> ConnectionsRedirectUri:
        return ConnectionsRedirectUri(self._client, self._bindings)


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
            lambda client: complete_authorization_api_v1_connections_callback_get.asyncio_detailed(
                client=client, state=state, code=code, error=error, iss=iss, session_uri=session_uri
            )
        )


class ConnectionsRedirectUri(Resource):
    """Bound Native resource: /connections / redirect-uri."""

    async def get(self) -> Result[wire.OAuthRedirect]:
        """Get Redirect Uri. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_redirect_uri_api_v1_connections_redirect_uri_get.asyncio_detailed(client=client)
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
            lambda client: accept_api_v1_invitations_invitation_id_accept_post.asyncio_detailed(
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
            lambda client: list_mcp_servers_api_v1_mcp_servers_get.asyncio_detailed(
                client=client, query=query, limit=limit, cursor=cursor
            )
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


class ModelCatalog(Resource):
    """Bound Native resource: /model-catalog."""

    async def get(self) -> Result[wire.ModelCatalog]:
        """Get Model Catalog. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_model_catalog_api_v1_model_catalog_get.asyncio_detailed(client=client)
        )


class Organizations(Resource):
    """Bound Native resource: /organizations."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.OrganizationPage]:
        """List Organizations. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_organizations_api_v1_organizations_get.asyncio_detailed(
                client=client, limit=limit, cursor=cursor
            )
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
            lambda client: get_organization_api_v1_organizations_organization_id_get.asyncio_detailed(
                client=client, organization_id=self._bindings["organization_id"]
            )
        )

    async def update(
        self, *, body: wire.OrganizationUpdate, if_match: str | Unset | None = UNSET
    ) -> Result[wire.Organization]:
        """Update Organization. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_organization_api_v1_organizations_organization_id_patch.asyncio_detailed(
                client=client, organization_id=self._bindings["organization_id"], body=body, if_match=if_match
            )
        )

    @property
    def audit_events(self) -> OrganizationsOrganizationIdAuditEvents:
        return OrganizationsOrganizationIdAuditEvents(self._client, self._bindings)

    @property
    def connector_providers(self) -> OrganizationsOrganizationIdConnectorProviders:
        return OrganizationsOrganizationIdConnectorProviders(self._client, self._bindings)

    @property
    def environment_providers(self) -> OrganizationsOrganizationIdEnvironmentProviders:
        return OrganizationsOrganizationIdEnvironmentProviders(self._client, self._bindings)

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
    def memory_providers(self) -> OrganizationsOrganizationIdMemoryProviders:
        return OrganizationsOrganizationIdMemoryProviders(self._client, self._bindings)

    @property
    def model_providers(self) -> OrganizationsOrganizationIdModelProviders:
        return OrganizationsOrganizationIdModelProviders(self._client, self._bindings)

    @property
    def models(self) -> OrganizationsOrganizationIdModels:
        return OrganizationsOrganizationIdModels(self._client, self._bindings)

    @property
    def web_providers(self) -> OrganizationsOrganizationIdWebProviders:
        return OrganizationsOrganizationIdWebProviders(self._client, self._bindings)

    @property
    def workspaces(self) -> OrganizationsOrganizationIdWorkspaces:
        return OrganizationsOrganizationIdWorkspaces(self._client, self._bindings)


class OrganizationsOrganizationIdAuditEvents(Resource):
    """Bound Native resource: /organizations / {organization_id} / audit-events."""

    async def list(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> Result[wire.AuditPage]:
        """List Organization Audit Events. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                list_organization_audit_events_api_v1_organizations_organization_id_audit_events_get.asyncio_detailed(
                    client=client, organization_id=self._bindings["organization_id"], limit=limit, cursor=cursor
                )
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


class OrganizationsOrganizationIdConnectorProviders(Resource):
    """Bound Native resource: /organizations / {organization_id} / connector-providers."""

    async def list(
        self,
        *,
        workspace_id: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> Result[wire.ProviderPage]:
        """List Providers. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_providers_api_v1_organizations_organization_id_connector_providers_get.asyncio_detailed(
                client=client,
                organization_id=self._bindings["organization_id"],
                workspace_id=workspace_id,
                limit=limit,
                cursor=cursor,
            )
        )

    def pages(
        self,
        *,
        workspace_id: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.ProviderPage]]:
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
    ) -> AsyncIterator[wire.Provider]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(workspace_id=workspace_id, limit=limit, cursor=cursor)
            for item in page.value.items
        )

    async def create(self, *, body: wire.ProviderCreate) -> Result[wire.Provider]:
        """Create Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                create_provider_api_v1_organizations_organization_id_connector_providers_post.asyncio_detailed(
                    client=client, organization_id=self._bindings["organization_id"], body=body
                )
            )
        )

    def __call__(self, provider_id: str) -> OrganizationsOrganizationIdConnectorProvidersProviderId:
        return OrganizationsOrganizationIdConnectorProvidersProviderId(
            self._client, self._bind("provider_id", provider_id)
        )


class OrganizationsOrganizationIdConnectorProvidersProviderId(Resource):
    """Bound Native resource: /organizations / {organization_id} / connector-providers / {provider_id}."""

    async def get(self) -> Result[wire.Provider]:
        """Get Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                get_provider_api_v1_organizations_organization_id_connector_providers_provider_id_get.asyncio_detailed(
                    client=client,
                    organization_id=self._bindings["organization_id"],
                    provider_id=self._bindings["provider_id"],
                )
            )
        )

    async def update(self, *, body: wire.ProviderUpdate, if_match: str | Unset | None = UNSET) -> Result[wire.Provider]:
        """Update Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                update_provider_api_v1_organizations_organization_id_connector_providers_provider_id_patch.asyncio_detailed(
                    client=client,
                    organization_id=self._bindings["organization_id"],
                    provider_id=self._bindings["provider_id"],
                    body=body,
                    if_match=if_match,
                )
            )
        )

    async def test(self) -> Result[wire.ProviderTest]:
        """Test Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                test_provider_api_v1_organizations_organization_id_connector_providers_provider_id_test_post.asyncio_detailed(
                    client=client,
                    organization_id=self._bindings["organization_id"],
                    provider_id=self._bindings["provider_id"],
                )
            )
        )


class OrganizationsOrganizationIdEnvironmentProviders(Resource):
    """Bound Native resource: /organizations / {organization_id} / environment-providers."""

    async def list(
        self,
        *,
        workspace_id: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> Result[wire.ProviderPage]:
        """List Providers. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                list_providers_api_v1_organizations_organization_id_environment_providers_get.asyncio_detailed(
                    client=client,
                    organization_id=self._bindings["organization_id"],
                    workspace_id=workspace_id,
                    limit=limit,
                    cursor=cursor,
                )
            )
        )

    def pages(
        self,
        *,
        workspace_id: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.ProviderPage]]:
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
    ) -> AsyncIterator[wire.Provider]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(workspace_id=workspace_id, limit=limit, cursor=cursor)
            for item in page.value.items
        )

    async def create(self, *, body: wire.ProviderCreate) -> Result[wire.Provider]:
        """Create Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                create_provider_api_v1_organizations_organization_id_environment_providers_post.asyncio_detailed(
                    client=client, organization_id=self._bindings["organization_id"], body=body
                )
            )
        )

    def __call__(self, provider_id: str) -> OrganizationsOrganizationIdEnvironmentProvidersProviderId:
        return OrganizationsOrganizationIdEnvironmentProvidersProviderId(
            self._client, self._bind("provider_id", provider_id)
        )


class OrganizationsOrganizationIdEnvironmentProvidersProviderId(Resource):
    """Bound Native resource: /organizations / {organization_id} / environment-providers / {provider_id}."""

    async def get(self) -> Result[wire.Provider]:
        """Get Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                get_provider_api_v1_organizations_organization_id_environment_providers_provider_id_get.asyncio_detailed(
                    client=client,
                    organization_id=self._bindings["organization_id"],
                    provider_id=self._bindings["provider_id"],
                )
            )
        )

    async def update(self, *, body: wire.ProviderUpdate, if_match: str | Unset | None = UNSET) -> Result[wire.Provider]:
        """Update Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                update_provider_api_v1_organizations_organization_id_environment_providers_provider_id_patch.asyncio_detailed(
                    client=client,
                    organization_id=self._bindings["organization_id"],
                    provider_id=self._bindings["provider_id"],
                    body=body,
                    if_match=if_match,
                )
            )
        )

    async def test(self) -> Result[wire.ProviderTest]:
        """Test Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                test_provider_api_v1_organizations_organization_id_environment_providers_provider_id_test_post.asyncio_detailed(
                    client=client,
                    organization_id=self._bindings["organization_id"],
                    provider_id=self._bindings["provider_id"],
                )
            )
        )


class OrganizationsOrganizationIdGrants(Resource):
    """Bound Native resource: /organizations / {organization_id} / grants."""

    async def list(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> Result[wire.GrantPage]:
        """List Organization Grants. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_organization_grants_api_v1_organizations_organization_id_grants_get.asyncio_detailed(
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
            lambda client: create_organization_grant_api_v1_organizations_organization_id_grants_post.asyncio_detailed(
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
            lambda client: (
                delete_organization_grant_api_v1_organizations_organization_id_grants_grant_id_delete.asyncio_detailed(
                    client=client,
                    organization_id=self._bindings["organization_id"],
                    grant_id=self._bindings["grant_id"],
                )
            )
        )

    async def update(self, *, body: wire.GrantUpdate) -> Result[wire.GrantView]:
        """Change Organization Grant. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                change_organization_grant_api_v1_organizations_organization_id_grants_grant_id_patch.asyncio_detailed(
                    client=client,
                    organization_id=self._bindings["organization_id"],
                    grant_id=self._bindings["grant_id"],
                    body=body,
                )
            )
        )


class OrganizationsOrganizationIdIcon(Resource):
    """Bound Native resource: /organizations / {organization_id} / icon."""

    async def delete(self, *, if_match: str | Unset | None = UNSET) -> Result[wire.Organization]:
        """Delete Organization Icon. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_organization_icon_api_v1_organizations_organization_id_icon_delete.asyncio_detailed(
                client=client, organization_id=self._bindings["organization_id"], if_match=if_match
            )
        )

    async def get(self) -> Result[File]:
        """Get Organization Icon. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_organization_icon_api_v1_organizations_organization_id_icon_get.asyncio_detailed(
                client=client, organization_id=self._bindings["organization_id"]
            )
        )

    def get_stream(self) -> AbstractAsyncContextManager[httpx2.Response]:
        """Unbuffered response; caller checks status and consumes within the context."""
        return self._stream(
            get_organization_icon_api_v1_organizations_organization_id_icon_get.build_request(
                organization_id=self._bindings["organization_id"]
            )
        )

    async def replace(self, *, body: File, if_match: str | Unset | None = UNSET) -> Result[wire.Organization]:
        """Put Organization Icon. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: put_organization_icon_api_v1_organizations_organization_id_icon_put.asyncio_detailed(
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
            lambda client: (
                list_organization_invitations_api_v1_organizations_organization_id_invitations_get.asyncio_detailed(
                    client=client, organization_id=self._bindings["organization_id"], limit=limit, cursor=cursor
                )
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
            lambda client: (
                create_organization_invitation_api_v1_organizations_organization_id_invitations_post.asyncio_detailed(
                    client=client, organization_id=self._bindings["organization_id"], body=body
                )
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
            lambda client: (
                resend_organization_invitation_api_v1_organizations_organization_id_invitations_invitation_id_resend_post.asyncio_detailed(
                    client=client,
                    organization_id=self._bindings["organization_id"],
                    invitation_id=self._bindings["invitation_id"],
                    if_match=if_match,
                )
            )
        )

    async def revoke(self, *, if_match: str | Unset | None = UNSET) -> Result[wire.Invitation]:
        """Revoke Organization Invitation. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                revoke_organization_invitation_api_v1_organizations_organization_id_invitations_invitation_id_revoke_post.asyncio_detailed(
                    client=client,
                    organization_id=self._bindings["organization_id"],
                    invitation_id=self._bindings["invitation_id"],
                    if_match=if_match,
                )
            )
        )


class OrganizationsOrganizationIdMembers(Resource):
    """Bound Native resource: /organizations / {organization_id} / members."""

    async def list(
        self,
        *,
        kind: wire.ListMembersApiV1OrganizationsOrganizationIdMembersGetKindType0 | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> Result[wire.MemberPage]:
        """List Members. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_members_api_v1_organizations_organization_id_members_get.asyncio_detailed(
                client=client, organization_id=self._bindings["organization_id"], kind=kind, limit=limit, cursor=cursor
            )
        )

    def pages(
        self,
        *,
        kind: wire.ListMembersApiV1OrganizationsOrganizationIdMembersGetKindType0 | Unset | None = UNSET,
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
        kind: wire.ListMembersApiV1OrganizationsOrganizationIdMembersGetKindType0 | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.PrincipalSummary]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(kind=kind, limit=limit, cursor=cursor) for item in page.value.items)


class OrganizationsOrganizationIdMemoryProviders(Resource):
    """Bound Native resource: /organizations / {organization_id} / memory-providers."""

    async def list(
        self,
        *,
        workspace_id: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> Result[wire.ProviderPage]:
        """List Providers. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_providers_api_v1_organizations_organization_id_memory_providers_get.asyncio_detailed(
                client=client,
                organization_id=self._bindings["organization_id"],
                workspace_id=workspace_id,
                limit=limit,
                cursor=cursor,
            )
        )

    def pages(
        self,
        *,
        workspace_id: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.ProviderPage]]:
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
    ) -> AsyncIterator[wire.Provider]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(workspace_id=workspace_id, limit=limit, cursor=cursor)
            for item in page.value.items
        )

    async def create(self, *, body: wire.ProviderCreate) -> Result[wire.Provider]:
        """Create Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_provider_api_v1_organizations_organization_id_memory_providers_post.asyncio_detailed(
                client=client, organization_id=self._bindings["organization_id"], body=body
            )
        )

    def __call__(self, provider_id: str) -> OrganizationsOrganizationIdMemoryProvidersProviderId:
        return OrganizationsOrganizationIdMemoryProvidersProviderId(
            self._client, self._bind("provider_id", provider_id)
        )


class OrganizationsOrganizationIdMemoryProvidersProviderId(Resource):
    """Bound Native resource: /organizations / {organization_id} / memory-providers / {provider_id}."""

    async def get(self) -> Result[wire.Provider]:
        """Get Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                get_provider_api_v1_organizations_organization_id_memory_providers_provider_id_get.asyncio_detailed(
                    client=client,
                    organization_id=self._bindings["organization_id"],
                    provider_id=self._bindings["provider_id"],
                )
            )
        )

    async def update(self, *, body: wire.ProviderUpdate, if_match: str | Unset | None = UNSET) -> Result[wire.Provider]:
        """Update Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                update_provider_api_v1_organizations_organization_id_memory_providers_provider_id_patch.asyncio_detailed(
                    client=client,
                    organization_id=self._bindings["organization_id"],
                    provider_id=self._bindings["provider_id"],
                    body=body,
                    if_match=if_match,
                )
            )
        )

    async def test(self) -> Result[wire.ProviderTest]:
        """Test Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                test_provider_api_v1_organizations_organization_id_memory_providers_provider_id_test_post.asyncio_detailed(
                    client=client,
                    organization_id=self._bindings["organization_id"],
                    provider_id=self._bindings["provider_id"],
                )
            )
        )


class OrganizationsOrganizationIdModelProviders(Resource):
    """Bound Native resource: /organizations / {organization_id} / model-providers."""

    async def list(
        self,
        *,
        workspace_id: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> Result[wire.ProviderPage]:
        """List Providers. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_providers_api_v1_organizations_organization_id_model_providers_get.asyncio_detailed(
                client=client,
                organization_id=self._bindings["organization_id"],
                workspace_id=workspace_id,
                limit=limit,
                cursor=cursor,
            )
        )

    def pages(
        self,
        *,
        workspace_id: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.ProviderPage]]:
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
    ) -> AsyncIterator[wire.Provider]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(workspace_id=workspace_id, limit=limit, cursor=cursor)
            for item in page.value.items
        )

    async def create(self, *, body: wire.ProviderCreate) -> Result[wire.Provider]:
        """Create Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_provider_api_v1_organizations_organization_id_model_providers_post.asyncio_detailed(
                client=client, organization_id=self._bindings["organization_id"], body=body
            )
        )

    def __call__(self, provider_id: str) -> OrganizationsOrganizationIdModelProvidersProviderId:
        return OrganizationsOrganizationIdModelProvidersProviderId(self._client, self._bind("provider_id", provider_id))


class OrganizationsOrganizationIdModelProvidersProviderId(Resource):
    """Bound Native resource: /organizations / {organization_id} / model-providers / {provider_id}."""

    async def get(self) -> Result[wire.Provider]:
        """Get Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                get_provider_api_v1_organizations_organization_id_model_providers_provider_id_get.asyncio_detailed(
                    client=client,
                    organization_id=self._bindings["organization_id"],
                    provider_id=self._bindings["provider_id"],
                )
            )
        )

    async def update(self, *, body: wire.ProviderUpdate, if_match: str | Unset | None = UNSET) -> Result[wire.Provider]:
        """Update Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                update_provider_api_v1_organizations_organization_id_model_providers_provider_id_patch.asyncio_detailed(
                    client=client,
                    organization_id=self._bindings["organization_id"],
                    provider_id=self._bindings["provider_id"],
                    body=body,
                    if_match=if_match,
                )
            )
        )

    async def test(self) -> Result[wire.ProviderTest]:
        """Test Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                test_provider_api_v1_organizations_organization_id_model_providers_provider_id_test_post.asyncio_detailed(
                    client=client,
                    organization_id=self._bindings["organization_id"],
                    provider_id=self._bindings["provider_id"],
                )
            )
        )


class OrganizationsOrganizationIdModels(Resource):
    """Bound Native resource: /organizations / {organization_id} / models."""

    async def list(
        self,
        *,
        workspace_id: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> Result[wire.ModelPage]:
        """List Models. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_models_api_v1_organizations_organization_id_models_get.asyncio_detailed(
                client=client,
                organization_id=self._bindings["organization_id"],
                workspace_id=workspace_id,
                limit=limit,
                cursor=cursor,
            )
        )

    def pages(
        self,
        *,
        workspace_id: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.ModelPage]]:
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
    ) -> AsyncIterator[wire.Model]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(workspace_id=workspace_id, limit=limit, cursor=cursor)
            for item in page.value.items
        )

    async def create(self, *, body: wire.ModelCreate) -> Result[wire.Model]:
        """Create Model. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_model_api_v1_organizations_organization_id_models_post.asyncio_detailed(
                client=client, organization_id=self._bindings["organization_id"], body=body
            )
        )

    def __call__(self, model_id: str) -> OrganizationsOrganizationIdModelsModelId:
        return OrganizationsOrganizationIdModelsModelId(self._client, self._bind("model_id", model_id))


class OrganizationsOrganizationIdModelsModelId(Resource):
    """Bound Native resource: /organizations / {organization_id} / models / {model_id}."""

    async def get(self) -> Result[wire.Model]:
        """Get Model. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_model_api_v1_organizations_organization_id_models_model_id_get.asyncio_detailed(
                client=client, organization_id=self._bindings["organization_id"], model_id=self._bindings["model_id"]
            )
        )

    async def update(self, *, body: wire.ModelUpdate, if_match: str | Unset | None = UNSET) -> Result[wire.Model]:
        """Update Model. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_model_api_v1_organizations_organization_id_models_model_id_patch.asyncio_detailed(
                client=client,
                organization_id=self._bindings["organization_id"],
                model_id=self._bindings["model_id"],
                body=body,
                if_match=if_match,
            )
        )


class OrganizationsOrganizationIdWebProviders(Resource):
    """Bound Native resource: /organizations / {organization_id} / web-providers."""

    async def list(
        self,
        *,
        workspace_id: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> Result[wire.ProviderPage]:
        """List Providers. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_providers_api_v1_organizations_organization_id_web_providers_get.asyncio_detailed(
                client=client,
                organization_id=self._bindings["organization_id"],
                workspace_id=workspace_id,
                limit=limit,
                cursor=cursor,
            )
        )

    def pages(
        self,
        *,
        workspace_id: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.ProviderPage]]:
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
    ) -> AsyncIterator[wire.Provider]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(workspace_id=workspace_id, limit=limit, cursor=cursor)
            for item in page.value.items
        )

    async def create(self, *, body: wire.ProviderCreate) -> Result[wire.Provider]:
        """Create Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_provider_api_v1_organizations_organization_id_web_providers_post.asyncio_detailed(
                client=client, organization_id=self._bindings["organization_id"], body=body
            )
        )

    def __call__(self, provider_id: str) -> OrganizationsOrganizationIdWebProvidersProviderId:
        return OrganizationsOrganizationIdWebProvidersProviderId(self._client, self._bind("provider_id", provider_id))


class OrganizationsOrganizationIdWebProvidersProviderId(Resource):
    """Bound Native resource: /organizations / {organization_id} / web-providers / {provider_id}."""

    async def get(self) -> Result[wire.Provider]:
        """Get Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                get_provider_api_v1_organizations_organization_id_web_providers_provider_id_get.asyncio_detailed(
                    client=client,
                    organization_id=self._bindings["organization_id"],
                    provider_id=self._bindings["provider_id"],
                )
            )
        )

    async def update(self, *, body: wire.ProviderUpdate, if_match: str | Unset | None = UNSET) -> Result[wire.Provider]:
        """Update Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                update_provider_api_v1_organizations_organization_id_web_providers_provider_id_patch.asyncio_detailed(
                    client=client,
                    organization_id=self._bindings["organization_id"],
                    provider_id=self._bindings["provider_id"],
                    body=body,
                    if_match=if_match,
                )
            )
        )

    async def test(self) -> Result[wire.ProviderTest]:
        """Test Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                test_provider_api_v1_organizations_organization_id_web_providers_provider_id_test_post.asyncio_detailed(
                    client=client,
                    organization_id=self._bindings["organization_id"],
                    provider_id=self._bindings["provider_id"],
                )
            )
        )


class OrganizationsOrganizationIdWorkspaces(Resource):
    """Bound Native resource: /organizations / {organization_id} / workspaces."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.WorkspacePage]:
        """List Organization Workspaces. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                list_organization_workspaces_api_v1_organizations_organization_id_workspaces_get.asyncio_detailed(
                    client=client, organization_id=self._bindings["organization_id"], limit=limit, cursor=cursor
                )
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
            lambda client: create_workspace_api_v1_organizations_organization_id_workspaces_post.asyncio_detailed(
                client=client, organization_id=self._bindings["organization_id"], body=body
            )
        )


class ProviderTypes(Resource):
    """Bound Native resource: /provider-types."""

    def __call__(self, kind: wire.ListProviderTypesApiV1ProviderTypesKindGetKind) -> ProviderTypesKind:
        return ProviderTypesKind(self._client, self._bind("kind", str(kind)))


class ProviderTypesKind(Resource):
    """Bound Native resource: /provider-types / {kind}."""

    async def list(self) -> Result[wire.ProviderTypePage]:
        """List Provider Types. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_provider_types_api_v1_provider_types_kind_get.asyncio_detailed(
                client=client, kind=wire.ListProviderTypesApiV1ProviderTypesKindGetKind(self._bindings["kind"])
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
        return await self._call(lambda client: get_profile_api_v1_users_me_get.asyncio_detailed(client=client))

    async def update(self, *, body: wire.ProfileUpdate, if_match: str | Unset | None = UNSET) -> Result[wire.Profile]:
        """Update Profile. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_profile_api_v1_users_me_patch.asyncio_detailed(
                client=client, body=body, if_match=if_match
            )
        )

    @property
    def audit_events(self) -> UsersMeAuditEvents:
        return UsersMeAuditEvents(self._client, self._bindings)

    @property
    def avatar(self) -> UsersMeAvatar:
        return UsersMeAvatar(self._client, self._bindings)

    async def disable(self, *, body: wire.AccountDisable) -> Result[None]:
        """Disable Account. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: disable_account_api_v1_users_me_disable_post.asyncio_detailed(client=client, body=body)
        )

    @property
    def keys(self) -> UsersMeKeys:
        return UsersMeKeys(self._client, self._bindings)

    @property
    def login_sessions(self) -> UsersMeLoginSessions:
        return UsersMeLoginSessions(self._client, self._bindings)

    async def password(self, *, body: wire.PasswordChange) -> Result[None]:
        """Change Password. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: change_password_api_v1_users_me_password_post.asyncio_detailed(client=client, body=body)
        )


class UsersMeAuditEvents(Resource):
    """Bound Native resource: /users / me / audit-events."""

    async def list(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> Result[wire.AuditPage]:
        """List Account Audit Events. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_account_audit_events_api_v1_users_me_audit_events_get.asyncio_detailed(
                client=client, limit=limit, cursor=cursor
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


class UsersMeAvatar(Resource):
    """Bound Native resource: /users / me / avatar."""

    async def delete(self, *, if_match: str | Unset | None = UNSET) -> Result[wire.Profile]:
        """Delete Avatar. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_avatar_api_v1_users_me_avatar_delete.asyncio_detailed(
                client=client, if_match=if_match
            )
        )

    async def replace(self, *, body: File, if_match: str | Unset | None = UNSET) -> Result[wire.Profile]:
        """Put Avatar. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: put_avatar_api_v1_users_me_avatar_put.asyncio_detailed(
                client=client, body=body, if_match=if_match
            )
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
            lambda client: list_user_keys_api_v1_users_me_keys_get.asyncio_detailed(
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
        return await self._call(
            lambda client: create_user_key_api_v1_users_me_keys_post.asyncio_detailed(client=client, body=body)
        )

    def __call__(self, key_id: str) -> UsersMeKeysKeyId:
        return UsersMeKeysKeyId(self._client, self._bind("key_id", key_id))


class UsersMeKeysKeyId(Resource):
    """Bound Native resource: /users / me / keys / {key_id}."""

    async def delete(self, *, if_match: str | Unset | None = UNSET) -> Result[wire.ApiKey]:
        """Revoke User Key. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: revoke_user_key_api_v1_users_me_keys_key_id_delete.asyncio_detailed(
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
            lambda client: list_login_sessions_api_v1_users_me_login_sessions_get.asyncio_detailed(
                client=client, limit=limit, cursor=cursor
            )
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
            lambda client: revoke_login_session_api_v1_users_me_login_sessions_session_id_delete.asyncio_detailed(
                client=client, session_id=self._bindings["session_id"]
            )
        )


class UsersUserId(Resource):
    """Bound Native resource: /users / {user_id}."""

    @property
    def avatar(self) -> UsersUserIdAvatar:
        return UsersUserIdAvatar(self._client, self._bindings)


class UsersUserIdAvatar(Resource):
    """Bound Native resource: /users / {user_id} / avatar."""

    async def get(self) -> Result[File]:
        """Get Avatar. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_avatar_api_v1_users_user_id_avatar_get.asyncio_detailed(
                client=client, user_id=self._bindings["user_id"]
            )
        )

    def get_stream(self) -> AbstractAsyncContextManager[httpx2.Response]:
        """Unbuffered response; caller checks status and consumes within the context."""
        return self._stream(get_avatar_api_v1_users_user_id_avatar_get.build_request(user_id=self._bindings["user_id"]))


class Workspaces(Resource):
    """Bound Native resource: /workspaces."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.WorkspacePage]:
        """List Workspaces. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_workspaces_api_v1_workspaces_get.asyncio_detailed(
                client=client, limit=limit, cursor=cursor
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

    def __call__(self, workspace_id: str) -> Workspace:
        return Workspace(self._client, self._bind("workspace_id", workspace_id))


class _WorkspaceResource(Resource):
    """Bound Native resource: /workspaces / {workspace_id}."""

    async def get(self) -> Result[wire.Workspace]:
        """Get Workspace. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspace_api_v1_workspaces_workspace_id_get.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"]
            )
        )

    async def update(
        self, *, body: wire.WorkspaceUpdate, if_match: str | Unset | None = UNSET
    ) -> Result[wire.Workspace]:
        """Update Workspace. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_workspace_api_v1_workspaces_workspace_id_patch.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], body=body, if_match=if_match
            )
        )

    @property
    def agents(self) -> WorkspacesWorkspaceIdAgents:
        return WorkspacesWorkspaceIdAgents(self._client, self._bindings)

    async def archive(self, *, if_match: str | Unset | None = UNSET) -> Result[wire.Workspace]:
        """Archive Workspace. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: archive_workspace_api_v1_workspaces_workspace_id_archive_post.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], if_match=if_match
            )
        )

    @property
    def assets(self) -> WorkspacesWorkspaceIdAssets:
        return WorkspacesWorkspaceIdAssets(self._client, self._bindings)

    @property
    def audit_events(self) -> WorkspacesWorkspaceIdAuditEvents:
        return WorkspacesWorkspaceIdAuditEvents(self._client, self._bindings)

    async def configuration_assistant(self) -> Result[wire.Agent]:
        """Prepare Assistant. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                prepare_assistant_api_v1_workspaces_workspace_id_configuration_assistant_post.asyncio_detailed(
                    client=client, workspace_id=self._bindings["workspace_id"]
                )
            )
        )

    @property
    def connections(self) -> WorkspacesWorkspaceIdConnections:
        return WorkspacesWorkspaceIdConnections(self._client, self._bindings)

    @property
    def connector_providers(self) -> WorkspacesWorkspaceIdConnectorProviders:
        return WorkspacesWorkspaceIdConnectorProviders(self._client, self._bindings)

    @property
    def environment_templates(self) -> WorkspacesWorkspaceIdEnvironmentTemplates:
        return WorkspacesWorkspaceIdEnvironmentTemplates(self._client, self._bindings)

    @property
    def environments(self) -> WorkspacesWorkspaceIdEnvironments:
        return WorkspacesWorkspaceIdEnvironments(self._client, self._bindings)

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
    def media_understanding_defaults(self) -> WorkspacesWorkspaceIdMediaUnderstandingDefaults:
        return WorkspacesWorkspaceIdMediaUnderstandingDefaults(self._client, self._bindings)

    @property
    def memories(self) -> WorkspacesWorkspaceIdMemories:
        return WorkspacesWorkspaceIdMemories(self._client, self._bindings)

    @property
    def runs(self) -> WorkspacesWorkspaceIdRuns:
        return WorkspacesWorkspaceIdRuns(self._client, self._bindings)

    @property
    def secrets(self) -> WorkspacesWorkspaceIdSecrets:
        return WorkspacesWorkspaceIdSecrets(self._client, self._bindings)

    @property
    def service_accounts(self) -> WorkspacesWorkspaceIdServiceAccounts:
        return WorkspacesWorkspaceIdServiceAccounts(self._client, self._bindings)

    @property
    def sessions(self) -> WorkspacesWorkspaceIdSessions:
        return WorkspacesWorkspaceIdSessions(self._client, self._bindings)

    @property
    def skills(self) -> WorkspacesWorkspaceIdSkills:
        return WorkspacesWorkspaceIdSkills(self._client, self._bindings)

    @property
    def subscriptions(self) -> WorkspacesWorkspaceIdSubscriptions:
        return WorkspacesWorkspaceIdSubscriptions(self._client, self._bindings)

    @property
    def threads(self) -> WorkspacesWorkspaceIdThreads:
        return WorkspacesWorkspaceIdThreads(self._client, self._bindings)

    @property
    def toolsets(self) -> WorkspacesWorkspaceIdToolsets:
        return WorkspacesWorkspaceIdToolsets(self._client, self._bindings)

    @property
    def trace_backend(self) -> WorkspacesWorkspaceIdTraceBackend:
        return WorkspacesWorkspaceIdTraceBackend(self._client, self._bindings)

    @property
    def traces(self) -> WorkspacesWorkspaceIdTraces:
        return WorkspacesWorkspaceIdTraces(self._client, self._bindings)

    @property
    def uploads(self) -> WorkspacesWorkspaceIdUploads:
        return WorkspacesWorkspaceIdUploads(self._client, self._bindings)

    @property
    def usage(self) -> WorkspacesWorkspaceIdUsage:
        return WorkspacesWorkspaceIdUsage(self._client, self._bindings)


class WorkspacesWorkspaceIdAgents(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / agents."""

    async def list(
        self,
        *,
        label: list[str] | Unset | None = UNSET,
        q: str | Unset | None = UNSET,
        archived: bool | Unset | None = UNSET,
        skill_id: str | Unset | None = UNSET,
        skill_revision_id: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> Result[wire.AgentPage]:
        """List Agents. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_agents_api_v1_workspaces_workspace_id_agents_get.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                label=label,
                q=q,
                archived=archived,
                skill_id=skill_id,
                skill_revision_id=skill_revision_id,
                limit=limit,
                cursor=cursor,
            )
        )

    def pages(
        self,
        *,
        label: list[str] | Unset | None = UNSET,
        q: str | Unset | None = UNSET,
        archived: bool | Unset | None = UNSET,
        skill_id: str | Unset | None = UNSET,
        skill_revision_id: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.AgentPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        label = label.copy() if isinstance(label, list) else label
        return pages(
            lambda next_cursor: self.list(
                label=label,
                q=q,
                archived=archived,
                skill_id=skill_id,
                skill_revision_id=skill_revision_id,
                limit=limit,
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
        skill_id: str | Unset | None = UNSET,
        skill_revision_id: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.Agent]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(
                label=label,
                q=q,
                archived=archived,
                skill_id=skill_id,
                skill_revision_id=skill_revision_id,
                limit=limit,
                cursor=cursor,
            )
            for item in page.value.items
        )

    async def create(self, *, body: wire.AgentCreate) -> Result[wire.Agent]:
        """Create Agent. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_agent_api_v1_workspaces_workspace_id_agents_post.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], body=body
            )
        )

    async def validate(self, *, body: wire.AgentValidate) -> Result[None]:
        """Validate Revision. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: validate_revision_api_v1_workspaces_workspace_id_agents_validate_post.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], body=body
            )
        )

    def __call__(self, agent_id: str) -> Agent:
        return Agent(self._client, self._bind("agent_id", agent_id))


class Agent(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / agents / {agent_id}."""

    async def get(self) -> Result[wire.Agent]:
        """Get Agent. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_agent_api_v1_workspaces_workspace_id_agents_agent_id_get.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], agent_id=self._bindings["agent_id"]
            )
        )

    async def update(self, *, body: wire.AgentUpdate, if_match: str | Unset | None = UNSET) -> Result[wire.Agent]:
        """Update Agent. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_agent_api_v1_workspaces_workspace_id_agents_agent_id_patch.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                agent_id=self._bindings["agent_id"],
                body=body,
                if_match=if_match,
            )
        )

    async def archive(self, *, if_match: str | Unset | None = UNSET) -> Result[wire.Agent]:
        """Archive Agent. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: archive_agent_api_v1_workspaces_workspace_id_agents_agent_id_archive_post.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                agent_id=self._bindings["agent_id"],
                if_match=if_match,
            )
        )

    @property
    def avatar(self) -> WorkspacesWorkspaceIdAgentsAgentIdAvatar:
        return WorkspacesWorkspaceIdAgentsAgentIdAvatar(self._client, self._bindings)

    async def duplicate(self, *, body: wire.AgentDuplicate) -> Result[wire.Agent]:
        """Duplicate Agent. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                duplicate_agent_api_v1_workspaces_workspace_id_agents_agent_id_duplicate_post.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    agent_id=self._bindings["agent_id"],
                    body=body,
                )
            )
        )

    @property
    def revisions(self) -> WorkspacesWorkspaceIdAgentsAgentIdRevisions:
        return WorkspacesWorkspaceIdAgentsAgentIdRevisions(self._client, self._bindings)

    async def unarchive(self, *, if_match: str | Unset | None = UNSET) -> Result[wire.Agent]:
        """Unarchive Agent. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                unarchive_agent_api_v1_workspaces_workspace_id_agents_agent_id_unarchive_post.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    agent_id=self._bindings["agent_id"],
                    if_match=if_match,
                )
            )
        )


class WorkspacesWorkspaceIdAgentsAgentIdAvatar(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / agents / {agent_id} / avatar."""

    async def delete(self, *, if_match: str | Unset | None = UNSET) -> Result[wire.Agent]:
        """Delete Avatar. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_avatar_api_v1_workspaces_workspace_id_agents_agent_id_avatar_delete.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                agent_id=self._bindings["agent_id"],
                if_match=if_match,
            )
        )

    async def get(self) -> Result[File]:
        """Get Avatar. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_avatar_api_v1_workspaces_workspace_id_agents_agent_id_avatar_get.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], agent_id=self._bindings["agent_id"]
            )
        )

    def get_stream(self) -> AbstractAsyncContextManager[httpx2.Response]:
        """Unbuffered response; caller checks status and consumes within the context."""
        return self._stream(
            get_avatar_api_v1_workspaces_workspace_id_agents_agent_id_avatar_get.build_request(
                workspace_id=self._bindings["workspace_id"], agent_id=self._bindings["agent_id"]
            )
        )

    async def replace(self, *, body: File, if_match: str | Unset | None = UNSET) -> Result[wire.Agent]:
        """Put Avatar. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: put_avatar_api_v1_workspaces_workspace_id_agents_agent_id_avatar_put.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                agent_id=self._bindings["agent_id"],
                body=body,
                if_match=if_match,
            )
        )


class WorkspacesWorkspaceIdAgentsAgentIdRevisions(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / agents / {agent_id} / revisions."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.AgentRevisionPage]:
        """List Revisions. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_revisions_api_v1_workspaces_workspace_id_agents_agent_id_revisions_get.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                agent_id=self._bindings["agent_id"],
                limit=limit,
                cursor=cursor,
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.AgentRevisionPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.AgentRevision]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    async def create(
        self, *, body: wire.AgentRevisionCreate, if_match: str | Unset | None = UNSET
    ) -> Result[wire.AgentRevision]:
        """Create Revision. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                create_revision_api_v1_workspaces_workspace_id_agents_agent_id_revisions_post.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    agent_id=self._bindings["agent_id"],
                    body=body,
                    if_match=if_match,
                )
            )
        )

    def __call__(self, revision_id: str) -> WorkspacesWorkspaceIdAgentsAgentIdRevisionsRevisionId:
        return WorkspacesWorkspaceIdAgentsAgentIdRevisionsRevisionId(
            self._client, self._bind("revision_id", revision_id)
        )


class WorkspacesWorkspaceIdAgentsAgentIdRevisionsRevisionId(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / agents / {agent_id} / revisions / {revision_id}."""

    async def get(self) -> Result[wire.AgentRevision]:
        """Get Revision. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                get_revision_api_v1_workspaces_workspace_id_agents_agent_id_revisions_revision_id_get.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    agent_id=self._bindings["agent_id"],
                    revision_id=self._bindings["revision_id"],
                )
            )
        )

    async def set_default(self, *, if_match: str | Unset | None = UNSET) -> Result[wire.Agent]:
        """Set Default. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                set_default_api_v1_workspaces_workspace_id_agents_agent_id_revisions_revision_id_set_default_post.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    agent_id=self._bindings["agent_id"],
                    revision_id=self._bindings["revision_id"],
                    if_match=if_match,
                )
            )
        )


class WorkspacesWorkspaceIdAssets(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / assets."""

    async def list(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> Result[wire.AssetPage]:
        """List Assets. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_assets_api_v1_workspaces_workspace_id_assets_get.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.AssetPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> AsyncIterator[wire.Asset]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    async def create(self, *, body: wire.AssetCreate) -> Result[wire.Asset]:
        """Create Asset. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_asset_api_v1_workspaces_workspace_id_assets_post.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], body=body
            )
        )

    def __call__(self, asset_id: str) -> WorkspacesWorkspaceIdAssetsAssetId:
        return WorkspacesWorkspaceIdAssetsAssetId(self._client, self._bind("asset_id", asset_id))


class WorkspacesWorkspaceIdAssetsAssetId(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / assets / {asset_id}."""

    async def delete(self, *, if_match: str | Unset | None = UNSET) -> Result[wire.Asset]:
        """Retire Asset. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: retire_asset_api_v1_workspaces_workspace_id_assets_asset_id_delete.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                asset_id=self._bindings["asset_id"],
                if_match=if_match,
            )
        )

    async def get(self) -> Result[wire.Asset]:
        """Get Asset. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_asset_api_v1_workspaces_workspace_id_assets_asset_id_get.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], asset_id=self._bindings["asset_id"]
            )
        )

    @property
    def content(self) -> WorkspacesWorkspaceIdAssetsAssetIdContent:
        return WorkspacesWorkspaceIdAssetsAssetIdContent(self._client, self._bindings)


class WorkspacesWorkspaceIdAssetsAssetIdContent(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / assets / {asset_id} / content."""

    async def get(self) -> Result[File]:
        """Read Asset Content. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                read_asset_content_api_v1_workspaces_workspace_id_assets_asset_id_content_get.asyncio_detailed(
                    client=client, workspace_id=self._bindings["workspace_id"], asset_id=self._bindings["asset_id"]
                )
            )
        )

    def get_stream(self) -> AbstractAsyncContextManager[httpx2.Response]:
        """Unbuffered response; caller checks status and consumes within the context."""
        return self._stream(
            read_asset_content_api_v1_workspaces_workspace_id_assets_asset_id_content_get.build_request(
                workspace_id=self._bindings["workspace_id"], asset_id=self._bindings["asset_id"]
            )
        )


class WorkspacesWorkspaceIdAuditEvents(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / audit-events."""

    async def list(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> Result[wire.AuditPage]:
        """List Workspace Audit Events. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_workspace_audit_events_api_v1_workspaces_workspace_id_audit_events_get.asyncio_detailed(
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


class WorkspacesWorkspaceIdConnections(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / connections."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.ConnectionPage]:
        """List Connections. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_connections_api_v1_workspaces_workspace_id_connections_get.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.ConnectionPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> AsyncIterator[wire.Connection]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    async def create(self, *, body: wire.ConnectionCreate) -> Result[wire.Connection]:
        """Create Connection. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_connection_api_v1_workspaces_workspace_id_connections_post.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], body=body
            )
        )

    def __call__(self, connection_id: str) -> WorkspacesWorkspaceIdConnectionsConnectionId:
        return WorkspacesWorkspaceIdConnectionsConnectionId(self._client, self._bind("connection_id", connection_id))


class WorkspacesWorkspaceIdConnectionsConnectionId(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / connections / {connection_id}."""

    async def get(self) -> Result[wire.Connection]:
        """Get Connection. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_connection_api_v1_workspaces_workspace_id_connections_connection_id_get.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                connection_id=self._bindings["connection_id"],
            )
        )

    async def update(
        self, *, body: wire.ConnectionUpdate, if_match: str | Unset | None = UNSET
    ) -> Result[wire.Connection]:
        """Update Connection. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                update_connection_api_v1_workspaces_workspace_id_connections_connection_id_patch.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    connection_id=self._bindings["connection_id"],
                    body=body,
                    if_match=if_match,
                )
            )
        )

    async def authorize(
        self, *, body: wire.AuthorizationRequest, if_match: str | Unset | None = UNSET
    ) -> Result[wire.AuthorizationResult]:
        """Authorize Connection. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                authorize_connection_api_v1_workspaces_workspace_id_connections_connection_id_authorize_post.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    connection_id=self._bindings["connection_id"],
                    body=body,
                    if_match=if_match,
                )
            )
        )

    async def revoke(self, *, if_match: str | Unset | None = UNSET) -> Result[wire.RevokedConnection]:
        """Revoke Connection. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                revoke_connection_api_v1_workspaces_workspace_id_connections_connection_id_revoke_post.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    connection_id=self._bindings["connection_id"],
                    if_match=if_match,
                )
            )
        )

    async def test(self) -> Result[wire.ConnectionTest]:
        """Test Connection. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                test_connection_api_v1_workspaces_workspace_id_connections_connection_id_test_post.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    connection_id=self._bindings["connection_id"],
                )
            )
        )

    @property
    def tools(self) -> WorkspacesWorkspaceIdConnectionsConnectionIdTools:
        return WorkspacesWorkspaceIdConnectionsConnectionIdTools(self._client, self._bindings)


class WorkspacesWorkspaceIdConnectionsConnectionIdTools(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / connections / {connection_id} / tools."""

    async def list(self) -> Result[wire.ToolPage]:
        """List Tools. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                list_tools_api_v1_workspaces_workspace_id_connections_connection_id_tools_get.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    connection_id=self._bindings["connection_id"],
                )
            )
        )


class WorkspacesWorkspaceIdConnectorProviders(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / connector-providers."""

    def __call__(self, provider_id: str) -> WorkspacesWorkspaceIdConnectorProvidersProviderId:
        return WorkspacesWorkspaceIdConnectorProvidersProviderId(self._client, self._bind("provider_id", provider_id))


class WorkspacesWorkspaceIdConnectorProvidersProviderId(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / connector-providers / {provider_id}."""

    @property
    def apps(self) -> WorkspacesWorkspaceIdConnectorProvidersProviderIdApps:
        return WorkspacesWorkspaceIdConnectorProvidersProviderIdApps(self._client, self._bindings)


class WorkspacesWorkspaceIdConnectorProvidersProviderIdApps(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / connector-providers / {provider_id} / apps."""

    async def list(
        self,
        *,
        query: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        refresh: bool | Unset = UNSET,
    ) -> Result[wire.ConnectorAppPage]:
        """List Apps. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                list_apps_api_v1_workspaces_workspace_id_connector_providers_provider_id_apps_get.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    provider_id=self._bindings["provider_id"],
                    query=query,
                    limit=limit,
                    cursor=cursor,
                    refresh=refresh,
                )
            )
        )

    def pages(
        self,
        *,
        query: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        refresh: bool | Unset = UNSET,
    ) -> AsyncIterator[Result[wire.ConnectorAppPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(query=query, limit=limit, refresh=refresh, cursor=next_cursor),
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
    ) -> AsyncIterator[wire.ConnectorApp]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(query=query, limit=limit, cursor=cursor, refresh=refresh)
            for item in page.value.items
        )

    def __call__(self, app: str) -> WorkspacesWorkspaceIdConnectorProvidersProviderIdAppsApp:
        return WorkspacesWorkspaceIdConnectorProvidersProviderIdAppsApp(self._client, self._bind("app", app))


class WorkspacesWorkspaceIdConnectorProvidersProviderIdAppsApp(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / connector-providers / {provider_id} / apps / {app}."""

    async def get(self) -> Result[wire.ConnectorApp]:
        """Get App. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                get_app_api_v1_workspaces_workspace_id_connector_providers_provider_id_apps_app_get.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    provider_id=self._bindings["provider_id"],
                    app=self._bindings["app"],
                )
            )
        )

    @property
    def actions(self) -> WorkspacesWorkspaceIdConnectorProvidersProviderIdAppsAppActions:
        return WorkspacesWorkspaceIdConnectorProvidersProviderIdAppsAppActions(self._client, self._bindings)


class WorkspacesWorkspaceIdConnectorProvidersProviderIdAppsAppActions(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / connector-providers / {provider_id} / apps / {app} / actions."""

    async def list(self) -> Result[wire.ConnectorActionPage]:
        """List Actions. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                list_actions_api_v1_workspaces_workspace_id_connector_providers_provider_id_apps_app_actions_get.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    provider_id=self._bindings["provider_id"],
                    app=self._bindings["app"],
                )
            )
        )


class WorkspacesWorkspaceIdEnvironmentTemplates(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / environment-templates."""

    async def list(
        self, *, label: list[str] | Unset | None = UNSET, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.TemplatePage]:
        """List Templates. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_templates_api_v1_workspaces_workspace_id_environment_templates_get.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], label=label, limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, label: list[str] | Unset | None = UNSET, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.TemplatePage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        label = label.copy() if isinstance(label, list) else label
        return pages(
            lambda next_cursor: self.list(label=label, limit=limit, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self, *, label: list[str] | Unset | None = UNSET, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.Template]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(label=label, limit=limit, cursor=cursor) for item in page.value.items)

    async def create(self, *, body: wire.TemplateCreate) -> Result[wire.Template]:
        """Create Template. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_template_api_v1_workspaces_workspace_id_environment_templates_post.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], body=body
            )
        )

    def __call__(self, template_id: str) -> WorkspacesWorkspaceIdEnvironmentTemplatesTemplateId:
        return WorkspacesWorkspaceIdEnvironmentTemplatesTemplateId(self._client, self._bind("template_id", template_id))


class WorkspacesWorkspaceIdEnvironmentTemplatesTemplateId(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / environment-templates / {template_id}."""

    async def get(self) -> Result[wire.Template]:
        """Get Template. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                get_template_api_v1_workspaces_workspace_id_environment_templates_template_id_get.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    template_id=self._bindings["template_id"],
                )
            )
        )

    async def update(self, *, body: wire.TemplateUpdate, if_match: str | Unset | None = UNSET) -> Result[wire.Template]:
        """Update Template. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                update_template_api_v1_workspaces_workspace_id_environment_templates_template_id_patch.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    template_id=self._bindings["template_id"],
                    body=body,
                    if_match=if_match,
                )
            )
        )


class WorkspacesWorkspaceIdEnvironments(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / environments."""

    async def list(
        self, *, status: str | Unset | None = UNSET, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.EnvironmentPage]:
        """List Environments. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_environments_api_v1_workspaces_workspace_id_environments_get.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], status=status, limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, status: str | Unset | None = UNSET, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.EnvironmentPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(status=status, limit=limit, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self, *, status: str | Unset | None = UNSET, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.EnvironmentView]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item async for page in self.pages(status=status, limit=limit, cursor=cursor) for item in page.value.items
        )

    async def create(
        self, *, body: wire.ExternalTargetCreate | wire.ManagedEnvironmentCreate
    ) -> Result[wire.EnvironmentView]:
        """Create Environment. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_environment_api_v1_workspaces_workspace_id_environments_post.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], body=body
            )
        )

    def __call__(self, environment_id: str) -> WorkspacesWorkspaceIdEnvironmentsEnvironmentId:
        return WorkspacesWorkspaceIdEnvironmentsEnvironmentId(
            self._client, self._bind("environment_id", environment_id)
        )


class WorkspacesWorkspaceIdEnvironmentsEnvironmentId(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / environments / {environment_id}."""

    async def delete(self, *, if_match: str | Unset | None = UNSET) -> Result[wire.EnvironmentView]:
        """Delete Environment. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                delete_environment_api_v1_workspaces_workspace_id_environments_environment_id_delete.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    environment_id=self._bindings["environment_id"],
                    if_match=if_match,
                )
            )
        )

    async def get(self) -> Result[wire.EnvironmentView]:
        """Get Environment. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                get_environment_api_v1_workspaces_workspace_id_environments_environment_id_get.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    environment_id=self._bindings["environment_id"],
                )
            )
        )

    async def update(
        self, *, body: wire.EnvironmentUpdate, if_match: str | Unset | None = UNSET
    ) -> Result[wire.EnvironmentView]:
        """Update Environment. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                update_environment_api_v1_workspaces_workspace_id_environments_environment_id_patch.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    environment_id=self._bindings["environment_id"],
                    body=body,
                    if_match=if_match,
                )
            )
        )

    async def stop(self, *, if_match: str | Unset | None = UNSET) -> Result[wire.EnvironmentView]:
        """Stop Environment. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                stop_environment_api_v1_workspaces_workspace_id_environments_environment_id_stop_post.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    environment_id=self._bindings["environment_id"],
                    if_match=if_match,
                )
            )
        )


class WorkspacesWorkspaceIdGrants(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / grants."""

    async def list(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> Result[wire.GrantPage]:
        """List Workspace Grants. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_workspace_grants_api_v1_workspaces_workspace_id_grants_get.asyncio_detailed(
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
            lambda client: create_workspace_grant_api_v1_workspaces_workspace_id_grants_post.asyncio_detailed(
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
            lambda client: (
                delete_workspace_grant_api_v1_workspaces_workspace_id_grants_grant_id_delete.asyncio_detailed(
                    client=client, workspace_id=self._bindings["workspace_id"], grant_id=self._bindings["grant_id"]
                )
            )
        )

    async def update(self, *, body: wire.GrantUpdate) -> Result[wire.GrantView]:
        """Change Workspace Grant. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: change_workspace_grant_api_v1_workspaces_workspace_id_grants_grant_id_patch.asyncio_detailed(
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
            lambda client: delete_workspace_icon_api_v1_workspaces_workspace_id_icon_delete.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], if_match=if_match
            )
        )

    async def get(self) -> Result[File]:
        """Get Workspace Icon. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspace_icon_api_v1_workspaces_workspace_id_icon_get.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"]
            )
        )

    def get_stream(self) -> AbstractAsyncContextManager[httpx2.Response]:
        """Unbuffered response; caller checks status and consumes within the context."""
        return self._stream(
            get_workspace_icon_api_v1_workspaces_workspace_id_icon_get.build_request(
                workspace_id=self._bindings["workspace_id"]
            )
        )

    async def replace(self, *, body: File, if_match: str | Unset | None = UNSET) -> Result[wire.Workspace]:
        """Put Workspace Icon. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: put_workspace_icon_api_v1_workspaces_workspace_id_icon_put.asyncio_detailed(
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
            lambda client: list_workspace_invitations_api_v1_workspaces_workspace_id_invitations_get.asyncio_detailed(
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
            lambda client: create_workspace_invitation_api_v1_workspaces_workspace_id_invitations_post.asyncio_detailed(
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
            lambda client: (
                resend_workspace_invitation_api_v1_workspaces_workspace_id_invitations_invitation_id_resend_post.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    invitation_id=self._bindings["invitation_id"],
                    if_match=if_match,
                )
            )
        )

    async def revoke(self, *, if_match: str | Unset | None = UNSET) -> Result[wire.Invitation]:
        """Revoke Workspace Invitation. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                revoke_workspace_invitation_api_v1_workspaces_workspace_id_invitations_invitation_id_revoke_post.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    invitation_id=self._bindings["invitation_id"],
                    if_match=if_match,
                )
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
            lambda client: list_workspace_keys_api_v1_workspaces_workspace_id_keys_get.asyncio_detailed(
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
            lambda client: revoke_workspace_key_api_v1_workspaces_workspace_id_keys_key_id_delete.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                key_id=self._bindings["key_id"],
                if_match=if_match,
            )
        )


class WorkspacesWorkspaceIdMediaUnderstandingDefaults(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / media-understanding-defaults."""

    async def get(self) -> Result[wire.MediaDefaults]:
        """Get Media Defaults. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                get_media_defaults_api_v1_workspaces_workspace_id_media_understanding_defaults_get.asyncio_detailed(
                    client=client, workspace_id=self._bindings["workspace_id"]
                )
            )
        )

    async def replace(
        self, *, body: wire.MediaUnderstandingSelection, if_match: str | Unset | None = UNSET
    ) -> Result[wire.MediaDefaults]:
        """Replace Media Defaults. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                replace_media_defaults_api_v1_workspaces_workspace_id_media_understanding_defaults_put.asyncio_detailed(
                    client=client, workspace_id=self._bindings["workspace_id"], body=body, if_match=if_match
                )
            )
        )


class WorkspacesWorkspaceIdMemories(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / memories."""

    async def list(
        self,
        *,
        label: list[str] | Unset | None = UNSET,
        kind: wire.MemoryKind | Unset | None = UNSET,
        type_: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> Result[wire.MemoryPage]:
        """List Memories. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_memories_api_v1_workspaces_workspace_id_memories_get.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                label=label,
                kind=kind,
                type_=type_,
                limit=limit,
                cursor=cursor,
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
    ) -> AsyncIterator[Result[wire.MemoryPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        label = label.copy() if isinstance(label, list) else label
        return pages(
            lambda next_cursor: self.list(label=label, kind=kind, type_=type_, limit=limit, cursor=next_cursor),
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
    ) -> AsyncIterator[wire.Memory]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(label=label, kind=kind, type_=type_, limit=limit, cursor=cursor)
            for item in page.value.items
        )

    async def create(self, *, body: wire.MemoryCreate) -> Result[wire.Memory]:
        """Create Memory. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_memory_api_v1_workspaces_workspace_id_memories_post.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], body=body
            )
        )

    def __call__(self, memory_id: str) -> WorkspacesWorkspaceIdMemoriesMemoryId:
        return WorkspacesWorkspaceIdMemoriesMemoryId(self._client, self._bind("memory_id", memory_id))


class WorkspacesWorkspaceIdMemoriesMemoryId(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / memories / {memory_id}."""

    async def delete(self, *, if_match: str | Unset | None = UNSET) -> Result[None]:
        """Delete Memory. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_memory_api_v1_workspaces_workspace_id_memories_memory_id_delete.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                memory_id=self._bindings["memory_id"],
                if_match=if_match,
            )
        )

    async def get(self) -> Result[wire.Memory]:
        """Get Memory. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_memory_api_v1_workspaces_workspace_id_memories_memory_id_get.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], memory_id=self._bindings["memory_id"]
            )
        )

    async def update(self, *, body: wire.MemoryUpdate, if_match: str | Unset | None = UNSET) -> Result[wire.Memory]:
        """Update Memory. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_memory_api_v1_workspaces_workspace_id_memories_memory_id_patch.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                memory_id=self._bindings["memory_id"],
                body=body,
                if_match=if_match,
            )
        )

    @property
    def files(self) -> WorkspacesWorkspaceIdMemoriesMemoryIdFiles:
        return WorkspacesWorkspaceIdMemoriesMemoryIdFiles(self._client, self._bindings)

    @property
    def records(self) -> WorkspacesWorkspaceIdMemoriesMemoryIdRecords:
        return WorkspacesWorkspaceIdMemoriesMemoryIdRecords(self._client, self._bindings)

    @property
    def revisions(self) -> WorkspacesWorkspaceIdMemoriesMemoryIdRevisions:
        return WorkspacesWorkspaceIdMemoriesMemoryIdRevisions(self._client, self._bindings)


class WorkspacesWorkspaceIdMemoriesMemoryIdFiles(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / memories / {memory_id} / files."""

    async def list(
        self, *, prefix: str | Unset = UNSET, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.MemoryFilePage]:
        """List Files. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_files_api_v1_workspaces_workspace_id_memories_memory_id_files_get.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                memory_id=self._bindings["memory_id"],
                prefix=prefix,
                limit=limit,
                cursor=cursor,
            )
        )

    def pages(
        self, *, prefix: str | Unset = UNSET, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.MemoryFilePage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(prefix=prefix, limit=limit, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self, *, prefix: str | Unset = UNSET, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.MemoryFileEntry]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item async for page in self.pages(prefix=prefix, limit=limit, cursor=cursor) for item in page.value.items
        )

    async def create(self, *, body: wire.MemoryFileCreate) -> Result[wire.MemoryFile]:
        """Create File. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_file_api_v1_workspaces_workspace_id_memories_memory_id_files_post.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                memory_id=self._bindings["memory_id"],
                body=body,
            )
        )

    async def move(self, *, body: wire.MemoryFileMove, if_match: str | Unset | None = UNSET) -> Result[wire.MemoryFile]:
        """Move File. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: move_file_api_v1_workspaces_workspace_id_memories_memory_id_files_move_post.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                memory_id=self._bindings["memory_id"],
                body=body,
                if_match=if_match,
            )
        )

    def __call__(self, path: str) -> WorkspacesWorkspaceIdMemoriesMemoryIdFilesPath:
        return WorkspacesWorkspaceIdMemoriesMemoryIdFilesPath(self._client, self._bind("path", path))


class WorkspacesWorkspaceIdMemoriesMemoryIdFilesPath(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / memories / {memory_id} / files / {path}."""

    async def delete(self, *, if_match: str | Unset | None = UNSET) -> Result[None]:
        """Delete File. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                delete_file_api_v1_workspaces_workspace_id_memories_memory_id_files_path_delete.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    memory_id=self._bindings["memory_id"],
                    path=self._bindings["path"],
                    if_match=if_match,
                )
            )
        )

    async def get(self) -> Result[wire.MemoryFile]:
        """Read File. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: read_file_api_v1_workspaces_workspace_id_memories_memory_id_files_path_get.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                memory_id=self._bindings["memory_id"],
                path=self._bindings["path"],
            )
        )

    async def replace(
        self, *, body: wire.MemoryFileReplace, if_match: str | Unset | None = UNSET
    ) -> Result[wire.MemoryFile]:
        """Replace File. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                replace_file_api_v1_workspaces_workspace_id_memories_memory_id_files_path_put.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    memory_id=self._bindings["memory_id"],
                    path=self._bindings["path"],
                    body=body,
                    if_match=if_match,
                )
            )
        )


class WorkspacesWorkspaceIdMemoriesMemoryIdRecords(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / memories / {memory_id} / records."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.MemoryRecordPage]:
        """List Records. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_records_api_v1_workspaces_workspace_id_memories_memory_id_records_get.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                memory_id=self._bindings["memory_id"],
                limit=limit,
                cursor=cursor,
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.MemoryRecordPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.MemoryRecordView]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    async def create(self, *, body: wire.MemoryRecordText) -> Result[wire.MemoryRecordView]:
        """Add Record. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: add_record_api_v1_workspaces_workspace_id_memories_memory_id_records_post.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                memory_id=self._bindings["memory_id"],
                body=body,
            )
        )

    async def search(self, *, body: wire.MemoryRecordSearch) -> Result[wire.MemoryRecordPage]:
        """Search Records. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                search_records_api_v1_workspaces_workspace_id_memories_memory_id_records_search_post.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    memory_id=self._bindings["memory_id"],
                    body=body,
                )
            )
        )

    def __call__(self, record_id: str) -> WorkspacesWorkspaceIdMemoriesMemoryIdRecordsRecordId:
        return WorkspacesWorkspaceIdMemoriesMemoryIdRecordsRecordId(self._client, self._bind("record_id", record_id))


class WorkspacesWorkspaceIdMemoriesMemoryIdRecordsRecordId(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / memories / {memory_id} / records / {record_id}."""

    async def delete(self) -> Result[None]:
        """Delete Record. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                delete_record_api_v1_workspaces_workspace_id_memories_memory_id_records_record_id_delete.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    memory_id=self._bindings["memory_id"],
                    record_id=self._bindings["record_id"],
                )
            )
        )

    async def replace(self, *, body: wire.MemoryRecordText) -> Result[wire.MemoryRecordView]:
        """Update Record. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                update_record_api_v1_workspaces_workspace_id_memories_memory_id_records_record_id_put.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    memory_id=self._bindings["memory_id"],
                    record_id=self._bindings["record_id"],
                    body=body,
                )
            )
        )


class WorkspacesWorkspaceIdMemoriesMemoryIdRevisions(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / memories / {memory_id} / revisions."""

    async def delete(self, *, path: str) -> Result[wire.HistoryPurge]:
        """Purge History. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                purge_history_api_v1_workspaces_workspace_id_memories_memory_id_revisions_delete.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    memory_id=self._bindings["memory_id"],
                    path=path,
                )
            )
        )

    async def list(
        self,
        *,
        path: str | Unset | None = UNSET,
        run_id: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> Result[wire.MemoryRevisionPage]:
        """List Revisions. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                list_revisions_api_v1_workspaces_workspace_id_memories_memory_id_revisions_get.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    memory_id=self._bindings["memory_id"],
                    path=path,
                    run_id=run_id,
                    limit=limit,
                    cursor=cursor,
                )
            )
        )

    def pages(
        self,
        *,
        path: str | Unset | None = UNSET,
        run_id: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.MemoryRevisionPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(path=path, run_id=run_id, limit=limit, cursor=next_cursor),
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
    ) -> AsyncIterator[wire.MemoryRevision]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(path=path, run_id=run_id, limit=limit, cursor=cursor)
            for item in page.value.items
        )

    def __call__(self, seq: int) -> WorkspacesWorkspaceIdMemoriesMemoryIdRevisionsSeq:
        return WorkspacesWorkspaceIdMemoriesMemoryIdRevisionsSeq(self._client, self._bind("seq", str(seq)))


class WorkspacesWorkspaceIdMemoriesMemoryIdRevisionsSeq(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / memories / {memory_id} / revisions / {seq}."""

    async def get(self) -> Result[wire.MemoryRevisionDetail]:
        """Get Revision. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                get_revision_api_v1_workspaces_workspace_id_memories_memory_id_revisions_seq_get.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    memory_id=self._bindings["memory_id"],
                    seq=int(self._bindings["seq"]),
                )
            )
        )

    async def restore(self, *, if_match: str | Unset | None = UNSET) -> Result[wire.MemoryFileState]:
        """Restore Revision. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                restore_revision_api_v1_workspaces_workspace_id_memories_memory_id_revisions_seq_restore_post.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    memory_id=self._bindings["memory_id"],
                    seq=int(self._bindings["seq"]),
                    if_match=if_match,
                )
            )
        )


class WorkspacesWorkspaceIdRuns(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / runs."""

    def __call__(self, run_id: str) -> Run:
        return Run(self._client, self._bind("run_id", run_id))


class _RunResource(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / runs / {run_id}."""

    async def get(self) -> Result[wire.RunView]:
        """Get Run. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_run_api_v1_workspaces_workspace_id_runs_run_id_get.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], run_id=self._bindings["run_id"]
            )
        )

    async def update(self, *, body: wire.RunLabels, if_match: str | Unset | None = UNSET) -> Result[wire.RunView]:
        """Update Run. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_run_api_v1_workspaces_workspace_id_runs_run_id_patch.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                run_id=self._bindings["run_id"],
                body=body,
                if_match=if_match,
            )
        )

    @property
    def attempts(self) -> WorkspacesWorkspaceIdRunsRunIdAttempts:
        return WorkspacesWorkspaceIdRunsRunIdAttempts(self._client, self._bindings)

    async def fork_receipt(self, *, body: wire.Fork, idempotency_key: str) -> Result[wire.Submitted]:
        """Fork Run. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: fork_run_api_v1_workspaces_workspace_id_runs_run_id_fork_post.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                run_id=self._bindings["run_id"],
                body=body,
                idempotency_key=idempotency_key,
            )
        )

    async def interrupt_receipt(self) -> Result[wire.RunView]:
        """Interrupt Run. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: interrupt_run_api_v1_workspaces_workspace_id_runs_run_id_interrupt_post.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], run_id=self._bindings["run_id"]
            )
        )

    @property
    def items(self) -> WorkspacesWorkspaceIdRunsRunIdItems:
        return WorkspacesWorkspaceIdRunsRunIdItems(self._client, self._bindings)

    @property
    def lineage(self) -> WorkspacesWorkspaceIdRunsRunIdLineage:
        return WorkspacesWorkspaceIdRunsRunIdLineage(self._client, self._bindings)

    async def resume_receipt(self, *, body: wire.ResumeRequest, idempotency_key: str) -> Result[wire.RunView]:
        """Resume Run. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: resume_run_api_v1_workspaces_workspace_id_runs_run_id_resume_post.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                run_id=self._bindings["run_id"],
                body=body,
                idempotency_key=idempotency_key,
            )
        )


class WorkspacesWorkspaceIdRunsRunIdAttempts(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / runs / {run_id} / attempts."""

    async def get(self) -> Result[wire.Attempts]:
        """Run Attempts. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: run_attempts_api_v1_workspaces_workspace_id_runs_run_id_attempts_get.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], run_id=self._bindings["run_id"]
            )
        )

    def __call__(self, attempt_id: str) -> WorkspacesWorkspaceIdRunsRunIdAttemptsAttemptId:
        return WorkspacesWorkspaceIdRunsRunIdAttemptsAttemptId(self._client, self._bind("attempt_id", attempt_id))


class WorkspacesWorkspaceIdRunsRunIdAttemptsAttemptId(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / runs / {run_id} / attempts / {attempt_id}."""

    @property
    def trace(self) -> WorkspacesWorkspaceIdRunsRunIdAttemptsAttemptIdTrace:
        return WorkspacesWorkspaceIdRunsRunIdAttemptsAttemptIdTrace(self._client, self._bindings)


class WorkspacesWorkspaceIdRunsRunIdAttemptsAttemptIdTrace(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / runs / {run_id} / attempts / {attempt_id} / trace."""

    async def list(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> Result[wire.SpanPage]:
        """List Attempt Spans. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                list_attempt_spans_api_v1_workspaces_workspace_id_runs_run_id_attempts_attempt_id_trace_get.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    run_id=self._bindings["run_id"],
                    attempt_id=self._bindings["attempt_id"],
                    limit=limit,
                    cursor=cursor,
                )
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.SpanPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> AsyncIterator[wire.Span]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)


class WorkspacesWorkspaceIdRunsRunIdItems(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / runs / {run_id} / items."""

    async def get(self) -> Result[wire.RunItems]:
        """Run Items. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: run_items_api_v1_workspaces_workspace_id_runs_run_id_items_get.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], run_id=self._bindings["run_id"]
            )
        )


class WorkspacesWorkspaceIdRunsRunIdLineage(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / runs / {run_id} / lineage."""

    async def list(self, *, cursor: str | Unset | None = UNSET) -> Result[wire.RunPage]:
        """Run Lineage. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: run_lineage_api_v1_workspaces_workspace_id_runs_run_id_lineage_get.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                run_id=self._bindings["run_id"],
                cursor=cursor,
            )
        )

    def pages(self, *, cursor: str | Unset | None = UNSET) -> AsyncIterator[Result[wire.RunPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(lambda next_cursor: self.list(cursor=next_cursor), lambda value: value.next_cursor, cursor)

    def iter(self, *, cursor: str | Unset | None = UNSET) -> AsyncIterator[wire.RunView]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(cursor=cursor) for item in page.value.items)


class WorkspacesWorkspaceIdSecrets(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / secrets."""

    async def list(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> Result[wire.SecretPage]:
        """List Secrets. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_secrets_api_v1_workspaces_workspace_id_secrets_get.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.SecretPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> AsyncIterator[wire.Secret]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    async def create(self, *, body: wire.SecretCreate) -> Result[wire.Secret]:
        """Create Secret. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_secret_api_v1_workspaces_workspace_id_secrets_post.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], body=body
            )
        )

    def __call__(self, secret_id: str) -> WorkspacesWorkspaceIdSecretsSecretId:
        return WorkspacesWorkspaceIdSecretsSecretId(self._client, self._bind("secret_id", secret_id))


class WorkspacesWorkspaceIdSecretsSecretId(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / secrets / {secret_id}."""

    async def delete(self, *, if_match: str | Unset | None = UNSET) -> Result[None]:
        """Delete Secret. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_secret_api_v1_workspaces_workspace_id_secrets_secret_id_delete.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                secret_id=self._bindings["secret_id"],
                if_match=if_match,
            )
        )

    async def get(self) -> Result[wire.Secret]:
        """Get Secret. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_secret_api_v1_workspaces_workspace_id_secrets_secret_id_get.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], secret_id=self._bindings["secret_id"]
            )
        )

    async def replace(self, *, body: wire.SecretUpdate, if_match: str | Unset | None = UNSET) -> Result[wire.Secret]:
        """Replace Secret. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: replace_secret_api_v1_workspaces_workspace_id_secrets_secret_id_put.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                secret_id=self._bindings["secret_id"],
                body=body,
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
            lambda client: list_service_accounts_api_v1_workspaces_workspace_id_service_accounts_get.asyncio_detailed(
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
            lambda client: create_service_account_api_v1_workspaces_workspace_id_service_accounts_post.asyncio_detailed(
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
            lambda client: (
                delete_service_account_api_v1_workspaces_workspace_id_service_accounts_account_id_delete.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    account_id=self._bindings["account_id"],
                    if_match=if_match,
                )
            )
        )

    async def get(self) -> Result[wire.ServiceAccount]:
        """Get Service Account. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                get_service_account_api_v1_workspaces_workspace_id_service_accounts_account_id_get.asyncio_detailed(
                    client=client, workspace_id=self._bindings["workspace_id"], account_id=self._bindings["account_id"]
                )
            )
        )

    async def update(
        self, *, body: wire.ServiceAccountUpdate, if_match: str | Unset | None = UNSET
    ) -> Result[wire.ServiceAccount]:
        """Update Service Account. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                update_service_account_api_v1_workspaces_workspace_id_service_accounts_account_id_patch.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    account_id=self._bindings["account_id"],
                    body=body,
                    if_match=if_match,
                )
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
            lambda client: (
                list_service_account_keys_api_v1_workspaces_workspace_id_service_accounts_account_id_keys_get.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    account_id=self._bindings["account_id"],
                    limit=limit,
                    cursor=cursor,
                )
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
            lambda client: (
                create_service_account_key_api_v1_workspaces_workspace_id_service_accounts_account_id_keys_post.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    account_id=self._bindings["account_id"],
                    body=body,
                )
            )
        )


class WorkspacesWorkspaceIdSessions(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / sessions."""

    async def list(
        self,
        *,
        q: str | Unset | None = UNSET,
        agent_id: str | Unset | None = UNSET,
        status: list[wire.RunStatus] | Unset = UNSET,
        trigger: list[wire.Trigger] | Unset = UNSET,
        updated_after: datetime.datetime | Unset | None = UNSET,
        updated_before: datetime.datetime | Unset | None = UNSET,
        label: list[str] | Unset = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> Result[wire.SessionPage]:
        """List Sessions. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_sessions_api_v1_workspaces_workspace_id_sessions_get.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                q=q,
                agent_id=agent_id,
                status=status,
                trigger=trigger,
                updated_after=updated_after,
                updated_before=updated_before,
                label=label,
                limit=limit,
                cursor=cursor,
            )
        )

    def pages(
        self,
        *,
        q: str | Unset | None = UNSET,
        agent_id: str | Unset | None = UNSET,
        status: list[wire.RunStatus] | Unset = UNSET,
        trigger: list[wire.Trigger] | Unset = UNSET,
        updated_after: datetime.datetime | Unset | None = UNSET,
        updated_before: datetime.datetime | Unset | None = UNSET,
        label: list[str] | Unset = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.SessionPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        status = status.copy() if isinstance(status, list) else status
        trigger = trigger.copy() if isinstance(trigger, list) else trigger
        label = label.copy() if isinstance(label, list) else label
        return pages(
            lambda next_cursor: self.list(
                q=q,
                agent_id=agent_id,
                status=status,
                trigger=trigger,
                updated_after=updated_after,
                updated_before=updated_before,
                label=label,
                limit=limit,
                cursor=next_cursor,
            ),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        q: str | Unset | None = UNSET,
        agent_id: str | Unset | None = UNSET,
        status: list[wire.RunStatus] | Unset = UNSET,
        trigger: list[wire.Trigger] | Unset = UNSET,
        updated_after: datetime.datetime | Unset | None = UNSET,
        updated_before: datetime.datetime | Unset | None = UNSET,
        label: list[str] | Unset = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.SessionView]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(
                q=q,
                agent_id=agent_id,
                status=status,
                trigger=trigger,
                updated_after=updated_after,
                updated_before=updated_before,
                label=label,
                limit=limit,
                cursor=cursor,
            )
            for item in page.value.items
        )

    async def create(self, *, body: wire.SessionCreate) -> Result[wire.SessionView]:
        """Create Session. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_session_api_v1_workspaces_workspace_id_sessions_post.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], body=body
            )
        )

    def __call__(self, session_id: str) -> Session:
        return Session(self._client, self._bind("session_id", session_id))


class Session(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / sessions / {session_id}."""

    async def get(self) -> Result[wire.SessionView]:
        """Get Session. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_session_api_v1_workspaces_workspace_id_sessions_session_id_get.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], session_id=self._bindings["session_id"]
            )
        )

    async def update(
        self, *, body: wire.SessionUpdate, if_match: str | Unset | None = UNSET
    ) -> Result[wire.SessionView]:
        """Update Session. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_session_api_v1_workspaces_workspace_id_sessions_session_id_patch.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                session_id=self._bindings["session_id"],
                body=body,
                if_match=if_match,
            )
        )


class WorkspacesWorkspaceIdSkills(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / skills."""

    async def list(
        self,
        *,
        label: list[str] | Unset | None = UNSET,
        q: str | Unset | None = UNSET,
        source: wire.ListSkillsApiV1WorkspacesWorkspaceIdSkillsGetSourceType0 | Unset | None = UNSET,
        archived: bool | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> Result[wire.SkillPage]:
        """List Skills. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_skills_api_v1_workspaces_workspace_id_skills_get.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                label=label,
                q=q,
                source=source,
                archived=archived,
                limit=limit,
                cursor=cursor,
            )
        )

    def pages(
        self,
        *,
        label: list[str] | Unset | None = UNSET,
        q: str | Unset | None = UNSET,
        source: wire.ListSkillsApiV1WorkspacesWorkspaceIdSkillsGetSourceType0 | Unset | None = UNSET,
        archived: bool | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.SkillPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        label = label.copy() if isinstance(label, list) else label
        return pages(
            lambda next_cursor: self.list(
                label=label, q=q, source=source, archived=archived, limit=limit, cursor=next_cursor
            ),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        label: list[str] | Unset | None = UNSET,
        q: str | Unset | None = UNSET,
        source: wire.ListSkillsApiV1WorkspacesWorkspaceIdSkillsGetSourceType0 | Unset | None = UNSET,
        archived: bool | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.Skill]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(label=label, q=q, source=source, archived=archived, limit=limit, cursor=cursor)
            for item in page.value.items
        )

    async def create(self, *, body: wire.SkillCreate) -> Result[wire.Skill]:
        """Create Skill. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_skill_api_v1_workspaces_workspace_id_skills_post.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], body=body
            )
        )

    async def validate(self, *, body: wire.SkillValidate) -> Result[wire.SkillManifest]:
        """Validate Package. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: validate_package_api_v1_workspaces_workspace_id_skills_validate_post.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], body=body
            )
        )

    def __call__(self, skill_id: str) -> WorkspacesWorkspaceIdSkillsSkillId:
        return WorkspacesWorkspaceIdSkillsSkillId(self._client, self._bind("skill_id", skill_id))


class WorkspacesWorkspaceIdSkillsSkillId(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / skills / {skill_id}."""

    async def get(self) -> Result[wire.Skill]:
        """Get Skill. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_skill_api_v1_workspaces_workspace_id_skills_skill_id_get.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], skill_id=self._bindings["skill_id"]
            )
        )

    async def update(self, *, body: wire.SkillUpdate, if_match: str | Unset | None = UNSET) -> Result[wire.Skill]:
        """Update Skill. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_skill_api_v1_workspaces_workspace_id_skills_skill_id_patch.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                skill_id=self._bindings["skill_id"],
                body=body,
                if_match=if_match,
            )
        )

    async def archive(self, *, if_match: str | Unset | None = UNSET) -> Result[wire.Skill]:
        """Archive Skill. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: archive_skill_api_v1_workspaces_workspace_id_skills_skill_id_archive_post.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                skill_id=self._bindings["skill_id"],
                if_match=if_match,
            )
        )

    @property
    def revisions(self) -> WorkspacesWorkspaceIdSkillsSkillIdRevisions:
        return WorkspacesWorkspaceIdSkillsSkillIdRevisions(self._client, self._bindings)

    async def unarchive(self, *, if_match: str | Unset | None = UNSET) -> Result[wire.Skill]:
        """Unarchive Skill. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                unarchive_skill_api_v1_workspaces_workspace_id_skills_skill_id_unarchive_post.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    skill_id=self._bindings["skill_id"],
                    if_match=if_match,
                )
            )
        )


class WorkspacesWorkspaceIdSkillsSkillIdRevisions(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / skills / {skill_id} / revisions."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.SkillRevisionPage]:
        """List Revisions. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_revisions_api_v1_workspaces_workspace_id_skills_skill_id_revisions_get.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                skill_id=self._bindings["skill_id"],
                limit=limit,
                cursor=cursor,
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.SkillRevisionPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.SkillRevision]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    async def create(
        self, *, body: wire.SkillRevisionCreate, if_match: str | Unset | None = UNSET
    ) -> Result[wire.SkillRevision]:
        """Create Revision. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                create_revision_api_v1_workspaces_workspace_id_skills_skill_id_revisions_post.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    skill_id=self._bindings["skill_id"],
                    body=body,
                    if_match=if_match,
                )
            )
        )

    def __call__(self, revision_id: str) -> WorkspacesWorkspaceIdSkillsSkillIdRevisionsRevisionId:
        return WorkspacesWorkspaceIdSkillsSkillIdRevisionsRevisionId(
            self._client, self._bind("revision_id", revision_id)
        )


class WorkspacesWorkspaceIdSkillsSkillIdRevisionsRevisionId(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / skills / {skill_id} / revisions / {revision_id}."""

    async def get(self) -> Result[wire.SkillRevision]:
        """Get Revision. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                get_revision_api_v1_workspaces_workspace_id_skills_skill_id_revisions_revision_id_get.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    skill_id=self._bindings["skill_id"],
                    revision_id=self._bindings["revision_id"],
                )
            )
        )

    @property
    def content(self) -> WorkspacesWorkspaceIdSkillsSkillIdRevisionsRevisionIdContent:
        return WorkspacesWorkspaceIdSkillsSkillIdRevisionsRevisionIdContent(self._client, self._bindings)

    @property
    def files(self) -> WorkspacesWorkspaceIdSkillsSkillIdRevisionsRevisionIdFiles:
        return WorkspacesWorkspaceIdSkillsSkillIdRevisionsRevisionIdFiles(self._client, self._bindings)

    async def set_default(self, *, if_match: str | Unset | None = UNSET) -> Result[wire.Skill]:
        """Set Default Revision. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                set_default_revision_api_v1_workspaces_workspace_id_skills_skill_id_revisions_revision_id_set_default_post.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    skill_id=self._bindings["skill_id"],
                    revision_id=self._bindings["revision_id"],
                    if_match=if_match,
                )
            )
        )


class WorkspacesWorkspaceIdSkillsSkillIdRevisionsRevisionIdContent(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / skills / {skill_id} / revisions / {revision_id} / content."""

    async def get(self) -> Result[File]:
        """Read Archive. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                read_archive_api_v1_workspaces_workspace_id_skills_skill_id_revisions_revision_id_content_get.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    skill_id=self._bindings["skill_id"],
                    revision_id=self._bindings["revision_id"],
                )
            )
        )

    def get_stream(self) -> AbstractAsyncContextManager[httpx2.Response]:
        """Unbuffered response; caller checks status and consumes within the context."""
        return self._stream(
            read_archive_api_v1_workspaces_workspace_id_skills_skill_id_revisions_revision_id_content_get.build_request(
                workspace_id=self._bindings["workspace_id"],
                skill_id=self._bindings["skill_id"],
                revision_id=self._bindings["revision_id"],
            )
        )


class WorkspacesWorkspaceIdSkillsSkillIdRevisionsRevisionIdFiles(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / skills / {skill_id} / revisions / {revision_id} / files."""

    def __call__(self, path: str) -> WorkspacesWorkspaceIdSkillsSkillIdRevisionsRevisionIdFilesPath:
        return WorkspacesWorkspaceIdSkillsSkillIdRevisionsRevisionIdFilesPath(self._client, self._bind("path", path))


class WorkspacesWorkspaceIdSkillsSkillIdRevisionsRevisionIdFilesPath(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / skills / {skill_id} / revisions / {revision_id} / files / {path}."""

    async def get(self) -> Result[File]:
        """Read File. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                read_file_api_v1_workspaces_workspace_id_skills_skill_id_revisions_revision_id_files_path_get.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    skill_id=self._bindings["skill_id"],
                    revision_id=self._bindings["revision_id"],
                    path=self._bindings["path"],
                )
            )
        )

    def get_stream(self) -> AbstractAsyncContextManager[httpx2.Response]:
        """Unbuffered response; caller checks status and consumes within the context."""
        return self._stream(
            read_file_api_v1_workspaces_workspace_id_skills_skill_id_revisions_revision_id_files_path_get.build_request(
                workspace_id=self._bindings["workspace_id"],
                skill_id=self._bindings["skill_id"],
                revision_id=self._bindings["revision_id"],
                path=self._bindings["path"],
            )
        )


class WorkspacesWorkspaceIdSubscriptions(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / subscriptions."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.SubscriptionPage]:
        """List Subscriptions. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_subscriptions_api_v1_workspaces_workspace_id_subscriptions_get.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.SubscriptionPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.Subscription]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    async def create(self, *, body: wire.SubscriptionCreate) -> Result[wire.CreatedSubscription]:
        """Create Subscription. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_subscription_api_v1_workspaces_workspace_id_subscriptions_post.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], body=body
            )
        )

    def __call__(self, subscription_id: str) -> WorkspacesWorkspaceIdSubscriptionsSubscriptionId:
        return WorkspacesWorkspaceIdSubscriptionsSubscriptionId(
            self._client, self._bind("subscription_id", subscription_id)
        )


class WorkspacesWorkspaceIdSubscriptionsSubscriptionId(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / subscriptions / {subscription_id}."""

    async def delete(self, *, if_match: str | Unset | None = UNSET) -> Result[None]:
        """Delete Subscription. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                delete_subscription_api_v1_workspaces_workspace_id_subscriptions_subscription_id_delete.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    subscription_id=self._bindings["subscription_id"],
                    if_match=if_match,
                )
            )
        )

    async def get(self) -> Result[wire.Subscription]:
        """Get Subscription. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                get_subscription_api_v1_workspaces_workspace_id_subscriptions_subscription_id_get.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    subscription_id=self._bindings["subscription_id"],
                )
            )
        )

    async def update(
        self, *, body: wire.SubscriptionUpdate, if_match: str | Unset | None = UNSET
    ) -> Result[wire.Subscription]:
        """Update Subscription. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                update_subscription_api_v1_workspaces_workspace_id_subscriptions_subscription_id_patch.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    subscription_id=self._bindings["subscription_id"],
                    body=body,
                    if_match=if_match,
                )
            )
        )

    @property
    def deliveries(self) -> WorkspacesWorkspaceIdSubscriptionsSubscriptionIdDeliveries:
        return WorkspacesWorkspaceIdSubscriptionsSubscriptionIdDeliveries(self._client, self._bindings)


class WorkspacesWorkspaceIdSubscriptionsSubscriptionIdDeliveries(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / subscriptions / {subscription_id} / deliveries."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.DeliveryPage]:
        """List Deliveries. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                list_deliveries_api_v1_workspaces_workspace_id_subscriptions_subscription_id_deliveries_get.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    subscription_id=self._bindings["subscription_id"],
                    limit=limit,
                    cursor=cursor,
                )
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.DeliveryPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.WebhookDelivery]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    def __call__(self, delivery_id: str) -> WorkspacesWorkspaceIdSubscriptionsSubscriptionIdDeliveriesDeliveryId:
        return WorkspacesWorkspaceIdSubscriptionsSubscriptionIdDeliveriesDeliveryId(
            self._client, self._bind("delivery_id", delivery_id)
        )


class WorkspacesWorkspaceIdSubscriptionsSubscriptionIdDeliveriesDeliveryId(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / subscriptions / {subscription_id} / deliveries / {delivery_id}."""

    async def redeliver(self) -> Result[wire.WebhookDelivery]:
        """Redeliver. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                redeliver_api_v1_workspaces_workspace_id_subscriptions_subscription_id_deliveries_delivery_id_redeliver_post.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    subscription_id=self._bindings["subscription_id"],
                    delivery_id=self._bindings["delivery_id"],
                )
            )
        )


class WorkspacesWorkspaceIdThreads(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / threads."""

    async def list(
        self,
        *,
        session_id: str | Unset | None = UNSET,
        label: list[str] | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> Result[wire.ThreadPage]:
        """List Threads. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_threads_api_v1_workspaces_workspace_id_threads_get.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                session_id=session_id,
                label=label,
                limit=limit,
                cursor=cursor,
            )
        )

    def pages(
        self,
        *,
        session_id: str | Unset | None = UNSET,
        label: list[str] | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.ThreadPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        label = label.copy() if isinstance(label, list) else label
        return pages(
            lambda next_cursor: self.list(session_id=session_id, label=label, limit=limit, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        session_id: str | Unset | None = UNSET,
        label: list[str] | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.ThreadView]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(session_id=session_id, label=label, limit=limit, cursor=cursor)
            for item in page.value.items
        )

    async def create(self, *, body: wire.NewThread, idempotency_key: str) -> Result[wire.Submitted]:
        """Create Thread. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_thread_api_v1_workspaces_workspace_id_threads_post.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], body=body, idempotency_key=idempotency_key
            )
        )

    def __call__(self, thread_id: str) -> Thread:
        return Thread(self._client, self._bind("thread_id", thread_id))


class _ThreadResource(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / threads / {thread_id}."""

    async def get(self) -> Result[wire.ThreadView]:
        """Get Thread. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_thread_api_v1_workspaces_workspace_id_threads_thread_id_get.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], thread_id=self._bindings["thread_id"]
            )
        )

    async def update(self, *, body: wire.ThreadUpdate, if_match: str | Unset | None = UNSET) -> Result[wire.ThreadView]:
        """Update Thread. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: update_thread_api_v1_workspaces_workspace_id_threads_thread_id_patch.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                thread_id=self._bindings["thread_id"],
                body=body,
                if_match=if_match,
            )
        )

    async def archive(self, *, if_match: str | Unset | None = UNSET) -> Result[wire.ThreadView]:
        """Archive Thread. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                archive_thread_api_v1_workspaces_workspace_id_threads_thread_id_archive_post.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    thread_id=self._bindings["thread_id"],
                    if_match=if_match,
                )
            )
        )

    @property
    def environments(self) -> WorkspacesWorkspaceIdThreadsThreadIdEnvironments:
        return WorkspacesWorkspaceIdThreadsThreadIdEnvironments(self._client, self._bindings)

    @property
    def inbox_entries(self) -> WorkspacesWorkspaceIdThreadsThreadIdInbox:
        return WorkspacesWorkspaceIdThreadsThreadIdInbox(self._client, self._bindings)

    @property
    def memories(self) -> WorkspacesWorkspaceIdThreadsThreadIdMemories:
        return WorkspacesWorkspaceIdThreadsThreadIdMemories(self._client, self._bindings)

    @property
    def runs(self) -> WorkspacesWorkspaceIdThreadsThreadIdRuns:
        return WorkspacesWorkspaceIdThreadsThreadIdRuns(self._client, self._bindings)

    @property
    def stream_response(self) -> WorkspacesWorkspaceIdThreadsThreadIdStream:
        return WorkspacesWorkspaceIdThreadsThreadIdStream(self._client, self._bindings)


class WorkspacesWorkspaceIdThreadsThreadIdEnvironments(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / threads / {thread_id} / environments."""

    async def list(self) -> Result[wire.MountPage]:
        """List Mounts. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                list_mounts_api_v1_workspaces_workspace_id_threads_thread_id_environments_get.asyncio_detailed(
                    client=client, workspace_id=self._bindings["workspace_id"], thread_id=self._bindings["thread_id"]
                )
            )
        )

    async def create(self, *, body: wire.MountCreate, if_match: str | Unset | None = UNSET) -> Result[wire.MountView]:
        """Add Mount. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                add_mount_api_v1_workspaces_workspace_id_threads_thread_id_environments_post.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    thread_id=self._bindings["thread_id"],
                    body=body,
                    if_match=if_match,
                )
            )
        )

    def __call__(self, name: str) -> WorkspacesWorkspaceIdThreadsThreadIdEnvironmentsName:
        return WorkspacesWorkspaceIdThreadsThreadIdEnvironmentsName(self._client, self._bind("name", name))


class WorkspacesWorkspaceIdThreadsThreadIdEnvironmentsName(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / threads / {thread_id} / environments / {name}."""

    async def delete(self, *, if_match: str | Unset | None = UNSET) -> Result[None]:
        """Remove Mount. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                remove_mount_api_v1_workspaces_workspace_id_threads_thread_id_environments_name_delete.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    thread_id=self._bindings["thread_id"],
                    name=self._bindings["name"],
                    if_match=if_match,
                )
            )
        )


class WorkspacesWorkspaceIdThreadsThreadIdInbox(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / threads / {thread_id} / inbox."""

    async def list(
        self,
        *,
        status: list[wire.EntryStatus] | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> Result[wire.EntryPage]:
        """List Inbox. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_inbox_api_v1_workspaces_workspace_id_threads_thread_id_inbox_get.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                thread_id=self._bindings["thread_id"],
                status=status,
                limit=limit,
                cursor=cursor,
            )
        )

    def pages(
        self,
        *,
        status: list[wire.EntryStatus] | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.EntryPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        status = status.copy() if isinstance(status, list) else status
        return pages(
            lambda next_cursor: self.list(status=status, limit=limit, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        status: list[wire.EntryStatus] | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.EntryView]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item async for page in self.pages(status=status, limit=limit, cursor=cursor) for item in page.value.items
        )

    async def create(self, *, body: wire.Message, idempotency_key: str) -> Result[wire.Submitted]:
        """Submit Message. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: submit_message_api_v1_workspaces_workspace_id_threads_thread_id_inbox_post.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                thread_id=self._bindings["thread_id"],
                body=body,
                idempotency_key=idempotency_key,
            )
        )

    @property
    def order(self) -> WorkspacesWorkspaceIdThreadsThreadIdInboxOrder:
        return WorkspacesWorkspaceIdThreadsThreadIdInboxOrder(self._client, self._bindings)

    def __call__(self, entry_id: str) -> InboxEntry:
        return InboxEntry(self._client, self._bind("entry_id", entry_id))


class WorkspacesWorkspaceIdThreadsThreadIdInboxOrder(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / threads / {thread_id} / inbox / order."""

    async def replace(self, *, body: wire.InboxOrder, if_match: str | Unset | None = UNSET) -> Result[wire.ThreadView]:
        """Reorder Inbox. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                reorder_inbox_api_v1_workspaces_workspace_id_threads_thread_id_inbox_order_put.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    thread_id=self._bindings["thread_id"],
                    body=body,
                    if_match=if_match,
                )
            )
        )


class _InboxEntryResource(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / threads / {thread_id} / inbox / {entry_id}."""

    async def delete(self, *, if_match: str | Unset | None = UNSET) -> Result[wire.Submitted]:
        """Withdraw Entry. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                withdraw_entry_api_v1_workspaces_workspace_id_threads_thread_id_inbox_entry_id_delete.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    thread_id=self._bindings["thread_id"],
                    entry_id=self._bindings["entry_id"],
                    if_match=if_match,
                )
            )
        )

    async def get(self) -> Result[wire.EntryView]:
        """Get Entry. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                get_entry_api_v1_workspaces_workspace_id_threads_thread_id_inbox_entry_id_get.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    thread_id=self._bindings["thread_id"],
                    entry_id=self._bindings["entry_id"],
                )
            )
        )

    async def update(self, *, body: wire.EntryUpdate, if_match: str | Unset | None = UNSET) -> Result[wire.Submitted]:
        """Edit Entry. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                edit_entry_api_v1_workspaces_workspace_id_threads_thread_id_inbox_entry_id_patch.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    thread_id=self._bindings["thread_id"],
                    entry_id=self._bindings["entry_id"],
                    body=body,
                    if_match=if_match,
                )
            )
        )


class WorkspacesWorkspaceIdThreadsThreadIdMemories(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / threads / {thread_id} / memories."""

    async def list(self) -> Result[wire.MemoryMountPage]:
        """List Mounts. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_mounts_api_v1_workspaces_workspace_id_threads_thread_id_memories_get.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], thread_id=self._bindings["thread_id"]
            )
        )

    async def create(self, *, body: wire.MemoryMount, if_match: str | Unset | None = UNSET) -> Result[wire.MemoryMount]:
        """Add Mount. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: add_mount_api_v1_workspaces_workspace_id_threads_thread_id_memories_post.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                thread_id=self._bindings["thread_id"],
                body=body,
                if_match=if_match,
            )
        )

    def __call__(self, name: str) -> WorkspacesWorkspaceIdThreadsThreadIdMemoriesName:
        return WorkspacesWorkspaceIdThreadsThreadIdMemoriesName(self._client, self._bind("name", name))


class WorkspacesWorkspaceIdThreadsThreadIdMemoriesName(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / threads / {thread_id} / memories / {name}."""

    async def delete(self, *, if_match: str | Unset | None = UNSET) -> Result[None]:
        """Remove Mount. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                remove_mount_api_v1_workspaces_workspace_id_threads_thread_id_memories_name_delete.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    thread_id=self._bindings["thread_id"],
                    name=self._bindings["name"],
                    if_match=if_match,
                )
            )
        )

    async def update(
        self, *, body: wire.MemoryMountUpdate, if_match: str | Unset | None = UNSET
    ) -> Result[wire.MemoryMount]:
        """Update Mount. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                update_mount_api_v1_workspaces_workspace_id_threads_thread_id_memories_name_patch.asyncio_detailed(
                    client=client,
                    workspace_id=self._bindings["workspace_id"],
                    thread_id=self._bindings["thread_id"],
                    name=self._bindings["name"],
                    body=body,
                    if_match=if_match,
                )
            )
        )


class WorkspacesWorkspaceIdThreadsThreadIdRuns(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / threads / {thread_id} / runs."""

    async def list(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> Result[wire.RunPage]:
        """List Thread Runs. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_thread_runs_api_v1_workspaces_workspace_id_threads_thread_id_runs_get.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                thread_id=self._bindings["thread_id"],
                limit=limit,
                cursor=cursor,
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.RunPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> AsyncIterator[wire.RunView]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)


class WorkspacesWorkspaceIdThreadsThreadIdStream(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / threads / {thread_id} / stream."""

    async def get(self, *, last_event_id: str | Unset | None = UNSET) -> Result[Any]:
        """Thread Stream. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: thread_stream_api_v1_workspaces_workspace_id_threads_thread_id_stream_get.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                thread_id=self._bindings["thread_id"],
                last_event_id=last_event_id,
            )
        )


class WorkspacesWorkspaceIdToolsets(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / toolsets."""

    async def get(self) -> Result[wire.ToolsetCatalog]:
        """List Toolsets. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_toolsets_api_v1_workspaces_workspace_id_toolsets_get.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"]
            )
        )


class WorkspacesWorkspaceIdTraceBackend(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / trace-backend."""

    async def get(self) -> Result[wire.TraceBackend]:
        """Get Trace Backend. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_trace_backend_api_v1_workspaces_workspace_id_trace_backend_get.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"]
            )
        )


class WorkspacesWorkspaceIdTraces(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / traces."""

    async def list(
        self,
        *,
        session_id: str | Unset | None = UNSET,
        thread_id: str | Unset | None = UNSET,
        run_id: str | Unset | None = UNSET,
        attribute: list[str] | Unset | None = UNSET,
        started_after: datetime.datetime | Unset | None = UNSET,
        started_before: datetime.datetime | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> Result[wire.SpanPage]:
        """List Traces. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_traces_api_v1_workspaces_workspace_id_traces_get.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                session_id=session_id,
                thread_id=thread_id,
                run_id=run_id,
                attribute=attribute,
                started_after=started_after,
                started_before=started_before,
                limit=limit,
                cursor=cursor,
            )
        )

    def pages(
        self,
        *,
        session_id: str | Unset | None = UNSET,
        thread_id: str | Unset | None = UNSET,
        run_id: str | Unset | None = UNSET,
        attribute: list[str] | Unset | None = UNSET,
        started_after: datetime.datetime | Unset | None = UNSET,
        started_before: datetime.datetime | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.SpanPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        attribute = attribute.copy() if isinstance(attribute, list) else attribute
        return pages(
            lambda next_cursor: self.list(
                session_id=session_id,
                thread_id=thread_id,
                run_id=run_id,
                attribute=attribute,
                started_after=started_after,
                started_before=started_before,
                limit=limit,
                cursor=next_cursor,
            ),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        session_id: str | Unset | None = UNSET,
        thread_id: str | Unset | None = UNSET,
        run_id: str | Unset | None = UNSET,
        attribute: list[str] | Unset | None = UNSET,
        started_after: datetime.datetime | Unset | None = UNSET,
        started_before: datetime.datetime | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.Span]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(
                session_id=session_id,
                thread_id=thread_id,
                run_id=run_id,
                attribute=attribute,
                started_after=started_after,
                started_before=started_before,
                limit=limit,
                cursor=cursor,
            )
            for item in page.value.items
        )

    def __call__(self, trace_id: str) -> WorkspacesWorkspaceIdTracesTraceId:
        return WorkspacesWorkspaceIdTracesTraceId(self._client, self._bind("trace_id", trace_id))


class WorkspacesWorkspaceIdTracesTraceId(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / traces / {trace_id}."""

    async def get(self) -> Result[wire.Span]:
        """Get Trace. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_trace_api_v1_workspaces_workspace_id_traces_trace_id_get.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], trace_id=self._bindings["trace_id"]
            )
        )

    @property
    def spans(self) -> WorkspacesWorkspaceIdTracesTraceIdSpans:
        return WorkspacesWorkspaceIdTracesTraceIdSpans(self._client, self._bindings)


class WorkspacesWorkspaceIdTracesTraceIdSpans(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / traces / {trace_id} / spans."""

    async def list(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> Result[wire.SpanPage]:
        """List Trace Spans. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: list_trace_spans_api_v1_workspaces_workspace_id_traces_trace_id_spans_get.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                trace_id=self._bindings["trace_id"],
                limit=limit,
                cursor=cursor,
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.SpanPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> AsyncIterator[wire.Span]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)


class WorkspacesWorkspaceIdUploads(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / uploads."""

    async def create(self, *, body: wire.UploadCreate, idempotency_key: str) -> Result[wire.Upload]:
        """Create Upload. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: create_upload_api_v1_workspaces_workspace_id_uploads_post.asyncio_detailed(
                client=client, workspace_id=self._bindings["workspace_id"], body=body, idempotency_key=idempotency_key
            )
        )


class WorkspacesWorkspaceIdUsage(Resource):
    """Bound Native resource: /workspaces / {workspace_id} / usage."""

    async def get(
        self,
        *,
        run_id: str | Unset | None = UNSET,
        thread_id: str | Unset | None = UNSET,
        session_id: str | Unset | None = UNSET,
        ingested_after: datetime.datetime | Unset | None = UNSET,
        ingested_before: datetime.datetime | Unset | None = UNSET,
    ) -> Result[wire.UsageSummary]:
        """Summarize Usage. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: summarize_usage_api_v1_workspaces_workspace_id_usage_get.asyncio_detailed(
                client=client,
                workspace_id=self._bindings["workspace_id"],
                run_id=run_id,
                thread_id=thread_id,
                session_id=session_id,
                ingested_after=ingested_after,
                ingested_before=ingested_before,
            )
        )


class Healthz(Resource):
    """Bound Native resource: /healthz."""

    async def get(self) -> Result[wire.HealthHealthzGetResponseHealthHealthzGet]:
        """Health. One HTTP request; no automatic replay."""
        return await self._call(lambda client: health_healthz_get.asyncio_detailed(client=client))


class Readyz(Resource):
    """Bound Native resource: /readyz."""

    async def get(self) -> Result[Any]:
        """Ready. One HTTP request; no automatic replay."""
        return await self._call(lambda client: ready_readyz_get.asyncio_detailed(client=client))


class Workspace(WorkspaceMethods, _WorkspaceResource):
    """Managed Workspace reference with bounded interaction helpers."""


class Thread(ThreadMethods, _ThreadResource):
    """Managed Thread reference with bounded interaction helpers."""


class Run(RunMethods, _RunResource):
    """Managed Run reference with bounded interaction helpers."""


class InboxEntry(InboxEntryMethods, _InboxEntryResource):
    """Managed InboxEntry reference with bounded interaction helpers."""
