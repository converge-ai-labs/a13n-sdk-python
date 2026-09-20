"""Generated typed Native resource navigation. Do not edit; run make generate."""

from __future__ import annotations

import datetime
from collections.abc import AsyncIterator
from contextlib import AbstractAsyncContextManager
from typing import Any

import httpx2

from .._interaction import AgentMethods, QueueMethods, RunMethods, ThreadMethods
from .._resources import Resource, Result, pages
from . import models as wire
from .api.agent_configuration import (
    get_configuration_drafts_draft_id,
    get_configuration_drafts_draft_id_applications,
    get_configuration_sessions_session_id,
    get_configuration_sessions_session_id_threads,
    get_configuration_threads_thread_id,
    get_workspaces_workspace_configuration_assistant_readiness,
    get_workspaces_workspace_configuration_sessions,
    patch_configuration_drafts_draft_id,
    post_configuration_drafts_draft_id_apply,
    post_configuration_drafts_draft_id_discard,
    post_configuration_drafts_draft_id_rebase,
    post_configuration_sessions_session_id_threads,
    post_configuration_threads_thread_id_inputs,
    post_workspaces_workspace_configuration_sessions,
)
from .api.agent_management import (
    delete_workspaces_workspace_agents_agent_avatar,
    get_agent_revisions_agent_revision_id,
    get_workspaces_workspace_agents,
    get_workspaces_workspace_agents_agent,
    get_workspaces_workspace_agents_agent_avatar_image_id,
    get_workspaces_workspace_agents_agent_labels,
    get_workspaces_workspace_agents_agent_revisions,
    get_workspaces_workspace_toolsets,
    patch_workspaces_workspace_agents_agent,
    post_workspaces_workspace_agents,
    post_workspaces_workspace_agents_agent_action,
    post_workspaces_workspace_agents_agent_duplicate,
    post_workspaces_workspace_agents_agent_revisions,
    post_workspaces_workspace_agents_agent_revisions_revision_id_default,
    post_workspaces_workspace_toolsets_validate,
    put_workspaces_workspace_agents_agent_avatar,
    put_workspaces_workspace_agents_agent_labels,
)
from .api.asset_management import (
    delete_assets_asset_id,
    get_assets_asset_id,
    get_assets_asset_id_content,
    get_workspaces_workspace_assets,
    post_workspaces_workspace_assets,
)
from .api.bot_memory import (
    delete_application_accounts_account_id_memory_scopes_scope_id_documents_document_id,
    get_application_accounts_account_id_bot_memory_settings,
    get_application_accounts_account_id_memory_scopes,
    get_application_accounts_account_id_memory_scopes_scope_id_documents,
    get_application_accounts_account_id_memory_scopes_scope_id_documents_document_id,
    get_application_accounts_account_id_memory_scopes_scope_id_index,
    get_application_accounts_account_id_memory_scopes_scope_id_operations,
    get_application_accounts_account_id_memory_scopes_scope_id_operations_document_id,
    post_application_accounts_account_id_memory_scopes,
    post_application_accounts_account_id_memory_scopes_scope_id_documents,
    post_application_accounts_account_id_memory_scopes_scope_id_documents_search,
    post_application_accounts_account_id_memory_scopes_scope_id_operations_document_id_reconcile,
    put_application_accounts_account_id_bot_memory_settings,
)
from .api.bots import (
    get_application_accounts_account_id_bot_checks_latest,
    get_application_accounts_account_id_bot_conversations,
    get_application_accounts_account_id_bot_replies,
    get_application_accounts_account_id_bot_setup,
    get_application_accounts_account_id_bot_summary,
    get_application_accounts_account_id_bot_tests_latest,
    get_application_accounts_account_id_bot_tests_test_id,
    get_application_accounts_account_id_bot_threads,
    get_workspaces_workspace_bots,
    post_application_accounts_account_id_bot_activate,
    post_application_accounts_account_id_bot_checks,
    post_application_accounts_account_id_bot_tests,
    post_workspaces_workspace_bots_feishu_installation,
    post_workspaces_workspace_bots_github_user,
)
from .api.connections import (
    delete_connections_connection_id,
    get_connection_authorizations_authorization_id,
    get_connections_connection_id,
    get_workspaces_workspace_connections,
    patch_connections_connection_id,
    post_connection_authorizations_authorization_id_cancel,
    post_connection_authorizations_authorization_id_complete,
    post_connection_authorizations_authorization_id_launch,
    post_connection_authorizations_authorization_id_receive,
    post_connections_connection_id_authorizations,
    post_connections_connection_id_check,
    post_connections_connection_id_connector_revoke,
    post_connections_connection_id_disable,
    post_connections_connection_id_enable,
    post_workspaces_workspace_connections,
)
from .api.connectivity_management import (
    delete_application_accounts_account_id,
    delete_application_accounts_account_id_targets_target_id,
    get_application_accounts_account_id,
    get_application_accounts_account_id_event_connection,
    get_application_accounts_account_id_targets,
    get_application_accounts_account_id_targets_target_id,
    get_connections_connection_id_mcp_oauth_client,
    get_connector_provider_types,
    get_connector_provider_types_provider_type,
    get_connector_providers_connector_provider_id,
    get_connector_providers_connector_provider_id_connectors_connector_key,
    get_connector_providers_connector_provider_id_connectors_connector_key_tools,
    get_mcp_servers,
    get_mcp_servers_server_key,
    get_organizations_organization_connector_providers,
    get_workspaces_workspace_application_account_provider_types,
    get_workspaces_workspace_application_accounts,
    get_workspaces_workspace_connector_providers,
    patch_application_accounts_account_id,
    patch_connector_providers_connector_provider_id,
    post_application_accounts_account_id_action,
    post_application_accounts_account_id_targets,
    post_connections_connection_id_mcp_discover,
    post_connections_connection_id_mcp_oauth_discovery,
    post_connections_connection_id_mcp_oauth_setup,
    post_connector_providers_connector_provider_id_action,
    post_connector_providers_connector_provider_id_credentials,
    post_connector_providers_connector_provider_id_discover_connectors,
    post_connector_providers_connector_provider_id_test,
    post_organizations_organization_connector_providers,
    post_workspaces_workspace_application_accounts,
    post_workspaces_workspace_connector_providers,
    put_application_accounts_account_id_credentials,
    put_application_accounts_account_id_targets_target_id,
    put_connections_connection_id_mcp_oauth_client,
)
from .api.environments import (
    get_environment_commands_command_id,
    get_environment_provider_types,
    get_environment_provider_types_provider_type,
    get_environment_providers_provider_id_connectivity,
    get_environment_providers_resource_id,
    get_environment_template_revisions_revision_id,
    get_environment_templates_resource_id,
    get_environment_templates_template_id_labels,
    get_environment_templates_template_id_revisions,
    get_environments_environment_id_connection,
    get_environments_environment_id_device,
    get_environments_environment_id_directories,
    get_environments_environment_id_labels,
    get_environments_resource_id,
    get_organizations_organization_environment_providers,
    get_organizations_organization_environment_templates,
    get_runs_run_id_environment_mounts,
    get_workspaces_workspace_device_pairings_pairing_id,
    get_workspaces_workspace_environment_providers,
    get_workspaces_workspace_environment_templates,
    get_workspaces_workspace_environments,
    patch_environment_providers_provider_id,
    patch_environment_templates_template_id,
    patch_environments_environment_id,
    post_environment_providers_provider_id_test_image,
    post_environment_providers_provider_id_test_image_request_id_cancel,
    post_environment_templates_template_id_revisions,
    post_environment_templates_template_id_revisions_revision_id_default,
    post_environments_environment_id_connection_tickets,
    post_environments_environment_id_delete,
    post_environments_environment_id_revoke_device,
    post_environments_environment_id_stop,
    post_organizations_organization_environment_providers,
    post_organizations_organization_environment_templates,
    post_runs_run_id_environment_mounts,
    post_workspaces_workspace_device_pairings_pairing_id_approve,
    post_workspaces_workspace_device_pairings_pairing_id_reject,
    post_workspaces_workspace_environment_providers,
    post_workspaces_workspace_environment_templates,
    post_workspaces_workspace_environments,
    put_environment_providers_provider_id_credential,
    put_environment_templates_template_id_labels,
    put_environments_environment_id_labels,
)
from .api.hook_subscriptions import (
    delete_hook_subscriptions_subscription_id,
    get_hook_subscriptions_subscription_id,
    get_workspaces_workspace_hook_subscriptions,
    patch_hook_subscriptions_subscription_id,
    post_hook_subscriptions_subscription_id_deliveries_delivery_id_redrive,
    post_workspaces_workspace_hook_subscriptions,
    put_hook_subscriptions_subscription_id,
)
from .api.identity import (
    delete_users_me_auth_sessions_session_id,
    get_auth_context,
    get_auth_csrf,
    get_users_me,
    get_users_me_auth_sessions,
    post_auth_login,
    post_auth_logout,
    post_invitations_invitation_id_accept,
    post_users_me_password,
)
from .api.identity_images import (
    delete_organizations_organization_icon,
    delete_users_me_avatar,
    delete_workspaces_workspace_icon,
    get_organizations_organization_icon_image_id,
    get_users_user_id_avatar_image_id,
    get_workspaces_workspace_icon_image_id,
    put_organizations_organization_icon,
    put_users_me_avatar,
    put_workspaces_workspace_icon,
)
from .api.identity_management import (
    delete_role_bindings_binding_id,
    delete_service_accounts_account_id,
    delete_workspaces_workspace,
    get_api_keys_key_id,
    get_organizations,
    get_organizations_organization_invitations,
    get_organizations_organization_role_bindings,
    get_organizations_organization_users,
    get_organizations_organization_workspaces,
    get_role_bindings_binding_id,
    get_service_accounts_account_id,
    get_service_accounts_account_id_api_keys,
    get_workspaces_workspace,
    get_workspaces_workspace_invitations,
    get_workspaces_workspace_personal_api_keys,
    get_workspaces_workspace_role_bindings,
    get_workspaces_workspace_service_accounts,
    patch_role_bindings_binding_id,
    patch_service_accounts_account_id,
    patch_workspaces_workspace,
    post_api_keys_key_id_revoke,
    post_invitations_invitation_id_resend,
    post_invitations_invitation_id_revoke,
    post_organizations_organization_invitations,
    post_organizations_organization_workspaces,
    post_service_accounts_account_id_api_keys,
    post_workspaces_workspace_invitations,
    post_workspaces_workspace_personal_api_keys,
    post_workspaces_workspace_role_bindings,
    post_workspaces_workspace_service_accounts,
)
from .api.identity_recovery import (
    get_auth_configuration,
    post_auth_password_reset,
    post_auth_password_reset_complete,
    post_users_me_email_change,
    post_users_me_email_change_complete,
)
from .api.identity_settings import (
    get_organizations_organization,
    get_organizations_organization_permissions,
    get_organizations_organization_security_audit_events,
    get_users_me_security_activity,
    get_workspaces_workspace_api_keys,
    get_workspaces_workspace_members,
    get_workspaces_workspace_permissions,
    get_workspaces_workspace_security_audit_events,
    patch_organizations_organization,
    patch_users_me,
    post_organizations_organization_role_bindings,
)
from .api.lifecycle_events import (
    get_run_attempts_run_attempt_id_events,
    get_runs_run_id_events,
    get_workspaces_workspace_events,
)
from .api.memory import (
    delete_workspaces_workspace_memory_providers_provider_id_memories_memory_id,
    get_workspaces_workspace_memory_providers_provider_id_memories,
    get_workspaces_workspace_memory_providers_provider_id_memories_memory_id,
    get_workspaces_workspace_memory_providers_provider_id_memory_access,
    post_workspaces_workspace_memory_providers_provider_id_memories,
    post_workspaces_workspace_memory_providers_provider_id_memories_search,
    put_workspaces_workspace_memory_providers_provider_id_memories_memory_id,
)
from .api.memory_documents import (
    delete_workspaces_workspace_memory_scopes_scope_id_documents_document_id,
    get_workspaces_workspace_memory_scopes,
    get_workspaces_workspace_memory_scopes_scope_id_documents,
    get_workspaces_workspace_memory_scopes_scope_id_documents_document_id,
    get_workspaces_workspace_memory_scopes_scope_id_documents_document_id_revisions,
    get_workspaces_workspace_memory_scopes_scope_id_documents_document_id_toc,
    get_workspaces_workspace_memory_scopes_scope_id_organization,
    post_workspaces_workspace_memory_scopes_scope_id_documents,
    put_workspaces_workspace_memory_scopes_scope_id_documents_document_id,
)
from .api.memory_providers import (
    get_memory_provider_types,
    get_memory_provider_types_provider_type,
    get_organizations_organization_memory_providers,
    get_organizations_organization_memory_providers_provider_id,
    get_organizations_organization_memory_providers_provider_id_references,
    get_workspaces_workspace_memory_providers,
    get_workspaces_workspace_memory_providers_provider_id,
    get_workspaces_workspace_memory_providers_provider_id_references,
    patch_organizations_organization_memory_providers_provider_id,
    patch_workspaces_workspace_memory_providers_provider_id,
    post_organizations_organization_memory_providers,
    post_workspaces_workspace_memory_providers,
)
from .api.model_management import (
    get_model_provider_types,
    get_model_provider_types_provider_type,
    get_organizations_organization_model_catalog,
    get_organizations_organization_model_providers,
    get_organizations_organization_model_providers_provider_id,
    get_organizations_organization_models,
    get_organizations_organization_models_model_id,
    get_workspaces_workspace_media_understanding_defaults,
    get_workspaces_workspace_model_catalog,
    get_workspaces_workspace_model_providers,
    get_workspaces_workspace_model_providers_provider_id,
    get_workspaces_workspace_models,
    get_workspaces_workspace_models_model_id,
    patch_organizations_organization_model_providers_provider_id,
    patch_organizations_organization_models_model_id,
    patch_workspaces_workspace_model_providers_provider_id,
    patch_workspaces_workspace_models_model_id,
    post_organizations_organization_model_providers,
    post_organizations_organization_model_providers_provider_id_test,
    post_organizations_organization_models,
    post_organizations_organization_models_model_id_test,
    post_workspaces_workspace_model_providers,
    post_workspaces_workspace_model_providers_provider_id_test,
    post_workspaces_workspace_models,
    post_workspaces_workspace_models_model_id_test,
    put_workspaces_workspace_media_understanding_defaults,
)
from .api.protocol_gateway import (
    delete_queued_submissions_queued_submission_id,
    get_queued_submissions_queued_submission_id,
    get_run_attempts_run_attempt_id,
    get_runs_run_id,
    get_runs_run_id_attempts,
    get_runs_run_id_items,
    get_runs_run_id_labels,
    get_runs_run_id_lineage,
    get_runs_run_id_pending_actions,
    get_runs_run_id_steers_steer_id,
    get_runs_run_id_stream,
    get_sessions_session_id_labels,
    get_sessions_session_id_threads,
    get_threads_thread_id,
    get_threads_thread_id_labels,
    get_threads_thread_id_queued_submissions,
    get_threads_thread_id_runs,
    get_workspaces_workspace_runs,
    get_workspaces_workspace_sessions,
    patch_queued_submissions_queued_submission_id,
    post_runs_run_id_feedback,
    post_runs_run_id_fork,
    post_runs_run_id_interrupt,
    post_runs_run_id_retry,
    post_runs_run_id_steer,
    post_runs_source_run_id_continue,
    post_threads_thread_id_queued_submissions_consume,
    post_threads_thread_id_queued_submissions_reorder,
    post_threads_thread_id_runs,
    post_workspaces_workspace_runs,
    put_runs_run_id_labels,
    put_sessions_session_id_labels,
    put_threads_thread_id_labels,
)
from .api.skill_management import (
    delete_skill_uploads_upload_id,
    delete_skills_skill_id,
    get_skill_revisions_skill_revision_id,
    get_skill_revisions_skill_revision_id_content,
    get_skill_uploads_upload_id,
    get_skills_skill_id,
    get_skills_skill_id_labels,
    get_skills_skill_id_references,
    get_skills_skill_id_revisions,
    get_workspaces_workspace_skills,
    get_workspaces_workspace_skills_skill_key,
    patch_skills_skill_id,
    post_skills_skill_id_revisions,
    post_skills_skill_id_revisions_skill_revision_id_default,
    post_workspaces_workspace_skill_uploads,
    post_workspaces_workspace_skills,
    put_skills_skill_id_labels,
)
from .api.threads import post_workspaces_workspace_threads
from .api.trace_query import (
    get_workspaces_workspace_trace_query,
    get_workspaces_workspace_traces,
    get_workspaces_workspace_traces_trace_id,
    get_workspaces_workspace_traces_trace_id_observations,
)
from .api.web_providers import (
    get_organizations_organization_web_providers,
    get_organizations_organization_web_providers_provider_id,
    get_organizations_organization_web_providers_provider_id_references,
    get_web_provider_types,
    get_web_provider_types_provider_type,
    get_workspaces_workspace_web_providers,
    get_workspaces_workspace_web_providers_provider_id,
    get_workspaces_workspace_web_providers_provider_id_references,
    patch_organizations_organization_web_providers_provider_id,
    patch_workspaces_workspace_web_providers_provider_id,
    post_organizations_organization_web_providers,
    post_organizations_organization_web_providers_provider_id_test,
    post_workspaces_workspace_web_providers,
    post_workspaces_workspace_web_providers_provider_id_test,
)
from .types import UNSET, File, Unset


class ServiceResources(Resource):
    """Bound Native resource: /api/v1."""

    @property
    def agent_revisions(self) -> AgentRevisions:
        return AgentRevisions(self._client, self._bindings)

    @property
    def api_keys(self) -> ApiKeys:
        return ApiKeys(self._client, self._bindings)

    @property
    def application_accounts(self) -> ApplicationAccounts:
        return ApplicationAccounts(self._client, self._bindings)

    @property
    def assets(self) -> Assets:
        return Assets(self._client, self._bindings)

    @property
    def auth(self) -> Auth:
        return Auth(self._client, self._bindings)

    @property
    def configuration_drafts(self) -> ConfigurationDrafts:
        return ConfigurationDrafts(self._client, self._bindings)

    @property
    def configuration_sessions(self) -> ConfigurationSessions:
        return ConfigurationSessions(self._client, self._bindings)

    @property
    def configuration_threads(self) -> ConfigurationThreads:
        return ConfigurationThreads(self._client, self._bindings)

    @property
    def connection_authorizations(self) -> ConnectionAuthorizations:
        return ConnectionAuthorizations(self._client, self._bindings)

    @property
    def connections(self) -> Connections:
        return Connections(self._client, self._bindings)

    @property
    def connector_provider_types(self) -> ConnectorProviderTypes:
        return ConnectorProviderTypes(self._client, self._bindings)

    @property
    def connector_providers(self) -> ConnectorProviders:
        return ConnectorProviders(self._client, self._bindings)

    @property
    def environment_commands(self) -> EnvironmentCommands:
        return EnvironmentCommands(self._client, self._bindings)

    @property
    def environment_provider_types(self) -> EnvironmentProviderTypes:
        return EnvironmentProviderTypes(self._client, self._bindings)

    @property
    def environment_providers(self) -> EnvironmentProviders:
        return EnvironmentProviders(self._client, self._bindings)

    @property
    def environment_template_revisions(self) -> EnvironmentTemplateRevisions:
        return EnvironmentTemplateRevisions(self._client, self._bindings)

    @property
    def environment_templates(self) -> EnvironmentTemplates:
        return EnvironmentTemplates(self._client, self._bindings)

    @property
    def environments(self) -> Environments:
        return Environments(self._client, self._bindings)

    @property
    def hook_subscriptions(self) -> HookSubscriptions:
        return HookSubscriptions(self._client, self._bindings)

    @property
    def invitations(self) -> Invitations:
        return Invitations(self._client, self._bindings)

    @property
    def mcp_servers(self) -> McpServers:
        return McpServers(self._client, self._bindings)

    @property
    def memory_provider_types(self) -> MemoryProviderTypes:
        return MemoryProviderTypes(self._client, self._bindings)

    @property
    def model_provider_types(self) -> ModelProviderTypes:
        return ModelProviderTypes(self._client, self._bindings)

    @property
    def organizations(self) -> Organizations:
        return Organizations(self._client, self._bindings)

    @property
    def queued_submissions(self) -> QueuedSubmissions:
        return QueuedSubmissions(self._client, self._bindings)

    @property
    def role_bindings(self) -> RoleBindings:
        return RoleBindings(self._client, self._bindings)

    @property
    def run_attempts(self) -> RunAttempts:
        return RunAttempts(self._client, self._bindings)

    @property
    def runs(self) -> Runs:
        return Runs(self._client, self._bindings)

    @property
    def service_accounts(self) -> ServiceAccounts:
        return ServiceAccounts(self._client, self._bindings)

    @property
    def sessions(self) -> Sessions:
        return Sessions(self._client, self._bindings)

    @property
    def skill_revisions(self) -> SkillRevisions:
        return SkillRevisions(self._client, self._bindings)

    @property
    def skill_uploads(self) -> SkillUploads:
        return SkillUploads(self._client, self._bindings)

    @property
    def skills(self) -> Skills:
        return Skills(self._client, self._bindings)

    @property
    def threads(self) -> Threads:
        return Threads(self._client, self._bindings)

    @property
    def users(self) -> Users:
        return Users(self._client, self._bindings)

    @property
    def web_provider_types(self) -> WebProviderTypes:
        return WebProviderTypes(self._client, self._bindings)

    @property
    def workspaces(self) -> Workspaces:
        return Workspaces(self._client, self._bindings)


class AgentRevisions(Resource):
    """Bound Native resource: /agent-revisions."""

    def __call__(self, agent_revision_id: str) -> AgentRevisionsAgentRevisionId:
        return AgentRevisionsAgentRevisionId(self._client, self._bind("agent_revision_id", agent_revision_id))


class AgentRevisionsAgentRevisionId(Resource):
    """Bound Native resource: /agent-revisions / {agent_revision_id}."""

    async def get(self) -> Result[wire.AgentRevision]:
        """Get Agent Revision. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_agent_revisions_agent_revision_id.asyncio_detailed(
                client=client, agent_revision_id=self._bindings["agent_revision_id"]
            )
        )


class ApiKeys(Resource):
    """Bound Native resource: /api-keys."""

    def __call__(self, key_id: str) -> ApiKeysKeyId:
        return ApiKeysKeyId(self._client, self._bind("key_id", key_id))


class ApiKeysKeyId(Resource):
    """Bound Native resource: /api-keys / {key_id}."""

    async def get(self) -> Result[wire.ApiKey]:
        """Key Metadata. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_api_keys_key_id.asyncio_detailed(client=client, key_id=self._bindings["key_id"])
        )

    async def revoke(self) -> Result[wire.ApiKey]:
        """Revoke Key. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_api_keys_key_id_revoke.asyncio_detailed(client=client, key_id=self._bindings["key_id"])
        )


class ApplicationAccounts(Resource):
    """Bound Native resource: /application-accounts."""

    def __call__(self, account_id: str) -> ApplicationAccountsAccountId:
        return ApplicationAccountsAccountId(self._client, self._bind("account_id", account_id))


class ApplicationAccountsAccountId(Resource):
    """Bound Native resource: /application-accounts / {account_id}."""

    async def delete(self, *, expected_version: int) -> Result[None]:
        """Delete Account. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_application_accounts_account_id.asyncio_detailed(
                client=client, account_id=self._bindings["account_id"], expected_version=expected_version
            )
        )

    async def get(self) -> Result[wire.Account]:
        """Get Account. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_application_accounts_account_id.asyncio_detailed(
                client=client, account_id=self._bindings["account_id"]
            )
        )

    async def update(self, *, body: wire.UpdateAccountRequest) -> Result[wire.Account]:
        """Update Account. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: patch_application_accounts_account_id.asyncio_detailed(
                client=client, account_id=self._bindings["account_id"], body=body
            )
        )

    @property
    def bot(self) -> ApplicationAccountsAccountIdBot:
        return ApplicationAccountsAccountIdBot(self._client, self._bindings)

    @property
    def credentials(self) -> ApplicationAccountsAccountIdCredentials:
        return ApplicationAccountsAccountIdCredentials(self._client, self._bindings)

    @property
    def event_connection(self) -> ApplicationAccountsAccountIdEventConnection:
        return ApplicationAccountsAccountIdEventConnection(self._client, self._bindings)

    @property
    def memory_scopes(self) -> ApplicationAccountsAccountIdMemoryScopes:
        return ApplicationAccountsAccountIdMemoryScopes(self._client, self._bindings)

    @property
    def targets(self) -> ApplicationAccountsAccountIdTargets:
        return ApplicationAccountsAccountIdTargets(self._client, self._bindings)

    def __call__(self, action: wire.PostApplicationAccountsAccountIdActionAction) -> ApplicationAccountsAccountIdAction:
        return ApplicationAccountsAccountIdAction(self._client, self._bind("action", action))


