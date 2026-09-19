from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.directory_list_result import DirectoryListResult
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def build_request(
    environment_id: str,
    *,
    path: str | Unset | None = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_path: str | Unset | None
    if isinstance(path, Unset):
        json_path = UNSET
    else:
        json_path = path
    params["path"] = json_path

    params["offset"] = offset

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/environments/{environment_id}/directories".format(
            environment_id=quote(str(environment_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> DirectoryListResult | ErrorResponse:
    if response.status_code == 200:
        response_200 = DirectoryListResult.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DirectoryListResult | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    path: str | Unset | None = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[DirectoryListResult | ErrorResponse]:
    """Device Directories

    Args:
        environment_id (str):
        path (None | str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DirectoryListResult | ErrorResponse]
    """

    kwargs = build_request(
        environment_id=environment_id,
        path=path,
        offset=offset,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    path: str | Unset | None = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> DirectoryListResult | ErrorResponse | None:
    """Device Directories

    Args:
        environment_id (str):
        path (None | str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DirectoryListResult | ErrorResponse
    """

    return sync_detailed(
        environment_id=environment_id,
        client=client,
        path=path,
        offset=offset,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    path: str | Unset | None = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> Response[DirectoryListResult | ErrorResponse]:
    """Device Directories

    Args:
        environment_id (str):
        path (None | str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DirectoryListResult | ErrorResponse]
    """

    kwargs = build_request(
        environment_id=environment_id,
        path=path,
        offset=offset,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    path: str | Unset | None = UNSET,
    offset: int | Unset = UNSET,
    limit: int | Unset = UNSET,
) -> DirectoryListResult | ErrorResponse | None:
    """Device Directories

    Args:
        environment_id (str):
        path (None | str | Unset):
        offset (int | Unset):
        limit (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DirectoryListResult | ErrorResponse
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            client=client,
            path=path,
            offset=offset,
            limit=limit,
        )
    ).parsed
