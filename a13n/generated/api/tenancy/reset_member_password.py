from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.password_reset_receipt import PasswordResetReceipt
from ...types import Response


def build_request(
    organization_id: str,
    user_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/organizations/{organization_id}/members/{user_id}/password-reset".format(
            organization_id=quote(str(organization_id), safe=""),
            user_id=quote(str(user_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | PasswordResetReceipt:
    if response.status_code == 200:
        response_200 = PasswordResetReceipt.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | PasswordResetReceipt]:
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
    organization_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorEnvelope | PasswordResetReceipt]:
    """Reset Member Password

    Args:
        organization_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | PasswordResetReceipt]
    """

    kwargs = build_request(
        organization_id=organization_id,
        user_id=user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorEnvelope | PasswordResetReceipt | None:
    """Reset Member Password

    Args:
        organization_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | PasswordResetReceipt
    """

    return sync_detailed(
        organization_id=organization_id,
        user_id=user_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorEnvelope | PasswordResetReceipt]:
    """Reset Member Password

    Args:
        organization_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | PasswordResetReceipt]
    """

    kwargs = build_request(
        organization_id=organization_id,
        user_id=user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    user_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorEnvelope | PasswordResetReceipt | None:
    """Reset Member Password

    Args:
        organization_id (str):
        user_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | PasswordResetReceipt
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            user_id=user_id,
            client=client,
        )
    ).parsed