class ApplicationAccountsAccountIdBot(Resource):
    """Bound Native resource: /application-accounts / {account_id} / bot."""

    async def activate(self, *, body: wire.ActivateBotRequest) -> Result[wire.Account]:
        """Activate Bot. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_application_accounts_account_id_bot_activate.asyncio_detailed(
                client=client, account_id=self._bindings["account_id"], body=body
            )
        )

    @property
    def checks(self) -> ApplicationAccountsAccountIdBotChecks:
        return ApplicationAccountsAccountIdBotChecks(self._client, self._bindings)

    @property
    def conversations(self) -> ApplicationAccountsAccountIdBotConversations:
        return ApplicationAccountsAccountIdBotConversations(self._client, self._bindings)

    @property
    def memory_settings(self) -> ApplicationAccountsAccountIdBotMemorySettings:
        return ApplicationAccountsAccountIdBotMemorySettings(self._client, self._bindings)

    @property
    def replies(self) -> ApplicationAccountsAccountIdBotReplies:
        return ApplicationAccountsAccountIdBotReplies(self._client, self._bindings)

    @property
    def setup(self) -> ApplicationAccountsAccountIdBotSetup:
        return ApplicationAccountsAccountIdBotSetup(self._client, self._bindings)

    @property
    def summary(self) -> ApplicationAccountsAccountIdBotSummary:
        return ApplicationAccountsAccountIdBotSummary(self._client, self._bindings)

    @property
    def tests(self) -> ApplicationAccountsAccountIdBotTests:
        return ApplicationAccountsAccountIdBotTests(self._client, self._bindings)

    @property
    def threads(self) -> ApplicationAccountsAccountIdBotThreads:
        return ApplicationAccountsAccountIdBotThreads(self._client, self._bindings)


class ApplicationAccountsAccountIdBotChecks(Resource):
    """Bound Native resource: /application-accounts / {account_id} / bot / checks."""

    async def create(self, *, body: wire.BotCheckRequest) -> Result[wire.BotCheck]:
        """Check Bot. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_application_accounts_account_id_bot_checks.asyncio_detailed(
                client=client, account_id=self._bindings["account_id"], body=body
            )
        )

    @property
    def latest(self) -> ApplicationAccountsAccountIdBotChecksLatest:
        return ApplicationAccountsAccountIdBotChecksLatest(self._client, self._bindings)


class ApplicationAccountsAccountIdBotChecksLatest(Resource):
    """Bound Native resource: /application-accounts / {account_id} / bot / checks / latest."""

    async def get(self, *, conversation_id: str | Unset | None = UNSET) -> Result[wire.BotCheckHistory]:
        """Latest Bot Check. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_application_accounts_account_id_bot_checks_latest.asyncio_detailed(
                client=client, account_id=self._bindings["account_id"], conversation_id=conversation_id
            )
        )


class ApplicationAccountsAccountIdBotConversations(Resource):
    """Bound Native resource: /application-accounts / {account_id} / bot / conversations."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.ConversationPage]:
        """Discover Bot Conversations. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_application_accounts_account_id_bot_conversations.asyncio_detailed(
                client=client, account_id=self._bindings["account_id"], limit=limit, cursor=cursor
            )
        )


class ApplicationAccountsAccountIdBotMemorySettings(Resource):
    """Bound Native resource: /application-accounts / {account_id} / bot / memory-settings."""

    async def get(self) -> Result[wire.AccountMemorySettings]:
        """Memory Settings. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_application_accounts_account_id_bot_memory_settings.asyncio_detailed(
                client=client, account_id=self._bindings["account_id"]
            )
        )

    async def replace(self, *, body: wire.ReplaceMemorySettings) -> Result[wire.AccountMemorySettings]:
        """Update Memory Settings. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: put_application_accounts_account_id_bot_memory_settings.asyncio_detailed(
                client=client, account_id=self._bindings["account_id"], body=body
            )
        )


class ApplicationAccountsAccountIdBotReplies(Resource):
    """Bound Native resource: /application-accounts / {account_id} / bot / replies."""

    async def list(
        self, *, run_id: str, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.BotReplyCollection]:
        """List Bot Reply Observations. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_application_accounts_account_id_bot_replies.asyncio_detailed(
                client=client, account_id=self._bindings["account_id"], run_id=run_id, limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, run_id: str, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.BotReplyCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(run_id=run_id, limit=limit, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self, *, run_id: str, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.BotReplyObservation]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item async for page in self.pages(run_id=run_id, limit=limit, cursor=cursor) for item in page.value.items
        )


class ApplicationAccountsAccountIdBotSetup(Resource):
    """Bound Native resource: /application-accounts / {account_id} / bot / setup."""

    async def get(self) -> Result[wire.BotSetup]:
        """Bot Setup. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_application_accounts_account_id_bot_setup.asyncio_detailed(
                client=client, account_id=self._bindings["account_id"]
            )
        )


class ApplicationAccountsAccountIdBotSummary(Resource):
    """Bound Native resource: /application-accounts / {account_id} / bot / summary."""

    async def get(self) -> Result[wire.BotSummary]:
        """Bot Summary. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_application_accounts_account_id_bot_summary.asyncio_detailed(
                client=client, account_id=self._bindings["account_id"]
            )
        )


class ApplicationAccountsAccountIdBotTests(Resource):
    """Bound Native resource: /application-accounts / {account_id} / bot / tests."""

    async def create(self, *, body: wire.CreateBotTest, idempotency_key: str) -> Result[wire.BotTest]:
        """Create Bot Setup Test. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_application_accounts_account_id_bot_tests.asyncio_detailed(
                client=client, account_id=self._bindings["account_id"], body=body, idempotency_key=idempotency_key
            )
        )

    @property
    def latest(self) -> ApplicationAccountsAccountIdBotTestsLatest:
        return ApplicationAccountsAccountIdBotTestsLatest(self._client, self._bindings)

    def __call__(self, test_id: str) -> ApplicationAccountsAccountIdBotTestsTestId:
        return ApplicationAccountsAccountIdBotTestsTestId(self._client, self._bind("test_id", test_id))


class ApplicationAccountsAccountIdBotTestsLatest(Resource):
    """Bound Native resource: /application-accounts / {account_id} / bot / tests / latest."""

    async def get(self) -> Result[wire.BotTestHistory]:
        """Latest Bot Setup Test. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_application_accounts_account_id_bot_tests_latest.asyncio_detailed(
                client=client, account_id=self._bindings["account_id"]
            )
        )


class ApplicationAccountsAccountIdBotTestsTestId(Resource):
    """Bound Native resource: /application-accounts / {account_id} / bot / tests / {test_id}."""

    async def get(self) -> Result[wire.BotTestHistory]:
        """Get Bot Setup Test. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_application_accounts_account_id_bot_tests_test_id.asyncio_detailed(
                client=client, account_id=self._bindings["account_id"], test_id=self._bindings["test_id"]
            )
        )


class ApplicationAccountsAccountIdBotThreads(Resource):
    """Bound Native resource: /application-accounts / {account_id} / bot / threads."""

    async def list(
        self, *, target_id: str | Unset | None = UNSET, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.BotThreadCollection]:
        """List Bot Conversation Threads. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_application_accounts_account_id_bot_threads.asyncio_detailed(
                client=client, account_id=self._bindings["account_id"], target_id=target_id, limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, target_id: str | Unset | None = UNSET, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.BotThreadCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(target_id=target_id, limit=limit, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self, *, target_id: str | Unset | None = UNSET, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.BotThread]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(target_id=target_id, limit=limit, cursor=cursor)
            for item in page.value.items
        )


class ApplicationAccountsAccountIdCredentials(Resource):
    """Bound Native resource: /application-accounts / {account_id} / credentials."""

    async def replace(
        self, *, body: wire.ReplaceAccountCredentialsRequest, idempotency_key: str
    ) -> Result[wire.Account]:
        """Replace Account Credentials. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: put_application_accounts_account_id_credentials.asyncio_detailed(
                client=client, account_id=self._bindings["account_id"], body=body, idempotency_key=idempotency_key
            )
        )


class ApplicationAccountsAccountIdEventConnection(Resource):
    """Bound Native resource: /application-accounts / {account_id} / event-connection."""

    async def get(self) -> Result[wire.EventConnectionStatus]:
        """Event Connection. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_application_accounts_account_id_event_connection.asyncio_detailed(
                client=client, account_id=self._bindings["account_id"]
            )
        )


class ApplicationAccountsAccountIdMemoryScopes(Resource):
    """Bound Native resource: /application-accounts / {account_id} / memory-scopes."""

    async def list(
        self,
        *,
        provider_id: str,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        target_id: str | Unset | None = UNSET,
    ) -> Result[wire.ScopeCollection]:
        """Scopes. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_application_accounts_account_id_memory_scopes.asyncio_detailed(
                client=client,
                account_id=self._bindings["account_id"],
                provider_id=provider_id,
                limit=limit,
                cursor=cursor,
                target_id=target_id,
            )
        )

    def pages(
        self,
        *,
        provider_id: str,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        target_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.ScopeCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(
                provider_id=provider_id, limit=limit, target_id=target_id, cursor=next_cursor
            ),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        provider_id: str,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        target_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.Scope]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(provider_id=provider_id, limit=limit, cursor=cursor, target_id=target_id)
            for item in page.value.items
        )

    async def create(self, *, body: wire.ConfigureScope) -> Result[wire.Scope]:
        """Configure. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_application_accounts_account_id_memory_scopes.asyncio_detailed(
                client=client, account_id=self._bindings["account_id"], body=body
            )
        )

    def __call__(self, scope_id: str) -> ApplicationAccountsAccountIdMemoryScopesScopeId:
        return ApplicationAccountsAccountIdMemoryScopesScopeId(self._client, self._bind("scope_id", scope_id))


class ApplicationAccountsAccountIdMemoryScopesScopeId(Resource):
    """Bound Native resource: /application-accounts / {account_id} / memory-scopes / {scope_id}."""

    @property
    def documents(self) -> ApplicationAccountsAccountIdMemoryScopesScopeIdDocuments:
        return ApplicationAccountsAccountIdMemoryScopesScopeIdDocuments(self._client, self._bindings)

    @property
    def index(self) -> ApplicationAccountsAccountIdMemoryScopesScopeIdIndex:
        return ApplicationAccountsAccountIdMemoryScopesScopeIdIndex(self._client, self._bindings)

    @property
    def operations(self) -> ApplicationAccountsAccountIdMemoryScopesScopeIdOperations:
        return ApplicationAccountsAccountIdMemoryScopesScopeIdOperations(self._client, self._bindings)


class ApplicationAccountsAccountIdMemoryScopesScopeIdDocuments(Resource):
    """Bound Native resource: /application-accounts / {account_id} / memory-scopes / {scope_id} / documents."""

    async def list(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        activity_date: datetime.date | Unset | None = UNSET,
        kind: wire.GetApplicationAccountsAccountIdMemoryScopesScopeIdDocumentsKindType0 | Unset | None = UNSET,
        include_shared: bool | Unset = UNSET,
    ) -> Result[wire.DocumentCollection]:
        """Documents. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_application_accounts_account_id_memory_scopes_scope_id_documents.asyncio_detailed(
                client=client,
                account_id=self._bindings["account_id"],
                scope_id=self._bindings["scope_id"],
                limit=limit,
                cursor=cursor,
                activity_date=activity_date,
                kind=kind,
                include_shared=include_shared,
            )
        )

    def pages(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        activity_date: datetime.date | Unset | None = UNSET,
        kind: wire.GetApplicationAccountsAccountIdMemoryScopesScopeIdDocumentsKindType0 | Unset | None = UNSET,
        include_shared: bool | Unset = UNSET,
    ) -> AsyncIterator[Result[wire.DocumentCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(
                limit=limit, activity_date=activity_date, kind=kind, include_shared=include_shared, cursor=next_cursor
            ),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        activity_date: datetime.date | Unset | None = UNSET,
        kind: wire.GetApplicationAccountsAccountIdMemoryScopesScopeIdDocumentsKindType0 | Unset | None = UNSET,
        include_shared: bool | Unset = UNSET,
    ) -> AsyncIterator[wire.DocumentEntry]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(
                limit=limit, cursor=cursor, activity_date=activity_date, kind=kind, include_shared=include_shared
            )
            for item in page.value.items
        )

    async def create(self, *, body: wire.CreateDocument, idempotency_key: str) -> Result[wire.Document]:
        """Add. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_application_accounts_account_id_memory_scopes_scope_id_documents.asyncio_detailed(
                client=client,
                account_id=self._bindings["account_id"],
                scope_id=self._bindings["scope_id"],
                body=body,
                idempotency_key=idempotency_key,
            )
        )

    async def search(self, *, body: wire.SearchDocuments) -> Result[wire.DocumentCollection]:
        """Search. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                post_application_accounts_account_id_memory_scopes_scope_id_documents_search.asyncio_detailed(
                    client=client,
                    account_id=self._bindings["account_id"],
                    scope_id=self._bindings["scope_id"],
                    body=body,
                )
            )
        )

    def __call__(self, document_id: str) -> ApplicationAccountsAccountIdMemoryScopesScopeIdDocumentsDocumentId:
        return ApplicationAccountsAccountIdMemoryScopesScopeIdDocumentsDocumentId(
            self._client, self._bind("document_id", document_id)
        )


class ApplicationAccountsAccountIdMemoryScopesScopeIdDocumentsDocumentId(Resource):
    """Bound Native resource: /application-accounts / {account_id} / memory-scopes / {scope_id} / documents / {document_id}."""

    async def delete(self) -> Result[None]:
        """Remove. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                delete_application_accounts_account_id_memory_scopes_scope_id_documents_document_id.asyncio_detailed(
                    client=client,
                    account_id=self._bindings["account_id"],
                    scope_id=self._bindings["scope_id"],
                    document_id=self._bindings["document_id"],
                )
            )
        )

    async def get(self) -> Result[wire.Document]:
        """Get. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                get_application_accounts_account_id_memory_scopes_scope_id_documents_document_id.asyncio_detailed(
                    client=client,
                    account_id=self._bindings["account_id"],
                    scope_id=self._bindings["scope_id"],
                    document_id=self._bindings["document_id"],
                )
            )
        )


class ApplicationAccountsAccountIdMemoryScopesScopeIdIndex(Resource):
    """Bound Native resource: /application-accounts / {account_id} / memory-scopes / {scope_id} / index."""

    async def get(self, *, cursor: str | Unset | None = UNSET) -> Result[wire.MemoryIndex]:
        """Index. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_application_accounts_account_id_memory_scopes_scope_id_index.asyncio_detailed(
                client=client,
                account_id=self._bindings["account_id"],
                scope_id=self._bindings["scope_id"],
                cursor=cursor,
            )
        )


class ApplicationAccountsAccountIdMemoryScopesScopeIdOperations(Resource):
    """Bound Native resource: /application-accounts / {account_id} / memory-scopes / {scope_id} / operations."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.DocumentCollection]:
        """Operations. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_application_accounts_account_id_memory_scopes_scope_id_operations.asyncio_detailed(
                client=client,
                account_id=self._bindings["account_id"],
                scope_id=self._bindings["scope_id"],
                limit=limit,
                cursor=cursor,
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.DocumentCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.DocumentEntry]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    def __call__(self, document_id: str) -> ApplicationAccountsAccountIdMemoryScopesScopeIdOperationsDocumentId:
        return ApplicationAccountsAccountIdMemoryScopesScopeIdOperationsDocumentId(
            self._client, self._bind("document_id", document_id)
        )


class ApplicationAccountsAccountIdMemoryScopesScopeIdOperationsDocumentId(Resource):
    """Bound Native resource: /application-accounts / {account_id} / memory-scopes / {scope_id} / operations / {document_id}."""

    async def get(self) -> Result[wire.DocumentEntry]:
        """Operation Status. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                get_application_accounts_account_id_memory_scopes_scope_id_operations_document_id.asyncio_detailed(
                    client=client,
                    account_id=self._bindings["account_id"],
                    scope_id=self._bindings["scope_id"],
                    document_id=self._bindings["document_id"],
                )
            )
        )

    async def reconcile(self) -> Result[wire.DocumentEntry]:
        """Reconcile Operation. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                post_application_accounts_account_id_memory_scopes_scope_id_operations_document_id_reconcile.asyncio_detailed(
                    client=client,
                    account_id=self._bindings["account_id"],
                    scope_id=self._bindings["scope_id"],
                    document_id=self._bindings["document_id"],
                )
            )
        )


class ApplicationAccountsAccountIdTargets(Resource):
    """Bound Native resource: /application-accounts / {account_id} / targets."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.TargetCollection]:
        """List Targets. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_application_accounts_account_id_targets.asyncio_detailed(
                client=client, account_id=self._bindings["account_id"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.TargetCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.AccountTarget]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    async def create(self, *, body: wire.TargetConfig, idempotency_key: str) -> Result[wire.AccountTarget]:
        """Create. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_application_accounts_account_id_targets.asyncio_detailed(
                client=client, account_id=self._bindings["account_id"], body=body, idempotency_key=idempotency_key
            )
        )

    def __call__(self, target_id: str) -> ApplicationAccountsAccountIdTargetsTargetId:
        return ApplicationAccountsAccountIdTargetsTargetId(self._client, self._bind("target_id", target_id))


class ApplicationAccountsAccountIdTargetsTargetId(Resource):
    """Bound Native resource: /application-accounts / {account_id} / targets / {target_id}."""

    async def delete(self, *, expected_version: int) -> Result[None]:
        """Delete. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_application_accounts_account_id_targets_target_id.asyncio_detailed(
                client=client,
                account_id=self._bindings["account_id"],
                target_id=self._bindings["target_id"],
                expected_version=expected_version,
            )
        )

    async def get(self) -> Result[wire.AccountTarget]:
        """Get. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_application_accounts_account_id_targets_target_id.asyncio_detailed(
                client=client, account_id=self._bindings["account_id"], target_id=self._bindings["target_id"]
            )
        )

    async def replace(self, *, body: wire.ReplaceTargetRequest) -> Result[wire.AccountTarget]:
        """Replace. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: put_application_accounts_account_id_targets_target_id.asyncio_detailed(
                client=client, account_id=self._bindings["account_id"], target_id=self._bindings["target_id"], body=body
            )
        )


class ApplicationAccountsAccountIdAction(Resource):
    """Bound Native resource: /application-accounts / {account_id} / {action}."""

    async def create(self, *, body: wire.AccountCommandRequest, idempotency_key: str) -> Result[wire.Account]:
        """Change Account Lifecycle. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_application_accounts_account_id_action.asyncio_detailed(
                client=client,
                account_id=self._bindings["account_id"],
                action=wire.PostApplicationAccountsAccountIdActionAction(self._bindings["action"]),
                body=body,
                idempotency_key=idempotency_key,
            )
        )


class Assets(Resource):
    """Bound Native resource: /assets."""

    def __call__(self, asset_id: str) -> AssetsAssetId:
        return AssetsAssetId(self._client, self._bind("asset_id", asset_id))


class AssetsAssetId(Resource):
    """Bound Native resource: /assets / {asset_id}."""

    async def delete(self) -> Result[None]:
        """Delete Asset. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_assets_asset_id.asyncio_detailed(client=client, asset_id=self._bindings["asset_id"])
        )

    async def get(self) -> Result[wire.Asset]:
        """Get Asset. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_assets_asset_id.asyncio_detailed(client=client, asset_id=self._bindings["asset_id"])
        )

    @property
    def content(self) -> AssetsAssetIdContent:
        return AssetsAssetIdContent(self._client, self._bindings)


class AssetsAssetIdContent(Resource):
    """Bound Native resource: /assets / {asset_id} / content."""

    async def get(self) -> Result[File]:
        """Get Asset Content. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_assets_asset_id_content.asyncio_detailed(
                client=client, asset_id=self._bindings["asset_id"]
            )
        )

    def get_stream(self) -> AbstractAsyncContextManager[httpx2.Response]:
        """Unbuffered response; caller checks status and consumes within the context."""
        return self._stream(get_assets_asset_id_content.build_request(asset_id=self._bindings["asset_id"]))


class Auth(Resource):
    """Bound Native resource: /auth."""

    @property
    def configuration(self) -> AuthConfiguration:
        return AuthConfiguration(self._client, self._bindings)

    @property
    def context(self) -> AuthContext:
        return AuthContext(self._client, self._bindings)

    @property
    def csrf(self) -> AuthCsrf:
        return AuthCsrf(self._client, self._bindings)

    async def login(self, *, body: wire.LoginRequest) -> Result[wire.LoginResult]:
        """Login. One HTTP request; no automatic replay."""
        return await self._call(lambda client: post_auth_login.asyncio_detailed(client=client, body=body))

    async def logout(self) -> Result[None]:
        """Logout. One HTTP request; no automatic replay."""
        return await self._call(lambda client: post_auth_logout.asyncio_detailed(client=client))

    @property
    def password_reset(self) -> AuthPasswordReset:
        return AuthPasswordReset(self._client, self._bindings)


class AuthConfiguration(Resource):
    """Bound Native resource: /auth / configuration."""

    async def get(self) -> Result[wire.AuthConfiguration]:
        """Auth Configuration. One HTTP request; no automatic replay."""
        return await self._call(lambda client: get_auth_configuration.asyncio_detailed(client=client))


class AuthContext(Resource):
    """Bound Native resource: /auth / context."""

    async def get(self) -> Result[wire.CredentialContext]:
        """Credential Context. One HTTP request; no automatic replay."""
        return await self._call(lambda client: get_auth_context.asyncio_detailed(client=client))


class AuthCsrf(Resource):
    """Bound Native resource: /auth / csrf."""

    async def get(self) -> Result[wire.GetAuthCsrfResponseBrowserProofApiV1AuthCsrfGet]:
        """Browser Proof. One HTTP request; no automatic replay."""
        return await self._call(lambda client: get_auth_csrf.asyncio_detailed(client=client))


class AuthPasswordReset(Resource):
    """Bound Native resource: /auth / password-reset."""

    async def create(self, *, body: wire.PasswordResetRequest) -> Result[Any]:
        """Request Password Reset. One HTTP request; no automatic replay."""
        return await self._call(lambda client: post_auth_password_reset.asyncio_detailed(client=client, body=body))

    async def complete(self, *, body: wire.CompletePasswordResetRequest) -> Result[None]:
        """Complete Password Reset. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_auth_password_reset_complete.asyncio_detailed(client=client, body=body)
        )


class ConfigurationDrafts(Resource):
    """Bound Native resource: /configuration-drafts."""

    def __call__(self, draft_id: str) -> ConfigurationDraftsDraftId:
        return ConfigurationDraftsDraftId(self._client, self._bind("draft_id", draft_id))


class ConfigurationDraftsDraftId(Resource):
    """Bound Native resource: /configuration-drafts / {draft_id}."""

    async def get(self) -> Result[wire.ConfigurationDraftReview]:
        """Get Draft. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_configuration_drafts_draft_id.asyncio_detailed(
                client=client, draft_id=self._bindings["draft_id"]
            )
        )

    async def update(
        self, *, body: wire.UpdateConfigurationDraftRequest, idempotency_key: str, if_match: str
    ) -> Result[wire.ConfigurationDraft]:
        """Update Draft. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: patch_configuration_drafts_draft_id.asyncio_detailed(
                client=client,
                draft_id=self._bindings["draft_id"],
                body=body,
                idempotency_key=idempotency_key,
                if_match=if_match,
            )
        )

    @property
    def applications(self) -> ConfigurationDraftsDraftIdApplications:
        return ConfigurationDraftsDraftIdApplications(self._client, self._bindings)

    async def apply(
        self, *, body: wire.ApplyDraftRequest, idempotency_key: str, if_match: str
    ) -> Result[wire.ConfigurationApplicationReceipt]:
        """Apply Draft. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_configuration_drafts_draft_id_apply.asyncio_detailed(
                client=client,
                draft_id=self._bindings["draft_id"],
                body=body,
                idempotency_key=idempotency_key,
                if_match=if_match,
            )
        )

    async def discard(
        self, *, body: wire.DiscardDraftRequest, idempotency_key: str, if_match: str
    ) -> Result[wire.ConfigurationDraft]:
        """Discard Draft. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_configuration_drafts_draft_id_discard.asyncio_detailed(
                client=client,
                draft_id=self._bindings["draft_id"],
                body=body,
                idempotency_key=idempotency_key,
                if_match=if_match,
            )
        )

    async def rebase(
        self, *, body: wire.RebaseDraftRequest, idempotency_key: str, if_match: str
    ) -> Result[wire.ConfigurationDraft]:
        """Rebase Draft. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_configuration_drafts_draft_id_rebase.asyncio_detailed(
                client=client,
                draft_id=self._bindings["draft_id"],
                body=body,
                idempotency_key=idempotency_key,
                if_match=if_match,
            )
        )


class ConfigurationDraftsDraftIdApplications(Resource):
    """Bound Native resource: /configuration-drafts / {draft_id} / applications."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.ConfigurationApplicationCollection]:
        """List Applications. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_configuration_drafts_draft_id_applications.asyncio_detailed(
                client=client, draft_id=self._bindings["draft_id"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.ConfigurationApplicationCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.ConfigurationApplicationReceipt]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)


