from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.list_provider_types_kind import ListProviderTypesKind
from ...models.provider_type_page import ProviderTypePage
from ...types import Response


def build_request(
    kind: ListProviderTypesKind,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/provider-types/{kind}".format(
            kind=quote(str(kind), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | ProviderTypePage:
    if response.status_code == 200:
        response_200 = ProviderTypePage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | ProviderTypePage]:
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
    kind: ListProviderTypesKind,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorEnvelope | ProviderTypePage]:
    """List Provider Types

    Args:
        kind (ListProviderTypesKind):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ProviderTypePage]
    """

    kwargs = build_request(
        kind=kind,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    kind: ListProviderTypesKind,
    *,
    client: AuthenticatedClient,
) -> ErrorEnvelope | ProviderTypePage | None:
    """List Provider Types

    Args:
        kind (ListProviderTypesKind):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ProviderTypePage
    """

    return sync_detailed(
        kind=kind,
        client=client,
    ).parsed


async def asyncio_detailed(
    kind: ListProviderTypesKind,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorEnvelope | ProviderTypePage]:
    """List Provider Types

    Args:
        kind (ListProviderTypesKind):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ProviderTypePage]
    """

    kwargs = build_request(
        kind=kind,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    kind: ListProviderTypesKind,
    *,
    client: AuthenticatedClient,
) -> ErrorEnvelope | ProviderTypePage | None:
    """List Provider Types

    Args:
        kind (ListProviderTypesKind):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ProviderTypePage
    """

    return (
        await asyncio_detailed(
            kind=kind,
            client=client,
        )
    ).parsed
