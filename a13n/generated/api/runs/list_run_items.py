from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.item_kind import ItemKind
from ...models.item_page import ItemPage
from ...models.item_state import ItemState
from ...models.read_view import ReadView
from ...models.run_items import RunItems
from ...types import UNSET, Response, Unset


def build_request(
    run_id: str,
    *,
    before: int | Unset | None = UNSET,
    after: int | Unset | None = UNSET,
    limit: int | Unset | None = UNSET,
    view: ReadView | Unset = UNSET,
    kind: ItemKind | Unset | None = UNSET,
    state: ItemState | Unset | None = UNSET,
    tool_name: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-ID"] = x_workspace_id

    params: dict[str, Any] = {}

    json_before: int | Unset | None
    if isinstance(before, Unset):
        json_before = UNSET
    else:
        json_before = before
    params["before"] = json_before

    json_after: int | Unset | None
    if isinstance(after, Unset):
        json_after = UNSET
    else:
        json_after = after
    params["after"] = json_after

    json_limit: int | Unset | None
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["limit"] = json_limit

    json_view: str | Unset = UNSET
    if not isinstance(view, Unset):
        json_view = view.value

    params["view"] = json_view

    json_kind: str | Unset | None
    if isinstance(kind, Unset):
        json_kind = UNSET
    elif isinstance(kind, ItemKind):
        json_kind = kind.value
    else:
        json_kind = kind
    params["kind"] = json_kind

    json_state: str | Unset | None
    if isinstance(state, Unset):
        json_state = UNSET
    elif isinstance(state, ItemState):
        json_state = state.value
    else:
        json_state = state
    params["state"] = json_state

    json_tool_name: str | Unset | None
    if isinstance(tool_name, Unset):
        json_tool_name = UNSET
    else:
        json_tool_name = tool_name
    params["tool_name"] = json_tool_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/runs/{run_id}/items".format(
            run_id=quote(str(run_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | ItemPage | RunItems:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> ItemPage | RunItems:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = RunItems.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = ItemPage.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | ItemPage | RunItems]:
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
    run_id: str,
    *,
    client: AuthenticatedClient,
    before: int | Unset | None = UNSET,
    after: int | Unset | None = UNSET,
    limit: int | Unset | None = UNSET,
    view: ReadView | Unset = UNSET,
    kind: ItemKind | Unset | None = UNSET,
    state: ItemState | Unset | None = UNSET,
    tool_name: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | ItemPage | RunItems]:
    """List Run Items

     A run's committed display items by ordinal. Detailed unfiltered reads default to the newest items
    and full tail.
    Compact or filtered reads start at the oldest ordinal and strictly honor limit. Use exclusive
    before/after
    positions, then follow next_before/next_after even when a filtered page is empty.

    Args:
        run_id (str):
        before (int | None | Unset): Return the items just before this ordinal
        after (int | None | Unset): Return the items just after this ordinal
        limit (int | None | Unset):
        view (ReadView | Unset):
        kind (ItemKind | None | Unset):
        state (ItemState | None | Unset):
        tool_name (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ItemPage | RunItems]
    """

    kwargs = build_request(
        run_id=run_id,
        before=before,
        after=after,
        limit=limit,
        view=view,
        kind=kind,
        state=state,
        tool_name=tool_name,
        x_workspace_id=x_workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    run_id: str,
    *,
    client: AuthenticatedClient,
    before: int | Unset | None = UNSET,
    after: int | Unset | None = UNSET,
    limit: int | Unset | None = UNSET,
    view: ReadView | Unset = UNSET,
    kind: ItemKind | Unset | None = UNSET,
    state: ItemState | Unset | None = UNSET,
    tool_name: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | ItemPage | RunItems | None:
    """List Run Items

     A run's committed display items by ordinal. Detailed unfiltered reads default to the newest items
    and full tail.
    Compact or filtered reads start at the oldest ordinal and strictly honor limit. Use exclusive
    before/after
    positions, then follow next_before/next_after even when a filtered page is empty.

    Args:
        run_id (str):
        before (int | None | Unset): Return the items just before this ordinal
        after (int | None | Unset): Return the items just after this ordinal
        limit (int | None | Unset):
        view (ReadView | Unset):
        kind (ItemKind | None | Unset):
        state (ItemState | None | Unset):
        tool_name (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ItemPage | RunItems
    """

    return sync_detailed(
        run_id=run_id,
        client=client,
        before=before,
        after=after,
        limit=limit,
        view=view,
        kind=kind,
        state=state,
        tool_name=tool_name,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    run_id: str,
    *,
    client: AuthenticatedClient,
    before: int | Unset | None = UNSET,
    after: int | Unset | None = UNSET,
    limit: int | Unset | None = UNSET,
    view: ReadView | Unset = UNSET,
    kind: ItemKind | Unset | None = UNSET,
    state: ItemState | Unset | None = UNSET,
    tool_name: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | ItemPage | RunItems]:
    """List Run Items

     A run's committed display items by ordinal. Detailed unfiltered reads default to the newest items
    and full tail.
    Compact or filtered reads start at the oldest ordinal and strictly honor limit. Use exclusive
    before/after
    positions, then follow next_before/next_after even when a filtered page is empty.

    Args:
        run_id (str):
        before (int | None | Unset): Return the items just before this ordinal
        after (int | None | Unset): Return the items just after this ordinal
        limit (int | None | Unset):
        view (ReadView | Unset):
        kind (ItemKind | None | Unset):
        state (ItemState | None | Unset):
        tool_name (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ItemPage | RunItems]
    """

    kwargs = build_request(
        run_id=run_id,
        before=before,
        after=after,
        limit=limit,
        view=view,
        kind=kind,
        state=state,
        tool_name=tool_name,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    run_id: str,
    *,
    client: AuthenticatedClient,
    before: int | Unset | None = UNSET,
    after: int | Unset | None = UNSET,
    limit: int | Unset | None = UNSET,
    view: ReadView | Unset = UNSET,
    kind: ItemKind | Unset | None = UNSET,
    state: ItemState | Unset | None = UNSET,
    tool_name: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | ItemPage | RunItems | None:
    """List Run Items

     A run's committed display items by ordinal. Detailed unfiltered reads default to the newest items
    and full tail.
    Compact or filtered reads start at the oldest ordinal and strictly honor limit. Use exclusive
    before/after
    positions, then follow next_before/next_after even when a filtered page is empty.

    Args:
        run_id (str):
        before (int | None | Unset): Return the items just before this ordinal
        after (int | None | Unset): Return the items just after this ordinal
        limit (int | None | Unset):
        view (ReadView | Unset):
        kind (ItemKind | None | Unset):
        state (ItemState | None | Unset):
        tool_name (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ItemPage | RunItems
    """

    return (
        await asyncio_detailed(
            run_id=run_id,
            client=client,
            before=before,
            after=after,
            limit=limit,
            view=view,
            kind=kind,
            state=state,
            tool_name=tool_name,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
