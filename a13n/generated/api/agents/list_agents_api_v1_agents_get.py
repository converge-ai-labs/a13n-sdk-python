from http import HTTPStatus
from typing import Any

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.agent_page import AgentPage
from ...models.agent_source import AgentSource
from ...models.error_envelope import ErrorEnvelope
from ...models.list_agents_api_v1_agents_get_preset_kind_type_0 import ListAgentsApiV1AgentsGetPresetKindType0
from ...types import UNSET, Response, Unset


def build_request(
    *,
    label: list[str] | Unset | None = UNSET,
    q: str | Unset | None = UNSET,
    archived: bool | Unset | None = UNSET,
    source: AgentSource | Unset | None = UNSET,
    preset_kind: ListAgentsApiV1AgentsGetPresetKindType0 | Unset | None = UNSET,
    skill_id: str | Unset | None = UNSET,
    skill_revision_id: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-ID"] = x_workspace_id

    params: dict[str, Any] = {}

    json_label: list[str] | Unset | None
    if isinstance(label, Unset):
        json_label = UNSET
    elif isinstance(label, list):
        json_label = label

    else:
        json_label = label
    params["label"] = json_label

    json_q: str | Unset | None
    if isinstance(q, Unset):
        json_q = UNSET
    else:
        json_q = q
    params["q"] = json_q

    json_archived: bool | Unset | None
    if isinstance(archived, Unset):
        json_archived = UNSET
    else:
        json_archived = archived
    params["archived"] = json_archived

    json_source: str | Unset | None
    if isinstance(source, Unset):
        json_source = UNSET
    elif isinstance(source, AgentSource):
        json_source = source.value
    else:
        json_source = source
    params["source"] = json_source

    json_preset_kind: str | Unset | None
    if isinstance(preset_kind, Unset):
        json_preset_kind = UNSET
    elif isinstance(preset_kind, ListAgentsApiV1AgentsGetPresetKindType0):
        json_preset_kind = preset_kind.value
    else:
        json_preset_kind = preset_kind
    params["preset_kind"] = json_preset_kind

    json_skill_id: str | Unset | None
    if isinstance(skill_id, Unset):
        json_skill_id = UNSET
    else:
        json_skill_id = skill_id
    params["skill_id"] = json_skill_id

    json_skill_revision_id: str | Unset | None
    if isinstance(skill_revision_id, Unset):
        json_skill_revision_id = UNSET
    else:
        json_skill_revision_id = skill_revision_id
    params["skill_revision_id"] = json_skill_revision_id

    params["limit"] = limit

    json_cursor: str | Unset | None
    if isinstance(cursor, Unset):
        json_cursor = UNSET
    else:
        json_cursor = cursor
    params["cursor"] = json_cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/agents",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AgentPage | ErrorEnvelope:
    if response.status_code == 200:
        response_200 = AgentPage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AgentPage | ErrorEnvelope]:
    from ....errors import ProtocolError

    try:
        return Response(
            status_code=HTTPStatus(response.status_code),
            content=response.content,
            headers=response.headers,
            parsed=_parse_response(client=client, response=response),
        )
    except (ValueError, KeyError, TypeError, AttributeError):
        raise ProtocolError("Malformed Service response") from None


def sync_detailed(
    *,
    client: AuthenticatedClient,
    label: list[str] | Unset | None = UNSET,
    q: str | Unset | None = UNSET,
    archived: bool | Unset | None = UNSET,
    source: AgentSource | Unset | None = UNSET,
    preset_kind: ListAgentsApiV1AgentsGetPresetKindType0 | Unset | None = UNSET,
    skill_id: str | Unset | None = UNSET,
    skill_revision_id: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[AgentPage | ErrorEnvelope]:
    """List Agents

     Agents of the workspace. `q` matches the name or description, ignoring case; `archived` keeps only
    archived agents, or only open ones; `source=builtin` finds managed presets; the skill filters keep
    those
    with a revision pinning that skill or that skill revision.

    Args:
        label (list[str] | None | Unset):
        q (None | str | Unset):
        archived (bool | None | Unset):
        source (AgentSource | None | Unset):
        preset_kind (ListAgentsApiV1AgentsGetPresetKindType0 | None | Unset):
        skill_id (None | str | Unset):
        skill_revision_id (None | str | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentPage | ErrorEnvelope]
    """

    kwargs = build_request(
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

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    label: list[str] | Unset | None = UNSET,
    q: str | Unset | None = UNSET,
    archived: bool | Unset | None = UNSET,
    source: AgentSource | Unset | None = UNSET,
    preset_kind: ListAgentsApiV1AgentsGetPresetKindType0 | Unset | None = UNSET,
    skill_id: str | Unset | None = UNSET,
    skill_revision_id: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> AgentPage | ErrorEnvelope | None:
    """List Agents

     Agents of the workspace. `q` matches the name or description, ignoring case; `archived` keeps only
    archived agents, or only open ones; `source=builtin` finds managed presets; the skill filters keep
    those
    with a revision pinning that skill or that skill revision.

    Args:
        label (list[str] | None | Unset):
        q (None | str | Unset):
        archived (bool | None | Unset):
        source (AgentSource | None | Unset):
        preset_kind (ListAgentsApiV1AgentsGetPresetKindType0 | None | Unset):
        skill_id (None | str | Unset):
        skill_revision_id (None | str | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentPage | ErrorEnvelope
    """

    return sync_detailed(
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
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    label: list[str] | Unset | None = UNSET,
    q: str | Unset | None = UNSET,
    archived: bool | Unset | None = UNSET,
    source: AgentSource | Unset | None = UNSET,
    preset_kind: ListAgentsApiV1AgentsGetPresetKindType0 | Unset | None = UNSET,
    skill_id: str | Unset | None = UNSET,
    skill_revision_id: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[AgentPage | ErrorEnvelope]:
    """List Agents

     Agents of the workspace. `q` matches the name or description, ignoring case; `archived` keeps only
    archived agents, or only open ones; `source=builtin` finds managed presets; the skill filters keep
    those
    with a revision pinning that skill or that skill revision.

    Args:
        label (list[str] | None | Unset):
        q (None | str | Unset):
        archived (bool | None | Unset):
        source (AgentSource | None | Unset):
        preset_kind (ListAgentsApiV1AgentsGetPresetKindType0 | None | Unset):
        skill_id (None | str | Unset):
        skill_revision_id (None | str | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentPage | ErrorEnvelope]
    """

    kwargs = build_request(
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

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    label: list[str] | Unset | None = UNSET,
    q: str | Unset | None = UNSET,
    archived: bool | Unset | None = UNSET,
    source: AgentSource | Unset | None = UNSET,
    preset_kind: ListAgentsApiV1AgentsGetPresetKindType0 | Unset | None = UNSET,
    skill_id: str | Unset | None = UNSET,
    skill_revision_id: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> AgentPage | ErrorEnvelope | None:
    """List Agents

     Agents of the workspace. `q` matches the name or description, ignoring case; `archived` keeps only
    archived agents, or only open ones; `source=builtin` finds managed presets; the skill filters keep
    those
    with a revision pinning that skill or that skill revision.

    Args:
        label (list[str] | None | Unset):
        q (None | str | Unset):
        archived (bool | None | Unset):
        source (AgentSource | None | Unset):
        preset_kind (ListAgentsApiV1AgentsGetPresetKindType0 | None | Unset):
        skill_id (None | str | Unset):
        skill_revision_id (None | str | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentPage | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
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
    ).parsed
