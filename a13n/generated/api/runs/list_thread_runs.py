from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.list_thread_runs_direction import ListThreadRunsDirection
from ...models.list_thread_runs_sort_type_0 import ListThreadRunsSortType0
from ...models.thread_run_page import ThreadRunPage
from ...types import UNSET, Response, Unset


def build_request(
    thread_id: str,
    *,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    anchor: str | Unset | None = UNSET,
    sort: ListThreadRunsSortType0 | Unset | None = UNSET,
    direction: ListThreadRunsDirection | Unset = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-ID"] = x_workspace_id

    params: dict[str, Any] = {}

    params["limit"] = limit

    json_cursor: str | Unset | None
    if isinstance(cursor, Unset):
        json_cursor = UNSET
    else:
        json_cursor = cursor
    params["cursor"] = json_cursor

    json_anchor: str | Unset | None
    if isinstance(anchor, Unset):
        json_anchor = UNSET
    else:
        json_anchor = anchor
    params["anchor"] = json_anchor

    json_sort: str | Unset | None
    if isinstance(sort, Unset):
        json_sort = UNSET
    elif isinstance(sort, ListThreadRunsSortType0):
        json_sort = sort.value
    else:
        json_sort = sort
    params["sort"] = json_sort

    json_direction: str | Unset = UNSET
    if not isinstance(direction, Unset):
        json_direction = direction.value

    params["direction"] = json_direction

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/threads/{thread_id}/runs".format(
            thread_id=quote(str(thread_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | ThreadRunPage:
    if response.status_code == 200:
        response_200 = ThreadRunPage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | ThreadRunPage]:
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
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    anchor: str | Unset | None = UNSET,
    sort: ListThreadRunsSortType0 | Unset | None = UNSET,
    direction: ListThreadRunsDirection | Unset = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | ThreadRunPage]:
    """List Thread Runs

     Page chronological history from an anchor, or rank all Thread runs by a recorded metric.

    Args:
        thread_id (str):
        limit (int | Unset):
        cursor (None | str | Unset):
        anchor (None | str | Unset):
        sort (ListThreadRunsSortType0 | None | Unset):
        direction (ListThreadRunsDirection | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ThreadRunPage]
    """

    kwargs = build_request(
        thread_id=thread_id,
        limit=limit,
        cursor=cursor,
        anchor=anchor,
        sort=sort,
        direction=direction,
        x_workspace_id=x_workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    thread_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    anchor: str | Unset | None = UNSET,
    sort: ListThreadRunsSortType0 | Unset | None = UNSET,
    direction: ListThreadRunsDirection | Unset = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | ThreadRunPage | None:
    """List Thread Runs

     Page chronological history from an anchor, or rank all Thread runs by a recorded metric.

    Args:
        thread_id (str):
        limit (int | Unset):
        cursor (None | str | Unset):
        anchor (None | str | Unset):
        sort (ListThreadRunsSortType0 | None | Unset):
        direction (ListThreadRunsDirection | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ThreadRunPage
    """

    return sync_detailed(
        thread_id=thread_id,
        client=client,
        limit=limit,
        cursor=cursor,
        anchor=anchor,
        sort=sort,
        direction=direction,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    thread_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    anchor: str | Unset | None = UNSET,
    sort: ListThreadRunsSortType0 | Unset | None = UNSET,
    direction: ListThreadRunsDirection | Unset = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | ThreadRunPage]:
    """List Thread Runs

     Page chronological history from an anchor, or rank all Thread runs by a recorded metric.

    Args:
        thread_id (str):
        limit (int | Unset):
        cursor (None | str | Unset):
        anchor (None | str | Unset):
        sort (ListThreadRunsSortType0 | None | Unset):
        direction (ListThreadRunsDirection | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ThreadRunPage]
    """

    kwargs = build_request(
        thread_id=thread_id,
        limit=limit,
        cursor=cursor,
        anchor=anchor,
        sort=sort,
        direction=direction,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    thread_id: str,
    *,
    client: AuthenticatedClient,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    anchor: str | Unset | None = UNSET,
    sort: ListThreadRunsSortType0 | Unset | None = UNSET,
    direction: ListThreadRunsDirection | Unset = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | ThreadRunPage | None:
    """List Thread Runs

     Page chronological history from an anchor, or rank all Thread runs by a recorded metric.

    Args:
        thread_id (str):
        limit (int | Unset):
        cursor (None | str | Unset):
        anchor (None | str | Unset):
        sort (ListThreadRunsSortType0 | None | Unset):
        direction (ListThreadRunsDirection | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ThreadRunPage
    """

    return (
        await asyncio_detailed(
            thread_id=thread_id,
            client=client,
            limit=limit,
            cursor=cursor,
            anchor=anchor,
            sort=sort,
            direction=direction,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
