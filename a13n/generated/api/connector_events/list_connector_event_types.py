from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.event_type_page import EventTypePage
from ...types import UNSET, Response, Unset


def build_request(
    provider_id: str,
    app: str,
    *,
    refresh: bool | Unset = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-ID"] = x_workspace_id

    params: dict[str, Any] = {}

    params["refresh"] = refresh

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/connector-providers/{provider_id}/apps/{app}/event-types".format(
            provider_id=quote(str(provider_id), safe=""),
            app=quote(str(app), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | EventTypePage:
    if response.status_code == 200:
        response_200 = EventTypePage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | EventTypePage]:
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
    provider_id: str,
    app: str,
    *,
    client: AuthenticatedClient,
    refresh: bool | Unset = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | EventTypePage]:
    """List Connector Event Types

    Args:
        provider_id (str):
        app (str):
        refresh (bool | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | EventTypePage]
    """

    kwargs = build_request(
        provider_id=provider_id,
        app=app,
        refresh=refresh,
        x_workspace_id=x_workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    provider_id: str,
    app: str,
    *,
    client: AuthenticatedClient,
    refresh: bool | Unset = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | EventTypePage | None:
    """List Connector Event Types

    Args:
        provider_id (str):
        app (str):
        refresh (bool | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | EventTypePage
    """

    return sync_detailed(
        provider_id=provider_id,
        app=app,
        client=client,
        refresh=refresh,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    provider_id: str,
    app: str,
    *,
    client: AuthenticatedClient,
    refresh: bool | Unset = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | EventTypePage]:
    """List Connector Event Types

    Args:
        provider_id (str):
        app (str):
        refresh (bool | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | EventTypePage]
    """

    kwargs = build_request(
        provider_id=provider_id,
        app=app,
        refresh=refresh,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    provider_id: str,
    app: str,
    *,
    client: AuthenticatedClient,
    refresh: bool | Unset = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | EventTypePage | None:
    """List Connector Event Types

    Args:
        provider_id (str):
        app (str):
        refresh (bool | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | EventTypePage
    """

    return (
        await asyncio_detailed(
            provider_id=provider_id,
            app=app,
            client=client,
            refresh=refresh,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
