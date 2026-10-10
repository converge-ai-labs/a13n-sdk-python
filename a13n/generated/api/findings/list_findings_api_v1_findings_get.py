from http import HTTPStatus
from typing import Any

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.assessment import Assessment
from ...models.category import Category
from ...models.error_envelope import ErrorEnvelope
from ...models.finding_page import FindingPage
from ...models.severity import Severity
from ...types import UNSET, Response, Unset


def build_request(
    *,
    agent_id: str | Unset | None = UNSET,
    category: Category | Unset | None = UNSET,
    severity: Severity | Unset | None = UNSET,
    assessment: Assessment | Unset | None = UNSET,
    closed: bool | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-ID"] = x_workspace_id

    params: dict[str, Any] = {}

    json_agent_id: str | Unset | None
    if isinstance(agent_id, Unset):
        json_agent_id = UNSET
    else:
        json_agent_id = agent_id
    params["agent_id"] = json_agent_id

    json_category: str | Unset | None
    if isinstance(category, Unset):
        json_category = UNSET
    elif isinstance(category, Category):
        json_category = category.value
    else:
        json_category = category
    params["category"] = json_category

    json_severity: str | Unset | None
    if isinstance(severity, Unset):
        json_severity = UNSET
    elif isinstance(severity, Severity):
        json_severity = severity.value
    else:
        json_severity = severity
    params["severity"] = json_severity

    json_assessment: str | Unset | None
    if isinstance(assessment, Unset):
        json_assessment = UNSET
    elif isinstance(assessment, Assessment):
        json_assessment = assessment.value
    else:
        json_assessment = assessment
    params["assessment"] = json_assessment

    json_closed: bool | Unset | None
    if isinstance(closed, Unset):
        json_closed = UNSET
    else:
        json_closed = closed
    params["closed"] = json_closed

    params["limit"] = limit

    json_cursor: str | Unset | None
    if isinstance(cursor, Unset):
        json_cursor = UNSET
    else:
        json_cursor = cursor
    params["cursor"] = json_cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/findings",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | FindingPage:
    if response.status_code == 200:
        response_200 = FindingPage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | FindingPage]:
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
    agent_id: str | Unset | None = UNSET,
    category: Category | Unset | None = UNSET,
    severity: Severity | Unset | None = UNSET,
    assessment: Assessment | Unset | None = UNSET,
    closed: bool | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | FindingPage]:
    """List Findings

    Args:
        agent_id (None | str | Unset):
        category (Category | None | Unset):
        severity (None | Severity | Unset):
        assessment (Assessment | None | Unset):
        closed (bool | None | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | FindingPage]
    """

    kwargs = build_request(
        agent_id=agent_id,
        category=category,
        severity=severity,
        assessment=assessment,
        closed=closed,
        limit=limit,
        cursor=cursor,
        x_workspace_id=x_workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    agent_id: str | Unset | None = UNSET,
    category: Category | Unset | None = UNSET,
    severity: Severity | Unset | None = UNSET,
    assessment: Assessment | Unset | None = UNSET,
    closed: bool | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | FindingPage | None:
    """List Findings

    Args:
        agent_id (None | str | Unset):
        category (Category | None | Unset):
        severity (None | Severity | Unset):
        assessment (Assessment | None | Unset):
        closed (bool | None | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | FindingPage
    """

    return sync_detailed(
        client=client,
        agent_id=agent_id,
        category=category,
        severity=severity,
        assessment=assessment,
        closed=closed,
        limit=limit,
        cursor=cursor,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    agent_id: str | Unset | None = UNSET,
    category: Category | Unset | None = UNSET,
    severity: Severity | Unset | None = UNSET,
    assessment: Assessment | Unset | None = UNSET,
    closed: bool | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | FindingPage]:
    """List Findings

    Args:
        agent_id (None | str | Unset):
        category (Category | None | Unset):
        severity (None | Severity | Unset):
        assessment (Assessment | None | Unset):
        closed (bool | None | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | FindingPage]
    """

    kwargs = build_request(
        agent_id=agent_id,
        category=category,
        severity=severity,
        assessment=assessment,
        closed=closed,
        limit=limit,
        cursor=cursor,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    agent_id: str | Unset | None = UNSET,
    category: Category | Unset | None = UNSET,
    severity: Severity | Unset | None = UNSET,
    assessment: Assessment | Unset | None = UNSET,
    closed: bool | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | FindingPage | None:
    """List Findings

    Args:
        agent_id (None | str | Unset):
        category (Category | None | Unset):
        severity (None | Severity | Unset):
        assessment (Assessment | None | Unset):
        closed (bool | None | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | FindingPage
    """

    return (
        await asyncio_detailed(
            client=client,
            agent_id=agent_id,
            category=category,
            severity=severity,
            assessment=assessment,
            closed=closed,
            limit=limit,
            cursor=cursor,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
