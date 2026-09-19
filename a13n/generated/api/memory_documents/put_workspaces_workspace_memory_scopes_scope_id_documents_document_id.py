from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.managed_document_mutation import ManagedDocumentMutation
from ...models.revise_document import ReviseDocument
from ...types import Response


def build_request(
    workspace: str,
    scope_id: str,
    document_id: str,
    *,
    body: ReviseDocument,
    idempotency_key: str,
    if_match: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    headers["If-Match"] = if_match

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/workspaces/{workspace}/memory-scopes/{scope_id}/documents/{document_id}".format(
            workspace=quote(str(workspace), safe=""),
            scope_id=quote(str(scope_id), safe=""),
            document_id=quote(str(document_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ManagedDocumentMutation:
    if response.status_code == 200:
        response_200 = ManagedDocumentMutation.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    response_default = ErrorResponse.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | ManagedDocumentMutation]:
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
    body: ReviseDocument,
    idempotency_key: str,
    if_match: str,
) -> Response[ErrorResponse | ManagedDocumentMutation]:
    """Revise

    Args:
        workspace (str):
        scope_id (str):
        document_id (str):
        idempotency_key (str):
        if_match (str):
        body (ReviseDocument):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ManagedDocumentMutation]
    """

    kwargs = build_request(
        workspace=workspace,
        scope_id=scope_id,
        document_id=document_id,
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
    scope_id: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
    body: ReviseDocument,
    idempotency_key: str,
    if_match: str,
) -> ErrorResponse | ManagedDocumentMutation | None:
    """Revise

    Args:
        workspace (str):
        scope_id (str):
        document_id (str):
        idempotency_key (str):
        if_match (str):
        body (ReviseDocument):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ManagedDocumentMutation
    """

    return sync_detailed(
        workspace=workspace,
        scope_id=scope_id,
        document_id=document_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    workspace: str,
    scope_id: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
    body: ReviseDocument,
    idempotency_key: str,
    if_match: str,
) -> Response[ErrorResponse | ManagedDocumentMutation]:
    """Revise

    Args:
        workspace (str):
        scope_id (str):
        document_id (str):
        idempotency_key (str):
        if_match (str):
        body (ReviseDocument):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ManagedDocumentMutation]
    """

    kwargs = build_request(
        workspace=workspace,
        scope_id=scope_id,
        document_id=document_id,
        body=body,
        idempotency_key=idempotency_key,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace: str,
    scope_id: str,
    document_id: str,
    *,
    client: AuthenticatedClient,
    body: ReviseDocument,
    idempotency_key: str,
    if_match: str,
) -> ErrorResponse | ManagedDocumentMutation | None:
    """Revise

    Args:
        workspace (str):
        scope_id (str):
        document_id (str):
        idempotency_key (str):
        if_match (str):
        body (ReviseDocument):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ManagedDocumentMutation
    """

    return (
        await asyncio_detailed(
            workspace=workspace,
            scope_id=scope_id,
            document_id=document_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
            if_match=if_match,
        )
    ).parsed
