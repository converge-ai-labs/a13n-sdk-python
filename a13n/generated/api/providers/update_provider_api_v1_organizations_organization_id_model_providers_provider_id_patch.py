from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.provider import Provider
from ...models.provider_update import ProviderUpdate
from ...types import UNSET, Response, Unset


def build_request(
    organization_id: str,
    provider_id: str,
    *,
    body: ProviderUpdate,
    if_match: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/organizations/{organization_id}/model-providers/{provider_id}".format(
            organization_id=quote(str(organization_id), safe=""),
            provider_id=quote(str(provider_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | Provider:
    if response.status_code == 200:
        response_200 = Provider.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | Provider]:
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
    body: ProviderUpdate,
    if_match: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | Provider]:
    """Update Provider

     A `config` change must also replace or remove a stored credential: it never follows a new endpoint.

    Args:
        organization_id (str):
        provider_id (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current view
        body (ProviderUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | Provider]
    """

    kwargs = build_request(
        organization_id=organization_id,
        provider_id=provider_id,
        body=body,
        if_match=if_match,
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
    body: ProviderUpdate,
    if_match: str | Unset | None = UNSET,
) -> ErrorEnvelope | Provider | None:
    """Update Provider

     A `config` change must also replace or remove a stored credential: it never follows a new endpoint.

    Args:
        organization_id (str):
        provider_id (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current view
        body (ProviderUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | Provider
    """

    return sync_detailed(
        organization_id=organization_id,
        provider_id=provider_id,
        client=client,
        body=body,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    provider_id: str,
    *,
    client: AuthenticatedClient,
    body: ProviderUpdate,
    if_match: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | Provider]:
    """Update Provider

     A `config` change must also replace or remove a stored credential: it never follows a new endpoint.

    Args:
        organization_id (str):
        provider_id (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current view
        body (ProviderUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | Provider]
    """

    kwargs = build_request(
        organization_id=organization_id,
        provider_id=provider_id,
        body=body,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    provider_id: str,
    *,
    client: AuthenticatedClient,
    body: ProviderUpdate,
    if_match: str | Unset | None = UNSET,
) -> ErrorEnvelope | Provider | None:
    """Update Provider

     A `config` change must also replace or remove a stored credential: it never follows a new endpoint.

    Args:
        organization_id (str):
        provider_id (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current view
        body (ProviderUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | Provider
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            provider_id=provider_id,
            client=client,
            body=body,
            if_match=if_match,
        )
    ).parsed
