from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.cancel_docker_image_request import CancelDockerImageRequest
from ...models.error_response import ErrorResponse
from ...types import Response


def build_request(
    provider_id: str,
    request_id: str,
    *,
    body: CancelDockerImageRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/environment-providers/{provider_id}/test-image/{request_id}/cancel".format(
            provider_id=quote(str(provider_id), safe=""),
            request_id=quote(str(request_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorResponse:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    provider_id: str,
    request_id: str,
    *,
    client: AuthenticatedClient,
    body: CancelDockerImageRequest,
) -> Response[Any | ErrorResponse]:
    """Cancel Image Test

    Args:
        provider_id (str):
        request_id (str):
        body (CancelDockerImageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse]
    """

    kwargs = build_request(
        provider_id=provider_id,
        request_id=request_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    provider_id: str,
    request_id: str,
    *,
    client: AuthenticatedClient,
    body: CancelDockerImageRequest,
) -> Any | ErrorResponse | None:
    """Cancel Image Test

    Args:
        provider_id (str):
        request_id (str):
        body (CancelDockerImageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse
    """

    return sync_detailed(
        provider_id=provider_id,
        request_id=request_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    provider_id: str,
    request_id: str,
    *,
    client: AuthenticatedClient,
    body: CancelDockerImageRequest,
) -> Response[Any | ErrorResponse]:
    """Cancel Image Test

    Args:
        provider_id (str):
        request_id (str):
        body (CancelDockerImageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse]
    """

    kwargs = build_request(
        provider_id=provider_id,
        request_id=request_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    provider_id: str,
    request_id: str,
    *,
    client: AuthenticatedClient,
    body: CancelDockerImageRequest,
) -> Any | ErrorResponse | None:
    """Cancel Image Test

    Args:
        provider_id (str):
        request_id (str):
        body (CancelDockerImageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse
    """

    return (
        await asyncio_detailed(
            provider_id=provider_id,
            request_id=request_id,
            client=client,
            body=body,
        )
    ).parsed
