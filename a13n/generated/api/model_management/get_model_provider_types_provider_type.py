from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.model_provider_metadata import ModelProviderMetadata
from ...types import Response


def build_request(
    provider_type: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/model-provider-types/{provider_type}".format(
            provider_type=quote(str(provider_type), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ModelProviderMetadata:
    if response.status_code == 200:
        response_200 = ModelProviderMetadata.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | ModelProviderMetadata]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    provider_type: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | ModelProviderMetadata]:
    """Get Model Provider Type

    Args:
        provider_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ModelProviderMetadata]
    """

    kwargs = build_request(
        provider_type=provider_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    provider_type: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | ModelProviderMetadata | None:
    """Get Model Provider Type

    Args:
        provider_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ModelProviderMetadata
    """

    return sync_detailed(
        provider_type=provider_type,
        client=client,
    ).parsed


async def asyncio_detailed(
    provider_type: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | ModelProviderMetadata]:
    """Get Model Provider Type

    Args:
        provider_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ModelProviderMetadata]
    """

    kwargs = build_request(
        provider_type=provider_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    provider_type: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | ModelProviderMetadata | None:
    """Get Model Provider Type

    Args:
        provider_type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ModelProviderMetadata
    """

    return (
        await asyncio_detailed(
            provider_type=provider_type,
            client=client,
        )
    ).parsed
