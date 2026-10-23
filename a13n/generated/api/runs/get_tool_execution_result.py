from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.text_read import TextRead
from ...types import UNSET, Response, Unset


def build_request(
    thread_id: str,
    execution_id: str,
    *,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    version: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-ID"] = x_workspace_id

    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    json_version: str | Unset | None
    if isinstance(version, Unset):
        json_version = UNSET
    else:
        json_version = version
    params["version"] = json_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/threads/{thread_id}/tool-executions/{execution_id}/result".format(
            thread_id=quote(str(thread_id), safe=""),
            execution_id=quote(str(execution_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | TextRead:
    if response.status_code == 200:
        response_200 = TextRead.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | TextRead]:
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
    thread_id: str,
    execution_id: str,
    *,
    client: AuthenticatedClient,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    version: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | TextRead]:
    """Get Tool Execution Result

    Args:
        thread_id (str):
        execution_id (str):
        offset (int | Unset): Unicode code-point offset; continue with next_offset.
        limit (int | Unset): Maximum Unicode code points in this fragment.
        version (None | str | Unset): Content version from the first read; required after offset
            0.
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | TextRead]
    """

    kwargs = build_request(
        thread_id=thread_id,
        execution_id=execution_id,
        offset=offset,
        limit=limit,
        version=version,
        x_workspace_id=x_workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    thread_id: str,
    execution_id: str,
    *,
    client: AuthenticatedClient,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    version: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | TextRead | None:
    """Get Tool Execution Result

    Args:
        thread_id (str):
        execution_id (str):
        offset (int | Unset): Unicode code-point offset; continue with next_offset.
        limit (int | Unset): Maximum Unicode code points in this fragment.
        version (None | str | Unset): Content version from the first read; required after offset
            0.
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | TextRead
    """

    return sync_detailed(
        thread_id=thread_id,
        execution_id=execution_id,
        client=client,
        offset=offset,
        limit=limit,
        version=version,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    thread_id: str,
    execution_id: str,
    *,
    client: AuthenticatedClient,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    version: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | TextRead]:
    """Get Tool Execution Result

    Args:
        thread_id (str):
        execution_id (str):
        offset (int | Unset): Unicode code-point offset; continue with next_offset.
        limit (int | Unset): Maximum Unicode code points in this fragment.
        version (None | str | Unset): Content version from the first read; required after offset
            0.
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | TextRead]
    """

    kwargs = build_request(
        thread_id=thread_id,
        execution_id=execution_id,
        offset=offset,
        limit=limit,
        version=version,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    thread_id: str,
    execution_id: str,
    *,
    client: AuthenticatedClient,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
    version: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | TextRead | None:
    """Get Tool Execution Result

    Args:
        thread_id (str):
        execution_id (str):
        offset (int | Unset): Unicode code-point offset; continue with next_offset.
        limit (int | Unset): Maximum Unicode code points in this fragment.
        version (None | str | Unset): Content version from the first read; required after offset
            0.
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | TextRead
    """

    return (
        await asyncio_detailed(
            thread_id=thread_id,
            execution_id=execution_id,
            client=client,
            offset=offset,
            limit=limit,
            version=version,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
