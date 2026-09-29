from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...types import UNSET, Response, Unset


def build_request(
    thread_id: str,
    *,
    run: str | Unset | None = UNSET,
    position: str | Unset | None = UNSET,
    last_event_id: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(last_event_id, Unset):
        headers["Last-Event-ID"] = last_event_id

    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-ID"] = x_workspace_id

    params: dict[str, Any] = {}

    json_run: str | Unset | None
    if isinstance(run, Unset):
        json_run = UNSET
    else:
        json_run = run
    params["run"] = json_run

    json_position: str | Unset | None
    if isinstance(position, Unset):
        json_position = UNSET
    else:
        json_position = position
    params["position"] = json_position

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/threads/{thread_id}/stream".format(
            thread_id=quote(str(thread_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorEnvelope:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

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
    thread_id: str,
    *,
    client: AuthenticatedClient,
    run: str | Unset | None = UNSET,
    position: str | Unset | None = UNSET,
    last_event_id: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[Any | ErrorEnvelope]:
    """Thread Stream

     Live output of the thread's runs over SSE: `delta` and `boundary` frames with `changed`, `reset`,
    `gap`.

    Args:
        thread_id (str):
        run (None | str | Unset):
        position (None | str | Unset):
        last_event_id (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorEnvelope]
    """

    kwargs = build_request(
        thread_id=thread_id,
        run=run,
        position=position,
        last_event_id=last_event_id,
        x_workspace_id=x_workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    thread_id: str,
    *,
    client: AuthenticatedClient,
    run: str | Unset | None = UNSET,
    position: str | Unset | None = UNSET,
    last_event_id: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Any | ErrorEnvelope | None:
    """Thread Stream

     Live output of the thread's runs over SSE: `delta` and `boundary` frames with `changed`, `reset`,
    `gap`.

    Args:
        thread_id (str):
        run (None | str | Unset):
        position (None | str | Unset):
        last_event_id (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorEnvelope
    """

    return sync_detailed(
        thread_id=thread_id,
        client=client,
        run=run,
        position=position,
        last_event_id=last_event_id,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    thread_id: str,
    *,
    client: AuthenticatedClient,
    run: str | Unset | None = UNSET,
    position: str | Unset | None = UNSET,
    last_event_id: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[Any | ErrorEnvelope]:
    """Thread Stream

     Live output of the thread's runs over SSE: `delta` and `boundary` frames with `changed`, `reset`,
    `gap`.

    Args:
        thread_id (str):
        run (None | str | Unset):
        position (None | str | Unset):
        last_event_id (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorEnvelope]
    """

    kwargs = build_request(
        thread_id=thread_id,
        run=run,
        position=position,
        last_event_id=last_event_id,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    thread_id: str,
    *,
    client: AuthenticatedClient,
    run: str | Unset | None = UNSET,
    position: str | Unset | None = UNSET,
    last_event_id: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Any | ErrorEnvelope | None:
    """Thread Stream

     Live output of the thread's runs over SSE: `delta` and `boundary` frames with `changed`, `reset`,
    `gap`.

    Args:
        thread_id (str):
        run (None | str | Unset):
        position (None | str | Unset):
        last_event_id (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            thread_id=thread_id,
            client=client,
            run=run,
            position=position,
            last_event_id=last_event_id,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
