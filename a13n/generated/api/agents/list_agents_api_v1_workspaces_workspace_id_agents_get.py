from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.agent_page import AgentPage
from ...models.error_envelope import ErrorEnvelope
from ...types import UNSET, Response, Unset


def build_request(
    workspace_id: str,
    *,
    label: list[str] | Unset | None = UNSET,
    q: str | Unset | None = UNSET,
    archived: bool | Unset | None = UNSET,
    skill_id: str | Unset | None = UNSET,
    skill_revision_id: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
) -> dict[str, Any]:

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
        "url": "/api/v1/workspaces/{workspace_id}/agents".format(
            workspace_id=quote(str(workspace_id), safe=""),
        ),
        "params": params,
    }

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
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    label: list[str] | Unset | None = UNSET,
    q: str | Unset | None = UNSET,
    archived: bool | Unset | None = UNSET,
    skill_id: str | Unset | None = UNSET,
    skill_revision_id: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
) -> Response[AgentPage | ErrorEnvelope]:
    """List Agents

     Agents of the workspace. `q` matches the key, name or description, ignoring case; `archived` keeps
    only
    archived agents, or only open ones; the skill filters keep those with a revision pinning that skill
    or
    revision.

    Args:
        workspace_id (str):
        label (list[str] | None | Unset):
        q (None | str | Unset):
        archived (bool | None | Unset):
        skill_id (None | str | Unset):
        skill_revision_id (None | str | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentPage | ErrorEnvelope]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        label=label,
        q=q,
        archived=archived,
        skill_id=skill_id,
        skill_revision_id=skill_revision_id,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    label: list[str] | Unset | None = UNSET,
    q: str | Unset | None = UNSET,
    archived: bool | Unset | None = UNSET,
    skill_id: str | Unset | None = UNSET,
    skill_revision_id: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
) -> AgentPage | ErrorEnvelope | None:
    """List Agents

     Agents of the workspace. `q` matches the key, name or description, ignoring case; `archived` keeps
    only
    archived agents, or only open ones; the skill filters keep those with a revision pinning that skill
    or
    revision.

    Args:
        workspace_id (str):
        label (list[str] | None | Unset):
        q (None | str | Unset):
        archived (bool | None | Unset):
        skill_id (None | str | Unset):
        skill_revision_id (None | str | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentPage | ErrorEnvelope
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        label=label,
        q=q,
        archived=archived,
        skill_id=skill_id,
        skill_revision_id=skill_revision_id,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    label: list[str] | Unset | None = UNSET,
    q: str | Unset | None = UNSET,
    archived: bool | Unset | None = UNSET,
    skill_id: str | Unset | None = UNSET,
    skill_revision_id: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
) -> Response[AgentPage | ErrorEnvelope]:
    """List Agents

     Agents of the workspace. `q` matches the key, name or description, ignoring case; `archived` keeps
    only
    archived agents, or only open ones; the skill filters keep those with a revision pinning that skill
    or
    revision.

    Args:
        workspace_id (str):
        label (list[str] | None | Unset):
        q (None | str | Unset):
        archived (bool | None | Unset):
        skill_id (None | str | Unset):
        skill_revision_id (None | str | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentPage | ErrorEnvelope]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        label=label,
        q=q,
        archived=archived,
        skill_id=skill_id,
        skill_revision_id=skill_revision_id,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    label: list[str] | Unset | None = UNSET,
    q: str | Unset | None = UNSET,
    archived: bool | Unset | None = UNSET,
    skill_id: str | Unset | None = UNSET,
    skill_revision_id: str | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
) -> AgentPage | ErrorEnvelope | None:
    """List Agents

     Agents of the workspace. `q` matches the key, name or description, ignoring case; `archived` keeps
    only
    archived agents, or only open ones; the skill filters keep those with a revision pinning that skill
    or
    revision.

    Args:
        workspace_id (str):
        label (list[str] | None | Unset):
        q (None | str | Unset):
        archived (bool | None | Unset):
        skill_id (None | str | Unset):
        skill_revision_id (None | str | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentPage | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            label=label,
            q=q,
            archived=archived,
            skill_id=skill_id,
            skill_revision_id=skill_revision_id,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
