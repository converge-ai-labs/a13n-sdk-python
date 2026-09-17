from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.client_connection_ticket import ClientConnectionTicket
from ...models.error_response import ErrorResponse
from ...types import Response


def build_request(
    environment_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/environments/{environment_id}/connection-tickets".format(
            environment_id=quote(str(environment_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ClientConnectionTicket | ErrorResponse:
    if response.status_code == 201:
        response_201 = ClientConnectionTicket.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ClientConnectionTicket | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    environment_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ClientConnectionTicket | ErrorResponse]:
    """Issue Ticket

    Args:
        environment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClientConnectionTicket | ErrorResponse]
    """

    kwargs = build_request(
        environment_id=environment_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_id: str,
    *,
    client: AuthenticatedClient,
) -> ClientConnectionTicket | ErrorResponse | None:
    """Issue Ticket

    Args:
        environment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClientConnectionTicket | ErrorResponse
    """

    return sync_detailed(
        environment_id=environment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ClientConnectionTicket | ErrorResponse]:
    """Issue Ticket

    Args:
        environment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClientConnectionTicket | ErrorResponse]
    """

    kwargs = build_request(
        environment_id=environment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    *,
    client: AuthenticatedClient,
) -> ClientConnectionTicket | ErrorResponse | None:
    """Issue Ticket

    Args:
        environment_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClientConnectionTicket | ErrorResponse
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            client=client,
        )
    ).parsed
