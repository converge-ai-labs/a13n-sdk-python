from http import HTTPStatus
from typing import Any

import httpx2 as httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.health_healthz_get_response_health_healthz_get import HealthHealthzGetResponseHealthHealthzGet
from ...types import Response


def build_request() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/healthz",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HealthHealthzGetResponseHealthHealthzGet | None:
    if response.status_code == 200:
        response_200 = HealthHealthzGetResponseHealthHealthzGet.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HealthHealthzGetResponseHealthHealthzGet]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[HealthHealthzGetResponseHealthHealthzGet]:
    """Health

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HealthHealthzGetResponseHealthHealthzGet]
    """

    kwargs = build_request()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> HealthHealthzGetResponseHealthHealthzGet | None:
    """Health

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HealthHealthzGetResponseHealthHealthzGet
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[HealthHealthzGetResponseHealthHealthzGet]:
    """Health

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HealthHealthzGetResponseHealthHealthzGet]
    """

    kwargs = build_request()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> HealthHealthzGetResponseHealthHealthzGet | None:
    """Health

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HealthHealthzGetResponseHealthHealthzGet
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
