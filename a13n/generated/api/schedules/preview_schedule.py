from http import HTTPStatus
from typing import Any

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.schedule_preview import SchedulePreview
from ...models.schedule_preview_request import SchedulePreviewRequest
from ...types import UNSET, Response, Unset


def build_request(
    *,
    body: SchedulePreviewRequest,
    x_workspace_id: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-ID"] = x_workspace_id

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/schedules/preview",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | SchedulePreview:
    if response.status_code == 200:
        response_200 = SchedulePreview.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | SchedulePreview]:
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
    *,
    client: AuthenticatedClient,
    body: SchedulePreviewRequest,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | SchedulePreview]:
    """Preview Schedule

    Args:
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (SchedulePreviewRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | SchedulePreview]
    """

    kwargs = build_request(
        body=body,
        x_workspace_id=x_workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: SchedulePreviewRequest,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | SchedulePreview | None:
    """Preview Schedule

    Args:
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (SchedulePreviewRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | SchedulePreview
    """

    return sync_detailed(
        client=client,
        body=body,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SchedulePreviewRequest,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | SchedulePreview]:
    """Preview Schedule

    Args:
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (SchedulePreviewRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | SchedulePreview]
    """

    kwargs = build_request(
        body=body,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SchedulePreviewRequest,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | SchedulePreview | None:
    """Preview Schedule

    Args:
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.
        body (SchedulePreviewRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | SchedulePreview
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