class ConfigurationSessions(Resource):
    """Bound Native resource: /configuration-sessions."""

    def __call__(self, session_id: str) -> ConfigurationSessionsSessionId:
        return ConfigurationSessionsSessionId(self._client, self._bind("session_id", session_id))


class ConfigurationSessionsSessionId(Resource):
    """Bound Native resource: /configuration-sessions / {session_id}."""

    async def get(self) -> Result[wire.ConfigurationSessionView]:
        """Get Session. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_configuration_sessions_session_id.asyncio_detailed(
                client=client, session_id=self._bindings["session_id"]
            )
        )

    @property
    def threads(self) -> ConfigurationSessionsSessionIdThreads:
        return ConfigurationSessionsSessionIdThreads(self._client, self._bindings)


class ConfigurationSessionsSessionIdThreads(Resource):
    """Bound Native resource: /configuration-sessions / {session_id} / threads."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.ConfigurationThreadCollection]:
        """List Threads. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_configuration_sessions_session_id_threads.asyncio_detailed(
                client=client, session_id=self._bindings["session_id"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.ConfigurationThreadCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.ConfigurationThreadView]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    async def create(
        self, *, body: wire.CreateConfigurationThreadRequest, idempotency_key: str
    ) -> Result[wire.ConfigurationThreadView]:
        """Create Thread. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_configuration_sessions_session_id_threads.asyncio_detailed(
                client=client, session_id=self._bindings["session_id"], body=body, idempotency_key=idempotency_key
            )
        )


class ConfigurationThreads(Resource):
    """Bound Native resource: /configuration-threads."""

    def __call__(self, thread_id: str) -> ConfigurationThreadsThreadId:
        return ConfigurationThreadsThreadId(self._client, self._bind("thread_id", thread_id))


class ConfigurationThreadsThreadId(Resource):
    """Bound Native resource: /configuration-threads / {thread_id}."""

    async def get(self) -> Result[wire.ConfigurationThreadView]:
        """Get Thread. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_configuration_threads_thread_id.asyncio_detailed(
                client=client, thread_id=self._bindings["thread_id"]
            )
        )

    @property
    def inputs(self) -> ConfigurationThreadsThreadIdInputs:
        return ConfigurationThreadsThreadIdInputs(self._client, self._bindings)


class ConfigurationThreadsThreadIdInputs(Resource):
    """Bound Native resource: /configuration-threads / {thread_id} / inputs."""

    async def create(
        self, *, body: wire.ConfigurationInputRequest, idempotency_key: str
    ) -> Result[wire.RunAcceptanceReceipt]:
        """Submit Input. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_configuration_threads_thread_id_inputs.asyncio_detailed(
                client=client, thread_id=self._bindings["thread_id"], body=body, idempotency_key=idempotency_key
            )
        )


class ConnectionAuthorizations(Resource):
    """Bound Native resource: /connection-authorizations."""

    def __call__(self, authorization_id: str) -> ConnectionAuthorizationsAuthorizationId:
        return ConnectionAuthorizationsAuthorizationId(self._client, self._bind("authorization_id", authorization_id))


class ConnectionAuthorizationsAuthorizationId(Resource):
    """Bound Native resource: /connection-authorizations / {authorization_id}."""

    async def get(self) -> Result[wire.Authorization]:
        """Get Connection Authorization. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_connection_authorizations_authorization_id.asyncio_detailed(
                client=client, authorization_id=self._bindings["authorization_id"]
            )
        )

    async def cancel(self) -> Result[wire.Authorization]:
        """Cancel Connection Authorization. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_connection_authorizations_authorization_id_cancel.asyncio_detailed(
                client=client, authorization_id=self._bindings["authorization_id"]
            )
        )

    async def complete(self, *, body: wire.CompleteAuthorizationRequest) -> Result[wire.Authorization]:
        """Complete Connection Authorization. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_connection_authorizations_authorization_id_complete.asyncio_detailed(
                client=client, authorization_id=self._bindings["authorization_id"], body=body
            )
        )

    async def launch(self, *, body: wire.LaunchAuthorizationRequest) -> Result[wire.AuthorizationRedirect]:
        """Launch Connection Authorization. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_connection_authorizations_authorization_id_launch.asyncio_detailed(
                client=client, authorization_id=self._bindings["authorization_id"], body=body
            )
        )

    async def receive(self, *, body: wire.ReceiveAuthorizationRequest) -> Result[wire.AuthorizationRedirect]:
        """Receive Connection Authorization. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_connection_authorizations_authorization_id_receive.asyncio_detailed(
                client=client, authorization_id=self._bindings["authorization_id"], body=body
            )
        )


class Connections(Resource):
    """Bound Native resource: /connections."""

    def __call__(self, connection_id: str) -> ConnectionsConnectionId:
        return ConnectionsConnectionId(self._client, self._bind("connection_id", connection_id))


class ConnectionsConnectionId(Resource):
    """Bound Native resource: /connections / {connection_id}."""

    async def delete(self, *, expected_version: int, idempotency_key: str) -> Result[wire.ConnectionCleanupReceipt]:
        """Delete Connection. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_connections_connection_id.asyncio_detailed(
                client=client,
                connection_id=self._bindings["connection_id"],
                expected_version=expected_version,
                idempotency_key=idempotency_key,
            )
        )

    async def get(self) -> Result[wire.Connection]:
        """Get Connection. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_connections_connection_id.asyncio_detailed(
                client=client, connection_id=self._bindings["connection_id"]
            )
        )

    async def update(self, *, body: wire.UpdateConnectionRequest) -> Result[wire.Connection]:
        """Update Connection. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: patch_connections_connection_id.asyncio_detailed(
                client=client, connection_id=self._bindings["connection_id"], body=body
            )
        )

    @property
    def authorizations(self) -> ConnectionsConnectionIdAuthorizations:
        return ConnectionsConnectionIdAuthorizations(self._client, self._bindings)

    async def check(self, *, body: wire.ConnectionCommandRequest) -> Result[wire.Connection]:
        """Check Connection. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_connections_connection_id_check.asyncio_detailed(
                client=client, connection_id=self._bindings["connection_id"], body=body
            )
        )

    @property
    def connector(self) -> ConnectionsConnectionIdConnector:
        return ConnectionsConnectionIdConnector(self._client, self._bindings)

    async def disable(self, *, body: wire.ConnectionCommandRequest, idempotency_key: str) -> Result[wire.Connection]:
        """Disable Connection. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_connections_connection_id_disable.asyncio_detailed(
                client=client, connection_id=self._bindings["connection_id"], body=body, idempotency_key=idempotency_key
            )
        )

    async def enable(self, *, body: wire.ConnectionCommandRequest, idempotency_key: str) -> Result[wire.Connection]:
        """Enable Connection. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_connections_connection_id_enable.asyncio_detailed(
                client=client, connection_id=self._bindings["connection_id"], body=body, idempotency_key=idempotency_key
            )
        )

    @property
    def mcp(self) -> ConnectionsConnectionIdMcp:
        return ConnectionsConnectionIdMcp(self._client, self._bindings)


class ConnectionsConnectionIdAuthorizations(Resource):
    """Bound Native resource: /connections / {connection_id} / authorizations."""

    async def create(
        self, *, body: wire.CreateAuthorizationRequest, idempotency_key: str
    ) -> Result[wire.Authorization]:
        """Create Connection Authorization. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_connections_connection_id_authorizations.asyncio_detailed(
                client=client, connection_id=self._bindings["connection_id"], body=body, idempotency_key=idempotency_key
            )
        )


class ConnectionsConnectionIdConnector(Resource):
    """Bound Native resource: /connections / {connection_id} / connector."""

    async def revoke(
        self, *, body: wire.ConnectionCommandRequest, idempotency_key: str
    ) -> Result[wire.ConnectionCleanupReceipt]:
        """Revoke Connector Authorization. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_connections_connection_id_connector_revoke.asyncio_detailed(
                client=client, connection_id=self._bindings["connection_id"], body=body, idempotency_key=idempotency_key
            )
        )


class ConnectionsConnectionIdMcp(Resource):
    """Bound Native resource: /connections / {connection_id} / mcp."""

    async def discover(self, *, body: wire.ConnectionCommandRequest) -> Result[wire.MCPToolCollection]:
        """Discover Mcp Tools. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_connections_connection_id_mcp_discover.asyncio_detailed(
                client=client, connection_id=self._bindings["connection_id"], body=body
            )
        )

    @property
    def oauth_client(self) -> ConnectionsConnectionIdMcpOauthClient:
        return ConnectionsConnectionIdMcpOauthClient(self._client, self._bindings)

    async def oauth_discovery(self, *, body: wire.MCPOAuthSetupRequest) -> Result[wire.MCPOAuthDiscovery]:
        """Discover Mcp Oauth. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_connections_connection_id_mcp_oauth_discovery.asyncio_detailed(
                client=client, connection_id=self._bindings["connection_id"], body=body
            )
        )

    async def oauth_setup(self, *, body: wire.MCPOAuthSetupRequest) -> Result[wire.MCPOAuthSetup]:
        """Get Mcp Oauth Setup. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_connections_connection_id_mcp_oauth_setup.asyncio_detailed(
                client=client, connection_id=self._bindings["connection_id"], body=body
            )
        )


class ConnectionsConnectionIdMcpOauthClient(Resource):
    """Bound Native resource: /connections / {connection_id} / mcp / oauth-client."""

    async def get(self) -> Result[wire.MCPOAuthClientConfiguration | None]:
        """Get Mcp Oauth Client. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_connections_connection_id_mcp_oauth_client.asyncio_detailed(
                client=client, connection_id=self._bindings["connection_id"]
            )
        )

    async def replace(self, *, body: wire.ConfigureMCPOAuthClientRequest) -> Result[wire.Connection]:
        """Configure Mcp Oauth Client. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: put_connections_connection_id_mcp_oauth_client.asyncio_detailed(
                client=client, connection_id=self._bindings["connection_id"], body=body
            )
        )


class ConnectorProviderTypes(Resource):
    """Bound Native resource: /connector-provider-types."""

    async def list(self) -> Result[wire.ProviderMetadataCollectionConnectorProviderMetadata]:
        """List Connector Provider Types. One HTTP request; no automatic replay."""
        return await self._call(lambda client: get_connector_provider_types.asyncio_detailed(client=client))

    def __call__(self, provider_type: str) -> ConnectorProviderTypesProviderType:
        return ConnectorProviderTypesProviderType(self._client, self._bind("provider_type", provider_type))


class ConnectorProviderTypesProviderType(Resource):
    """Bound Native resource: /connector-provider-types / {provider_type}."""

    async def get(self) -> Result[wire.ConnectorProviderMetadata]:
        """Get Connector Provider Type. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_connector_provider_types_provider_type.asyncio_detailed(
                client=client, provider_type=self._bindings["provider_type"]
            )
        )


class ConnectorProviders(Resource):
    """Bound Native resource: /connector-providers."""

    def __call__(self, connector_provider_id: str) -> ConnectorProvidersConnectorProviderId:
        return ConnectorProvidersConnectorProviderId(
            self._client, self._bind("connector_provider_id", connector_provider_id)
        )


class ConnectorProvidersConnectorProviderId(Resource):
    """Bound Native resource: /connector-providers / {connector_provider_id}."""

    async def get(self) -> Result[wire.ConnectorProvider]:
        """Get Connector Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_connector_providers_connector_provider_id.asyncio_detailed(
                client=client, connector_provider_id=self._bindings["connector_provider_id"]
            )
        )

    async def update(self, *, body: wire.UpdateConnectorProviderRequest) -> Result[wire.ConnectorProvider]:
        """Update Connector Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: patch_connector_providers_connector_provider_id.asyncio_detailed(
                client=client, connector_provider_id=self._bindings["connector_provider_id"], body=body
            )
        )

    @property
    def connectors(self) -> ConnectorProvidersConnectorProviderIdConnectors:
        return ConnectorProvidersConnectorProviderIdConnectors(self._client, self._bindings)

    @property
    def credentials(self) -> ConnectorProvidersConnectorProviderIdCredentials:
        return ConnectorProvidersConnectorProviderIdCredentials(self._client, self._bindings)

    @property
    def discover_connectors(self) -> ConnectorProvidersConnectorProviderIdDiscoverConnectors:
        return ConnectorProvidersConnectorProviderIdDiscoverConnectors(self._client, self._bindings)

    async def test(
        self, *, body: wire.ConnectorProviderCommandRequest, idempotency_key: str
    ) -> Result[wire.ConnectorProviderTestResult]:
        """Test Connector Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_connector_providers_connector_provider_id_test.asyncio_detailed(
                client=client,
                connector_provider_id=self._bindings["connector_provider_id"],
                body=body,
                idempotency_key=idempotency_key,
            )
        )

    def __call__(
        self, action: wire.PostConnectorProvidersConnectorProviderIdActionAction
    ) -> ConnectorProvidersConnectorProviderIdAction:
        return ConnectorProvidersConnectorProviderIdAction(self._client, self._bind("action", action))


class ConnectorProvidersConnectorProviderIdConnectors(Resource):
    """Bound Native resource: /connector-providers / {connector_provider_id} / connectors."""

    def __call__(self, connector_key: str) -> ConnectorProvidersConnectorProviderIdConnectorsConnectorKey:
        return ConnectorProvidersConnectorProviderIdConnectorsConnectorKey(
            self._client, self._bind("connector_key", connector_key)
        )


class ConnectorProvidersConnectorProviderIdConnectorsConnectorKey(Resource):
    """Bound Native resource: /connector-providers / {connector_provider_id} / connectors / {connector_key}."""

    async def get(self) -> Result[wire.Connector]:
        """Get Connector. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_connector_providers_connector_provider_id_connectors_connector_key.asyncio_detailed(
                client=client,
                connector_provider_id=self._bindings["connector_provider_id"],
                connector_key=self._bindings["connector_key"],
            )
        )

    @property
    def tools(self) -> ConnectorProvidersConnectorProviderIdConnectorsConnectorKeyTools:
        return ConnectorProvidersConnectorProviderIdConnectorsConnectorKeyTools(self._client, self._bindings)


class ConnectorProvidersConnectorProviderIdConnectorsConnectorKeyTools(Resource):
    """Bound Native resource: /connector-providers / {connector_provider_id} / connectors / {connector_key} / tools."""

    async def list(self) -> Result[wire.ConnectorToolPage]:
        """Preview Connector Tools. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                get_connector_providers_connector_provider_id_connectors_connector_key_tools.asyncio_detailed(
                    client=client,
                    connector_provider_id=self._bindings["connector_provider_id"],
                    connector_key=self._bindings["connector_key"],
                )
            )
        )


class ConnectorProvidersConnectorProviderIdCredentials(Resource):
    """Bound Native resource: /connector-providers / {connector_provider_id} / credentials."""

    async def create(
        self, *, body: wire.ReplaceConnectorProviderCredentialsRequest, idempotency_key: str
    ) -> Result[wire.ConnectorProvider]:
        """Replace Connector Provider Credentials. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_connector_providers_connector_provider_id_credentials.asyncio_detailed(
                client=client,
                connector_provider_id=self._bindings["connector_provider_id"],
                body=body,
                idempotency_key=idempotency_key,
            )
        )


class ConnectorProvidersConnectorProviderIdDiscoverConnectors(Resource):
    """Bound Native resource: /connector-providers / {connector_provider_id} / discover-connectors."""

    async def create(
        self,
        *,
        query: str | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        refresh: bool | Unset = UNSET,
    ) -> Result[wire.ConnectorCollection]:
        """Discover Connectors. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_connector_providers_connector_provider_id_discover_connectors.asyncio_detailed(
                client=client,
                connector_provider_id=self._bindings["connector_provider_id"],
                query=query,
                cursor=cursor,
                limit=limit,
                refresh=refresh,
            )
        )


class ConnectorProvidersConnectorProviderIdAction(Resource):
    """Bound Native resource: /connector-providers / {connector_provider_id} / {action}."""

    async def create(
        self, *, body: wire.ConnectorProviderCommandRequest, idempotency_key: str
    ) -> Result[wire.ConnectorProvider]:
        """Change Connector Provider Lifecycle. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_connector_providers_connector_provider_id_action.asyncio_detailed(
                client=client,
                connector_provider_id=self._bindings["connector_provider_id"],
                action=wire.PostConnectorProvidersConnectorProviderIdActionAction(self._bindings["action"]),
                body=body,
                idempotency_key=idempotency_key,
            )
        )


class EnvironmentCommands(Resource):
    """Bound Native resource: /environment-commands."""

    def __call__(self, command_id: str) -> EnvironmentCommandsCommandId:
        return EnvironmentCommandsCommandId(self._client, self._bind("command_id", command_id))


class EnvironmentCommandsCommandId(Resource):
    """Bound Native resource: /environment-commands / {command_id}."""

    async def get(self) -> Result[wire.EnvironmentCommand]:
        """Get Command. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_environment_commands_command_id.asyncio_detailed(
                client=client, command_id=self._bindings["command_id"]
            )
        )


class EnvironmentProviderTypes(Resource):
    """Bound Native resource: /environment-provider-types."""

    async def list(self) -> Result[wire.ProviderMetadataCollectionEnvironmentProviderMetadata]:
        """Provider Types. One HTTP request; no automatic replay."""
        return await self._call(lambda client: get_environment_provider_types.asyncio_detailed(client=client))

    def __call__(self, provider_type: str) -> EnvironmentProviderTypesProviderType:
        return EnvironmentProviderTypesProviderType(self._client, self._bind("provider_type", provider_type))


class EnvironmentProviderTypesProviderType(Resource):
    """Bound Native resource: /environment-provider-types / {provider_type}."""

    async def get(self) -> Result[wire.EnvironmentProviderMetadata]:
        """Get Provider Type. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_environment_provider_types_provider_type.asyncio_detailed(
                client=client, provider_type=self._bindings["provider_type"]
            )
        )


class EnvironmentProviders(Resource):
    """Bound Native resource: /environment-providers."""

    def __call__(self, provider_id: str) -> EnvironmentProvidersProviderId:
        return EnvironmentProvidersProviderId(self._client, self._bind("provider_id", provider_id))


class EnvironmentProvidersProviderId(Resource):
    """Bound Native resource: /environment-providers / {provider_id}."""

    async def update(
        self, *, body: wire.UpdateProviderRequest, if_match: str
    ) -> Result[wire.EnvironmentProviderAccount]:
        """Update Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: patch_environment_providers_provider_id.asyncio_detailed(
                client=client, provider_id=self._bindings["provider_id"], body=body, if_match=if_match
            )
        )

    async def get(self) -> Result[wire.EnvironmentProviderAccount]:
        """Get Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_environment_providers_resource_id.asyncio_detailed(
                client=client, resource_id=self._bindings["provider_id"]
            )
        )

    @property
    def connectivity(self) -> EnvironmentProvidersProviderIdConnectivity:
        return EnvironmentProvidersProviderIdConnectivity(self._client, self._bindings)

    @property
    def credential(self) -> EnvironmentProvidersProviderIdCredential:
        return EnvironmentProvidersProviderIdCredential(self._client, self._bindings)

    @property
    def test_image(self) -> EnvironmentProvidersProviderIdTestImage:
        return EnvironmentProvidersProviderIdTestImage(self._client, self._bindings)


class EnvironmentProvidersProviderIdConnectivity(Resource):
    """Bound Native resource: /environment-providers / {provider_id} / connectivity."""

    async def get(self) -> Result[wire.ProviderConnectivity]:
        """Provider Connectivity. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_environment_providers_provider_id_connectivity.asyncio_detailed(
                client=client, provider_id=self._bindings["provider_id"]
            )
        )


class EnvironmentProvidersProviderIdCredential(Resource):
    """Bound Native resource: /environment-providers / {provider_id} / credential."""

    async def replace(
        self, *, body: wire.ReplaceCredentialRequest, if_match: str
    ) -> Result[wire.EnvironmentProviderAccount]:
        """Replace Credential. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: put_environment_providers_provider_id_credential.asyncio_detailed(
                client=client, provider_id=self._bindings["provider_id"], body=body, if_match=if_match
            )
        )


class EnvironmentProvidersProviderIdTestImage(Resource):
    """Bound Native resource: /environment-providers / {provider_id} / test-image."""

    async def create(self, *, body: wire.TestDockerImageRequest) -> Result[wire.ImageTestResponse]:
        """Test Image. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_environment_providers_provider_id_test_image.asyncio_detailed(
                client=client, provider_id=self._bindings["provider_id"], body=body
            )
        )

    def __call__(self, request_id: str) -> EnvironmentProvidersProviderIdTestImageRequestId:
        return EnvironmentProvidersProviderIdTestImageRequestId(self._client, self._bind("request_id", request_id))


class EnvironmentProvidersProviderIdTestImageRequestId(Resource):
    """Bound Native resource: /environment-providers / {provider_id} / test-image / {request_id}."""

    async def cancel(self, *, body: wire.CancelDockerImageRequest) -> Result[None]:
        """Cancel Image Test. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_environment_providers_provider_id_test_image_request_id_cancel.asyncio_detailed(
                client=client,
                provider_id=self._bindings["provider_id"],
                request_id=self._bindings["request_id"],
                body=body,
            )
        )


class EnvironmentTemplateRevisions(Resource):
    """Bound Native resource: /environment-template-revisions."""

    def __call__(self, revision_id: str) -> EnvironmentTemplateRevisionsRevisionId:
        return EnvironmentTemplateRevisionsRevisionId(self._client, self._bind("revision_id", revision_id))


class EnvironmentTemplateRevisionsRevisionId(Resource):
    """Bound Native resource: /environment-template-revisions / {revision_id}."""

    async def get(self) -> Result[wire.EnvironmentTemplateRevision]:
        """Get Revision. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_environment_template_revisions_revision_id.asyncio_detailed(
                client=client, revision_id=self._bindings["revision_id"]
            )
        )


class EnvironmentTemplates(Resource):
    """Bound Native resource: /environment-templates."""

    def __call__(self, resource_id: str) -> EnvironmentTemplatesResourceId:
        return EnvironmentTemplatesResourceId(self._client, self._bind("resource_id", resource_id))


class EnvironmentTemplatesResourceId(Resource):
    """Bound Native resource: /environment-templates / {resource_id}."""

    async def get(self) -> Result[wire.EnvironmentTemplate]:
        """Get Template. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_environment_templates_resource_id.asyncio_detailed(
                client=client, resource_id=self._bindings["resource_id"]
            )
        )

    async def update(self, *, body: wire.UpdateTemplateRequest, if_match: str) -> Result[wire.EnvironmentTemplate]:
        """Update Template. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: patch_environment_templates_template_id.asyncio_detailed(
                client=client, template_id=self._bindings["resource_id"], body=body, if_match=if_match
            )
        )

    @property
    def labels(self) -> EnvironmentTemplatesResourceIdLabels:
        return EnvironmentTemplatesResourceIdLabels(self._client, self._bindings)

    @property
    def revisions(self) -> EnvironmentTemplatesResourceIdRevisions:
        return EnvironmentTemplatesResourceIdRevisions(self._client, self._bindings)


class EnvironmentTemplatesResourceIdLabels(Resource):
    """Bound Native resource: /environment-templates / {resource_id} / labels."""

    async def get(self) -> Result[wire.LabelsBody]:
        """Get Template Labels. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_environment_templates_template_id_labels.asyncio_detailed(
                client=client, template_id=self._bindings["resource_id"]
            )
        )

    async def replace(self, *, body: wire.LabelsBody, if_match: str) -> Result[wire.LabelsBody]:
        """Put Template Labels. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: put_environment_templates_template_id_labels.asyncio_detailed(
                client=client, template_id=self._bindings["resource_id"], body=body, if_match=if_match
            )
        )


class EnvironmentTemplatesResourceIdRevisions(Resource):
    """Bound Native resource: /environment-templates / {resource_id} / revisions."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.CollectionEnvironmentTemplateRevision]:
        """List Revisions. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_environment_templates_template_id_revisions.asyncio_detailed(
                client=client, template_id=self._bindings["resource_id"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.CollectionEnvironmentTemplateRevision]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.EnvironmentTemplateRevision]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    async def create(self, *, body: wire.CreateTemplateRevisionRequest) -> Result[wire.EnvironmentTemplateRevision]:
        """Create Revision. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_environment_templates_template_id_revisions.asyncio_detailed(
                client=client, template_id=self._bindings["resource_id"], body=body
            )
        )

    def __call__(self, revision_id: str) -> EnvironmentTemplatesResourceIdRevisionsRevisionId:
        return EnvironmentTemplatesResourceIdRevisionsRevisionId(self._client, self._bind("revision_id", revision_id))


class EnvironmentTemplatesResourceIdRevisionsRevisionId(Resource):
    """Bound Native resource: /environment-templates / {resource_id} / revisions / {revision_id}."""

    async def default(self, *, if_match: str) -> Result[wire.EnvironmentTemplate]:
        """Set Default Revision. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_environment_templates_template_id_revisions_revision_id_default.asyncio_detailed(
                client=client,
                template_id=self._bindings["resource_id"],
                revision_id=self._bindings["revision_id"],
                if_match=if_match,
            )
        )


