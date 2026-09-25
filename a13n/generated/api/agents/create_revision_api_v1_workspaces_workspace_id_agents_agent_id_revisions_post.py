from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.agent_revision import AgentRevision
from ...models.agent_revision_create import AgentRevisionCreate
from ...models.error_envelope import ErrorEnvelope
from ...types import UNSET, Response, Unset


def build_request(
    workspace_id: str,
    agent_id: str,
    *,
    body: AgentRevisionCreate,
    if_match: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/workspaces/{workspace_id}/agents/{agent_id}/revisions".format(
            workspace_id=quote(str(workspace_id), safe=""),
            agent_id=quote(str(agent_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AgentRevision | ErrorEnvelope:
    if response.status_code == 201:
        response_201 = AgentRevision.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AgentRevision | ErrorEnvelope]:
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
    workspace_id: str,
    agent_id: str,
    *,
    client: AuthenticatedClient,
    body: AgentRevisionCreate,
    if_match: str | Unset | None = UNSET,
) -> Response[AgentRevision | ErrorEnvelope]:
    """Create Revision

     A configuration that validates to the default revision's creates nothing and returns that revision.

    Args:
        workspace_id (str):
        agent_id (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current view
        body (AgentRevisionCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentRevision | ErrorEnvelope]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        agent_id=agent_id,
        body=body,
        if_match=if_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    agent_id: str,
    *,
    client: AuthenticatedClient,
    body: AgentRevisionCreate,
    if_match: str | Unset | None = UNSET,
) -> AgentRevision | ErrorEnvelope | None:
    """Create Revision

     A configuration that validates to the default revision's creates nothing and returns that revision.

    Args:
        workspace_id (str):
        agent_id (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current view
        body (AgentRevisionCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentRevision | ErrorEnvelope
    """

    return sync_detailed(
        workspace_id=workspace_id,
        agent_id=agent_id,
        client=client,
        body=body,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    agent_id: str,
    *,
    client: AuthenticatedClient,
    body: AgentRevisionCreate,
    if_match: str | Unset | None = UNSET,
) -> Response[AgentRevision | ErrorEnvelope]:
    """Create Revision

     A configuration that validates to the default revision's creates nothing and returns that revision.

    Args:
        workspace_id (str):
        agent_id (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current view
        body (AgentRevisionCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentRevision | ErrorEnvelope]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        agent_id=agent_id,
        body=body,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    agent_id: str,
    *,
    client: AuthenticatedClient,
    body: AgentRevisionCreate,
    if_match: str | Unset | None = UNSET,
) -> AgentRevision | ErrorEnvelope | None:
    """Create Revision

     A configuration that validates to the default revision's creates nothing and returns that revision.

    Args:
        workspace_id (str):
        agent_id (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current view
        body (AgentRevisionCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentRevision | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            agent_id=agent_id,
            client=client,
            body=body,
            if_match=if_match,
        )
    ).parsed
