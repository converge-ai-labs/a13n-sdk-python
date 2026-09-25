from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...types import Response


def build_request(
    organization_id: str,
    grant_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/organizations/{organization_id}/grants/{grant_id}".format(
            organization_id=quote(str(organization_id), safe=""),
            grant_id=quote(str(grant_id), safe=""),
        ),
    }

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
    organization_id: str,
    grant_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ErrorEnvelope]:
    """Delete Organization Grant

    Args:
        organization_id (str):
        grant_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorEnvelope]
    """

    kwargs = build_request(
        organization_id=organization_id,
        grant_id=grant_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    grant_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | ErrorEnvelope | None:
    """Delete Organization Grant

    Args:
        organization_id (str):
        grant_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorEnvelope
    """

    return sync_detailed(
        organization_id=organization_id,
        grant_id=grant_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    grant_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ErrorEnvelope]:
    """Delete Organization Grant

    Args:
        organization_id (str):
        grant_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorEnvelope]
    """

    kwargs = build_request(
        organization_id=organization_id,
        grant_id=grant_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    grant_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | ErrorEnvelope | None:
    """Delete Organization Grant

    Args:
        organization_id (str):
        grant_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            grant_id=grant_id,
            client=client,
        )
    ).parsed
