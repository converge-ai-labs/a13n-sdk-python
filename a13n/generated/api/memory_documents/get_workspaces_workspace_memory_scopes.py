from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.stored_scope_collection import StoredScopeCollection
from ...types import UNSET, Response, Unset


def build_request(
    workspace: str,
    *,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    environment_id: str | Unset | None = UNSET,
    subject_id: str | Unset | None = UNSET,
    conversation_scope_id: str | Unset | None = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    json_cursor: str | Unset | None
    if isinstance(cursor, Unset):
        json_cursor = UNSET
    else:
        json_cursor = cursor
    params["cursor"] = json_cursor

    json_environment_id: str | Unset | None
    if isinstance(environment_id, Unset):
        json_environment_id = UNSET
    else:
        json_environment_id = environment_id
    params["environment_id"] = json_environment_id

    json_subject_id: str | Unset | None
    if isinstance(subject_id, Unset):
        json_subject_id = UNSET
    else:
        json_subject_id = subject_id
    params["subject_id"] = json_subject_id

    json_conversation_scope_id: str | Unset | None
    if isinstance(conversation_scope_id, Unset):
        json_conversation_scope_id = UNSET
    else:
        json_conversation_scope_id = conversation_scope_id
    params["conversation_scope_id"] = json_conversation_scope_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/workspaces/{workspace}/memory-scopes".format(
            workspace=quote(str(workspace), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | StoredScopeCollection:
    if response.status_code == 200:
        response_200 = StoredScopeCollection.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | StoredScopeCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    environment_id: str | Unset | None = UNSET,
    subject_id: str | Unset | None = UNSET,
    conversation_scope_id: str | Unset | None = UNSET,
) -> Response[ErrorResponse | StoredScopeCollection]:
    """Scopes

    Args:
        workspace (str):
        limit (int | Unset):
        cursor (None | str | Unset):
        environment_id (None | str | Unset):
        subject_id (None | str | Unset):
        conversation_scope_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | StoredScopeCollection]
    """

    kwargs = build_request(
        workspace=workspace,
        limit=limit,
        cursor=cursor,
        environment_id=environment_id,
        subject_id=subject_id,
        conversation_scope_id=conversation_scope_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    environment_id: str | Unset | None = UNSET,
    subject_id: str | Unset | None = UNSET,
    conversation_scope_id: str | Unset | None = UNSET,
) -> ErrorResponse | StoredScopeCollection | None:
    """Scopes

    Args:
        workspace (str):
        limit (int | Unset):
        cursor (None | str | Unset):
        environment_id (None | str | Unset):
        subject_id (None | str | Unset):
        conversation_scope_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | StoredScopeCollection
    """

    return sync_detailed(
        workspace=workspace,
        client=client,
        limit=limit,
        cursor=cursor,
        environment_id=environment_id,
        subject_id=subject_id,
        conversation_scope_id=conversation_scope_id,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    environment_id: str | Unset | None = UNSET,
    subject_id: str | Unset | None = UNSET,
    conversation_scope_id: str | Unset | None = UNSET,
) -> Response[ErrorResponse | StoredScopeCollection]:
    """Scopes

    Args:
        workspace (str):
        limit (int | Unset):
        cursor (None | str | Unset):
        environment_id (None | str | Unset):
        subject_id (None | str | Unset):
        conversation_scope_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | StoredScopeCollection]
    """

    kwargs = build_request(
        workspace=workspace,
        limit=limit,
        cursor=cursor,
        environment_id=environment_id,
        subject_id=subject_id,
        conversation_scope_id=conversation_scope_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    environment_id: str | Unset | None = UNSET,
    subject_id: str | Unset | None = UNSET,
    conversation_scope_id: str | Unset | None = UNSET,
) -> ErrorResponse | StoredScopeCollection | None:
    """Scopes

    Args:
        workspace (str):
        limit (int | Unset):
        cursor (None | str | Unset):
        environment_id (None | str | Unset):
        subject_id (None | str | Unset):
        conversation_scope_id (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | StoredScopeCollection
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            client=client,
            limit=limit,
            cursor=cursor,
            environment_id=environment_id,
            subject_id=subject_id,
            conversation_scope_id=conversation_scope_id,
        )
    ).parsed
