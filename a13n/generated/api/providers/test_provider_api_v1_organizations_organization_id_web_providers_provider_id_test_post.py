from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.provider_test import ProviderTest
from ...types import Response


def build_request(
    organization_id: str,
    provider_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/organizations/{organization_id}/web-providers/{provider_id}/test".format(
            organization_id=quote(str(organization_id), safe=""),
            provider_id=quote(str(provider_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | ProviderTest:
    if response.status_code == 200:
        response_200 = ProviderTest.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | ProviderTest]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    provider_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorEnvelope | ProviderTest]:
    """Test Provider

    Args:
        organization_id (str):
        provider_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ProviderTest]
    """

    kwargs = build_request(
        organization_id=organization_id,
        provider_id=provider_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    provider_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorEnvelope | ProviderTest | None:
    """Test Provider

    Args:
        organization_id (str):
        provider_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ProviderTest
    """

    return sync_detailed(
        organization_id=organization_id,
        provider_id=provider_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    provider_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorEnvelope | ProviderTest]:
    """Test Provider

    Args:
        organization_id (str):
        provider_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ProviderTest]
    """

    kwargs = build_request(
        organization_id=organization_id,
        provider_id=provider_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    provider_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorEnvelope | ProviderTest | None:
    """Test Provider

    Args:
        organization_id (str):
        provider_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ProviderTest
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            provider_id=provider_id,
            client=client,
        )
    ).parsed
