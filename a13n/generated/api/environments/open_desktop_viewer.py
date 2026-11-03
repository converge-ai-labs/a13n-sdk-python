from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.desktop_viewer import DesktopViewer
from ...models.error_envelope import ErrorEnvelope
from ...models.open_viewer import OpenViewer
from ...types import UNSET, Response, Unset


def build_request(
    environment_id: str,
    *,
    body: OpenViewer,
    x_workspace_id: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-ID"] = x_workspace_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/environments/{environment_id}/desktop-viewer".format(
            environment_id=quote(str(environment_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DesktopViewer | ErrorEnvelope:
    if response.status_code == 200:
        response_200 = DesktopViewer.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[DesktopViewer | ErrorEnvelope]:
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
    environment_id: str,
    *,
    client: AuthenticatedClient,
    body: OpenViewer,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[DesktopViewer | ErrorEnvelope]:
    """Open Desktop Viewer

    Args:
        environment_id (str):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (OpenViewer):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DesktopViewer | ErrorEnvelope]
    """

    kwargs = build_request(
        environment_id=environment_id,
        body=body,
        x_workspace_id=x_workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    body: OpenViewer,
    x_workspace_id: str | Unset | None = UNSET,
) -> DesktopViewer | ErrorEnvelope | None:
    """Open Desktop Viewer

    Args:
        environment_id (str):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (OpenViewer):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DesktopViewer | ErrorEnvelope
    """

    return sync_detailed(
        environment_id=environment_id,
        client=client,
        body=body,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    body: OpenViewer,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[DesktopViewer | ErrorEnvelope]:
    """Open Desktop Viewer

    Args:
        environment_id (str):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (OpenViewer):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DesktopViewer | ErrorEnvelope]
    """

    kwargs = build_request(
        environment_id=environment_id,
        body=body,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    body: OpenViewer,
    x_workspace_id: str | Unset | None = UNSET,
) -> DesktopViewer | ErrorEnvelope | None:
    """Open Desktop Viewer

    Args:
        environment_id (str):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (OpenViewer):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DesktopViewer | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            client=client,
            body=body,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
