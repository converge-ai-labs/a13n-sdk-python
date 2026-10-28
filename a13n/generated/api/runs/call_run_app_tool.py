from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.app_tool_call import AppToolCall
from ...models.app_tool_result import AppToolResult
from ...models.error_envelope import ErrorEnvelope
from ...types import UNSET, Response, Unset


def build_request(
    run_id: str,
    app_id: str,
    *,
    body: AppToolCall,
    x_workspace_id: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-ID"] = x_workspace_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/runs/{run_id}/apps/{app_id}/tools/call".format(
            run_id=quote(str(run_id), safe=""),
            app_id=quote(str(app_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AppToolResult | ErrorEnvelope:
    if response.status_code == 200:
        response_200 = AppToolResult.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppToolResult | ErrorEnvelope]:
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
    app_id: str,
    *,
    client: AuthenticatedClient,
    body: AppToolCall,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[AppToolResult | ErrorEnvelope]:
    """Call Run App Tool

     Call an App-visible tool on the saved connection without starting a Run.

    Args:
        run_id (str):
        app_id (str):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (AppToolCall):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppToolResult | ErrorEnvelope]
    """

    kwargs = build_request(
        run_id=run_id,
        app_id=app_id,
        body=body,
        x_workspace_id=x_workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    run_id: str,
    app_id: str,
    *,
    client: AuthenticatedClient,
    body: AppToolCall,
    x_workspace_id: str | Unset | None = UNSET,
) -> AppToolResult | ErrorEnvelope | None:
    """Call Run App Tool

     Call an App-visible tool on the saved connection without starting a Run.

    Args:
        run_id (str):
        app_id (str):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (AppToolCall):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppToolResult | ErrorEnvelope
    """

    return sync_detailed(
        run_id=run_id,
        app_id=app_id,
        client=client,
        body=body,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    run_id: str,
    app_id: str,
    *,
    client: AuthenticatedClient,
    body: AppToolCall,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[AppToolResult | ErrorEnvelope]:
    """Call Run App Tool

     Call an App-visible tool on the saved connection without starting a Run.

    Args:
        run_id (str):
        app_id (str):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (AppToolCall):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppToolResult | ErrorEnvelope]
    """

    kwargs = build_request(
        run_id=run_id,
        app_id=app_id,
        body=body,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    run_id: str,
    app_id: str,
    *,
    client: AuthenticatedClient,
    body: AppToolCall,
    x_workspace_id: str | Unset | None = UNSET,
) -> AppToolResult | ErrorEnvelope | None:
    """Call Run App Tool

     Call an App-visible tool on the saved connection without starting a Run.

    Args:
        run_id (str):
        app_id (str):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (AppToolCall):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppToolResult | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            run_id=run_id,
            app_id=app_id,
            client=client,
            body=body,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