class Environments(Resource):
    """Bound Native resource: /environments."""

    def __call__(self, environment_id: str) -> EnvironmentsEnvironmentId:
        return EnvironmentsEnvironmentId(self._client, self._bind("environment_id", environment_id))


class EnvironmentsEnvironmentId(Resource):
    """Bound Native resource: /environments / {environment_id}."""

    async def update(self, *, body: wire.UpdateEnvironmentRequest, if_match: str) -> Result[wire.Environment]:
        """Update Environment. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: patch_environments_environment_id.asyncio_detailed(
                client=client, environment_id=self._bindings["environment_id"], body=body, if_match=if_match
            )
        )

    async def get(self) -> Result[wire.EnvironmentDetail]:
        """Get Environment. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_environments_resource_id.asyncio_detailed(
                client=client, resource_id=self._bindings["environment_id"]
            )
        )

    @property
    def connection(self) -> EnvironmentsEnvironmentIdConnection:
        return EnvironmentsEnvironmentIdConnection(self._client, self._bindings)

    @property
    def connection_tickets(self) -> EnvironmentsEnvironmentIdConnectionTickets:
        return EnvironmentsEnvironmentIdConnectionTickets(self._client, self._bindings)

    async def delete(self, *, idempotency_key: str) -> Result[wire.EnvironmentCommand]:
        """Delete Environment. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_environments_environment_id_delete.asyncio_detailed(
                client=client, environment_id=self._bindings["environment_id"], idempotency_key=idempotency_key
            )
        )

    @property
    def device(self) -> EnvironmentsEnvironmentIdDevice:
        return EnvironmentsEnvironmentIdDevice(self._client, self._bindings)

    @property
    def directories(self) -> EnvironmentsEnvironmentIdDirectories:
        return EnvironmentsEnvironmentIdDirectories(self._client, self._bindings)

    @property
    def labels(self) -> EnvironmentsEnvironmentIdLabels:
        return EnvironmentsEnvironmentIdLabels(self._client, self._bindings)

    async def revoke_device(self) -> Result[wire.Environment]:
        """Revoke Device. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_environments_environment_id_revoke_device.asyncio_detailed(
                client=client, environment_id=self._bindings["environment_id"]
            )
        )

    async def stop(self, *, idempotency_key: str) -> Result[wire.EnvironmentCommand]:
        """Stop Environment. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_environments_environment_id_stop.asyncio_detailed(
                client=client, environment_id=self._bindings["environment_id"], idempotency_key=idempotency_key
            )
        )


class EnvironmentsEnvironmentIdConnection(Resource):
    """Bound Native resource: /environments / {environment_id} / connection."""

    async def get(self) -> Result[wire.ClientConnectionStatus]:
        """Connection Status. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_environments_environment_id_connection.asyncio_detailed(
                client=client, environment_id=self._bindings["environment_id"]
            )
        )


class EnvironmentsEnvironmentIdConnectionTickets(Resource):
    """Bound Native resource: /environments / {environment_id} / connection-tickets."""

    async def create(self) -> Result[wire.ClientConnectionTicket]:
        """Issue Ticket. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_environments_environment_id_connection_tickets.asyncio_detailed(
                client=client, environment_id=self._bindings["environment_id"]
            )
        )


class EnvironmentsEnvironmentIdDevice(Resource):
    """Bound Native resource: /environments / {environment_id} / device."""

    async def get(self) -> Result[wire.DeviceInfo]:
        """Device Info. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_environments_environment_id_device.asyncio_detailed(
                client=client, environment_id=self._bindings["environment_id"]
            )
        )


class EnvironmentsEnvironmentIdDirectories(Resource):
    """Bound Native resource: /environments / {environment_id} / directories."""

    async def get(
        self, *, path: str | Unset | None = UNSET, offset: int | Unset = UNSET, limit: int | Unset = UNSET
    ) -> Result[wire.DirectoryListResult]:
        """Device Directories. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_environments_environment_id_directories.asyncio_detailed(
                client=client, environment_id=self._bindings["environment_id"], path=path, offset=offset, limit=limit
            )
        )


class EnvironmentsEnvironmentIdLabels(Resource):
    """Bound Native resource: /environments / {environment_id} / labels."""

    async def get(self) -> Result[wire.LabelsBody]:
        """Get Environment Labels. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_environments_environment_id_labels.asyncio_detailed(
                client=client, environment_id=self._bindings["environment_id"]
            )
        )

    async def replace(self, *, body: wire.LabelsBody, if_match: str) -> Result[wire.LabelsBody]:
        """Put Environment Labels. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: put_environments_environment_id_labels.asyncio_detailed(
                client=client, environment_id=self._bindings["environment_id"], body=body, if_match=if_match
            )
        )


class HookSubscriptions(Resource):
    """Bound Native resource: /hook-subscriptions."""

    def __call__(self, subscription_id: str) -> HookSubscriptionsSubscriptionId:
        return HookSubscriptionsSubscriptionId(self._client, self._bind("subscription_id", subscription_id))


class HookSubscriptionsSubscriptionId(Resource):
    """Bound Native resource: /hook-subscriptions / {subscription_id}."""

    async def delete(self, *, if_match: str) -> Result[None]:
        """Delete Hook Subscription. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_hook_subscriptions_subscription_id.asyncio_detailed(
                client=client, subscription_id=self._bindings["subscription_id"], if_match=if_match
            )
        )

    async def get(self) -> Result[wire.HookSubscription]:
        """Get Hook Subscription. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_hook_subscriptions_subscription_id.asyncio_detailed(
                client=client, subscription_id=self._bindings["subscription_id"]
            )
        )

    async def update(
        self, *, body: wire.UpdateHookSubscriptionStateRequest, if_match: str
    ) -> Result[wire.HookSubscription]:
        """Update Hook Subscription State. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: patch_hook_subscriptions_subscription_id.asyncio_detailed(
                client=client, subscription_id=self._bindings["subscription_id"], body=body, if_match=if_match
            )
        )

    async def replace(
        self, *, body: wire.UpdateHookSubscriptionRequest, if_match: str
    ) -> Result[wire.HookSubscription]:
        """Update Hook Subscription. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: put_hook_subscriptions_subscription_id.asyncio_detailed(
                client=client, subscription_id=self._bindings["subscription_id"], body=body, if_match=if_match
            )
        )

    @property
    def deliveries(self) -> HookSubscriptionsSubscriptionIdDeliveries:
        return HookSubscriptionsSubscriptionIdDeliveries(self._client, self._bindings)


class HookSubscriptionsSubscriptionIdDeliveries(Resource):
    """Bound Native resource: /hook-subscriptions / {subscription_id} / deliveries."""

    def __call__(self, delivery_id: str) -> HookSubscriptionsSubscriptionIdDeliveriesDeliveryId:
        return HookSubscriptionsSubscriptionIdDeliveriesDeliveryId(self._client, self._bind("delivery_id", delivery_id))


class HookSubscriptionsSubscriptionIdDeliveriesDeliveryId(Resource):
    """Bound Native resource: /hook-subscriptions / {subscription_id} / deliveries / {delivery_id}."""

    async def redrive(self) -> Result[None]:
        """Redrive Hook Delivery. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_hook_subscriptions_subscription_id_deliveries_delivery_id_redrive.asyncio_detailed(
                client=client,
                subscription_id=self._bindings["subscription_id"],
                delivery_id=self._bindings["delivery_id"],
            )
        )


class Invitations(Resource):
    """Bound Native resource: /invitations."""

    def __call__(self, invitation_id: str) -> InvitationsInvitationId:
        return InvitationsInvitationId(self._client, self._bind("invitation_id", invitation_id))


class InvitationsInvitationId(Resource):
    """Bound Native resource: /invitations / {invitation_id}."""

    async def accept(self, *, body: wire.AcceptInvitationRequest) -> Result[wire.LoginResult]:
        """Accept Invitation. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_invitations_invitation_id_accept.asyncio_detailed(
                client=client, invitation_id=self._bindings["invitation_id"], body=body
            )
        )

    async def resend(self, *, body: wire.ExpectedVersion) -> Result[wire.InvitationDelivery]:
        """Resend Invitation. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_invitations_invitation_id_resend.asyncio_detailed(
                client=client, invitation_id=self._bindings["invitation_id"], body=body
            )
        )

    async def revoke(self, *, body: wire.ExpectedVersion) -> Result[wire.Invitation]:
        """Revoke Invitation. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_invitations_invitation_id_revoke.asyncio_detailed(
                client=client, invitation_id=self._bindings["invitation_id"], body=body
            )
        )


class McpServers(Resource):
    """Bound Native resource: /mcp-servers."""

    async def list(
        self, *, query: str | Unset = UNSET, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.MCPServerCollection]:
        """List Mcp Servers. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_mcp_servers.asyncio_detailed(client=client, query=query, limit=limit, cursor=cursor)
        )

    def pages(
        self, *, query: str | Unset = UNSET, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.MCPServerCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(query=query, limit=limit, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self, *, query: str | Unset = UNSET, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.MCPServer]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(query=query, limit=limit, cursor=cursor) for item in page.value.items)

    def __call__(self, server_key: str) -> McpServersServerKey:
        return McpServersServerKey(self._client, self._bind("server_key", server_key))


class McpServersServerKey(Resource):
    """Bound Native resource: /mcp-servers / {server_key}."""

    async def get(self) -> Result[wire.MCPServer]:
        """Get Mcp Server. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_mcp_servers_server_key.asyncio_detailed(
                client=client, server_key=self._bindings["server_key"]
            )
        )


class MemoryProviderTypes(Resource):
    """Bound Native resource: /memory-provider-types."""

    async def list(self) -> Result[wire.ProviderMetadataCollectionMemoryProviderMetadata]:
        """List Types. One HTTP request; no automatic replay."""
        return await self._call(lambda client: get_memory_provider_types.asyncio_detailed(client=client))

    def __call__(self, provider_type: str) -> MemoryProviderTypesProviderType:
        return MemoryProviderTypesProviderType(self._client, self._bind("provider_type", provider_type))


class MemoryProviderTypesProviderType(Resource):
    """Bound Native resource: /memory-provider-types / {provider_type}."""

    async def get(self) -> Result[wire.MemoryProviderMetadata]:
        """Get Type. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_memory_provider_types_provider_type.asyncio_detailed(
                client=client, provider_type=self._bindings["provider_type"]
            )
        )


class ModelProviderTypes(Resource):
    """Bound Native resource: /model-provider-types."""

    async def list(self) -> Result[wire.ProviderMetadataCollectionModelProviderMetadata]:
        """List Model Provider Types. One HTTP request; no automatic replay."""
        return await self._call(lambda client: get_model_provider_types.asyncio_detailed(client=client))

    def __call__(self, provider_type: str) -> ModelProviderTypesProviderType:
        return ModelProviderTypesProviderType(self._client, self._bind("provider_type", provider_type))


class ModelProviderTypesProviderType(Resource):
    """Bound Native resource: /model-provider-types / {provider_type}."""

    async def get(self) -> Result[wire.ModelProviderMetadata]:
        """Get Model Provider Type. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_model_provider_types_provider_type.asyncio_detailed(
                client=client, provider_type=self._bindings["provider_type"]
            )
        )


class Organizations(Resource):
    """Bound Native resource: /organizations."""

    async def list(self) -> Result[wire.PageOrganization]:
        """Organizations. One HTTP request; no automatic replay."""
        return await self._call(lambda client: get_organizations.asyncio_detailed(client=client))

    def __call__(self, organization: str) -> Organization:
        return Organization(self._client, self._bind("organization", organization))


class Organization(Resource):
    """Bound Native resource: /organizations / {organization}."""

    async def get(self) -> Result[wire.Organization]:
        """Organization. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_organizations_organization.asyncio_detailed(
                client=client, organization=self._bindings["organization"]
            )
        )

    async def update(self, *, body: wire.UpdateResourceProfileRequest, if_match: str) -> Result[wire.Organization]:
        """Update Organization. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: patch_organizations_organization.asyncio_detailed(
                client=client, organization=self._bindings["organization"], body=body, if_match=if_match
            )
        )

    @property
    def connector_providers(self) -> OrganizationsOrganizationConnectorProviders:
        return OrganizationsOrganizationConnectorProviders(self._client, self._bindings)

    @property
    def environment_providers(self) -> OrganizationsOrganizationEnvironmentProviders:
        return OrganizationsOrganizationEnvironmentProviders(self._client, self._bindings)

    @property
    def environment_templates(self) -> OrganizationsOrganizationEnvironmentTemplates:
        return OrganizationsOrganizationEnvironmentTemplates(self._client, self._bindings)

    @property
    def icon(self) -> OrganizationsOrganizationIcon:
        return OrganizationsOrganizationIcon(self._client, self._bindings)

    @property
    def invitations(self) -> OrganizationsOrganizationInvitations:
        return OrganizationsOrganizationInvitations(self._client, self._bindings)

    @property
    def memory_providers(self) -> OrganizationsOrganizationMemoryProviders:
        return OrganizationsOrganizationMemoryProviders(self._client, self._bindings)

    @property
    def model_catalog(self) -> OrganizationsOrganizationModelCatalog:
        return OrganizationsOrganizationModelCatalog(self._client, self._bindings)

    @property
    def model_providers(self) -> OrganizationsOrganizationModelProviders:
        return OrganizationsOrganizationModelProviders(self._client, self._bindings)

    @property
    def models(self) -> OrganizationsOrganizationModels:
        return OrganizationsOrganizationModels(self._client, self._bindings)

    @property
    def permissions(self) -> OrganizationsOrganizationPermissions:
        return OrganizationsOrganizationPermissions(self._client, self._bindings)

    @property
    def role_bindings(self) -> OrganizationsOrganizationRoleBindings:
        return OrganizationsOrganizationRoleBindings(self._client, self._bindings)

    @property
    def security_audit_events(self) -> OrganizationsOrganizationSecurityAuditEvents:
        return OrganizationsOrganizationSecurityAuditEvents(self._client, self._bindings)

    @property
    def users(self) -> OrganizationsOrganizationUsers:
        return OrganizationsOrganizationUsers(self._client, self._bindings)

    @property
    def web_providers(self) -> OrganizationsOrganizationWebProviders:
        return OrganizationsOrganizationWebProviders(self._client, self._bindings)

    @property
    def workspaces(self) -> OrganizationsOrganizationWorkspaces:
        return OrganizationsOrganizationWorkspaces(self._client, self._bindings)


class OrganizationsOrganizationConnectorProviders(Resource):
    """Bound Native resource: /organizations / {organization} / connector-providers."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.ConnectorProviderCollection]:
        """Organization List Connector Providers. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_organizations_organization_connector_providers.asyncio_detailed(
                client=client, organization=self._bindings["organization"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.ConnectorProviderCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.ConnectorProvider]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    async def create(
        self, *, body: wire.CreateConnectorProviderRequest, idempotency_key: str
    ) -> Result[wire.ConnectorProvider]:
        """Organization Create Connector Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_organizations_organization_connector_providers.asyncio_detailed(
                client=client, organization=self._bindings["organization"], body=body, idempotency_key=idempotency_key
            )
        )


class OrganizationsOrganizationEnvironmentProviders(Resource):
    """Bound Native resource: /organizations / {organization} / environment-providers."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.CollectionEnvironmentProviderAccount]:
        """Organization List Providers. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_organizations_organization_environment_providers.asyncio_detailed(
                client=client, organization=self._bindings["organization"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.CollectionEnvironmentProviderAccount]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.EnvironmentProviderAccount]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    async def create(self, *, body: wire.CreateProviderRequest) -> Result[wire.EnvironmentProviderAccount]:
        """Organization Create Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_organizations_organization_environment_providers.asyncio_detailed(
                client=client, organization=self._bindings["organization"], body=body
            )
        )


class OrganizationsOrganizationEnvironmentTemplates(Resource):
    """Bound Native resource: /organizations / {organization} / environment-templates."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET, label: list[str] | Unset = UNSET
    ) -> Result[wire.CollectionEnvironmentTemplate]:
        """Organization List Templates. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_organizations_organization_environment_templates.asyncio_detailed(
                client=client, organization=self._bindings["organization"], limit=limit, cursor=cursor, label=label
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET, label: list[str] | Unset = UNSET
    ) -> AsyncIterator[Result[wire.CollectionEnvironmentTemplate]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        label = label.copy() if isinstance(label, list) else label
        return pages(
            lambda next_cursor: self.list(limit=limit, label=label, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET, label: list[str] | Unset = UNSET
    ) -> AsyncIterator[wire.EnvironmentTemplate]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor, label=label) for item in page.value.items)

    async def create(
        self, *, body: wire.CreateTemplateRequest, idempotency_key: str
    ) -> Result[wire.EnvironmentTemplate]:
        """Organization Create Template. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_organizations_organization_environment_templates.asyncio_detailed(
                client=client, organization=self._bindings["organization"], body=body, idempotency_key=idempotency_key
            )
        )


class OrganizationsOrganizationIcon(Resource):
    """Bound Native resource: /organizations / {organization} / icon."""

    async def delete(self, *, if_match: str) -> Result[wire.Organization]:
        """Delete Organization Icon. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_organizations_organization_icon.asyncio_detailed(
                client=client, organization=self._bindings["organization"], if_match=if_match
            )
        )

    async def replace(self, *, body: File, if_match: str) -> Result[wire.Organization]:
        """Put Organization Icon. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: put_organizations_organization_icon.asyncio_detailed(
                client=client, organization=self._bindings["organization"], body=body, if_match=if_match
            )
        )

    def __call__(self, image_id: str) -> OrganizationsOrganizationIconImageId:
        return OrganizationsOrganizationIconImageId(self._client, self._bind("image_id", image_id))


class OrganizationsOrganizationIconImageId(Resource):
    """Bound Native resource: /organizations / {organization} / icon / {image_id}."""

    async def get(self) -> Result[File]:
        """Get Organization Icon. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_organizations_organization_icon_image_id.asyncio_detailed(
                client=client, organization=self._bindings["organization"], image_id=self._bindings["image_id"]
            )
        )

    def get_stream(self) -> AbstractAsyncContextManager[httpx2.Response]:
        """Unbuffered response; caller checks status and consumes within the context."""
        return self._stream(
            get_organizations_organization_icon_image_id.build_request(
                organization=self._bindings["organization"], image_id=self._bindings["image_id"]
            )
        )


class OrganizationsOrganizationInvitations(Resource):
    """Bound Native resource: /organizations / {organization} / invitations."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.PageInvitation]:
        """Invitations. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_organizations_organization_invitations.asyncio_detailed(
                client=client, organization=self._bindings["organization"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.PageInvitation]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> AsyncIterator[wire.Invitation]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    async def create(self, *, body: wire.CreateInvitationRequest) -> Result[wire.InvitationDelivery]:
        """Invite. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_organizations_organization_invitations.asyncio_detailed(
                client=client, organization=self._bindings["organization"], body=body
            )
        )


class OrganizationsOrganizationMemoryProviders(Resource):
    """Bound Native resource: /organizations / {organization} / memory-providers."""

    async def list(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        type_: str | Unset | None = UNSET,
        enabled: bool | Unset | None = UNSET,
    ) -> Result[wire.MemoryProviderCollection]:
        """List Organization Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_organizations_organization_memory_providers.asyncio_detailed(
                client=client,
                organization=self._bindings["organization"],
                limit=limit,
                cursor=cursor,
                type_=type_,
                enabled=enabled,
            )
        )

    def pages(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        type_: str | Unset | None = UNSET,
        enabled: bool | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.MemoryProviderCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, type_=type_, enabled=enabled, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        type_: str | Unset | None = UNSET,
        enabled: bool | Unset | None = UNSET,
    ) -> AsyncIterator[wire.MemoryProvider]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(limit=limit, cursor=cursor, type_=type_, enabled=enabled)
            for item in page.value.items
        )

    async def create(self, *, body: wire.CreateMemoryProviderRequest) -> Result[wire.MemoryProvider]:
        """Create Organization Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_organizations_organization_memory_providers.asyncio_detailed(
                client=client, organization=self._bindings["organization"], body=body
            )
        )

    def __call__(self, provider_id: str) -> OrganizationsOrganizationMemoryProvidersProviderId:
        return OrganizationsOrganizationMemoryProvidersProviderId(self._client, self._bind("provider_id", provider_id))


class OrganizationsOrganizationMemoryProvidersProviderId(Resource):
    """Bound Native resource: /organizations / {organization} / memory-providers / {provider_id}."""

    async def get(self) -> Result[wire.MemoryProvider]:
        """Get Organization Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_organizations_organization_memory_providers_provider_id.asyncio_detailed(
                client=client, organization=self._bindings["organization"], provider_id=self._bindings["provider_id"]
            )
        )

    async def update(self, *, body: wire.UpdateMemoryProviderRequest, if_match: str) -> Result[wire.MemoryProvider]:
        """Update Organization Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: patch_organizations_organization_memory_providers_provider_id.asyncio_detailed(
                client=client,
                organization=self._bindings["organization"],
                provider_id=self._bindings["provider_id"],
                body=body,
                if_match=if_match,
            )
        )

    @property
    def references(self) -> OrganizationsOrganizationMemoryProvidersProviderIdReferences:
        return OrganizationsOrganizationMemoryProvidersProviderIdReferences(self._client, self._bindings)


class OrganizationsOrganizationMemoryProvidersProviderIdReferences(Resource):
    """Bound Native resource: /organizations / {organization} / memory-providers / {provider_id} / references."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.MemoryProviderReferenceCollection]:
        """References Organization Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_organizations_organization_memory_providers_provider_id_references.asyncio_detailed(
                client=client,
                organization=self._bindings["organization"],
                provider_id=self._bindings["provider_id"],
                limit=limit,
                cursor=cursor,
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.MemoryProviderReferenceCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.MemoryProviderReference]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)


class OrganizationsOrganizationModelCatalog(Resource):
    """Bound Native resource: /organizations / {organization} / model-catalog."""

    async def list(self) -> Result[wire.ModelCatalogCollection]:
        """Organization List Model Catalog. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_organizations_organization_model_catalog.asyncio_detailed(
                client=client, organization=self._bindings["organization"]
            )
        )


class OrganizationsOrganizationModelProviders(Resource):
    """Bound Native resource: /organizations / {organization} / model-providers."""

    async def list(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        name: str | Unset | None = UNSET,
        provider_type: str | Unset | None = UNSET,
        enabled: bool | Unset | None = UNSET,
    ) -> Result[wire.ModelProviderCollection]:
        """Organization List Model Providers. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_organizations_organization_model_providers.asyncio_detailed(
                client=client,
                organization=self._bindings["organization"],
                limit=limit,
                cursor=cursor,
                name=name,
                provider_type=provider_type,
                enabled=enabled,
            )
        )

    def pages(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        name: str | Unset | None = UNSET,
        provider_type: str | Unset | None = UNSET,
        enabled: bool | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.ModelProviderCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(
                limit=limit, name=name, provider_type=provider_type, enabled=enabled, cursor=next_cursor
            ),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        name: str | Unset | None = UNSET,
        provider_type: str | Unset | None = UNSET,
        enabled: bool | Unset | None = UNSET,
    ) -> AsyncIterator[wire.ModelProvider]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(
                limit=limit, cursor=cursor, name=name, provider_type=provider_type, enabled=enabled
            )
            for item in page.value.items
        )

    async def create(self, *, body: wire.CreateModelProviderRequest) -> Result[wire.ModelProvider]:
        """Organization Create Model Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_organizations_organization_model_providers.asyncio_detailed(
                client=client, organization=self._bindings["organization"], body=body
            )
        )

    def __call__(self, provider_id: str) -> OrganizationsOrganizationModelProvidersProviderId:
        return OrganizationsOrganizationModelProvidersProviderId(self._client, self._bind("provider_id", provider_id))


class OrganizationsOrganizationModelProvidersProviderId(Resource):
    """Bound Native resource: /organizations / {organization} / model-providers / {provider_id}."""

    async def get(self) -> Result[wire.ModelProvider]:
        """Organization Get Model Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_organizations_organization_model_providers_provider_id.asyncio_detailed(
                client=client, organization=self._bindings["organization"], provider_id=self._bindings["provider_id"]
            )
        )

    async def update(self, *, body: wire.UpdateModelProviderRequest, if_match: str) -> Result[wire.ModelProvider]:
        """Organization Update Model Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: patch_organizations_organization_model_providers_provider_id.asyncio_detailed(
                client=client,
                organization=self._bindings["organization"],
                provider_id=self._bindings["provider_id"],
                body=body,
                if_match=if_match,
            )
        )

    async def test(self) -> Result[wire.ModelConnectionTestResult]:
        """Organization Test Model Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_organizations_organization_model_providers_provider_id_test.asyncio_detailed(
                client=client, organization=self._bindings["organization"], provider_id=self._bindings["provider_id"]
            )
        )


