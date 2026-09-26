from http import HTTPStatus
from typing import Any

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.profile import Profile
from ...models.profile_update import ProfileUpdate
from ...types import UNSET, Response, Unset


def build_request(
    *,
    body: ProfileUpdate,
    if_match: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/users/me",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | Profile:
    if response.status_code == 200:
        response_200 = Profile.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | Profile]:
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
    *,
    client: AuthenticatedClient,
    body: ProfileUpdate,
    if_match: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | Profile]:
    """Update Profile

    Args:
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current view
        body (ProfileUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | Profile]
    """

    kwargs = build_request(
        body=body,
        if_match=if_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: ProfileUpdate,
    if_match: str | Unset | None = UNSET,
) -> ErrorEnvelope | Profile | None:
    """Update Profile

    Args:
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current view
        body (ProfileUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | Profile
    """

    return sync_detailed(
        client=client,
        body=body,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ProfileUpdate,
    if_match: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | Profile]:
    """Update Profile

    Args:
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current view
        body (ProfileUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | Profile]
    """

    kwargs = build_request(
        body=body,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ProfileUpdate,
    if_match: str | Unset | None = UNSET,
) -> ErrorEnvelope | Profile | None:
    """Update Profile

    Args:
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current view
        body (ProfileUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | Profile
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            if_match=if_match,
        )
    ).parsed
