from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.upload import Upload
from ...models.upload_create import UploadCreate
from ...types import Response


def build_request(
    workspace_id: str,
    *,
    body: UploadCreate,
    idempotency_key: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Idempotency-Key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/workspaces/{workspace_id}/uploads".format(
            workspace_id=quote(str(workspace_id), safe=""),
        ),
    }

    _kwargs["files"] = body.to_multipart()

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | Upload:
    if response.status_code == 200:
        response_200 = Upload.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | Upload]:
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
    *,
    client: AuthenticatedClient,
    body: UploadCreate,
    idempotency_key: str,
) -> Response[ErrorEnvelope | Upload]:
    """Create Upload

     Repeating a request with the same `Idempotency-Key` and bytes returns the same upload.

    Args:
        workspace_id (str):
        idempotency_key (str):
        body (UploadCreate): The multipart form: one file part named `file`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | Upload]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    body: UploadCreate,
    idempotency_key: str,
) -> ErrorEnvelope | Upload | None:
    """Create Upload

     Repeating a request with the same `Idempotency-Key` and bytes returns the same upload.

    Args:
        workspace_id (str):
        idempotency_key (str):
        body (UploadCreate): The multipart form: one file part named `file`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | Upload
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    body: UploadCreate,
    idempotency_key: str,
) -> Response[ErrorEnvelope | Upload]:
    """Create Upload

     Repeating a request with the same `Idempotency-Key` and bytes returns the same upload.

    Args:
        workspace_id (str):
        idempotency_key (str):
        body (UploadCreate): The multipart form: one file part named `file`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | Upload]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    body: UploadCreate,
    idempotency_key: str,
) -> ErrorEnvelope | Upload | None:
    """Create Upload

     Repeating a request with the same `Idempotency-Key` and bytes returns the same upload.

    Args:
        workspace_id (str):
        idempotency_key (str):
        body (UploadCreate): The multipart form: one file part named `file`.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | Upload
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