class OrganizationsOrganizationModels(Resource):
    """Bound Native resource: /organizations / {organization} / models."""

    async def list(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        query: str | Unset | None = UNSET,
        provider_id: str | Unset | None = UNSET,
        enabled: bool | Unset | None = UNSET,
    ) -> Result[wire.ModelCollection]:
        """Organization List Models. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_organizations_organization_models.asyncio_detailed(
                client=client,
                organization=self._bindings["organization"],
                limit=limit,
                cursor=cursor,
                query=query,
                provider_id=provider_id,
                enabled=enabled,
            )
        )

    def pages(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        query: str | Unset | None = UNSET,
        provider_id: str | Unset | None = UNSET,
        enabled: bool | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.ModelCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(
                limit=limit, query=query, provider_id=provider_id, enabled=enabled, cursor=next_cursor
            ),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        query: str | Unset | None = UNSET,
        provider_id: str | Unset | None = UNSET,
        enabled: bool | Unset | None = UNSET,
    ) -> AsyncIterator[wire.Model]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(
                limit=limit, cursor=cursor, query=query, provider_id=provider_id, enabled=enabled
            )
            for item in page.value.items
        )

    async def create(self, *, body: wire.CreateModelRequest) -> Result[wire.Model]:
        """Organization Create Model. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_organizations_organization_models.asyncio_detailed(
                client=client, organization=self._bindings["organization"], body=body
            )
        )

    def __call__(self, model_id: str) -> OrganizationsOrganizationModelsModelId:
        return OrganizationsOrganizationModelsModelId(self._client, self._bind("model_id", model_id))


class OrganizationsOrganizationModelsModelId(Resource):
    """Bound Native resource: /organizations / {organization} / models / {model_id}."""

    async def get(self) -> Result[wire.Model]:
        """Organization Get Model. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_organizations_organization_models_model_id.asyncio_detailed(
                client=client, organization=self._bindings["organization"], model_id=self._bindings["model_id"]
            )
        )

    async def update(self, *, body: wire.UpdateModelRequest, if_match: str) -> Result[wire.Model]:
        """Organization Update Model. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: patch_organizations_organization_models_model_id.asyncio_detailed(
                client=client,
                organization=self._bindings["organization"],
                model_id=self._bindings["model_id"],
                body=body,
                if_match=if_match,
            )
        )

    async def test(
        self, *, body: wire.ModelTestRequest | Unset | None = UNSET
    ) -> Result[wire.ModelConnectionTestResult]:
        """Organization Test Model. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_organizations_organization_models_model_id_test.asyncio_detailed(
                client=client,
                organization=self._bindings["organization"],
                model_id=self._bindings["model_id"],
                body=body,
            )
        )


class OrganizationsOrganizationPermissions(Resource):
    """Bound Native resource: /organizations / {organization} / permissions."""

    async def get(self) -> Result[wire.OrganizationPermissions]:
        """Organization Permissions. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_organizations_organization_permissions.asyncio_detailed(
                client=client, organization=self._bindings["organization"]
            )
        )


class OrganizationsOrganizationRoleBindings(Resource):
    """Bound Native resource: /organizations / {organization} / role-bindings."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.PageRoleBinding]:
        """Organization Roles. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_organizations_organization_role_bindings.asyncio_detailed(
                client=client, organization=self._bindings["organization"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.PageRoleBinding]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.RoleBinding]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    async def create(self, *, body: wire.SetRoleRequest) -> Result[wire.RoleBinding]:
        """Create Organization Binding. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_organizations_organization_role_bindings.asyncio_detailed(
                client=client, organization=self._bindings["organization"], body=body
            )
        )


class OrganizationsOrganizationSecurityAuditEvents(Resource):
    """Bound Native resource: /organizations / {organization} / security-audit-events."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.PageSecurityEvent]:
        """Organization Security Events. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_organizations_organization_security_audit_events.asyncio_detailed(
                client=client, organization=self._bindings["organization"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.PageSecurityEvent]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.SecurityEvent]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)


class OrganizationsOrganizationUsers(Resource):
    """Bound Native resource: /organizations / {organization} / users."""

    async def list(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> Result[wire.PageUser]:
        """Users. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_organizations_organization_users.asyncio_detailed(
                client=client, organization=self._bindings["organization"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.PageUser]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> AsyncIterator[wire.User]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)


class OrganizationsOrganizationWebProviders(Resource):
    """Bound Native resource: /organizations / {organization} / web-providers."""

    async def list(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        type_: str | Unset | None = UNSET,
        enabled: bool | Unset | None = UNSET,
    ) -> Result[wire.WebProviderCollection]:
        """List Organization Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_organizations_organization_web_providers.asyncio_detailed(
                client=client,
                organization=self._bindings["organization"],
                limit=limit,
                cursor=cursor,
                type_=type_,
                enabled=enabled,
            )
        )

    def pages(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        type_: str | Unset | None = UNSET,
        enabled: bool | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.WebProviderCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, type_=type_, enabled=enabled, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        type_: str | Unset | None = UNSET,
        enabled: bool | Unset | None = UNSET,
    ) -> AsyncIterator[wire.WebProvider]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(limit=limit, cursor=cursor, type_=type_, enabled=enabled)
            for item in page.value.items
        )

    async def create(self, *, body: wire.CreateWebProviderRequest) -> Result[wire.WebProvider]:
        """Create Organization Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_organizations_organization_web_providers.asyncio_detailed(
                client=client, organization=self._bindings["organization"], body=body
            )
        )

    def __call__(self, provider_id: str) -> OrganizationsOrganizationWebProvidersProviderId:
        return OrganizationsOrganizationWebProvidersProviderId(self._client, self._bind("provider_id", provider_id))


class OrganizationsOrganizationWebProvidersProviderId(Resource):
    """Bound Native resource: /organizations / {organization} / web-providers / {provider_id}."""

    async def get(self) -> Result[wire.WebProvider]:
        """Get Organization Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_organizations_organization_web_providers_provider_id.asyncio_detailed(
                client=client, organization=self._bindings["organization"], provider_id=self._bindings["provider_id"]
            )
        )

    async def update(self, *, body: wire.UpdateWebProviderRequest, if_match: str) -> Result[wire.WebProvider]:
        """Update Organization Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: patch_organizations_organization_web_providers_provider_id.asyncio_detailed(
                client=client,
                organization=self._bindings["organization"],
                provider_id=self._bindings["provider_id"],
                body=body,
                if_match=if_match,
            )
        )

    @property
    def references(self) -> OrganizationsOrganizationWebProvidersProviderIdReferences:
        return OrganizationsOrganizationWebProvidersProviderIdReferences(self._client, self._bindings)

    async def test(self) -> Result[wire.WebProviderTestResult]:
        """Test Organization Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_organizations_organization_web_providers_provider_id_test.asyncio_detailed(
                client=client, organization=self._bindings["organization"], provider_id=self._bindings["provider_id"]
            )
        )


class OrganizationsOrganizationWebProvidersProviderIdReferences(Resource):
    """Bound Native resource: /organizations / {organization} / web-providers / {provider_id} / references."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.WebProviderReferenceCollection]:
        """References Organization Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_organizations_organization_web_providers_provider_id_references.asyncio_detailed(
                client=client,
                organization=self._bindings["organization"],
                provider_id=self._bindings["provider_id"],
                limit=limit,
                cursor=cursor,
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.WebProviderReferenceCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.WebProviderReference]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)


class OrganizationsOrganizationWorkspaces(Resource):
    """Bound Native resource: /organizations / {organization} / workspaces."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.PageWorkspace]:
        """Workspaces. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_organizations_organization_workspaces.asyncio_detailed(
                client=client, organization=self._bindings["organization"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.PageWorkspace]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> AsyncIterator[wire.Workspace]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    async def create(self, *, body: wire.CreateWorkspaceRequest) -> Result[wire.Workspace]:
        """Create Workspace. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_organizations_organization_workspaces.asyncio_detailed(
                client=client, organization=self._bindings["organization"], body=body
            )
        )


class QueuedSubmissions(Resource):
    """Bound Native resource: /queued-submissions."""

    def __call__(self, queued_submission_id: str) -> QueuedSubmission:
        return QueuedSubmission(self._client, self._bind("queued_submission_id", queued_submission_id))


class _QueuedSubmissionResource(Resource):
    """Bound Native resource: /queued-submissions / {queued_submission_id}."""

    async def delete(self, *, expected_version: int, idempotency_key: str) -> Result[None]:
        """Delete Queued Submission. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_queued_submissions_queued_submission_id.asyncio_detailed(
                client=client,
                queued_submission_id=self._bindings["queued_submission_id"],
                expected_version=expected_version,
                idempotency_key=idempotency_key,
            )
        )

    async def get(self) -> Result[wire.QueuedSubmission]:
        """Get Queued Submission. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_queued_submissions_queued_submission_id.asyncio_detailed(
                client=client, queued_submission_id=self._bindings["queued_submission_id"]
            )
        )

    async def update(
        self, *, body: wire.UpdateQueuedSubmissionRequest, idempotency_key: str
    ) -> Result[wire.QueuedSubmissionMutationReceipt]:
        """Update Queued Submission. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: patch_queued_submissions_queued_submission_id.asyncio_detailed(
                client=client,
                queued_submission_id=self._bindings["queued_submission_id"],
                body=body,
                idempotency_key=idempotency_key,
            )
        )


class RoleBindings(Resource):
    """Bound Native resource: /role-bindings."""

    def __call__(self, binding_id: str) -> RoleBindingsBindingId:
        return RoleBindingsBindingId(self._client, self._bind("binding_id", binding_id))


class RoleBindingsBindingId(Resource):
    """Bound Native resource: /role-bindings / {binding_id}."""

    async def delete(self, *, if_match: str) -> Result[None]:
        """Remove Member. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_role_bindings_binding_id.asyncio_detailed(
                client=client, binding_id=self._bindings["binding_id"], if_match=if_match
            )
        )

    async def get(self) -> Result[wire.RoleBinding]:
        """Role Binding. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_role_bindings_binding_id.asyncio_detailed(
                client=client, binding_id=self._bindings["binding_id"]
            )
        )

    async def update(self, *, body: wire.ChangeRoleRequest, if_match: str) -> Result[wire.RoleBinding]:
        """Change Role. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: patch_role_bindings_binding_id.asyncio_detailed(
                client=client, binding_id=self._bindings["binding_id"], body=body, if_match=if_match
            )
        )


class RunAttempts(Resource):
    """Bound Native resource: /run-attempts."""

    def __call__(self, run_attempt_id: str) -> RunAttempt:
        return RunAttempt(self._client, self._bind("run_attempt_id", run_attempt_id))


class RunAttempt(Resource):
    """Bound Native resource: /run-attempts / {run_attempt_id}."""

    async def get(self) -> Result[wire.RunAttemptResource]:
        """Get Run Attempt. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_run_attempts_run_attempt_id.asyncio_detailed(
                client=client, run_attempt_id=self._bindings["run_attempt_id"]
            )
        )

    @property
    def events(self) -> RunAttemptsRunAttemptIdEvents:
        return RunAttemptsRunAttemptIdEvents(self._client, self._bindings)


class RunAttemptsRunAttemptIdEvents(Resource):
    """Bound Native resource: /run-attempts / {run_attempt_id} / events."""

    async def list(
        self, *, after_resource_seq: int | Unset = UNSET, limit: int | Unset = UNSET
    ) -> Result[wire.ResourceLifecycleEventPage]:
        """List Run Attempt Events. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_run_attempts_run_attempt_id_events.asyncio_detailed(
                client=client,
                run_attempt_id=self._bindings["run_attempt_id"],
                after_resource_seq=after_resource_seq,
                limit=limit,
            )
        )


class Runs(Resource):
    """Bound Native resource: /runs."""

    def __call__(self, run_id: str) -> Run:
        return Run(self._client, self._bind("run_id", run_id))


class _RunResource(Resource):
    """Bound Native resource: /runs / {run_id}."""

    async def get(self) -> Result[wire.RunResource]:
        """Get Run. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_runs_run_id.asyncio_detailed(client=client, run_id=self._bindings["run_id"])
        )

    @property
    def attempts(self) -> RunsRunIdAttempts:
        return RunsRunIdAttempts(self._client, self._bindings)

    @property
    def environment_mounts(self) -> RunsRunIdEnvironmentMounts:
        return RunsRunIdEnvironmentMounts(self._client, self._bindings)

    @property
    def events(self) -> RunsRunIdEvents:
        return RunsRunIdEvents(self._client, self._bindings)

    async def feedback_receipt(
        self, *, body: wire.WaitingRunFeedbackRequest, idempotency_key: str
    ) -> Result[wire.RunAcceptanceReceipt]:
        """Feedback Run. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_runs_run_id_feedback.asyncio_detailed(
                client=client, run_id=self._bindings["run_id"], body=body, idempotency_key=idempotency_key
            )
        )

    async def fork_receipt(
        self, *, body: wire.ForkRunRequest, idempotency_key: str
    ) -> Result[wire.RunAcceptanceReceipt]:
        """Fork Run. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_runs_run_id_fork.asyncio_detailed(
                client=client, run_id=self._bindings["run_id"], body=body, idempotency_key=idempotency_key
            )
        )

    async def interrupt(self, *, body: wire.InterruptRequest, idempotency_key: str) -> Result[wire.InterruptReceipt]:
        """Interrupt Run. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_runs_run_id_interrupt.asyncio_detailed(
                client=client, run_id=self._bindings["run_id"], body=body, idempotency_key=idempotency_key
            )
        )

    @property
    def items(self) -> RunsRunIdItems:
        return RunsRunIdItems(self._client, self._bindings)

    @property
    def labels(self) -> RunsRunIdLabels:
        return RunsRunIdLabels(self._client, self._bindings)

    @property
    def lineage(self) -> RunsRunIdLineage:
        return RunsRunIdLineage(self._client, self._bindings)

    @property
    def pending_actions(self) -> RunsRunIdPendingActions:
        return RunsRunIdPendingActions(self._client, self._bindings)

    async def retry_receipt(
        self, *, body: wire.RetryRunRequest, idempotency_key: str
    ) -> Result[wire.RunAcceptanceReceipt]:
        """Retry Run. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_runs_run_id_retry.asyncio_detailed(
                client=client, run_id=self._bindings["run_id"], body=body, idempotency_key=idempotency_key
            )
        )

    async def steer_receipt(self, *, body: wire.AgentInput, idempotency_key: str) -> Result[wire.SteerReceipt]:
        """Steer Run. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_runs_run_id_steer.asyncio_detailed(
                client=client, run_id=self._bindings["run_id"], body=body, idempotency_key=idempotency_key
            )
        )

    @property
    def steers(self) -> RunsRunIdSteers:
        return RunsRunIdSteers(self._client, self._bindings)

    @property
    def stream_response(self) -> RunsRunIdStream:
        return RunsRunIdStream(self._client, self._bindings)

    async def continue_receipt(
        self, *, body: wire.ContinueRunRequest, idempotency_key: str
    ) -> Result[wire.RunAcceptanceReceipt]:
        """Continue From Run. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_runs_source_run_id_continue.asyncio_detailed(
                client=client, source_run_id=self._bindings["run_id"], body=body, idempotency_key=idempotency_key
            )
        )


class RunsRunIdAttempts(Resource):
    """Bound Native resource: /runs / {run_id} / attempts."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.RunAttemptCollection]:
        """List Run Attempts. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_runs_run_id_attempts.asyncio_detailed(
                client=client, run_id=self._bindings["run_id"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.RunAttemptCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.RunAttemptResource]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)


class RunsRunIdEnvironmentMounts(Resource):
    """Bound Native resource: /runs / {run_id} / environment-mounts."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.CollectionRunEnvironmentMount]:
        """List Mounts. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_runs_run_id_environment_mounts.asyncio_detailed(
                client=client, run_id=self._bindings["run_id"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.CollectionRunEnvironmentMount]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.RunEnvironmentMount]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    async def create(
        self, *, body: wire.AddEnvironmentMountRequest, idempotency_key: str
    ) -> Result[wire.RunEnvironmentMount]:
        """Add Mount. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_runs_run_id_environment_mounts.asyncio_detailed(
                client=client, run_id=self._bindings["run_id"], body=body, idempotency_key=idempotency_key
            )
        )


class RunsRunIdEvents(Resource):
    """Bound Native resource: /runs / {run_id} / events."""

    async def list(
        self, *, after_resource_seq: int | Unset = UNSET, limit: int | Unset = UNSET
    ) -> Result[wire.ResourceLifecycleEventPage]:
        """List Run Events. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_runs_run_id_events.asyncio_detailed(
                client=client, run_id=self._bindings["run_id"], after_resource_seq=after_resource_seq, limit=limit
            )
        )


class RunsRunIdItems(Resource):
    """Bound Native resource: /runs / {run_id} / items."""

    async def list(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        order: wire.GetRunsRunIdItemsOrder | Unset = UNSET,
    ) -> Result[wire.ItemCollection]:
        """List Run Items. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_runs_run_id_items.asyncio_detailed(
                client=client, run_id=self._bindings["run_id"], limit=limit, cursor=cursor, order=order
            )
        )

    def pages(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        order: wire.GetRunsRunIdItemsOrder | Unset = UNSET,
    ) -> AsyncIterator[Result[wire.ItemCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, order=order, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )


class RunsRunIdLabels(Resource):
    """Bound Native resource: /runs / {run_id} / labels."""

    async def get(self) -> Result[wire.LabelsBody]:
        """Get Run Labels. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_runs_run_id_labels.asyncio_detailed(client=client, run_id=self._bindings["run_id"])
        )

    async def replace(self, *, body: wire.LabelsBody, if_match: str) -> Result[wire.LabelsBody]:
        """Put Run Labels. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: put_runs_run_id_labels.asyncio_detailed(
                client=client, run_id=self._bindings["run_id"], body=body, if_match=if_match
            )
        )


class RunsRunIdLineage(Resource):
    """Bound Native resource: /runs / {run_id} / lineage."""

    async def get(self) -> Result[wire.RunLineage]:
        """Get Run Lineage. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_runs_run_id_lineage.asyncio_detailed(client=client, run_id=self._bindings["run_id"])
        )


class RunsRunIdPendingActions(Resource):
    """Bound Native resource: /runs / {run_id} / pending-actions."""

    async def list(self) -> Result[wire.PendingActionCollection]:
        """List Pending Actions. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_runs_run_id_pending_actions.asyncio_detailed(
                client=client, run_id=self._bindings["run_id"]
            )
        )


class RunsRunIdSteers(Resource):
    """Bound Native resource: /runs / {run_id} / steers."""

    def __call__(self, steer_id: str) -> RunsRunIdSteersSteerId:
        return RunsRunIdSteersSteerId(self._client, self._bind("steer_id", steer_id))


class RunsRunIdSteersSteerId(Resource):
    """Bound Native resource: /runs / {run_id} / steers / {steer_id}."""

    async def get(self) -> Result[wire.SteerStatus]:
        """Get Run Steer. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_runs_run_id_steers_steer_id.asyncio_detailed(
                client=client, run_id=self._bindings["run_id"], steer_id=self._bindings["steer_id"]
            )
        )


class RunsRunIdStream(Resource):
    """Bound Native resource: /runs / {run_id} / stream."""

    async def get(
        self, *, accept: str | Unset | None = UNSET, last_event_id: str | Unset | None = UNSET
    ) -> Result[str]:
        """Stream Run. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_runs_run_id_stream.asyncio_detailed(
                client=client, run_id=self._bindings["run_id"], accept=accept, last_event_id=last_event_id
            )
        )


class ServiceAccounts(Resource):
    """Bound Native resource: /service-accounts."""

    def __call__(self, account_id: str) -> ServiceAccountsAccountId:
        return ServiceAccountsAccountId(self._client, self._bind("account_id", account_id))


class ServiceAccountsAccountId(Resource):
    """Bound Native resource: /service-accounts / {account_id}."""

    async def delete(self, *, body: wire.ExpectedVersion) -> Result[None]:
        """Delete Account. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_service_accounts_account_id.asyncio_detailed(
                client=client, account_id=self._bindings["account_id"], body=body
            )
        )

    async def get(self) -> Result[wire.ServiceAccount]:
        """Account. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_service_accounts_account_id.asyncio_detailed(
                client=client, account_id=self._bindings["account_id"]
            )
        )

    async def update(self, *, body: wire.UpdateServiceAccountRequest) -> Result[wire.ServiceAccount]:
        """Update Account. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: patch_service_accounts_account_id.asyncio_detailed(
                client=client, account_id=self._bindings["account_id"], body=body
            )
        )

    @property
    def api_keys(self) -> ServiceAccountsAccountIdApiKeys:
        return ServiceAccountsAccountIdApiKeys(self._client, self._bindings)


class ServiceAccountsAccountIdApiKeys(Resource):
    """Bound Native resource: /service-accounts / {account_id} / api-keys."""

    async def list(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> Result[wire.PageApiKey]:
        """Account Keys. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_service_accounts_account_id_api_keys.asyncio_detailed(
                client=client, account_id=self._bindings["account_id"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.PageApiKey]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> AsyncIterator[wire.ApiKey]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    async def create(self, *, body: wire.CreateKeyRequest) -> Result[wire.CreatedKey]:
        """Create Account Key. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_service_accounts_account_id_api_keys.asyncio_detailed(
                client=client, account_id=self._bindings["account_id"], body=body
            )
        )


class Sessions(Resource):
    """Bound Native resource: /sessions."""

    def __call__(self, session_id: str) -> Session:
        return Session(self._client, self._bind("session_id", session_id))


class Session(Resource):
    """Bound Native resource: /sessions / {session_id}."""

    @property
    def labels(self) -> SessionsSessionIdLabels:
        return SessionsSessionIdLabels(self._client, self._bindings)

    @property
    def threads(self) -> SessionsSessionIdThreads:
        return SessionsSessionIdThreads(self._client, self._bindings)


class SessionsSessionIdLabels(Resource):
    """Bound Native resource: /sessions / {session_id} / labels."""

    async def get(self) -> Result[wire.LabelsBody]:
        """Get Session Labels. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_sessions_session_id_labels.asyncio_detailed(
                client=client, session_id=self._bindings["session_id"]
            )
        )

    async def replace(self, *, body: wire.LabelsBody, if_match: str) -> Result[wire.LabelsBody]:
        """Put Session Labels. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: put_sessions_session_id_labels.asyncio_detailed(
                client=client, session_id=self._bindings["session_id"], body=body, if_match=if_match
            )
        )


class SessionsSessionIdThreads(Resource):
    """Bound Native resource: /sessions / {session_id} / threads."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET, label: list[str] | Unset = UNSET
    ) -> Result[wire.ThreadCollection]:
        """List Threads. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_sessions_session_id_threads.asyncio_detailed(
                client=client, session_id=self._bindings["session_id"], limit=limit, cursor=cursor, label=label
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET, label: list[str] | Unset = UNSET
    ) -> AsyncIterator[Result[wire.ThreadCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        label = label.copy() if isinstance(label, list) else label
        return pages(
            lambda next_cursor: self.list(limit=limit, label=label, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET, label: list[str] | Unset = UNSET
    ) -> AsyncIterator[wire.ThreadResource]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor, label=label) for item in page.value.items)


class SkillRevisions(Resource):
    """Bound Native resource: /skill-revisions."""

    def __call__(self, skill_revision_id: str) -> SkillRevisionsSkillRevisionId:
        return SkillRevisionsSkillRevisionId(self._client, self._bind("skill_revision_id", skill_revision_id))


class SkillRevisionsSkillRevisionId(Resource):
    """Bound Native resource: /skill-revisions / {skill_revision_id}."""

    async def get(self) -> Result[wire.SkillRevision]:
        """Get Skill Revision. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_skill_revisions_skill_revision_id.asyncio_detailed(
                client=client, skill_revision_id=self._bindings["skill_revision_id"]
            )
        )

    @property
    def content(self) -> SkillRevisionsSkillRevisionIdContent:
        return SkillRevisionsSkillRevisionIdContent(self._client, self._bindings)


class SkillRevisionsSkillRevisionIdContent(Resource):
    """Bound Native resource: /skill-revisions / {skill_revision_id} / content."""

    async def get(self) -> Result[Any]:
        """Get Skill Revision Content. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_skill_revisions_skill_revision_id_content.asyncio_detailed(
                client=client, skill_revision_id=self._bindings["skill_revision_id"]
            )
        )


class SkillUploads(Resource):
    """Bound Native resource: /skill-uploads."""

    def __call__(self, upload_id: str) -> SkillUploadsUploadId:
        return SkillUploadsUploadId(self._client, self._bind("upload_id", upload_id))


class SkillUploadsUploadId(Resource):
    """Bound Native resource: /skill-uploads / {upload_id}."""

    async def delete(self) -> Result[None]:
        """Delete Skill Upload. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_skill_uploads_upload_id.asyncio_detailed(
                client=client, upload_id=self._bindings["upload_id"]
            )
        )

    async def get(self) -> Result[wire.SkillUploadReceipt]:
        """Get Skill Upload. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_skill_uploads_upload_id.asyncio_detailed(
                client=client, upload_id=self._bindings["upload_id"]
            )
        )


class Skills(Resource):
    """Bound Native resource: /skills."""

    def __call__(self, skill_id: str) -> SkillsSkillId:
        return SkillsSkillId(self._client, self._bind("skill_id", skill_id))


class SkillsSkillId(Resource):
    """Bound Native resource: /skills / {skill_id}."""

    async def delete(self, *, if_match: str) -> Result[None]:
        """Delete Skill. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_skills_skill_id.asyncio_detailed(
                client=client, skill_id=self._bindings["skill_id"], if_match=if_match
            )
        )

    async def get(self) -> Result[wire.Skill]:
        """Get Skill. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_skills_skill_id.asyncio_detailed(client=client, skill_id=self._bindings["skill_id"])
        )

    async def update(self, *, body: wire.UpdateSkillRequest, if_match: str) -> Result[wire.Skill]:
        """Update Skill. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: patch_skills_skill_id.asyncio_detailed(
                client=client, skill_id=self._bindings["skill_id"], body=body, if_match=if_match
            )
        )

    @property
    def labels(self) -> SkillsSkillIdLabels:
        return SkillsSkillIdLabels(self._client, self._bindings)

    @property
    def references(self) -> SkillsSkillIdReferences:
        return SkillsSkillIdReferences(self._client, self._bindings)

    @property
    def revisions(self) -> SkillsSkillIdRevisions:
        return SkillsSkillIdRevisions(self._client, self._bindings)


