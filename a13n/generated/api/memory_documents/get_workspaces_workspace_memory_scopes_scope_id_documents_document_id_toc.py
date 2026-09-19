from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.document_heading import DocumentHeading
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def build_request(
    workspace: str,
    scope_id: str,
    document_id: str,
    *,
    version: int | Unset | None = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_version: int | Unset | None
    if isinstance(version, Unset):
        json_version = UNSET
    else:
        json_version = version
    params["version"] = json_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/workspaces/{workspace}/memory-scopes/{scope_id}/documents/{document_id}/toc".format(
            workspace=quote(str(workspace), safe=""),
            scope_id=quote(str(scope_id), safe=""),
            document_id=quote(str(document_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | list[DocumentHeading]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = DocumentHeading.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | list[DocumentHeading]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace: str,
    scope_id: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
    version: int | Unset | None = UNSET,
) -> Response[ErrorResponse | list[DocumentHeading]]:
    """Toc

    Args:
        workspace (str):
        scope_id (str):
        document_id (str):
        version (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | list[DocumentHeading]]
    """

    kwargs = build_request(
        workspace=workspace,
        scope_id=scope_id,
        document_id=document_id,
        version=version,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace: str,
    scope_id: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
    version: int | Unset | None = UNSET,
) -> ErrorResponse | list[DocumentHeading] | None:
    """Toc

    Args:
        workspace (str):
        scope_id (str):
        document_id (str):
        version (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | list[DocumentHeading]
    """

    return sync_detailed(
        workspace=workspace,
        scope_id=scope_id,
        document_id=document_id,
        client=client,
        version=version,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    scope_id: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
    version: int | Unset | None = UNSET,
) -> Response[ErrorResponse | list[DocumentHeading]]:
    """Toc

    Args:
        workspace (str):
        scope_id (str):
        document_id (str):
        version (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | list[DocumentHeading]]
    """

    kwargs = build_request(
        workspace=workspace,
        scope_id=scope_id,
        document_id=document_id,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    scope_id: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
    version: int | Unset | None = UNSET,
) -> ErrorResponse | list[DocumentHeading] | None:
    """Toc

    Args:
        workspace (str):
        scope_id (str):
        document_id (str):
        version (int | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | list[DocumentHeading]
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            scope_id=scope_id,
            document_id=document_id,
            client=client,
            version=version,
        )
    ).parsed
