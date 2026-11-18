from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.client_environment import ClientEnvironment
from ...models.error_envelope import ErrorEnvelope
from ...models.status_change import StatusChange
from ...types import UNSET, Response, Unset


def build_request(
    environment_id: str,
    *,
    body: StatusChange,
    if_match: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-ID"] = x_workspace_id

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/client-environments/{environment_id}/status".format(
            environment_id=quote(str(environment_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ClientEnvironment | ErrorEnvelope:
    if response.status_code == 200:
        response_200 = ClientEnvironment.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ClientEnvironment | ErrorEnvelope]:
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
    environment_id: str,
    *,
    client: AuthenticatedClient,
    body: StatusChange,
    if_match: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ClientEnvironment | ErrorEnvelope]:
    """Change Client Environment Status

    Args:
        environment_id (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current
            view, `"{key}:{version}"` for a model
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (StatusChange):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClientEnvironment | ErrorEnvelope]
    """

    kwargs = build_request(
        environment_id=environment_id,
        body=body,
        if_match=if_match,
        x_workspace_id=x_workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    body: StatusChange,
    if_match: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ClientEnvironment | ErrorEnvelope | None:
    """Change Client Environment Status

    Args:
        environment_id (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current
            view, `"{key}:{version}"` for a model
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (StatusChange):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClientEnvironment | ErrorEnvelope
    """

    return sync_detailed(
        environment_id=environment_id,
        client=client,
        body=body,
        if_match=if_match,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    body: StatusChange,
    if_match: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ClientEnvironment | ErrorEnvelope]:
    """Change Client Environment Status

    Args:
        environment_id (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current
            view, `"{key}:{version}"` for a model
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (StatusChange):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ClientEnvironment | ErrorEnvelope]
    """

    kwargs = build_request(
        environment_id=environment_id,
        body=body,
        if_match=if_match,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    body: StatusChange,
    if_match: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ClientEnvironment | ErrorEnvelope | None:
    """Change Client Environment Status

    Args:
        environment_id (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current
            view, `"{key}:{version}"` for a model
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (StatusChange):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ClientEnvironment | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            client=client,
            body=body,
            if_match=if_match,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
