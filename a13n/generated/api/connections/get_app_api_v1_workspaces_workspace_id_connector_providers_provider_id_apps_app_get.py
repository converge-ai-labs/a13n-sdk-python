from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.connector_app import ConnectorApp
from ...models.error_envelope import ErrorEnvelope
from ...types import Response


def build_request(
    workspace_id: str,
    provider_id: str,
    app: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/workspaces/{workspace_id}/connector-providers/{provider_id}/apps/{app}".format(
            workspace_id=quote(str(workspace_id), safe=""),
            provider_id=quote(str(provider_id), safe=""),
            app=quote(str(app), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ConnectorApp | ErrorEnvelope:
    if response.status_code == 200:
        response_200 = ConnectorApp.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ConnectorApp | ErrorEnvelope]:
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
    workspace_id: str,
    provider_id: str,
    app: str,
    *,
    client: AuthenticatedClient,
) -> Response[ConnectorApp | ErrorEnvelope]:
    """Get App

    Args:
        workspace_id (str):
        provider_id (str):
        app (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectorApp | ErrorEnvelope]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        provider_id=provider_id,
        app=app,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    provider_id: str,
    app: str,
    *,
    client: AuthenticatedClient,
) -> ConnectorApp | ErrorEnvelope | None:
    """Get App

    Args:
        workspace_id (str):
        provider_id (str):
        app (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectorApp | ErrorEnvelope
    """

    return sync_detailed(
        workspace_id=workspace_id,
        provider_id=provider_id,
        app=app,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    provider_id: str,
    app: str,
    *,
    client: AuthenticatedClient,
) -> Response[ConnectorApp | ErrorEnvelope]:
    """Get App

    Args:
        workspace_id (str):
        provider_id (str):
        app (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ConnectorApp | ErrorEnvelope]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        provider_id=provider_id,
        app=app,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    provider_id: str,
    app: str,
    *,
    client: AuthenticatedClient,
) -> ConnectorApp | ErrorEnvelope | None:
    """Get App

    Args:
        workspace_id (str):
        provider_id (str):
        app (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ConnectorApp | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            provider_id=provider_id,
            app=app,
            client=client,
        )
    ).parsed