class SkillsSkillIdLabels(Resource):
    """Bound Native resource: /skills / {skill_id} / labels."""

    async def get(self) -> Result[wire.LabelsBody]:
        """Get Skill Labels. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_skills_skill_id_labels.asyncio_detailed(
                client=client, skill_id=self._bindings["skill_id"]
            )
        )

    async def replace(self, *, body: wire.LabelsBody, if_match: str) -> Result[wire.LabelsBody]:
        """Put Skill Labels. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: put_skills_skill_id_labels.asyncio_detailed(
                client=client, skill_id=self._bindings["skill_id"], body=body, if_match=if_match
            )
        )


class SkillsSkillIdReferences(Resource):
    """Bound Native resource: /skills / {skill_id} / references."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.SkillAgentReferenceCollection]:
        """List Skill References. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_skills_skill_id_references.asyncio_detailed(
                client=client, skill_id=self._bindings["skill_id"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.SkillAgentReferenceCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.SkillAgentReference]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)


class SkillsSkillIdRevisions(Resource):
    """Bound Native resource: /skills / {skill_id} / revisions."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.SkillRevisionCollection]:
        """List Skill Revisions. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_skills_skill_id_revisions.asyncio_detailed(
                client=client, skill_id=self._bindings["skill_id"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.SkillRevisionCollection]]:
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
        self, *, body: wire.CreateSkillRevisionRequest, idempotency_key: str
    ) -> Result[wire.SkillPublicationReceipt]:
        """Create Skill Revision. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_skills_skill_id_revisions.asyncio_detailed(
                client=client, skill_id=self._bindings["skill_id"], body=body, idempotency_key=idempotency_key
            )
        )

    def __call__(self, skill_revision_id: str) -> SkillsSkillIdRevisionsSkillRevisionId:
        return SkillsSkillIdRevisionsSkillRevisionId(self._client, self._bind("skill_revision_id", skill_revision_id))


class SkillsSkillIdRevisionsSkillRevisionId(Resource):
    """Bound Native resource: /skills / {skill_id} / revisions / {skill_revision_id}."""

    async def default(self, *, if_match: str) -> Result[wire.Skill]:
        """Set Default Skill Revision. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_skills_skill_id_revisions_skill_revision_id_default.asyncio_detailed(
                client=client,
                skill_id=self._bindings["skill_id"],
                skill_revision_id=self._bindings["skill_revision_id"],
                if_match=if_match,
            )
        )


class Threads(Resource):
    """Bound Native resource: /threads."""

    def __call__(self, thread_id: str) -> Thread:
        return Thread(self._client, self._bind("thread_id", thread_id))


class _ThreadResource(Resource):
    """Bound Native resource: /threads / {thread_id}."""

    async def get(self) -> Result[wire.ThreadResource]:
        """Get Thread. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_threads_thread_id.asyncio_detailed(client=client, thread_id=self._bindings["thread_id"])
        )

    @property
    def labels(self) -> ThreadsThreadIdLabels:
        return ThreadsThreadIdLabels(self._client, self._bindings)

    @property
    def queued_submissions(self) -> ThreadsThreadIdQueuedSubmissions:
        return ThreadsThreadIdQueuedSubmissions(self._client, self._bindings)

    @property
    def runs(self) -> ThreadsThreadIdRuns:
        return ThreadsThreadIdRuns(self._client, self._bindings)


class ThreadsThreadIdLabels(Resource):
    """Bound Native resource: /threads / {thread_id} / labels."""

    async def get(self) -> Result[wire.LabelsBody]:
        """Get Thread Labels. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_threads_thread_id_labels.asyncio_detailed(
                client=client, thread_id=self._bindings["thread_id"]
            )
        )

    async def replace(self, *, body: wire.LabelsBody, if_match: str) -> Result[wire.LabelsBody]:
        """Put Thread Labels. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: put_threads_thread_id_labels.asyncio_detailed(
                client=client, thread_id=self._bindings["thread_id"], body=body, if_match=if_match
            )
        )


class ThreadsThreadIdQueuedSubmissions(Resource):
    """Bound Native resource: /threads / {thread_id} / queued-submissions."""

    async def list(
        self, *, state: wire.QueuedSubmissionState | Unset = UNSET, limit: int | Unset = UNSET
    ) -> Result[wire.QueuedSubmissionCollection]:
        """List Queued Submissions. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_threads_thread_id_queued_submissions.asyncio_detailed(
                client=client, thread_id=self._bindings["thread_id"], state=state, limit=limit
            )
        )

    async def consume(
        self, *, body: wire.ConsumeQueuedSubmissionRequest, idempotency_key: str
    ) -> Result[wire.QueuedSubmissionConsumptionReceipt]:
        """Consume Queued Submission. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_threads_thread_id_queued_submissions_consume.asyncio_detailed(
                client=client, thread_id=self._bindings["thread_id"], body=body, idempotency_key=idempotency_key
            )
        )

    async def reorder(
        self, *, body: wire.ReorderQueuedSubmissionsRequest, idempotency_key: str
    ) -> Result[wire.ThreadQueueMutationReceipt]:
        """Reorder Queued Submissions. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_threads_thread_id_queued_submissions_reorder.asyncio_detailed(
                client=client, thread_id=self._bindings["thread_id"], body=body, idempotency_key=idempotency_key
            )
        )


class ThreadsThreadIdRuns(Resource):
    """Bound Native resource: /threads / {thread_id} / runs."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET, label: list[str] | Unset = UNSET
    ) -> Result[wire.RunCollection]:
        """List Thread Runs. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_threads_thread_id_runs.asyncio_detailed(
                client=client, thread_id=self._bindings["thread_id"], limit=limit, cursor=cursor, label=label
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET, label: list[str] | Unset = UNSET
    ) -> AsyncIterator[Result[wire.RunCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        label = label.copy() if isinstance(label, list) else label
        return pages(
            lambda next_cursor: self.list(limit=limit, label=label, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET, label: list[str] | Unset = UNSET
    ) -> AsyncIterator[wire.RunResource]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor, label=label) for item in page.value.items)

    async def create(
        self, *, body: wire.ThreadRunSubmissionRequest, idempotency_key: str
    ) -> Result[wire.ThreadRunSubmissionReceipt]:
        """Submit Thread Run. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_threads_thread_id_runs.asyncio_detailed(
                client=client, thread_id=self._bindings["thread_id"], body=body, idempotency_key=idempotency_key
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

    async def get(self) -> Result[wire.User]:
        """Current User. One HTTP request; no automatic replay."""
        return await self._call(lambda client: get_users_me.asyncio_detailed(client=client))

    async def update(self, *, body: wire.UpdateProfileRequest, if_match: str) -> Result[wire.User]:
        """Update Profile. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: patch_users_me.asyncio_detailed(client=client, body=body, if_match=if_match)
        )

    @property
    def auth_sessions(self) -> UsersMeAuthSessions:
        return UsersMeAuthSessions(self._client, self._bindings)

    @property
    def avatar(self) -> UsersMeAvatar:
        return UsersMeAvatar(self._client, self._bindings)

    @property
    def email_change(self) -> UsersMeEmailChange:
        return UsersMeEmailChange(self._client, self._bindings)

    async def password(self, *, body: wire.ChangePasswordRequest) -> Result[None]:
        """Change Password. One HTTP request; no automatic replay."""
        return await self._call(lambda client: post_users_me_password.asyncio_detailed(client=client, body=body))

    @property
    def security_activity(self) -> UsersMeSecurityActivity:
        return UsersMeSecurityActivity(self._client, self._bindings)


class UsersMeAuthSessions(Resource):
    """Bound Native resource: /users / me / auth-sessions."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.PageAuthSession]:
        """Sessions. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_users_me_auth_sessions.asyncio_detailed(client=client, limit=limit, cursor=cursor)
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.PageAuthSession]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.AuthSession]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    def __call__(self, session_id: str) -> UsersMeAuthSessionsSessionId:
        return UsersMeAuthSessionsSessionId(self._client, self._bind("session_id", session_id))


class UsersMeAuthSessionsSessionId(Resource):
    """Bound Native resource: /users / me / auth-sessions / {session_id}."""

    async def delete(self) -> Result[None]:
        """Revoke Session. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_users_me_auth_sessions_session_id.asyncio_detailed(
                client=client, session_id=self._bindings["session_id"]
            )
        )


class UsersMeAvatar(Resource):
    """Bound Native resource: /users / me / avatar."""

    async def delete(self, *, if_match: str) -> Result[wire.User]:
        """Delete Avatar. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_users_me_avatar.asyncio_detailed(client=client, if_match=if_match)
        )

    async def replace(self, *, body: File, if_match: str) -> Result[wire.User]:
        """Put Avatar. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: put_users_me_avatar.asyncio_detailed(client=client, body=body, if_match=if_match)
        )


class UsersMeEmailChange(Resource):
    """Bound Native resource: /users / me / email-change."""

    async def create(self, *, body: wire.EmailChangeRequest) -> Result[Any]:
        """Request Email Change. One HTTP request; no automatic replay."""
        return await self._call(lambda client: post_users_me_email_change.asyncio_detailed(client=client, body=body))

    async def complete(self, *, body: wire.CompleteEmailChangeRequest) -> Result[None]:
        """Complete Email Change. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_users_me_email_change_complete.asyncio_detailed(client=client, body=body)
        )


class UsersMeSecurityActivity(Resource):
    """Bound Native resource: /users / me / security-activity."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.PageSecurityEvent]:
        """Personal Security Activity. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_users_me_security_activity.asyncio_detailed(client=client, limit=limit, cursor=cursor)
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.PageSecurityEvent]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.SecurityEvent]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)


class UsersUserId(Resource):
    """Bound Native resource: /users / {user_id}."""

    @property
    def avatar(self) -> UsersUserIdAvatar:
        return UsersUserIdAvatar(self._client, self._bindings)


class UsersUserIdAvatar(Resource):
    """Bound Native resource: /users / {user_id} / avatar."""

    def __call__(self, image_id: str) -> UsersUserIdAvatarImageId:
        return UsersUserIdAvatarImageId(self._client, self._bind("image_id", image_id))


class UsersUserIdAvatarImageId(Resource):
    """Bound Native resource: /users / {user_id} / avatar / {image_id}."""

    async def get(self) -> Result[File]:
        """Get Avatar. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_users_user_id_avatar_image_id.asyncio_detailed(
                client=client, user_id=self._bindings["user_id"], image_id=self._bindings["image_id"]
            )
        )

    def get_stream(self) -> AbstractAsyncContextManager[httpx2.Response]:
        """Unbuffered response; caller checks status and consumes within the context."""
        return self._stream(
            get_users_user_id_avatar_image_id.build_request(
                user_id=self._bindings["user_id"], image_id=self._bindings["image_id"]
            )
        )


class WebProviderTypes(Resource):
    """Bound Native resource: /web-provider-types."""

    async def list(self) -> Result[wire.ProviderMetadataCollectionWebProviderMetadata]:
        """List Types. One HTTP request; no automatic replay."""
        return await self._call(lambda client: get_web_provider_types.asyncio_detailed(client=client))

    def __call__(self, provider_type: str) -> WebProviderTypesProviderType:
        return WebProviderTypesProviderType(self._client, self._bind("provider_type", provider_type))


class WebProviderTypesProviderType(Resource):
    """Bound Native resource: /web-provider-types / {provider_type}."""

    async def get(self) -> Result[wire.WebProviderMetadata]:
        """Get Type. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_web_provider_types_provider_type.asyncio_detailed(
                client=client, provider_type=self._bindings["provider_type"]
            )
        )


class Workspaces(Resource):
    """Bound Native resource: /workspaces."""

    def __call__(self, workspace: str) -> Workspace:
        return Workspace(self._client, self._bind("workspace", workspace))


class Workspace(Resource):
    """Bound Native resource: /workspaces / {workspace}."""

    async def delete(self, *, if_match: str) -> Result[None]:
        """Delete Workspace. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_workspaces_workspace.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], if_match=if_match
            )
        )

    async def get(self) -> Result[wire.Workspace]:
        """Workspace. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"]
            )
        )

    async def update(self, *, body: wire.UpdateResourceProfileRequest, if_match: str) -> Result[wire.Workspace]:
        """Update Workspace. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: patch_workspaces_workspace.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], body=body, if_match=if_match
            )
        )

    @property
    def agents(self) -> WorkspacesWorkspaceAgents:
        return WorkspacesWorkspaceAgents(self._client, self._bindings)

    @property
    def api_keys(self) -> WorkspacesWorkspaceApiKeys:
        return WorkspacesWorkspaceApiKeys(self._client, self._bindings)

    @property
    def application_account_provider_types(self) -> WorkspacesWorkspaceApplicationAccountProviderTypes:
        return WorkspacesWorkspaceApplicationAccountProviderTypes(self._client, self._bindings)

    @property
    def application_accounts(self) -> WorkspacesWorkspaceApplicationAccounts:
        return WorkspacesWorkspaceApplicationAccounts(self._client, self._bindings)

    @property
    def assets(self) -> WorkspacesWorkspaceAssets:
        return WorkspacesWorkspaceAssets(self._client, self._bindings)

    @property
    def bots(self) -> WorkspacesWorkspaceBots:
        return WorkspacesWorkspaceBots(self._client, self._bindings)

    @property
    def configuration_assistant(self) -> WorkspacesWorkspaceConfigurationAssistant:
        return WorkspacesWorkspaceConfigurationAssistant(self._client, self._bindings)

    @property
    def configuration_sessions(self) -> WorkspacesWorkspaceConfigurationSessions:
        return WorkspacesWorkspaceConfigurationSessions(self._client, self._bindings)

    @property
    def connections(self) -> WorkspacesWorkspaceConnections:
        return WorkspacesWorkspaceConnections(self._client, self._bindings)

    @property
    def connector_providers(self) -> WorkspacesWorkspaceConnectorProviders:
        return WorkspacesWorkspaceConnectorProviders(self._client, self._bindings)

    @property
    def device_pairings(self) -> WorkspacesWorkspaceDevicePairings:
        return WorkspacesWorkspaceDevicePairings(self._client, self._bindings)

    @property
    def environment_providers(self) -> WorkspacesWorkspaceEnvironmentProviders:
        return WorkspacesWorkspaceEnvironmentProviders(self._client, self._bindings)

    @property
    def environment_templates(self) -> WorkspacesWorkspaceEnvironmentTemplates:
        return WorkspacesWorkspaceEnvironmentTemplates(self._client, self._bindings)

    @property
    def environments(self) -> WorkspacesWorkspaceEnvironments:
        return WorkspacesWorkspaceEnvironments(self._client, self._bindings)

    @property
    def events(self) -> WorkspacesWorkspaceEvents:
        return WorkspacesWorkspaceEvents(self._client, self._bindings)

    @property
    def hook_subscriptions(self) -> WorkspacesWorkspaceHookSubscriptions:
        return WorkspacesWorkspaceHookSubscriptions(self._client, self._bindings)

    @property
    def icon(self) -> WorkspacesWorkspaceIcon:
        return WorkspacesWorkspaceIcon(self._client, self._bindings)

    @property
    def invitations(self) -> WorkspacesWorkspaceInvitations:
        return WorkspacesWorkspaceInvitations(self._client, self._bindings)

    @property
    def media_understanding_defaults(self) -> WorkspacesWorkspaceMediaUnderstandingDefaults:
        return WorkspacesWorkspaceMediaUnderstandingDefaults(self._client, self._bindings)

    @property
    def members(self) -> WorkspacesWorkspaceMembers:
        return WorkspacesWorkspaceMembers(self._client, self._bindings)

    @property
    def memory_providers(self) -> WorkspacesWorkspaceMemoryProviders:
        return WorkspacesWorkspaceMemoryProviders(self._client, self._bindings)

    @property
    def memory_scopes(self) -> WorkspacesWorkspaceMemoryScopes:
        return WorkspacesWorkspaceMemoryScopes(self._client, self._bindings)

    @property
    def model_catalog(self) -> WorkspacesWorkspaceModelCatalog:
        return WorkspacesWorkspaceModelCatalog(self._client, self._bindings)

    @property
    def model_providers(self) -> WorkspacesWorkspaceModelProviders:
        return WorkspacesWorkspaceModelProviders(self._client, self._bindings)

    @property
    def models(self) -> WorkspacesWorkspaceModels:
        return WorkspacesWorkspaceModels(self._client, self._bindings)

    @property
    def permissions(self) -> WorkspacesWorkspacePermissions:
        return WorkspacesWorkspacePermissions(self._client, self._bindings)

    @property
    def personal_api_keys(self) -> WorkspacesWorkspacePersonalApiKeys:
        return WorkspacesWorkspacePersonalApiKeys(self._client, self._bindings)

    @property
    def role_bindings(self) -> WorkspacesWorkspaceRoleBindings:
        return WorkspacesWorkspaceRoleBindings(self._client, self._bindings)

    @property
    def runs(self) -> WorkspacesWorkspaceRuns:
        return WorkspacesWorkspaceRuns(self._client, self._bindings)

    @property
    def security_audit_events(self) -> WorkspacesWorkspaceSecurityAuditEvents:
        return WorkspacesWorkspaceSecurityAuditEvents(self._client, self._bindings)

    @property
    def service_accounts(self) -> WorkspacesWorkspaceServiceAccounts:
        return WorkspacesWorkspaceServiceAccounts(self._client, self._bindings)

    @property
    def sessions(self) -> WorkspacesWorkspaceSessions:
        return WorkspacesWorkspaceSessions(self._client, self._bindings)

    @property
    def skill_uploads(self) -> WorkspacesWorkspaceSkillUploads:
        return WorkspacesWorkspaceSkillUploads(self._client, self._bindings)

    @property
    def skills(self) -> WorkspacesWorkspaceSkills:
        return WorkspacesWorkspaceSkills(self._client, self._bindings)

    @property
    def threads(self) -> WorkspacesWorkspaceThreads:
        return WorkspacesWorkspaceThreads(self._client, self._bindings)

    @property
    def toolsets(self) -> WorkspacesWorkspaceToolsets:
        return WorkspacesWorkspaceToolsets(self._client, self._bindings)

    @property
    def trace_query(self) -> WorkspacesWorkspaceTraceQuery:
        return WorkspacesWorkspaceTraceQuery(self._client, self._bindings)

    @property
    def traces(self) -> WorkspacesWorkspaceTraces:
        return WorkspacesWorkspaceTraces(self._client, self._bindings)

    @property
    def web_providers(self) -> WorkspacesWorkspaceWebProviders:
        return WorkspacesWorkspaceWebProviders(self._client, self._bindings)


class WorkspacesWorkspaceAgents(Resource):
    """Bound Native resource: /workspaces / {workspace} / agents."""

    async def list(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        enabled: bool | Unset | None = UNSET,
        source: wire.AgentSource | Unset | None = UNSET,
        include_archived: bool | Unset = UNSET,
        label: list[str] | Unset = UNSET,
    ) -> Result[wire.AgentCollection]:
        """List Agents. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_agents.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                limit=limit,
                cursor=cursor,
                enabled=enabled,
                source=source,
                include_archived=include_archived,
                label=label,
            )
        )

    def pages(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        enabled: bool | Unset | None = UNSET,
        source: wire.AgentSource | Unset | None = UNSET,
        include_archived: bool | Unset = UNSET,
        label: list[str] | Unset = UNSET,
    ) -> AsyncIterator[Result[wire.AgentCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        label = label.copy() if isinstance(label, list) else label
        return pages(
            lambda next_cursor: self.list(
                limit=limit,
                enabled=enabled,
                source=source,
                include_archived=include_archived,
                label=label,
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
        enabled: bool | Unset | None = UNSET,
        source: wire.AgentSource | Unset | None = UNSET,
        include_archived: bool | Unset = UNSET,
        label: list[str] | Unset = UNSET,
    ) -> AsyncIterator[wire.Agent]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(
                limit=limit,
                cursor=cursor,
                enabled=enabled,
                source=source,
                include_archived=include_archived,
                label=label,
            )
            for item in page.value.items
        )

    async def create(
        self, *, body: wire.CreateAgentRequest, idempotency_key: str
    ) -> Result[wire.AgentRevisionCreateResult]:
        """Create Agent. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_agents.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], body=body, idempotency_key=idempotency_key
            )
        )

    def __call__(self, agent: str) -> Agent:
        return Agent(self._client, self._bind("agent", agent))


class _AgentResource(Resource):
    """Bound Native resource: /workspaces / {workspace} / agents / {agent}."""

    async def get(self) -> Result[wire.Agent]:
        """Get Agent. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_agents_agent.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], agent=self._bindings["agent"]
            )
        )

    async def update(self, *, body: wire.UpdateAgentRequest, if_match: str) -> Result[wire.Agent]:
        """Update Agent. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: patch_workspaces_workspace_agents_agent.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                agent=self._bindings["agent"],
                body=body,
                if_match=if_match,
            )
        )

    @property
    def avatar(self) -> WorkspacesWorkspaceAgentsAgentAvatar:
        return WorkspacesWorkspaceAgentsAgentAvatar(self._client, self._bindings)

    async def duplicate(
        self, *, body: wire.DuplicateAgentRequest, idempotency_key: str, if_match: str
    ) -> Result[wire.Agent]:
        """Duplicate Agent. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_agents_agent_duplicate.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                agent=self._bindings["agent"],
                body=body,
                idempotency_key=idempotency_key,
                if_match=if_match,
            )
        )

    @property
    def labels(self) -> WorkspacesWorkspaceAgentsAgentLabels:
        return WorkspacesWorkspaceAgentsAgentLabels(self._client, self._bindings)

    @property
    def revisions(self) -> WorkspacesWorkspaceAgentsAgentRevisions:
        return WorkspacesWorkspaceAgentsAgentRevisions(self._client, self._bindings)

    def __call__(
        self, action: wire.PostWorkspacesWorkspaceAgentsAgentActionAction
    ) -> WorkspacesWorkspaceAgentsAgentAction:
        return WorkspacesWorkspaceAgentsAgentAction(self._client, self._bind("action", action))


class WorkspacesWorkspaceAgentsAgentAvatar(Resource):
    """Bound Native resource: /workspaces / {workspace} / agents / {agent} / avatar."""

    async def delete(self, *, if_match: str) -> Result[wire.Agent]:
        """Delete Agent Avatar. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_workspaces_workspace_agents_agent_avatar.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], agent=self._bindings["agent"], if_match=if_match
            )
        )

    async def replace(self, *, body: File, if_match: str) -> Result[wire.Agent]:
        """Put Agent Avatar. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: put_workspaces_workspace_agents_agent_avatar.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                agent=self._bindings["agent"],
                body=body,
                if_match=if_match,
            )
        )

    def __call__(self, image_id: str) -> WorkspacesWorkspaceAgentsAgentAvatarImageId:
        return WorkspacesWorkspaceAgentsAgentAvatarImageId(self._client, self._bind("image_id", image_id))


class WorkspacesWorkspaceAgentsAgentAvatarImageId(Resource):
    """Bound Native resource: /workspaces / {workspace} / agents / {agent} / avatar / {image_id}."""

    async def get(self) -> Result[Any]:
        """Get Agent Avatar. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_agents_agent_avatar_image_id.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                agent=self._bindings["agent"],
                image_id=self._bindings["image_id"],
            )
        )


class WorkspacesWorkspaceAgentsAgentLabels(Resource):
    """Bound Native resource: /workspaces / {workspace} / agents / {agent} / labels."""

    async def get(self) -> Result[wire.LabelsBody]:
        """Get Agent Labels. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_agents_agent_labels.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], agent=self._bindings["agent"]
            )
        )

    async def replace(self, *, body: wire.LabelsBody, if_match: str) -> Result[wire.LabelsBody]:
        """Put Agent Labels. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: put_workspaces_workspace_agents_agent_labels.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                agent=self._bindings["agent"],
                body=body,
                if_match=if_match,
            )
        )


class WorkspacesWorkspaceAgentsAgentRevisions(Resource):
    """Bound Native resource: /workspaces / {workspace} / agents / {agent} / revisions."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.AgentRevisionCollection]:
        """List Agent Revisions. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_agents_agent_revisions.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                agent=self._bindings["agent"],
                limit=limit,
                cursor=cursor,
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.AgentRevisionCollection]]:
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
        self, *, body: wire.CreateAgentRevisionRequest, idempotency_key: str, if_match: str
    ) -> Result[wire.AgentRevisionCreateResult]:
        """Create Agent Revision. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_agents_agent_revisions.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                agent=self._bindings["agent"],
                body=body,
                idempotency_key=idempotency_key,
                if_match=if_match,
            )
        )

    def __call__(self, revision_id: str) -> WorkspacesWorkspaceAgentsAgentRevisionsRevisionId:
        return WorkspacesWorkspaceAgentsAgentRevisionsRevisionId(self._client, self._bind("revision_id", revision_id))


