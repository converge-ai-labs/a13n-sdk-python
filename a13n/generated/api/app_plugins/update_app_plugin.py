from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.app_plugins import AppPlugins
from ...models.app_update import AppUpdate
from ...models.error_envelope import ErrorEnvelope
from ...types import UNSET, Response, Unset


def build_request(
    organization_id: str,
    app_id: str,
    *,
    body: AppUpdate,
    if_match: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/organizations/{organization_id}/app-plugins/{app_id}".format(
            organization_id=quote(str(organization_id), safe=""),
            app_id=quote(str(app_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AppPlugins | ErrorEnvelope:
    if response.status_code == 200:
        response_200 = AppPlugins.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AppPlugins | ErrorEnvelope]:
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
    app_id: str,
    *,
    client: AuthenticatedClient,
    body: AppUpdate,
    if_match: str | Unset | None = UNSET,
) -> Response[AppPlugins | ErrorEnvelope]:
    """Update App Plugin

    Args:
        organization_id (str):
        app_id (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current
            view, `"{key}:{version}"` for a model
        body (AppUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppPlugins | ErrorEnvelope]
    """

    kwargs = build_request(
        organization_id=organization_id,
        app_id=app_id,
        body=body,
        if_match=if_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    app_id: str,
    *,
    client: AuthenticatedClient,
    body: AppUpdate,
    if_match: str | Unset | None = UNSET,
) -> AppPlugins | ErrorEnvelope | None:
    """Update App Plugin

    Args:
        organization_id (str):
        app_id (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current
            view, `"{key}:{version}"` for a model
        body (AppUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppPlugins | ErrorEnvelope
    """

    return sync_detailed(
        organization_id=organization_id,
        app_id=app_id,
        client=client,
        body=body,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    app_id: str,
    *,
    client: AuthenticatedClient,
    body: AppUpdate,
    if_match: str | Unset | None = UNSET,
) -> Response[AppPlugins | ErrorEnvelope]:
    """Update App Plugin

    Args:
        organization_id (str):
        app_id (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current
            view, `"{key}:{version}"` for a model
        body (AppUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppPlugins | ErrorEnvelope]
    """

    kwargs = build_request(
        organization_id=organization_id,
        app_id=app_id,
        body=body,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    app_id: str,
    *,
    client: AuthenticatedClient,
    body: AppUpdate,
    if_match: str | Unset | None = UNSET,
) -> AppPlugins | ErrorEnvelope | None:
    """Update App Plugin

    Args:
        organization_id (str):
        app_id (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current
            view, `"{key}:{version}"` for a model
        body (AppUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppPlugins | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            app_id=app_id,
            client=client,
            body=body,
            if_match=if_match,
        )
    ).parsed
