from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.agent_revision_create_result import AgentRevisionCreateResult
from ...models.error_response import ErrorResponse
from ...models.set_default_agent_revision_request import SetDefaultAgentRevisionRequest
from ...types import Response


def build_request(
    workspace: str,
    agent: str,
    revision_id: str,
    *,
    body: SetDefaultAgentRevisionRequest,
    idempotency_key: str,
    if_match: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    headers["If-Match"] = if_match

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/workspaces/{workspace}/agents/{agent}/revisions/{revision_id}/default".format(
            workspace=quote(str(workspace), safe=""),
            agent=quote(str(agent), safe=""),
            revision_id=quote(str(revision_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AgentRevisionCreateResult | ErrorResponse:
    if response.status_code == 200:
        response_200 = AgentRevisionCreateResult.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AgentRevisionCreateResult | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace: str,
    agent: str,
    revision_id: str,
    *,
    client: AuthenticatedClient,
    body: SetDefaultAgentRevisionRequest,
    idempotency_key: str,
    if_match: str,
) -> Response[AgentRevisionCreateResult | ErrorResponse]:
    """Set Default Agent Revision

    Args:
        workspace (str):
        agent (str):
        revision_id (str):
        idempotency_key (str):
        if_match (str):
        body (SetDefaultAgentRevisionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentRevisionCreateResult | ErrorResponse]
    """

    kwargs = build_request(
        workspace=workspace,
        agent=agent,
        revision_id=revision_id,
        body=body,
        idempotency_key=idempotency_key,
        if_match=if_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    agent: str,
    revision_id: str,
    *,
    client: AuthenticatedClient,
    body: SetDefaultAgentRevisionRequest,
    idempotency_key: str,
    if_match: str,
) -> AgentRevisionCreateResult | ErrorResponse | None:
    """Set Default Agent Revision

    Args:
        workspace (str):
        agent (str):
        revision_id (str):
        idempotency_key (str):
        if_match (str):
        body (SetDefaultAgentRevisionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentRevisionCreateResult | ErrorResponse
    """

    return sync_detailed(
        workspace=workspace,
        agent=agent,
        revision_id=revision_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    agent: str,
    revision_id: str,
    *,
    client: AuthenticatedClient,
    body: SetDefaultAgentRevisionRequest,
    idempotency_key: str,
    if_match: str,
) -> Response[AgentRevisionCreateResult | ErrorResponse]:
    """Set Default Agent Revision

    Args:
        workspace (str):
        agent (str):
        revision_id (str):
        idempotency_key (str):
        if_match (str):
        body (SetDefaultAgentRevisionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentRevisionCreateResult | ErrorResponse]
    """

    kwargs = build_request(
        workspace=workspace,
        agent=agent,
        revision_id=revision_id,
        body=body,
        idempotency_key=idempotency_key,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    agent: str,
    revision_id: str,
    *,
    client: AuthenticatedClient,
    body: SetDefaultAgentRevisionRequest,
    idempotency_key: str,
    if_match: str,
) -> AgentRevisionCreateResult | ErrorResponse | None:
    """Set Default Agent Revision

    Args:
        workspace (str):
        agent (str):
        revision_id (str):
        idempotency_key (str):
        if_match (str):
        body (SetDefaultAgentRevisionRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentRevisionCreateResult | ErrorResponse
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            agent=agent,
            revision_id=revision_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
            if_match=if_match,
        )
    ).parsed
