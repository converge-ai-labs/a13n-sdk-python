from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.agent_revision import AgentRevision
from ...models.error_envelope import ErrorEnvelope
from ...types import Response


def build_request(
    workspace_id: str,
    agent_id: str,
    revision_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/workspaces/{workspace_id}/agents/{agent_id}/revisions/{revision_id}".format(
            workspace_id=quote(str(workspace_id), safe=""),
            agent_id=quote(str(agent_id), safe=""),
            revision_id=quote(str(revision_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AgentRevision | ErrorEnvelope:
    if response.status_code == 200:
        response_200 = AgentRevision.from_dict(response.json())

        return response_200

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
    revision_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AgentRevision | ErrorEnvelope]:
    """Get Revision

    Args:
        workspace_id (str):
        agent_id (str):
        revision_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentRevision | ErrorEnvelope]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        agent_id=agent_id,
        revision_id=revision_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    agent_id: str,
    revision_id: str,
    *,
    client: AuthenticatedClient,
) -> AgentRevision | ErrorEnvelope | None:
    """Get Revision

    Args:
        workspace_id (str):
        agent_id (str):
        revision_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentRevision | ErrorEnvelope
    """

    return sync_detailed(
        workspace_id=workspace_id,
        agent_id=agent_id,
        revision_id=revision_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    agent_id: str,
    revision_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[AgentRevision | ErrorEnvelope]:
    """Get Revision

    Args:
        workspace_id (str):
        agent_id (str):
        revision_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentRevision | ErrorEnvelope]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        agent_id=agent_id,
        revision_id=revision_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    agent_id: str,
    revision_id: str,
    *,
    client: AuthenticatedClient,
) -> AgentRevision | ErrorEnvelope | None:
    """Get Revision

    Args:
        workspace_id (str):
        agent_id (str):
        revision_id (str):

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
            revision_id=revision_id,
            client=client,
        )
    ).parsed