class WorkspacesWorkspaceAgentsAgentRevisionsRevisionId(Resource):
    """Bound Native resource: /workspaces / {workspace} / agents / {agent} / revisions / {revision_id}."""

    async def default(
        self, *, body: wire.SetDefaultAgentRevisionRequest, idempotency_key: str, if_match: str
    ) -> Result[wire.AgentRevisionCreateResult]:
        """Set Default Agent Revision. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_agents_agent_revisions_revision_id_default.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                agent=self._bindings["agent"],
                revision_id=self._bindings["revision_id"],
                body=body,
                idempotency_key=idempotency_key,
                if_match=if_match,
            )
        )


class WorkspacesWorkspaceAgentsAgentAction(Resource):
    """Bound Native resource: /workspaces / {workspace} / agents / {agent} / {action}."""

    async def create(self, *, idempotency_key: str, if_match: str) -> Result[wire.Agent]:
        """Change Agent Lifecycle. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_agents_agent_action.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                agent=self._bindings["agent"],
                action=wire.PostWorkspacesWorkspaceAgentsAgentActionAction(self._bindings["action"]),
                idempotency_key=idempotency_key,
                if_match=if_match,
            )
        )


class WorkspacesWorkspaceApiKeys(Resource):
    """Bound Native resource: /workspaces / {workspace} / api-keys."""

    async def list(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> Result[wire.PageApiKey]:
        """Workspace Member Keys. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_api_keys.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.PageApiKey]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> AsyncIterator[wire.ApiKey]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)


class WorkspacesWorkspaceApplicationAccountProviderTypes(Resource):
    """Bound Native resource: /workspaces / {workspace} / application-account-provider-types."""

    async def list(self) -> Result[wire.AccountProviderDefinitionCollection]:
        """Account Provider Types. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_application_account_provider_types.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"]
            )
        )


class WorkspacesWorkspaceApplicationAccounts(Resource):
    """Bound Native resource: /workspaces / {workspace} / application-accounts."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.AccountCollection]:
        """List Accounts. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_application_accounts.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.AccountCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> AsyncIterator[wire.Account]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    async def create(self, *, body: wire.CreateAccountRequest, idempotency_key: str) -> Result[wire.Account]:
        """Create Account. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_application_accounts.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], body=body, idempotency_key=idempotency_key
            )
        )


class WorkspacesWorkspaceAssets(Resource):
    """Bound Native resource: /workspaces / {workspace} / assets."""

    async def list(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        source_kind: wire.AssetSourceKind | Unset | None = UNSET,
        source_run_id: str | Unset | None = UNSET,
    ) -> Result[wire.AssetCollection]:
        """List Assets. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_assets.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                limit=limit,
                cursor=cursor,
                source_kind=source_kind,
                source_run_id=source_run_id,
            )
        )

    def pages(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        source_kind: wire.AssetSourceKind | Unset | None = UNSET,
        source_run_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.AssetCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(
                limit=limit, source_kind=source_kind, source_run_id=source_run_id, cursor=next_cursor
            ),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        source_kind: wire.AssetSourceKind | Unset | None = UNSET,
        source_run_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.Asset]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(
                limit=limit, cursor=cursor, source_kind=source_kind, source_run_id=source_run_id
            )
            for item in page.value.items
        )

    async def create(
        self, *, body: File, filename: str, media_type: str | Unset | None = UNSET, idempotency_key: str
    ) -> Result[wire.Asset]:
        """Upload Asset. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_assets.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                body=body,
                filename=filename,
                media_type=media_type,
                idempotency_key=idempotency_key,
            )
        )


class WorkspacesWorkspaceBots(Resource):
    """Bound Native resource: /workspaces / {workspace} / bots."""

    async def list(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        platform: wire.GetWorkspacesWorkspaceBotsPlatformType0 | Unset | None = UNSET,
        condition: wire.GetWorkspacesWorkspaceBotsConditionType0 | Unset | None = UNSET,
        search: str | Unset | None = UNSET,
    ) -> Result[wire.BotCollection]:
        """Bot Collection. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_bots.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                limit=limit,
                cursor=cursor,
                platform=platform,
                condition=condition,
                search=search,
            )
        )

    def pages(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        platform: wire.GetWorkspacesWorkspaceBotsPlatformType0 | Unset | None = UNSET,
        condition: wire.GetWorkspacesWorkspaceBotsConditionType0 | Unset | None = UNSET,
        search: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.BotCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(
                limit=limit, platform=platform, condition=condition, search=search, cursor=next_cursor
            ),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        platform: wire.GetWorkspacesWorkspaceBotsPlatformType0 | Unset | None = UNSET,
        condition: wire.GetWorkspacesWorkspaceBotsConditionType0 | Unset | None = UNSET,
        search: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.BotSummary]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(
                limit=limit, cursor=cursor, platform=platform, condition=condition, search=search
            )
            for item in page.value.items
        )

    @property
    def feishu(self) -> WorkspacesWorkspaceBotsFeishu:
        return WorkspacesWorkspaceBotsFeishu(self._client, self._bindings)

    @property
    def github(self) -> WorkspacesWorkspaceBotsGithub:
        return WorkspacesWorkspaceBotsGithub(self._client, self._bindings)


class WorkspacesWorkspaceBotsFeishu(Resource):
    """Bound Native resource: /workspaces / {workspace} / bots / feishu."""

    async def installation(self, *, body: wire.DiscoverFeishuInstallationRequest) -> Result[wire.InstallationInfo]:
        """Discover Feishu Installation. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_bots_feishu_installation.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], body=body
            )
        )


class WorkspacesWorkspaceBotsGithub(Resource):
    """Bound Native resource: /workspaces / {workspace} / bots / github."""

    async def user(self, *, body: wire.DiscoverGitHubUserRequest) -> Result[wire.InstallationInfo]:
        """Discover Github User. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_bots_github_user.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], body=body
            )
        )


class WorkspacesWorkspaceConfigurationAssistant(Resource):
    """Bound Native resource: /workspaces / {workspace} / configuration-assistant."""

    @property
    def readiness(self) -> WorkspacesWorkspaceConfigurationAssistantReadiness:
        return WorkspacesWorkspaceConfigurationAssistantReadiness(self._client, self._bindings)


class WorkspacesWorkspaceConfigurationAssistantReadiness(Resource):
    """Bound Native resource: /workspaces / {workspace} / configuration-assistant / readiness."""

    async def get(self, *, target_agent_id: str | Unset | None = UNSET) -> Result[wire.AssistantReadiness]:
        """Readiness. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_configuration_assistant_readiness.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], target_agent_id=target_agent_id
            )
        )


class WorkspacesWorkspaceConfigurationSessions(Resource):
    """Bound Native resource: /workspaces / {workspace} / configuration-sessions."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.ConfigurationSessionCollection]:
        """List Sessions. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_configuration_sessions.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.ConfigurationSessionCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.ConfigurationSessionView]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    async def create(
        self, *, body: wire.CreateSessionRequest, idempotency_key: str
    ) -> Result[wire.ConfigurationSessionView]:
        """Create Session. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_configuration_sessions.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], body=body, idempotency_key=idempotency_key
            )
        )


class WorkspacesWorkspaceConnections(Resource):
    """Bound Native resource: /workspaces / {workspace} / connections."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.ConnectionCollection]:
        """List Connections. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_connections.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.ConnectionCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> AsyncIterator[wire.Connection]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    async def create(self, *, body: wire.CreateConnectionRequest, idempotency_key: str) -> Result[wire.Connection]:
        """Create Connection. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_connections.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], body=body, idempotency_key=idempotency_key
            )
        )


class WorkspacesWorkspaceConnectorProviders(Resource):
    """Bound Native resource: /workspaces / {workspace} / connector-providers."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.ConnectorProviderCollection]:
        """List Connector Providers. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_connector_providers.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.ConnectorProviderCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.ConnectorProvider]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    async def create(
        self, *, body: wire.CreateConnectorProviderRequest, idempotency_key: str
    ) -> Result[wire.ConnectorProvider]:
        """Create Connector Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_connector_providers.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], body=body, idempotency_key=idempotency_key
            )
        )


class WorkspacesWorkspaceDevicePairings(Resource):
    """Bound Native resource: /workspaces / {workspace} / device-pairings."""

    def __call__(self, pairing_id: str) -> WorkspacesWorkspaceDevicePairingsPairingId:
        return WorkspacesWorkspaceDevicePairingsPairingId(self._client, self._bind("pairing_id", pairing_id))


class WorkspacesWorkspaceDevicePairingsPairingId(Resource):
    """Bound Native resource: /workspaces / {workspace} / device-pairings / {pairing_id}."""

    async def get(self) -> Result[wire.PairingChallenge]:
        """Inspect Pairing. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_device_pairings_pairing_id.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], pairing_id=self._bindings["pairing_id"]
            )
        )

    async def approve(self) -> Result[wire.Environment]:
        """Approve Pairing. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_device_pairings_pairing_id_approve.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], pairing_id=self._bindings["pairing_id"]
            )
        )

    async def reject(self) -> Result[None]:
        """Reject Pairing. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_device_pairings_pairing_id_reject.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], pairing_id=self._bindings["pairing_id"]
            )
        )


class WorkspacesWorkspaceEnvironmentProviders(Resource):
    """Bound Native resource: /workspaces / {workspace} / environment-providers."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.CollectionEnvironmentProviderAccount]:
        """List Providers. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_environment_providers.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.CollectionEnvironmentProviderAccount]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.EnvironmentProviderAccount]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    async def create(self, *, body: wire.CreateProviderRequest) -> Result[wire.EnvironmentProviderAccount]:
        """Create Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_environment_providers.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], body=body
            )
        )


class WorkspacesWorkspaceEnvironmentTemplates(Resource):
    """Bound Native resource: /workspaces / {workspace} / environment-templates."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET, label: list[str] | Unset = UNSET
    ) -> Result[wire.CollectionEnvironmentTemplate]:
        """List Templates. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_environment_templates.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], limit=limit, cursor=cursor, label=label
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET, label: list[str] | Unset = UNSET
    ) -> AsyncIterator[Result[wire.CollectionEnvironmentTemplate]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        label = label.copy() if isinstance(label, list) else label
        return pages(
            lambda next_cursor: self.list(limit=limit, label=label, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET, label: list[str] | Unset = UNSET
    ) -> AsyncIterator[wire.EnvironmentTemplate]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor, label=label) for item in page.value.items)

    async def create(
        self, *, body: wire.CreateTemplateRequest, idempotency_key: str
    ) -> Result[wire.EnvironmentTemplate]:
        """Create Template. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_environment_templates.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], body=body, idempotency_key=idempotency_key
            )
        )


class WorkspacesWorkspaceEnvironments(Resource):
    """Bound Native resource: /workspaces / {workspace} / environments."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET, label: list[str] | Unset = UNSET
    ) -> Result[wire.CollectionEnvironment]:
        """List Environments. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_environments.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], limit=limit, cursor=cursor, label=label
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET, label: list[str] | Unset = UNSET
    ) -> AsyncIterator[Result[wire.CollectionEnvironment]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        label = label.copy() if isinstance(label, list) else label
        return pages(
            lambda next_cursor: self.list(limit=limit, label=label, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET, label: list[str] | Unset = UNSET
    ) -> AsyncIterator[wire.Environment]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor, label=label) for item in page.value.items)

    async def create(
        self, *, body: wire.CreateManagedEnvironmentRequest | wire.RegisterEnvironmentRequest, idempotency_key: str
    ) -> Result[wire.Environment]:
        """Create Environment. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_environments.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], body=body, idempotency_key=idempotency_key
            )
        )


class WorkspacesWorkspaceEvents(Resource):
    """Bound Native resource: /workspaces / {workspace} / events."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.WorkspaceEventPage]:
        """List Workspace Events. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_events.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.WorkspaceEventPage]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.LifecycleEvent]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)


class WorkspacesWorkspaceHookSubscriptions(Resource):
    """Bound Native resource: /workspaces / {workspace} / hook-subscriptions."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.HookSubscriptionCollection]:
        """List Hook Subscriptions. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_hook_subscriptions.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.HookSubscriptionCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.HookSubscription]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    async def create(self, *, body: wire.CreateHookSubscriptionRequest) -> Result[wire.HookSubscription]:
        """Create Hook Subscription. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_hook_subscriptions.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], body=body
            )
        )


class WorkspacesWorkspaceIcon(Resource):
    """Bound Native resource: /workspaces / {workspace} / icon."""

    async def delete(self, *, if_match: str) -> Result[wire.Workspace]:
        """Delete Workspace Icon. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_workspaces_workspace_icon.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], if_match=if_match
            )
        )

    async def replace(self, *, body: File, if_match: str) -> Result[wire.Workspace]:
        """Put Workspace Icon. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: put_workspaces_workspace_icon.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], body=body, if_match=if_match
            )
        )

    def __call__(self, image_id: str) -> WorkspacesWorkspaceIconImageId:
        return WorkspacesWorkspaceIconImageId(self._client, self._bind("image_id", image_id))


class WorkspacesWorkspaceIconImageId(Resource):
    """Bound Native resource: /workspaces / {workspace} / icon / {image_id}."""

    async def get(self) -> Result[File]:
        """Get Workspace Icon. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_icon_image_id.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], image_id=self._bindings["image_id"]
            )
        )

    def get_stream(self) -> AbstractAsyncContextManager[httpx2.Response]:
        """Unbuffered response; caller checks status and consumes within the context."""
        return self._stream(
            get_workspaces_workspace_icon_image_id.build_request(
                workspace=self._bindings["workspace"], image_id=self._bindings["image_id"]
            )
        )


class WorkspacesWorkspaceInvitations(Resource):
    """Bound Native resource: /workspaces / {workspace} / invitations."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.PageInvitation]:
        """Workspace Invitations. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_invitations.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.PageInvitation]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> AsyncIterator[wire.Invitation]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    async def create(self, *, body: wire.InviteWorkspaceRequest) -> Result[wire.InvitationDelivery]:
        """Invite To Workspace. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_invitations.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], body=body
            )
        )


class WorkspacesWorkspaceMediaUnderstandingDefaults(Resource):
    """Bound Native resource: /workspaces / {workspace} / media-understanding-defaults."""

    async def get(self) -> Result[wire.MediaUnderstandingDefaults]:
        """Get Media Understanding Defaults. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_media_understanding_defaults.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"]
            )
        )

    async def replace(
        self, *, body: wire.MediaUnderstandingSelection, if_match: str
    ) -> Result[wire.MediaUnderstandingDefaults]:
        """Replace Media Understanding Defaults. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: put_workspaces_workspace_media_understanding_defaults.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], body=body, if_match=if_match
            )
        )


class WorkspacesWorkspaceMembers(Resource):
    """Bound Native resource: /workspaces / {workspace} / members."""

    async def list(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> Result[wire.PageUser]:
        """Workspace Members. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_members.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.PageUser]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> AsyncIterator[wire.User]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)


class WorkspacesWorkspaceMemoryProviders(Resource):
    """Bound Native resource: /workspaces / {workspace} / memory-providers."""

    async def list(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        type_: str | Unset | None = UNSET,
        enabled: bool | Unset | None = UNSET,
    ) -> Result[wire.MemoryProviderCollection]:
        """List Workspace Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_memory_providers.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                limit=limit,
                cursor=cursor,
                type_=type_,
                enabled=enabled,
            )
        )

    def pages(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        type_: str | Unset | None = UNSET,
        enabled: bool | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.MemoryProviderCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, type_=type_, enabled=enabled, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        type_: str | Unset | None = UNSET,
        enabled: bool | Unset | None = UNSET,
    ) -> AsyncIterator[wire.MemoryProvider]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(limit=limit, cursor=cursor, type_=type_, enabled=enabled)
            for item in page.value.items
        )

    async def create(self, *, body: wire.CreateMemoryProviderRequest) -> Result[wire.MemoryProvider]:
        """Create Workspace Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_memory_providers.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], body=body
            )
        )

    def __call__(self, provider_id: str) -> WorkspacesWorkspaceMemoryProvidersProviderId:
        return WorkspacesWorkspaceMemoryProvidersProviderId(self._client, self._bind("provider_id", provider_id))


class WorkspacesWorkspaceMemoryProvidersProviderId(Resource):
    """Bound Native resource: /workspaces / {workspace} / memory-providers / {provider_id}."""

    async def get(self) -> Result[wire.MemoryProvider]:
        """Get Workspace Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_memory_providers_provider_id.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], provider_id=self._bindings["provider_id"]
            )
        )

    async def update(self, *, body: wire.UpdateMemoryProviderRequest, if_match: str) -> Result[wire.MemoryProvider]:
        """Update Workspace Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: patch_workspaces_workspace_memory_providers_provider_id.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                provider_id=self._bindings["provider_id"],
                body=body,
                if_match=if_match,
            )
        )

    @property
    def memories(self) -> WorkspacesWorkspaceMemoryProvidersProviderIdMemories:
        return WorkspacesWorkspaceMemoryProvidersProviderIdMemories(self._client, self._bindings)

    @property
    def memory_access(self) -> WorkspacesWorkspaceMemoryProvidersProviderIdMemoryAccess:
        return WorkspacesWorkspaceMemoryProvidersProviderIdMemoryAccess(self._client, self._bindings)

    @property
    def references(self) -> WorkspacesWorkspaceMemoryProvidersProviderIdReferences:
        return WorkspacesWorkspaceMemoryProvidersProviderIdReferences(self._client, self._bindings)


class WorkspacesWorkspaceMemoryProvidersProviderIdMemories(Resource):
    """Bound Native resource: /workspaces / {workspace} / memory-providers / {provider_id} / memories."""

    async def list(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        scope: wire.MemoryScope,
        subject_id: str | Unset | None = UNSET,
    ) -> Result[wire.MemoryCollection]:
        """List Memories. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_memory_providers_provider_id_memories.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                provider_id=self._bindings["provider_id"],
                limit=limit,
                cursor=cursor,
                scope=scope,
                subject_id=subject_id,
            )
        )

    async def create(
        self, *, body: wire.MemoryWrite, scope: wire.MemoryScope, subject_id: str | Unset | None = UNSET
    ) -> Result[wire.Memory]:
        """Add Memory. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_memory_providers_provider_id_memories.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                provider_id=self._bindings["provider_id"],
                body=body,
                scope=scope,
                subject_id=subject_id,
            )
        )

    async def search(
        self, *, body: wire.MemorySearch, scope: wire.MemoryScope, subject_id: str | Unset | None = UNSET
    ) -> Result[wire.MemoryCollection]:
        """Search Memories. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_memory_providers_provider_id_memories_search.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                provider_id=self._bindings["provider_id"],
                body=body,
                scope=scope,
                subject_id=subject_id,
            )
        )

    def __call__(self, memory_id: str) -> WorkspacesWorkspaceMemoryProvidersProviderIdMemoriesMemoryId:
        return WorkspacesWorkspaceMemoryProvidersProviderIdMemoriesMemoryId(
            self._client, self._bind("memory_id", memory_id)
        )


class WorkspacesWorkspaceMemoryProvidersProviderIdMemoriesMemoryId(Resource):
    """Bound Native resource: /workspaces / {workspace} / memory-providers / {provider_id} / memories / {memory_id}."""

    async def delete(self, *, scope: wire.MemoryScope, subject_id: str | Unset | None = UNSET) -> Result[None]:
        """Delete Memory. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_workspaces_workspace_memory_providers_provider_id_memories_memory_id.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                provider_id=self._bindings["provider_id"],
                memory_id=self._bindings["memory_id"],
                scope=scope,
                subject_id=subject_id,
            )
        )

    async def get(self, *, scope: wire.MemoryScope, subject_id: str | Unset | None = UNSET) -> Result[wire.Memory]:
        """Get Memory. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_memory_providers_provider_id_memories_memory_id.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                provider_id=self._bindings["provider_id"],
                memory_id=self._bindings["memory_id"],
                scope=scope,
                subject_id=subject_id,
            )
        )

    async def replace(
        self, *, body: wire.MemoryWrite, scope: wire.MemoryScope, subject_id: str | Unset | None = UNSET
    ) -> Result[wire.Memory]:
        """Update Memory. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: put_workspaces_workspace_memory_providers_provider_id_memories_memory_id.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                provider_id=self._bindings["provider_id"],
                memory_id=self._bindings["memory_id"],
                body=body,
                scope=scope,
                subject_id=subject_id,
            )
        )


class WorkspacesWorkspaceMemoryProvidersProviderIdMemoryAccess(Resource):
    """Bound Native resource: /workspaces / {workspace} / memory-providers / {provider_id} / memory-access."""

    async def get(
        self, *, scope: wire.MemoryScope, subject_id: str | Unset | None = UNSET
    ) -> Result[wire.MemoryAccess]:
        """Get Memory Access. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_memory_providers_provider_id_memory_access.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                provider_id=self._bindings["provider_id"],
                scope=scope,
                subject_id=subject_id,
            )
        )


class WorkspacesWorkspaceMemoryProvidersProviderIdReferences(Resource):
    """Bound Native resource: /workspaces / {workspace} / memory-providers / {provider_id} / references."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.MemoryProviderReferenceCollection]:
        """References Workspace Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_memory_providers_provider_id_references.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                provider_id=self._bindings["provider_id"],
                limit=limit,
                cursor=cursor,
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.MemoryProviderReferenceCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.MemoryProviderReference]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)


class WorkspacesWorkspaceMemoryScopes(Resource):
    """Bound Native resource: /workspaces / {workspace} / memory-scopes."""

    async def list(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        environment_id: str | Unset | None = UNSET,
        subject_id: str | Unset | None = UNSET,
        conversation_scope_id: str | Unset | None = UNSET,
    ) -> Result[wire.StoredScopeCollection]:
        """Scopes. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_memory_scopes.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                limit=limit,
                cursor=cursor,
                environment_id=environment_id,
                subject_id=subject_id,
                conversation_scope_id=conversation_scope_id,
            )
        )

    def pages(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        environment_id: str | Unset | None = UNSET,
        subject_id: str | Unset | None = UNSET,
        conversation_scope_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.StoredScopeCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(
                limit=limit,
                environment_id=environment_id,
                subject_id=subject_id,
                conversation_scope_id=conversation_scope_id,
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
        environment_id: str | Unset | None = UNSET,
        subject_id: str | Unset | None = UNSET,
        conversation_scope_id: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.StoredMemoryScope]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(
                limit=limit,
                cursor=cursor,
                environment_id=environment_id,
                subject_id=subject_id,
                conversation_scope_id=conversation_scope_id,
            )
            for item in page.value.items
        )

    def __call__(self, scope_id: str) -> WorkspacesWorkspaceMemoryScopesScopeId:
        return WorkspacesWorkspaceMemoryScopesScopeId(self._client, self._bind("scope_id", scope_id))


class WorkspacesWorkspaceMemoryScopesScopeId(Resource):
    """Bound Native resource: /workspaces / {workspace} / memory-scopes / {scope_id}."""

    @property
    def documents(self) -> WorkspacesWorkspaceMemoryScopesScopeIdDocuments:
        return WorkspacesWorkspaceMemoryScopesScopeIdDocuments(self._client, self._bindings)

    @property
    def organization(self) -> WorkspacesWorkspaceMemoryScopesScopeIdOrganization:
        return WorkspacesWorkspaceMemoryScopesScopeIdOrganization(self._client, self._bindings)


