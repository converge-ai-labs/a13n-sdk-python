from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.oidc_backchannel_logout_body import OidcBackchannelLogoutBody
from ...types import Response


def build_request(
    provider_id: str,
    *,
    body: OidcBackchannelLogoutBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/auth/oidc/{provider_id}/backchannel-logout".format(
            provider_id=quote(str(provider_id), safe=""),
        ),
    }

    _kwargs["data"] = body.to_dict()
    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorEnvelope:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ErrorEnvelope]:
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
    *,
    client: AuthenticatedClient | Client,
    body: OidcBackchannelLogoutBody,
) -> Response[Any | ErrorEnvelope]:
    """Oidc Backchannel Logout

     Revoke OIDC login sessions on receipt of a signed Logout Token from their provider.

    Args:
        provider_id (str):
        body (OidcBackchannelLogoutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorEnvelope]
    """

    kwargs = build_request(
        provider_id=provider_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    provider_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: OidcBackchannelLogoutBody,
) -> Any | ErrorEnvelope | None:
    """Oidc Backchannel Logout

     Revoke OIDC login sessions on receipt of a signed Logout Token from their provider.

    Args:
        provider_id (str):
        body (OidcBackchannelLogoutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorEnvelope
    """

    return sync_detailed(
        provider_id=provider_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    provider_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: OidcBackchannelLogoutBody,
) -> Response[Any | ErrorEnvelope]:
    """Oidc Backchannel Logout

     Revoke OIDC login sessions on receipt of a signed Logout Token from their provider.

    Args:
        provider_id (str):
        body (OidcBackchannelLogoutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorEnvelope]
    """

    kwargs = build_request(
        provider_id=provider_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    provider_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: OidcBackchannelLogoutBody,
) -> Any | ErrorEnvelope | None:
    """Oidc Backchannel Logout

     Revoke OIDC login sessions on receipt of a signed Logout Token from their provider.

    Args:
        provider_id (str):
        body (OidcBackchannelLogoutBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            provider_id=provider_id,
            client=client,
            body=body,
        )
    ).parsed
