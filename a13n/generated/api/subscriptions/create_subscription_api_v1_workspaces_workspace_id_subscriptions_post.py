from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.created_subscription import CreatedSubscription
from ...models.error_envelope import ErrorEnvelope
from ...models.subscription_create import SubscriptionCreate
from ...types import Response


def build_request(
    workspace_id: str,
    *,
    body: SubscriptionCreate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/workspaces/{workspace_id}/subscriptions".format(
            workspace_id=quote(str(workspace_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreatedSubscription | ErrorEnvelope:
    if response.status_code == 201:
        response_201 = CreatedSubscription.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreatedSubscription | ErrorEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    body: SubscriptionCreate,
) -> Response[CreatedSubscription | ErrorEnvelope]:
    """Create Subscription

     The response is the only time the signing secret is returned.

    Args:
        workspace_id (str):
        body (SubscriptionCreate): Without `signing_secret` the service generates one; either way
            it is returned only by this request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatedSubscription | ErrorEnvelope]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    body: SubscriptionCreate,
) -> CreatedSubscription | ErrorEnvelope | None:
    """Create Subscription

     The response is the only time the signing secret is returned.

    Args:
        workspace_id (str):
        body (SubscriptionCreate): Without `signing_secret` the service generates one; either way
            it is returned only by this request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatedSubscription | ErrorEnvelope
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    body: SubscriptionCreate,
) -> Response[CreatedSubscription | ErrorEnvelope]:
    """Create Subscription

     The response is the only time the signing secret is returned.

    Args:
        workspace_id (str):
        body (SubscriptionCreate): Without `signing_secret` the service generates one; either way
            it is returned only by this request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatedSubscription | ErrorEnvelope]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    body: SubscriptionCreate,
) -> CreatedSubscription | ErrorEnvelope | None:
    """Create Subscription

     The response is the only time the signing secret is returned.

    Args:
        workspace_id (str):
        body (SubscriptionCreate): Without `signing_secret` the service generates one; either way
            it is returned only by this request.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatedSubscription | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            body=body,
        )
    ).parsed
