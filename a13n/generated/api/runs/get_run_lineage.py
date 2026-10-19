from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.read_view import ReadView
from ...models.run_page import RunPage
from ...models.run_summary_page import RunSummaryPage
from ...types import UNSET, Response, Unset


def build_request(
    run_id: str,
    *,
    cursor: str | Unset | None = UNSET,
    view: ReadView | Unset = UNSET,
    limit: int | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-ID"] = x_workspace_id

    params: dict[str, Any] = {}

    json_cursor: str | Unset | None
    if isinstance(cursor, Unset):
        json_cursor = UNSET
    else:
        json_cursor = cursor
    params["cursor"] = json_cursor

    json_view: str | Unset = UNSET
    if not isinstance(view, Unset):
        json_view = view.value

    params["view"] = json_view

    json_limit: int | Unset | None
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["limit"] = json_limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/runs/{run_id}/lineage".format(
            run_id=quote(str(run_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | RunPage | RunSummaryPage:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> RunPage | RunSummaryPage:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = RunPage.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = RunSummaryPage.from_dict(data)

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
) -> Response[ErrorEnvelope | RunPage | RunSummaryPage]:
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
    cursor: str | Unset | None = UNSET,
    view: ReadView | Unset = UNSET,
    limit: int | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | RunPage | RunSummaryPage]:
    """Get Run Lineage

     The run and its ancestors, nearest first, across fork origins.

    Args:
        run_id (str):
        cursor (None | str | Unset):
        view (ReadView | Unset):
        limit (int | None | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | RunPage | RunSummaryPage]
    """

    kwargs = build_request(
        run_id=run_id,
        cursor=cursor,
        view=view,
        limit=limit,
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
    cursor: str | Unset | None = UNSET,
    view: ReadView | Unset = UNSET,
    limit: int | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | RunPage | RunSummaryPage | None:
    """Get Run Lineage

     The run and its ancestors, nearest first, across fork origins.

    Args:
        run_id (str):
        cursor (None | str | Unset):
        view (ReadView | Unset):
        limit (int | None | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | RunPage | RunSummaryPage
    """

    return sync_detailed(
        run_id=run_id,
        client=client,
        cursor=cursor,
        view=view,
        limit=limit,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    run_id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset | None = UNSET,
    view: ReadView | Unset = UNSET,
    limit: int | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | RunPage | RunSummaryPage]:
    """Get Run Lineage

     The run and its ancestors, nearest first, across fork origins.

    Args:
        run_id (str):
        cursor (None | str | Unset):
        view (ReadView | Unset):
        limit (int | None | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | RunPage | RunSummaryPage]
    """

    kwargs = build_request(
        run_id=run_id,
        cursor=cursor,
        view=view,
        limit=limit,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    run_id: str,
    *,
    client: AuthenticatedClient,
    cursor: str | Unset | None = UNSET,
    view: ReadView | Unset = UNSET,
    limit: int | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | RunPage | RunSummaryPage | None:
    """Get Run Lineage

     The run and its ancestors, nearest first, across fork origins.

    Args:
        run_id (str):
        cursor (None | str | Unset):
        view (ReadView | Unset):
        limit (int | None | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | RunPage | RunSummaryPage
    """

    return (
        await asyncio_detailed(
            run_id=run_id,
            client=client,
            cursor=cursor,
            view=view,
            limit=limit,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
