from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.finding import Finding
from ...models.finding_update import FindingUpdate
from ...types import UNSET, Response, Unset


def build_request(
    finding_id: str,
    *,
    body: FindingUpdate,
    if_match: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(if_match, Unset):
        headers["If-Match"] = if_match

    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-ID"] = x_workspace_id

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/findings/{finding_id}".format(
            finding_id=quote(str(finding_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | Finding:
    if response.status_code == 200:
        response_200 = Finding.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | Finding]:
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
    finding_id: str,
    *,
    client: AuthenticatedClient,
    body: FindingUpdate,
    if_match: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | Finding]:
    """Update Finding

    Args:
        finding_id (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current
            view, `"{key}:{version}"` for a model
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (FindingUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | Finding]
    """

    kwargs = build_request(
        finding_id=finding_id,
        body=body,
        if_match=if_match,
        x_workspace_id=x_workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    finding_id: str,
    *,
    client: AuthenticatedClient,
    body: FindingUpdate,
    if_match: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | Finding | None:
    """Update Finding

    Args:
        finding_id (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current
            view, `"{key}:{version}"` for a model
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (FindingUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | Finding
    """

    return sync_detailed(
        finding_id=finding_id,
        client=client,
        body=body,
        if_match=if_match,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    finding_id: str,
    *,
    client: AuthenticatedClient,
    body: FindingUpdate,
    if_match: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | Finding]:
    """Update Finding

    Args:
        finding_id (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current
            view, `"{key}:{version}"` for a model
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (FindingUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | Finding]
    """

    kwargs = build_request(
        finding_id=finding_id,
        body=body,
        if_match=if_match,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    finding_id: str,
    *,
    client: AuthenticatedClient,
    body: FindingUpdate,
    if_match: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | Finding | None:
    """Update Finding

    Args:
        finding_id (str):
        if_match (None | str | Unset): The resource's ETag: `"{id}:{version}"` of its current
            view, `"{key}:{version}"` for a model
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (FindingUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | Finding
    """

    return (
        await asyncio_detailed(
            finding_id=finding_id,
            client=client,
            body=body,
            if_match=if_match,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
