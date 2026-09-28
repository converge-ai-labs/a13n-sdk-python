from http import HTTPStatus
from io import BytesIO
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...types import UNSET, File, Response, Unset


def build_request(
    skill_id: str,
    revision_id: str,
    path: str,
    *,
    x_workspace_id: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-ID"] = x_workspace_id

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/skills/{skill_id}/revisions/{revision_id}/files/{path}".format(
            skill_id=quote(str(skill_id), safe=""),
            revision_id=quote(str(revision_id), safe=""),
            path=quote(str(path), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | File:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | File]:
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
    skill_id: str,
    revision_id: str,
    path: str,
    *,
    client: AuthenticatedClient,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | File]:
    """Read File

     One package file, by the path the revision's manifest lists.

    Args:
        skill_id (str):
        revision_id (str):
        path (str):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | File]
    """

    kwargs = build_request(
        skill_id=skill_id,
        revision_id=revision_id,
        path=path,
        x_workspace_id=x_workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    skill_id: str,
    revision_id: str,
    path: str,
    *,
    client: AuthenticatedClient,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | File | None:
    """Read File

     One package file, by the path the revision's manifest lists.

    Args:
        skill_id (str):
        revision_id (str):
        path (str):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | File
    """

    return sync_detailed(
        skill_id=skill_id,
        revision_id=revision_id,
        path=path,
        client=client,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    skill_id: str,
    revision_id: str,
    path: str,
    *,
    client: AuthenticatedClient,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | File]:
    """Read File

     One package file, by the path the revision's manifest lists.

    Args:
        skill_id (str):
        revision_id (str):
        path (str):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | File]
    """

    kwargs = build_request(
        skill_id=skill_id,
        revision_id=revision_id,
        path=path,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    skill_id: str,
    revision_id: str,
    path: str,
    *,
    client: AuthenticatedClient,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | File | None:
    """Read File

     One package file, by the path the revision's manifest lists.

    Args:
        skill_id (str):
        revision_id (str):
        path (str):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | File
    """

    return (
        await asyncio_detailed(
            skill_id=skill_id,
            revision_id=revision_id,
            path=path,
            client=client,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
