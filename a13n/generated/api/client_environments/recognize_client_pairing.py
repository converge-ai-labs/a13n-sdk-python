from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.pairing import Pairing
from ...models.recognition import Recognition
from ...types import Response


def build_request(
    pairing_id: str,
    *,
    body: Recognition,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/client-environments/pairings/{pairing_id}/recognize".format(
            pairing_id=quote(str(pairing_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | Pairing:
    if response.status_code == 200:
        response_200 = Pairing.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | Pairing]:
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
    pairing_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: Recognition,
) -> Response[ErrorEnvelope | Pairing]:
    """Recognize Client Pairing

    Args:
        pairing_id (str):
        body (Recognition):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | Pairing]
    """

    kwargs = build_request(
        pairing_id=pairing_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    pairing_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: Recognition,
) -> ErrorEnvelope | Pairing | None:
    """Recognize Client Pairing

    Args:
        pairing_id (str):
        body (Recognition):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | Pairing
    """

    return sync_detailed(
        pairing_id=pairing_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    pairing_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: Recognition,
) -> Response[ErrorEnvelope | Pairing]:
    """Recognize Client Pairing

    Args:
        pairing_id (str):
        body (Recognition):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | Pairing]
    """

    kwargs = build_request(
        pairing_id=pairing_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    pairing_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: Recognition,
) -> ErrorEnvelope | Pairing | None:
    """Recognize Client Pairing

    Args:
        pairing_id (str):
        body (Recognition):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | Pairing
    """

    return (
        await asyncio_detailed(
            pairing_id=pairing_id,
            client=client,
            body=body,
        )
    ).parsed
