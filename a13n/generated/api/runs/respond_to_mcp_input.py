from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.mcp_input_response import McpInputResponse
from ...types import UNSET, Response, Unset


def build_request(
    run_id: str,
    request_id: str,
    *,
    body: McpInputResponse,
    x_workspace_id: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-ID"] = x_workspace_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/runs/{run_id}/mcp-inputs/{request_id}/response".format(
            run_id=quote(str(run_id), safe=""),
            request_id=quote(str(request_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorEnvelope:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ErrorEnvelope]:
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
    run_id: str,
    request_id: str,
    *,
    client: AuthenticatedClient,
    body: McpInputResponse,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[Any | ErrorEnvelope]:
    """Respond To Mcp Input

     Send one answer to the originating MCP task, without resuming the run.

    Args:
        run_id (str):
        request_id (str):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (McpInputResponse):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorEnvelope]
    """

    kwargs = build_request(
        run_id=run_id,
        request_id=request_id,
        body=body,
        x_workspace_id=x_workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    run_id: str,
    request_id: str,
    *,
    client: AuthenticatedClient,
    body: McpInputResponse,
    x_workspace_id: str | Unset | None = UNSET,
) -> Any | ErrorEnvelope | None:
    """Respond To Mcp Input

     Send one answer to the originating MCP task, without resuming the run.

    Args:
        run_id (str):
        request_id (str):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (McpInputResponse):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorEnvelope
    """

    return sync_detailed(
        run_id=run_id,
        request_id=request_id,
        client=client,
        body=body,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    run_id: str,
    request_id: str,
    *,
    client: AuthenticatedClient,
    body: McpInputResponse,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[Any | ErrorEnvelope]:
    """Respond To Mcp Input

     Send one answer to the originating MCP task, without resuming the run.

    Args:
        run_id (str):
        request_id (str):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (McpInputResponse):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorEnvelope]
    """

    kwargs = build_request(
        run_id=run_id,
        request_id=request_id,
        body=body,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    run_id: str,
    request_id: str,
    *,
    client: AuthenticatedClient,
    body: McpInputResponse,
    x_workspace_id: str | Unset | None = UNSET,
) -> Any | ErrorEnvelope | None:
    """Respond To Mcp Input

     Send one answer to the originating MCP task, without resuming the run.

    Args:
        run_id (str):
        request_id (str):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (McpInputResponse):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            run_id=run_id,
            request_id=request_id,
            client=client,
            body=body,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
