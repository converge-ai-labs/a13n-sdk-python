from http import HTTPStatus
from typing import Any

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.list_skills_api_v1_skills_get_source_type_0 import ListSkillsApiV1SkillsGetSourceType0
from ...models.skill_page import SkillPage
from ...types import UNSET, Response, Unset


def build_request(
    *,
    label: list[str] | Unset | None = UNSET,
    q: str | Unset | None = UNSET,
    source: ListSkillsApiV1SkillsGetSourceType0 | Unset | None = UNSET,
    archived: bool | Unset | None = UNSET,
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

    json_source: str | Unset | None
    if isinstance(source, Unset):
        json_source = UNSET
    elif isinstance(source, ListSkillsApiV1SkillsGetSourceType0):
        json_source = source.value
    else:
        json_source = source
    params["source"] = json_source

    json_archived: bool | Unset | None
    if isinstance(archived, Unset):
        json_archived = UNSET
    else:
        json_archived = archived
    params["archived"] = json_archived

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
        "url": "/api/v1/skills",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | SkillPage:
    if response.status_code == 200:
        response_200 = SkillPage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | SkillPage]:
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
    source: ListSkillsApiV1SkillsGetSourceType0 | Unset | None = UNSET,
    archived: bool | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | SkillPage]:
    """List Skills

     Skills of the workspace. `q` matches the name or description, ignoring case; `source` the kind of
    source the default revision was read from; `archived` keeps only archived skills, or only open ones.

    Args:
        label (list[str] | None | Unset):
        q (None | str | Unset):
        source (ListSkillsApiV1SkillsGetSourceType0 | None | Unset):
        archived (bool | None | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | SkillPage]
    """

    kwargs = build_request(
        label=label,
        q=q,
        source=source,
        archived=archived,
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
    source: ListSkillsApiV1SkillsGetSourceType0 | Unset | None = UNSET,
    archived: bool | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | SkillPage | None:
    """List Skills

     Skills of the workspace. `q` matches the name or description, ignoring case; `source` the kind of
    source the default revision was read from; `archived` keeps only archived skills, or only open ones.

    Args:
        label (list[str] | None | Unset):
        q (None | str | Unset):
        source (ListSkillsApiV1SkillsGetSourceType0 | None | Unset):
        archived (bool | None | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | SkillPage
    """

    return sync_detailed(
        client=client,
        label=label,
        q=q,
        source=source,
        archived=archived,
        limit=limit,
        cursor=cursor,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    label: list[str] | Unset | None = UNSET,
    q: str | Unset | None = UNSET,
    source: ListSkillsApiV1SkillsGetSourceType0 | Unset | None = UNSET,
    archived: bool | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | SkillPage]:
    """List Skills

     Skills of the workspace. `q` matches the name or description, ignoring case; `source` the kind of
    source the default revision was read from; `archived` keeps only archived skills, or only open ones.

    Args:
        label (list[str] | None | Unset):
        q (None | str | Unset):
        source (ListSkillsApiV1SkillsGetSourceType0 | None | Unset):
        archived (bool | None | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | SkillPage]
    """

    kwargs = build_request(
        label=label,
        q=q,
        source=source,
        archived=archived,
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
    source: ListSkillsApiV1SkillsGetSourceType0 | Unset | None = UNSET,
    archived: bool | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | SkillPage | None:
    """List Skills

     Skills of the workspace. `q` matches the name or description, ignoring case; `source` the kind of
    source the default revision was read from; `archived` keeps only archived skills, or only open ones.

    Args:
        label (list[str] | None | Unset):
        q (None | str | Unset):
        source (ListSkillsApiV1SkillsGetSourceType0 | None | Unset):
        archived (bool | None | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | SkillPage
    """

    return (
        await asyncio_detailed(
            client=client,
            label=label,
            q=q,
            source=source,
            archived=archived,
            limit=limit,
            cursor=cursor,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
