from http import HTTPStatus
from typing import Any

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.context_usage import ContextUsage
from ...models.error_envelope import ErrorEnvelope
from ...types import UNSET, Response, Unset


def build_request(
    *,
    thread_id: str | Unset | None = UNSET,
    run_id: str | Unset | None = UNSET,
    record_id: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-ID"] = x_workspace_id

    params: dict[str, Any] = {}

    json_thread_id: str | Unset | None
    if isinstance(thread_id, Unset):
        json_thread_id = UNSET
    else:
        json_thread_id = thread_id
    params["thread_id"] = json_thread_id

    json_run_id: str | Unset | None
    if isinstance(run_id, Unset):
        json_run_id = UNSET
    else:
        json_run_id = run_id
    params["run_id"] = json_run_id

    json_record_id: str | Unset | None
    if isinstance(record_id, Unset):
        json_record_id = UNSET
    else:
        json_record_id = record_id
    params["record_id"] = json_record_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/usage/context",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ContextUsage | ErrorEnvelope | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> ContextUsage | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = ContextUsage.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            raise ValueError("Invalid nullable model value")

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ContextUsage | ErrorEnvelope | None]:
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
    *,
    client: AuthenticatedClient,
    thread_id: str | Unset | None = UNSET,
    run_id: str | Unset | None = UNSET,
    record_id: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ContextUsage | ErrorEnvelope | None]:
    """Context Usage

    Args:
        thread_id (None | str | Unset):
        run_id (None | str | Unset):
        record_id (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContextUsage | None | ErrorEnvelope]
    """

    kwargs = build_request(
        thread_id=thread_id,
        run_id=run_id,
        record_id=record_id,
        x_workspace_id=x_workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    thread_id: str | Unset | None = UNSET,
    run_id: str | Unset | None = UNSET,
    record_id: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ContextUsage | None | ErrorEnvelope | None:
    """Context Usage

    Args:
        thread_id (None | str | Unset):
        run_id (None | str | Unset):
        record_id (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContextUsage | None | ErrorEnvelope
    """

    return sync_detailed(
        client=client,
        thread_id=thread_id,
        run_id=run_id,
        record_id=record_id,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    thread_id: str | Unset | None = UNSET,
    run_id: str | Unset | None = UNSET,
    record_id: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ContextUsage | ErrorEnvelope | None]:
    """Context Usage

    Args:
        thread_id (None | str | Unset):
        run_id (None | str | Unset):
        record_id (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContextUsage | None | ErrorEnvelope]
    """

    kwargs = build_request(
        thread_id=thread_id,
        run_id=run_id,
        record_id=record_id,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    thread_id: str | Unset | None = UNSET,
    run_id: str | Unset | None = UNSET,
    record_id: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ContextUsage | None | ErrorEnvelope | None:
    """Context Usage

    Args:
        thread_id (None | str | Unset):
        run_id (None | str | Unset):
        record_id (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContextUsage | None | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            client=client,
            thread_id=thread_id,
            run_id=run_id,
            record_id=record_id,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
