from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.environment_query import EnvironmentQuery
from ...models.error_envelope import ErrorEnvelope
from ...models.local_result import LocalResult
from ...models.query_result import QueryResult
from ...types import UNSET, Response, Unset


def build_request(
    device_id: str,
    *,
    body: EnvironmentQuery,
    x_workspace_id: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-ID"] = x_workspace_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/devices/{device_id}/metrics/query".format(
            device_id=quote(str(device_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | LocalResult | QueryResult:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> LocalResult | QueryResult:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = QueryResult.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = LocalResult.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | LocalResult | QueryResult]:
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
    device_id: str,
    *,
    client: AuthenticatedClient,
    body: EnvironmentQuery,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | LocalResult | QueryResult]:
    """Query Device Metrics

    Args:
        device_id (str):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (EnvironmentQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | LocalResult | QueryResult]
    """

    kwargs = build_request(
        device_id=device_id,
        body=body,
        x_workspace_id=x_workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    device_id: str,
    *,
    client: AuthenticatedClient,
    body: EnvironmentQuery,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | LocalResult | QueryResult | None:
    """Query Device Metrics

    Args:
        device_id (str):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (EnvironmentQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | LocalResult | QueryResult
    """

    return sync_detailed(
        device_id=device_id,
        client=client,
        body=body,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    device_id: str,
    *,
    client: AuthenticatedClient,
    body: EnvironmentQuery,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | LocalResult | QueryResult]:
    """Query Device Metrics

    Args:
        device_id (str):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (EnvironmentQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | LocalResult | QueryResult]
    """

    kwargs = build_request(
        device_id=device_id,
        body=body,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    device_id: str,
    *,
    client: AuthenticatedClient,
    body: EnvironmentQuery,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | LocalResult | QueryResult | None:
    """Query Device Metrics

    Args:
        device_id (str):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (EnvironmentQuery):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | LocalResult | QueryResult
    """

    return (
        await asyncio_detailed(
            device_id=device_id,
            client=client,
            body=body,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