class WorkspacesWorkspaceMemoryScopesScopeIdDocuments(Resource):
    """Bound Native resource: /workspaces / {workspace} / memory-scopes / {scope_id} / documents."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.FileDocumentCollection]:
        """Listing. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_memory_scopes_scope_id_documents.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                scope_id=self._bindings["scope_id"],
                limit=limit,
                cursor=cursor,
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.FileDocumentCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.DocumentNavigation]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    async def create(self, *, body: wire.DocumentInput, idempotency_key: str) -> Result[wire.ManagedDocumentMutation]:
        """Create. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_memory_scopes_scope_id_documents.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                scope_id=self._bindings["scope_id"],
                body=body,
                idempotency_key=idempotency_key,
            )
        )

    def __call__(self, document_id: str) -> WorkspacesWorkspaceMemoryScopesScopeIdDocumentsDocumentId:
        return WorkspacesWorkspaceMemoryScopesScopeIdDocumentsDocumentId(
            self._client, self._bind("document_id", document_id)
        )


class WorkspacesWorkspaceMemoryScopesScopeIdDocumentsDocumentId(Resource):
    """Bound Native resource: /workspaces / {workspace} / memory-scopes / {scope_id} / documents / {document_id}."""

    async def delete(self) -> Result[None]:
        """Remove. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: delete_workspaces_workspace_memory_scopes_scope_id_documents_document_id.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                scope_id=self._bindings["scope_id"],
                document_id=self._bindings["document_id"],
            )
        )

    async def get(self, *, version: int | Unset | None = UNSET) -> Result[wire.ManagedMemoryDocument]:
        """Read. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_memory_scopes_scope_id_documents_document_id.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                scope_id=self._bindings["scope_id"],
                document_id=self._bindings["document_id"],
                version=version,
            )
        )

    async def replace(
        self, *, body: wire.ReviseDocument, idempotency_key: str, if_match: str
    ) -> Result[wire.ManagedDocumentMutation]:
        """Revise. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: put_workspaces_workspace_memory_scopes_scope_id_documents_document_id.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                scope_id=self._bindings["scope_id"],
                document_id=self._bindings["document_id"],
                body=body,
                idempotency_key=idempotency_key,
                if_match=if_match,
            )
        )

    @property
    def revisions(self) -> WorkspacesWorkspaceMemoryScopesScopeIdDocumentsDocumentIdRevisions:
        return WorkspacesWorkspaceMemoryScopesScopeIdDocumentsDocumentIdRevisions(self._client, self._bindings)

    @property
    def toc(self) -> WorkspacesWorkspaceMemoryScopesScopeIdDocumentsDocumentIdToc:
        return WorkspacesWorkspaceMemoryScopesScopeIdDocumentsDocumentIdToc(self._client, self._bindings)


class WorkspacesWorkspaceMemoryScopesScopeIdDocumentsDocumentIdRevisions(Resource):
    """Bound Native resource: /workspaces / {workspace} / memory-scopes / {scope_id} / documents / {document_id} / revisions."""

    async def get(
        self, *, before_version: int | Unset | None = UNSET, limit: int | Unset = UNSET
    ) -> Result[list[wire.ManagedMemoryDocument]]:
        """History. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: (
                get_workspaces_workspace_memory_scopes_scope_id_documents_document_id_revisions.asyncio_detailed(
                    client=client,
                    workspace=self._bindings["workspace"],
                    scope_id=self._bindings["scope_id"],
                    document_id=self._bindings["document_id"],
                    before_version=before_version,
                    limit=limit,
                )
            )
        )


class WorkspacesWorkspaceMemoryScopesScopeIdDocumentsDocumentIdToc(Resource):
    """Bound Native resource: /workspaces / {workspace} / memory-scopes / {scope_id} / documents / {document_id} / toc."""

    async def get(self, *, version: int | Unset | None = UNSET) -> Result[list[wire.DocumentHeading]]:
        """Toc. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_memory_scopes_scope_id_documents_document_id_toc.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                scope_id=self._bindings["scope_id"],
                document_id=self._bindings["document_id"],
                version=version,
            )
        )


class WorkspacesWorkspaceMemoryScopesScopeIdOrganization(Resource):
    """Bound Native resource: /workspaces / {workspace} / memory-scopes / {scope_id} / organization."""

    async def get(self) -> Result[list[wire.OrganizationStatus]]:
        """Organization Status. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_memory_scopes_scope_id_organization.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], scope_id=self._bindings["scope_id"]
            )
        )


class WorkspacesWorkspaceModelCatalog(Resource):
    """Bound Native resource: /workspaces / {workspace} / model-catalog."""

    async def list(self) -> Result[wire.ModelCatalogCollection]:
        """List Model Catalog. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_model_catalog.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"]
            )
        )


class WorkspacesWorkspaceModelProviders(Resource):
    """Bound Native resource: /workspaces / {workspace} / model-providers."""

    async def list(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        name: str | Unset | None = UNSET,
        provider_type: str | Unset | None = UNSET,
        enabled: bool | Unset | None = UNSET,
    ) -> Result[wire.ModelProviderCollection]:
        """List Model Providers. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_model_providers.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                limit=limit,
                cursor=cursor,
                name=name,
                provider_type=provider_type,
                enabled=enabled,
            )
        )

    def pages(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        name: str | Unset | None = UNSET,
        provider_type: str | Unset | None = UNSET,
        enabled: bool | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.ModelProviderCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(
                limit=limit, name=name, provider_type=provider_type, enabled=enabled, cursor=next_cursor
            ),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        name: str | Unset | None = UNSET,
        provider_type: str | Unset | None = UNSET,
        enabled: bool | Unset | None = UNSET,
    ) -> AsyncIterator[wire.ModelProvider]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(
                limit=limit, cursor=cursor, name=name, provider_type=provider_type, enabled=enabled
            )
            for item in page.value.items
        )

    async def create(self, *, body: wire.CreateModelProviderRequest) -> Result[wire.ModelProvider]:
        """Create Model Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_model_providers.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], body=body
            )
        )

    def __call__(self, provider_id: str) -> WorkspacesWorkspaceModelProvidersProviderId:
        return WorkspacesWorkspaceModelProvidersProviderId(self._client, self._bind("provider_id", provider_id))


class WorkspacesWorkspaceModelProvidersProviderId(Resource):
    """Bound Native resource: /workspaces / {workspace} / model-providers / {provider_id}."""

    async def get(self) -> Result[wire.ModelProvider]:
        """Get Model Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_model_providers_provider_id.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], provider_id=self._bindings["provider_id"]
            )
        )

    async def update(self, *, body: wire.UpdateModelProviderRequest, if_match: str) -> Result[wire.ModelProvider]:
        """Update Model Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: patch_workspaces_workspace_model_providers_provider_id.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                provider_id=self._bindings["provider_id"],
                body=body,
                if_match=if_match,
            )
        )

    async def test(self) -> Result[wire.ModelConnectionTestResult]:
        """Test Model Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_model_providers_provider_id_test.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], provider_id=self._bindings["provider_id"]
            )
        )


class WorkspacesWorkspaceModels(Resource):
    """Bound Native resource: /workspaces / {workspace} / models."""

    async def list(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        query: str | Unset | None = UNSET,
        provider_id: str | Unset | None = UNSET,
        enabled: bool | Unset | None = UNSET,
        scope: wire.GetWorkspacesWorkspaceModelsScopeType0 | Unset | None = UNSET,
    ) -> Result[wire.ModelCollection]:
        """List Models. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_models.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                limit=limit,
                cursor=cursor,
                query=query,
                provider_id=provider_id,
                enabled=enabled,
                scope=scope,
            )
        )

    def pages(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        query: str | Unset | None = UNSET,
        provider_id: str | Unset | None = UNSET,
        enabled: bool | Unset | None = UNSET,
        scope: wire.GetWorkspacesWorkspaceModelsScopeType0 | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.ModelCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(
                limit=limit, query=query, provider_id=provider_id, enabled=enabled, scope=scope, cursor=next_cursor
            ),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        query: str | Unset | None = UNSET,
        provider_id: str | Unset | None = UNSET,
        enabled: bool | Unset | None = UNSET,
        scope: wire.GetWorkspacesWorkspaceModelsScopeType0 | Unset | None = UNSET,
    ) -> AsyncIterator[wire.Model]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(
                limit=limit, cursor=cursor, query=query, provider_id=provider_id, enabled=enabled, scope=scope
            )
            for item in page.value.items
        )

    async def create(self, *, body: wire.CreateModelRequest) -> Result[wire.Model]:
        """Create Model. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_models.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], body=body
            )
        )

    def __call__(self, model_id: str) -> WorkspacesWorkspaceModelsModelId:
        return WorkspacesWorkspaceModelsModelId(self._client, self._bind("model_id", model_id))


class WorkspacesWorkspaceModelsModelId(Resource):
    """Bound Native resource: /workspaces / {workspace} / models / {model_id}."""

    async def get(self) -> Result[wire.Model]:
        """Get Model. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_models_model_id.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], model_id=self._bindings["model_id"]
            )
        )

    async def update(self, *, body: wire.UpdateModelRequest, if_match: str) -> Result[wire.Model]:
        """Update Model. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: patch_workspaces_workspace_models_model_id.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                model_id=self._bindings["model_id"],
                body=body,
                if_match=if_match,
            )
        )

    async def test(
        self, *, body: wire.ModelTestRequest | Unset | None = UNSET
    ) -> Result[wire.ModelConnectionTestResult]:
        """Test Model. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_models_model_id_test.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], model_id=self._bindings["model_id"], body=body
            )
        )


class WorkspacesWorkspacePermissions(Resource):
    """Bound Native resource: /workspaces / {workspace} / permissions."""

    async def get(self) -> Result[wire.Permissions]:
        """Workspace Permissions. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_permissions.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"]
            )
        )


class WorkspacesWorkspacePersonalApiKeys(Resource):
    """Bound Native resource: /workspaces / {workspace} / personal-api-keys."""

    async def list(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> Result[wire.PageApiKey]:
        """Personal Keys. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_personal_api_keys.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.PageApiKey]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET) -> AsyncIterator[wire.ApiKey]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    async def create(self, *, body: wire.CreateKeyRequest) -> Result[wire.CreatedKey]:
        """Create Personal Key. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_personal_api_keys.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], body=body
            )
        )


class WorkspacesWorkspaceRoleBindings(Resource):
    """Bound Native resource: /workspaces / {workspace} / role-bindings."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.PageRoleBinding]:
        """Workspace Roles. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_role_bindings.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.PageRoleBinding]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.RoleBinding]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    async def create(self, *, body: wire.SetRoleRequest) -> Result[wire.RoleBinding]:
        """Add Workspace Member. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_role_bindings.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], body=body
            )
        )


class WorkspacesWorkspaceRuns(Resource):
    """Bound Native resource: /workspaces / {workspace} / runs."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET, label: list[str] | Unset = UNSET
    ) -> Result[wire.RunCollection]:
        """List Workspace Runs. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_runs.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], limit=limit, cursor=cursor, label=label
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET, label: list[str] | Unset = UNSET
    ) -> AsyncIterator[Result[wire.RunCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        label = label.copy() if isinstance(label, list) else label
        return pages(
            lambda next_cursor: self.list(limit=limit, label=label, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET, label: list[str] | Unset = UNSET
    ) -> AsyncIterator[wire.RunResource]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor, label=label) for item in page.value.items)

    async def create(self, *, body: wire.StartRunRequest, idempotency_key: str) -> Result[wire.RunAcceptanceReceipt]:
        """Start Run. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_runs.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], body=body, idempotency_key=idempotency_key
            )
        )


class WorkspacesWorkspaceSecurityAuditEvents(Resource):
    """Bound Native resource: /workspaces / {workspace} / security-audit-events."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.PageSecurityEvent]:
        """Workspace Security Events. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_security_audit_events.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.PageSecurityEvent]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.SecurityEvent]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)


class WorkspacesWorkspaceServiceAccounts(Resource):
    """Bound Native resource: /workspaces / {workspace} / service-accounts."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.PageServiceAccount]:
        """Accounts. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_service_accounts.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], limit=limit, cursor=cursor
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.PageServiceAccount]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.ServiceAccount]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)

    async def create(self, *, body: wire.CreateServiceAccountRequest) -> Result[wire.ServiceAccount]:
        """Create Account. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_service_accounts.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], body=body
            )
        )


class WorkspacesWorkspaceSessions(Resource):
    """Bound Native resource: /workspaces / {workspace} / sessions."""

    async def list(
        self,
        *,
        q: str | Unset | None = UNSET,
        agent_id: str | Unset | None = UNSET,
        status: list[wire.RunStatus] | Unset = UNSET,
        trigger_type: list[str] | Unset = UNSET,
        updated_after: datetime.datetime | Unset | None = UNSET,
        updated_before: datetime.datetime | Unset | None = UNSET,
        label: list[str] | Unset = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> Result[wire.SessionCollection]:
        """List Sessions. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_sessions.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                q=q,
                agent_id=agent_id,
                status=status,
                trigger_type=trigger_type,
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
        trigger_type: list[str] | Unset = UNSET,
        updated_after: datetime.datetime | Unset | None = UNSET,
        updated_before: datetime.datetime | Unset | None = UNSET,
        label: list[str] | Unset = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.SessionCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        status = status.copy() if isinstance(status, list) else status
        trigger_type = trigger_type.copy() if isinstance(trigger_type, list) else trigger_type
        label = label.copy() if isinstance(label, list) else label
        return pages(
            lambda next_cursor: self.list(
                q=q,
                agent_id=agent_id,
                status=status,
                trigger_type=trigger_type,
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
        trigger_type: list[str] | Unset = UNSET,
        updated_after: datetime.datetime | Unset | None = UNSET,
        updated_before: datetime.datetime | Unset | None = UNSET,
        label: list[str] | Unset = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
    ) -> AsyncIterator[wire.SessionResource]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(
                q=q,
                agent_id=agent_id,
                status=status,
                trigger_type=trigger_type,
                updated_after=updated_after,
                updated_before=updated_before,
                label=label,
                limit=limit,
                cursor=cursor,
            )
            for item in page.value.items
        )


class WorkspacesWorkspaceSkillUploads(Resource):
    """Bound Native resource: /workspaces / {workspace} / skill-uploads."""

    async def create(self, *, body: File, idempotency_key: str) -> Result[wire.SkillUploadReceipt]:
        """Stage Skill Upload. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_skill_uploads.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], body=body, idempotency_key=idempotency_key
            )
        )


class WorkspacesWorkspaceSkills(Resource):
    """Bound Native resource: /workspaces / {workspace} / skills."""

    async def list(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        q: str | Unset | None = UNSET,
        source_kind: wire.GetWorkspacesWorkspaceSkillsSourceKindType0 | Unset | None = UNSET,
        label: list[str] | Unset = UNSET,
    ) -> Result[wire.SkillCollection]:
        """List Skills. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_skills.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                limit=limit,
                cursor=cursor,
                q=q,
                source_kind=source_kind,
                label=label,
            )
        )

    def pages(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        q: str | Unset | None = UNSET,
        source_kind: wire.GetWorkspacesWorkspaceSkillsSourceKindType0 | Unset | None = UNSET,
        label: list[str] | Unset = UNSET,
    ) -> AsyncIterator[Result[wire.SkillCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        label = label.copy() if isinstance(label, list) else label
        return pages(
            lambda next_cursor: self.list(limit=limit, q=q, source_kind=source_kind, label=label, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        q: str | Unset | None = UNSET,
        source_kind: wire.GetWorkspacesWorkspaceSkillsSourceKindType0 | Unset | None = UNSET,
        label: list[str] | Unset = UNSET,
    ) -> AsyncIterator[wire.SkillListItem]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(limit=limit, cursor=cursor, q=q, source_kind=source_kind, label=label)
            for item in page.value.items
        )

    async def create(
        self, *, body: wire.CreateSkillRequest, idempotency_key: str
    ) -> Result[wire.SkillPublicationReceipt]:
        """Create Skill. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_skills.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], body=body, idempotency_key=idempotency_key
            )
        )

    def __call__(self, skill_key: str) -> WorkspacesWorkspaceSkillsSkillKey:
        return WorkspacesWorkspaceSkillsSkillKey(self._client, self._bind("skill_key", skill_key))


class WorkspacesWorkspaceSkillsSkillKey(Resource):
    """Bound Native resource: /workspaces / {workspace} / skills / {skill_key}."""

    async def get(self) -> Result[wire.Skill]:
        """Get Skill By Key. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_skills_skill_key.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], skill_key=self._bindings["skill_key"]
            )
        )


class WorkspacesWorkspaceThreads(Resource):
    """Bound Native resource: /workspaces / {workspace} / threads."""

    async def create(self, *, body: wire.CreateThreadRequest, idempotency_key: str) -> Result[wire.Thread]:
        """Create Thread. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_threads.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], body=body, idempotency_key=idempotency_key
            )
        )


class WorkspacesWorkspaceToolsets(Resource):
    """Bound Native resource: /workspaces / {workspace} / toolsets."""

    async def get(self) -> Result[wire.ToolsetCatalog]:
        """Get Toolsets. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_toolsets.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"]
            )
        )

    async def validate(self, *, body: wire.ToolsetCandidate) -> Result[wire.ToolsetCandidateResult]:
        """Validate Toolsets. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_toolsets_validate.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], body=body
            )
        )


class WorkspacesWorkspaceTraceQuery(Resource):
    """Bound Native resource: /workspaces / {workspace} / trace-query."""

    async def get(self) -> Result[wire.TraceQueryDescriptor]:
        """Get Trace Query. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_trace_query.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"]
            )
        )


class WorkspacesWorkspaceTraces(Resource):
    """Bound Native resource: /workspaces / {workspace} / traces."""

    async def list(
        self,
        *,
        from_: datetime.datetime | Unset | None = UNSET,
        to: datetime.datetime | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        query: str | Unset | None = UNSET,
        search_in: wire.SearchIn | Unset | None = UNSET,
        session_id: str | Unset | None = UNSET,
        thread_id: str | Unset | None = UNSET,
        run_id: str | Unset | None = UNSET,
        run_attempt_id: str | Unset | None = UNSET,
        metadata: list[str] | Unset | None = UNSET,
        view: wire.TraceView | Unset = UNSET,
    ) -> Result[wire.TraceCollection]:
        """List Traces. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_traces.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                from_=from_,
                to=to,
                limit=limit,
                cursor=cursor,
                query=query,
                search_in=search_in,
                session_id=session_id,
                thread_id=thread_id,
                run_id=run_id,
                run_attempt_id=run_attempt_id,
                metadata=metadata,
                view=view,
            )
        )

    def pages(
        self,
        *,
        from_: datetime.datetime | Unset | None = UNSET,
        to: datetime.datetime | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        query: str | Unset | None = UNSET,
        search_in: wire.SearchIn | Unset | None = UNSET,
        session_id: str | Unset | None = UNSET,
        thread_id: str | Unset | None = UNSET,
        run_id: str | Unset | None = UNSET,
        run_attempt_id: str | Unset | None = UNSET,
        metadata: list[str] | Unset | None = UNSET,
        view: wire.TraceView | Unset = UNSET,
    ) -> AsyncIterator[Result[wire.TraceCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        metadata = metadata.copy() if isinstance(metadata, list) else metadata
        return pages(
            lambda next_cursor: self.list(
                from_=from_,
                to=to,
                limit=limit,
                query=query,
                search_in=search_in,
                session_id=session_id,
                thread_id=thread_id,
                run_id=run_id,
                run_attempt_id=run_attempt_id,
                metadata=metadata,
                view=view,
                cursor=next_cursor,
            ),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        from_: datetime.datetime | Unset | None = UNSET,
        to: datetime.datetime | Unset | None = UNSET,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        query: str | Unset | None = UNSET,
        search_in: wire.SearchIn | Unset | None = UNSET,
        session_id: str | Unset | None = UNSET,
        thread_id: str | Unset | None = UNSET,
        run_id: str | Unset | None = UNSET,
        run_attempt_id: str | Unset | None = UNSET,
        metadata: list[str] | Unset | None = UNSET,
        view: wire.TraceView | Unset = UNSET,
    ) -> AsyncIterator[wire.Trace]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(
                from_=from_,
                to=to,
                limit=limit,
                cursor=cursor,
                query=query,
                search_in=search_in,
                session_id=session_id,
                thread_id=thread_id,
                run_id=run_id,
                run_attempt_id=run_attempt_id,
                metadata=metadata,
                view=view,
            )
            for item in page.value.items
        )

    def __call__(self, trace_id: str) -> WorkspacesWorkspaceTracesTraceId:
        return WorkspacesWorkspaceTracesTraceId(self._client, self._bind("trace_id", trace_id))


class WorkspacesWorkspaceTracesTraceId(Resource):
    """Bound Native resource: /workspaces / {workspace} / traces / {trace_id}."""

    async def get(self, *, view: wire.TraceView | Unset = UNSET) -> Result[wire.Trace]:
        """Get Trace. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_traces_trace_id.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], trace_id=self._bindings["trace_id"], view=view
            )
        )

    @property
    def observations(self) -> WorkspacesWorkspaceTracesTraceIdObservations:
        return WorkspacesWorkspaceTracesTraceIdObservations(self._client, self._bindings)


class WorkspacesWorkspaceTracesTraceIdObservations(Resource):
    """Bound Native resource: /workspaces / {workspace} / traces / {trace_id} / observations."""

    async def list(
        self, *, view: wire.TraceView | Unset = UNSET, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.ObservationCollection]:
        """List Trace Observations. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_traces_trace_id_observations.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                trace_id=self._bindings["trace_id"],
                view=view,
                limit=limit,
                cursor=cursor,
            )
        )

    def pages(
        self, *, view: wire.TraceView | Unset = UNSET, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.ObservationCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(view=view, limit=limit, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self, *, view: wire.TraceView | Unset = UNSET, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.Observation]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(view=view, limit=limit, cursor=cursor) for item in page.value.items)


class WorkspacesWorkspaceWebProviders(Resource):
    """Bound Native resource: /workspaces / {workspace} / web-providers."""

    async def list(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        type_: str | Unset | None = UNSET,
        enabled: bool | Unset | None = UNSET,
    ) -> Result[wire.WebProviderCollection]:
        """List Workspace Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_web_providers.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                limit=limit,
                cursor=cursor,
                type_=type_,
                enabled=enabled,
            )
        )

    def pages(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        type_: str | Unset | None = UNSET,
        enabled: bool | Unset | None = UNSET,
    ) -> AsyncIterator[Result[wire.WebProviderCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, type_=type_, enabled=enabled, cursor=next_cursor),
            lambda value: value.next_cursor,
            cursor,
        )

    def iter(
        self,
        *,
        limit: int | Unset = UNSET,
        cursor: str | Unset | None = UNSET,
        type_: str | Unset | None = UNSET,
        enabled: bool | Unset | None = UNSET,
    ) -> AsyncIterator[wire.WebProvider]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (
            item
            async for page in self.pages(limit=limit, cursor=cursor, type_=type_, enabled=enabled)
            for item in page.value.items
        )

    async def create(self, *, body: wire.CreateWebProviderRequest) -> Result[wire.WebProvider]:
        """Create Workspace Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_web_providers.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], body=body
            )
        )

    def __call__(self, provider_id: str) -> WorkspacesWorkspaceWebProvidersProviderId:
        return WorkspacesWorkspaceWebProvidersProviderId(self._client, self._bind("provider_id", provider_id))


class WorkspacesWorkspaceWebProvidersProviderId(Resource):
    """Bound Native resource: /workspaces / {workspace} / web-providers / {provider_id}."""

    async def get(self) -> Result[wire.WebProvider]:
        """Get Workspace Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_web_providers_provider_id.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], provider_id=self._bindings["provider_id"]
            )
        )

    async def update(self, *, body: wire.UpdateWebProviderRequest, if_match: str) -> Result[wire.WebProvider]:
        """Update Workspace Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: patch_workspaces_workspace_web_providers_provider_id.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                provider_id=self._bindings["provider_id"],
                body=body,
                if_match=if_match,
            )
        )

    @property
    def references(self) -> WorkspacesWorkspaceWebProvidersProviderIdReferences:
        return WorkspacesWorkspaceWebProvidersProviderIdReferences(self._client, self._bindings)

    async def test(self) -> Result[wire.WebProviderTestResult]:
        """Test Workspace Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: post_workspaces_workspace_web_providers_provider_id_test.asyncio_detailed(
                client=client, workspace=self._bindings["workspace"], provider_id=self._bindings["provider_id"]
            )
        )


class WorkspacesWorkspaceWebProvidersProviderIdReferences(Resource):
    """Bound Native resource: /workspaces / {workspace} / web-providers / {provider_id} / references."""

    async def list(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> Result[wire.WebProviderReferenceCollection]:
        """References Workspace Provider. One HTTP request; no automatic replay."""
        return await self._call(
            lambda client: get_workspaces_workspace_web_providers_provider_id_references.asyncio_detailed(
                client=client,
                workspace=self._bindings["workspace"],
                provider_id=self._bindings["provider_id"],
                limit=limit,
                cursor=cursor,
            )
        )

    def pages(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[Result[wire.WebProviderReferenceCollection]]:
        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""
        return pages(
            lambda next_cursor: self.list(limit=limit, cursor=next_cursor), lambda value: value.next_cursor, cursor
        )

    def iter(
        self, *, limit: int | Unset = UNSET, cursor: str | Unset | None = UNSET
    ) -> AsyncIterator[wire.WebProviderReference]:
        """Yield ordinary wire values lazily with a filter snapshot and server order."""
        return (item async for page in self.pages(limit=limit, cursor=cursor) for item in page.value.items)


class Agent(AgentMethods, _AgentResource):
    """Managed Agent reference with bounded interaction helpers."""


class Thread(ThreadMethods, _ThreadResource):
    """Managed Thread reference with bounded interaction helpers."""


class Run(RunMethods, _RunResource):
    """Managed Run reference with bounded interaction helpers."""


class QueuedSubmission(QueueMethods, _QueuedSubmissionResource):
    """Managed QueuedSubmission reference with bounded interaction helpers."""
