from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.skill import Skill
from ...types import UNSET, Response, Unset


def build_request(
    workspace_id: str,
    skill_id: str,
    *,
    if_match: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/workspaces/{workspace_id}/skills/{skill_id}/unarchive".format(
            workspace_id=quote(str(workspace_id), safe=""),
            skill_id=quote(str(skill_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | Skill:
    if response.status_code == 200:
        response_200 = Skill.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | Skill]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    skill_id: str,
    *,
    client: AuthenticatedClient,
    if_match: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | Skill]:
    """Unarchive Skill

    Args:
        workspace_id (str):
        skill_id (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current view

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | Skill]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        skill_id=skill_id,
        if_match=if_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    skill_id: str,
    *,
    client: AuthenticatedClient,
    if_match: str | Unset | None = UNSET,
) -> ErrorEnvelope | Skill | None:
    """Unarchive Skill

    Args:
        workspace_id (str):
        skill_id (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current view

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | Skill
    """

    return sync_detailed(
        workspace_id=workspace_id,
        skill_id=skill_id,
        client=client,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    skill_id: str,
    *,
    client: AuthenticatedClient,
    if_match: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | Skill]:
    """Unarchive Skill

    Args:
        workspace_id (str):
        skill_id (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current view

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | Skill]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        skill_id=skill_id,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    skill_id: str,
    *,
    client: AuthenticatedClient,
    if_match: str | Unset | None = UNSET,
) -> ErrorEnvelope | Skill | None:
    """Unarchive Skill

    Args:
        workspace_id (str):
        skill_id (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current view

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | Skill
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            skill_id=skill_id,
            client=client,
            if_match=if_match,
        )
    ).parsed
