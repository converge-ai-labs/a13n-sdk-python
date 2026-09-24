from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.grant_update import GrantUpdate
from ...models.grant_view import GrantView
from ...types import Response


def build_request(
    organization_id: str,
    grant_id: str,
    *,
    body: GrantUpdate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/organizations/{organization_id}/grants/{grant_id}".format(
            organization_id=quote(str(organization_id), safe=""),
            grant_id=quote(str(grant_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | GrantView:
    if response.status_code == 200:
        response_200 = GrantView.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | GrantView]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    grant_id: str,
    *,
    client: AuthenticatedClient,
    body: GrantUpdate,
) -> Response[ErrorEnvelope | GrantView]:
    """Change Organization Grant

     The grant is replaced: the result carries its new ID.

    Args:
        organization_id (str):
        grant_id (str):
        body (GrantUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GrantView]
    """

    kwargs = build_request(
        organization_id=organization_id,
        grant_id=grant_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    grant_id: str,
    *,
    client: AuthenticatedClient,
    body: GrantUpdate,
) -> ErrorEnvelope | GrantView | None:
    """Change Organization Grant

     The grant is replaced: the result carries its new ID.

    Args:
        organization_id (str):
        grant_id (str):
        body (GrantUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GrantView
    """

    return sync_detailed(
        organization_id=organization_id,
        grant_id=grant_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    grant_id: str,
    *,
    client: AuthenticatedClient,
    body: GrantUpdate,
) -> Response[ErrorEnvelope | GrantView]:
    """Change Organization Grant

     The grant is replaced: the result carries its new ID.

    Args:
        organization_id (str):
        grant_id (str):
        body (GrantUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | GrantView]
    """

    kwargs = build_request(
        organization_id=organization_id,
        grant_id=grant_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    grant_id: str,
    *,
    client: AuthenticatedClient,
    body: GrantUpdate,
) -> ErrorEnvelope | GrantView | None:
    """Change Organization Grant

     The grant is replaced: the result carries its new ID.

    Args:
        organization_id (str):
        grant_id (str):
        body (GrantUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | GrantView
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            grant_id=grant_id,
            client=client,
            body=body,
        )
    ).parsed
