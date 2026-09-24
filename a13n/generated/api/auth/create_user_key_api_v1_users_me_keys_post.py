from http import HTTPStatus
from typing import Any

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.issued_key import IssuedKey
from ...models.user_key_create import UserKeyCreate
from ...types import Response


def build_request(
    *,
    body: UserKeyCreate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/users/me/keys",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | IssuedKey:
    if response.status_code == 201:
        response_201 = IssuedKey.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | IssuedKey]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UserKeyCreate,
) -> Response[ErrorEnvelope | IssuedKey]:
    """Create User Key

     Needs a login session: an API key never issues keys, so a leaked key cannot outlive its revocation.

    Args:
        body (UserKeyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | IssuedKey]
    """

    kwargs = build_request(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: UserKeyCreate,
) -> ErrorEnvelope | IssuedKey | None:
    """Create User Key

     Needs a login session: an API key never issues keys, so a leaked key cannot outlive its revocation.

    Args:
        body (UserKeyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | IssuedKey
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UserKeyCreate,
) -> Response[ErrorEnvelope | IssuedKey]:
    """Create User Key

     Needs a login session: an API key never issues keys, so a leaked key cannot outlive its revocation.

    Args:
        body (UserKeyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | IssuedKey]
    """

    kwargs = build_request(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UserKeyCreate,
) -> ErrorEnvelope | IssuedKey | None:
    """Create User Key

     Needs a login session: an API key never issues keys, so a leaked key cannot outlive its revocation.

    Args:
        body (UserKeyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | IssuedKey
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
