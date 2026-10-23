from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.access import Access
from ...models.control import Control
from ...models.error_envelope import ErrorEnvelope
from ...types import UNSET, Response, Unset


def build_request(
    assistance_id: str,
    *,
    body: Control,
    renew: bool | Unset = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-ID"] = x_workspace_id

    params: dict[str, Any] = {}

    params["renew"] = renew

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/desktop-assistance/{assistance_id}/control".format(
            assistance_id=quote(str(assistance_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Access | ErrorEnvelope:
    if response.status_code == 200:
        response_200 = Access.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Access | ErrorEnvelope]:
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
    assistance_id: str,
    *,
    client: AuthenticatedClient,
    body: Control,
    renew: bool | Unset = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[Access | ErrorEnvelope]:
    """Control Desktop

    Args:
        assistance_id (str):
        renew (bool | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (Control):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Access | ErrorEnvelope]
    """

    kwargs = build_request(
        assistance_id=assistance_id,
        body=body,
        renew=renew,
        x_workspace_id=x_workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    assistance_id: str,
    *,
    client: AuthenticatedClient,
    body: Control,
    renew: bool | Unset = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Access | ErrorEnvelope | None:
    """Control Desktop

    Args:
        assistance_id (str):
        renew (bool | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (Control):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Access | ErrorEnvelope
    """

    return sync_detailed(
        assistance_id=assistance_id,
        client=client,
        body=body,
        renew=renew,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    assistance_id: str,
    *,
    client: AuthenticatedClient,
    body: Control,
    renew: bool | Unset = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[Access | ErrorEnvelope]:
    """Control Desktop

    Args:
        assistance_id (str):
        renew (bool | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (Control):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Access | ErrorEnvelope]
    """

    kwargs = build_request(
        assistance_id=assistance_id,
        body=body,
        renew=renew,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    assistance_id: str,
    *,
    client: AuthenticatedClient,
    body: Control,
    renew: bool | Unset = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Access | ErrorEnvelope | None:
    """Control Desktop

    Args:
        assistance_id (str):
        renew (bool | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (Control):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Access | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            assistance_id=assistance_id,
            client=client,
            body=body,
            renew=renew,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
