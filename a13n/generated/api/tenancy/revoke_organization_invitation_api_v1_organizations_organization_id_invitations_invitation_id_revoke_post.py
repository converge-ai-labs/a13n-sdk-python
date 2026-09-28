from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.invitation import Invitation
from ...types import UNSET, Response, Unset


def build_request(
    organization_id: str,
    invitation_id: str,
    *,
    if_match: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/organizations/{organization_id}/invitations/{invitation_id}/revoke".format(
            organization_id=quote(str(organization_id), safe=""),
            invitation_id=quote(str(invitation_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | Invitation:
    if response.status_code == 200:
        response_200 = Invitation.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | Invitation]:
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
    invitation_id: str,
    *,
    client: AuthenticatedClient,
    if_match: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | Invitation]:
    """Revoke Organization Invitation

    Args:
        organization_id (str):
        invitation_id (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current
            view, `"{key}:{version}"` for a model

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | Invitation]
    """

    kwargs = build_request(
        organization_id=organization_id,
        invitation_id=invitation_id,
        if_match=if_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    invitation_id: str,
    *,
    client: AuthenticatedClient,
    if_match: str | Unset | None = UNSET,
) -> ErrorEnvelope | Invitation | None:
    """Revoke Organization Invitation

    Args:
        organization_id (str):
        invitation_id (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current
            view, `"{key}:{version}"` for a model

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | Invitation
    """

    return sync_detailed(
        organization_id=organization_id,
        invitation_id=invitation_id,
        client=client,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    invitation_id: str,
    *,
    client: AuthenticatedClient,
    if_match: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | Invitation]:
    """Revoke Organization Invitation

    Args:
        organization_id (str):
        invitation_id (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current
            view, `"{key}:{version}"` for a model

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | Invitation]
    """

    kwargs = build_request(
        organization_id=organization_id,
        invitation_id=invitation_id,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    invitation_id: str,
    *,
    client: AuthenticatedClient,
    if_match: str | Unset | None = UNSET,
) -> ErrorEnvelope | Invitation | None:
    """Revoke Organization Invitation

    Args:
        organization_id (str):
        invitation_id (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current
            view, `"{key}:{version}"` for a model

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | Invitation
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            invitation_id=invitation_id,
            client=client,
            if_match=if_match,
        )
    ).parsed
