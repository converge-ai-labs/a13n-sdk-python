from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.invitation_accept import InvitationAccept
from ...models.login_output import LoginOutput
from ...types import Response


def build_request(
    invitation_id: str,
    *,
    body: InvitationAccept,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/invitations/{invitation_id}/accept".format(
            invitation_id=quote(str(invitation_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | LoginOutput:
    if response.status_code == 200:
        response_200 = LoginOutput.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | LoginOutput]:
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
    invitation_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: InvitationAccept,
) -> Response[ErrorEnvelope | LoginOutput]:
    """Accept

     Public by token: creates or joins the invited account and starts a login session.

    Args:
        invitation_id (str):
        body (InvitationAccept):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | LoginOutput]
    """

    kwargs = build_request(
        invitation_id=invitation_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    invitation_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: InvitationAccept,
) -> ErrorEnvelope | LoginOutput | None:
    """Accept

     Public by token: creates or joins the invited account and starts a login session.

    Args:
        invitation_id (str):
        body (InvitationAccept):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | LoginOutput
    """

    return sync_detailed(
        invitation_id=invitation_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    invitation_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: InvitationAccept,
) -> Response[ErrorEnvelope | LoginOutput]:
    """Accept

     Public by token: creates or joins the invited account and starts a login session.

    Args:
        invitation_id (str):
        body (InvitationAccept):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | LoginOutput]
    """

    kwargs = build_request(
        invitation_id=invitation_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    invitation_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: InvitationAccept,
) -> ErrorEnvelope | LoginOutput | None:
    """Accept

     Public by token: creates or joins the invited account and starts a login session.

    Args:
        invitation_id (str):
        body (InvitationAccept):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | LoginOutput
    """

    return (
        await asyncio_detailed(
            invitation_id=invitation_id,
            client=client,
            body=body,
        )
    ).parsed
