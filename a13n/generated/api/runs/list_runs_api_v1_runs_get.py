import datetime
from http import HTTPStatus
from typing import Any

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.list_runs_api_v1_runs_get_status_type_0 import ListRunsApiV1RunsGetStatusType0
from ...models.list_runs_api_v1_runs_get_view import ListRunsApiV1RunsGetView
from ...models.run_page import RunPage
from ...models.run_summary_page import RunSummaryPage
from ...types import UNSET, Response, Unset


def build_request(
    *,
    text_query: str | Unset | None = UNSET,
    agent_id: str | Unset | None = UNSET,
    session_id: str | Unset | None = UNSET,
    thread_id: str | Unset | None = UNSET,
    principal_id: str | Unset | None = UNSET,
    status: ListRunsApiV1RunsGetStatusType0 | Unset | None = UNSET,
    created_after: datetime.datetime | Unset | None = UNSET,
    created_before: datetime.datetime | Unset | None = UNSET,
    view: ListRunsApiV1RunsGetView | Unset = UNSET,
    limit: int | Unset | None = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-ID"] = x_workspace_id

    params: dict[str, Any] = {}

    json_text_query: str | Unset | None
    if isinstance(text_query, Unset):
        json_text_query = UNSET
    else:
        json_text_query = text_query
    params["text_query"] = json_text_query

    json_agent_id: str | Unset | None
    if isinstance(agent_id, Unset):
        json_agent_id = UNSET
    else:
        json_agent_id = agent_id
    params["agent_id"] = json_agent_id

    json_session_id: str | Unset | None
    if isinstance(session_id, Unset):
        json_session_id = UNSET
    else:
        json_session_id = session_id
    params["session_id"] = json_session_id

    json_thread_id: str | Unset | None
    if isinstance(thread_id, Unset):
        json_thread_id = UNSET
    else:
        json_thread_id = thread_id
    params["thread_id"] = json_thread_id

    json_principal_id: str | Unset | None
    if isinstance(principal_id, Unset):
        json_principal_id = UNSET
    else:
        json_principal_id = principal_id
    params["principal_id"] = json_principal_id

    json_status: str | Unset | None
    if isinstance(status, Unset):
        json_status = UNSET
    elif isinstance(status, ListRunsApiV1RunsGetStatusType0):
        json_status = status.value
    else:
        json_status = status
    params["status"] = json_status

    json_created_after: str | Unset | None
    if isinstance(created_after, Unset):
        json_created_after = UNSET
    elif isinstance(created_after, datetime.datetime):
        json_created_after = created_after.isoformat()
    else:
        json_created_after = created_after
    params["created_after"] = json_created_after

    json_created_before: str | Unset | None
    if isinstance(created_before, Unset):
        json_created_before = UNSET
    elif isinstance(created_before, datetime.datetime):
        json_created_before = created_before.isoformat()
    else:
        json_created_before = created_before
    params["created_before"] = json_created_before

    json_view: str | Unset = UNSET
    if not isinstance(view, Unset):
        json_view = view.value

    params["view"] = json_view

    json_limit: int | Unset | None
    if isinstance(limit, Unset):
        json_limit = UNSET
    else:
        json_limit = limit
    params["limit"] = json_limit

    json_cursor: str | Unset | None
    if isinstance(cursor, Unset):
        json_cursor = UNSET
    else:
        json_cursor = cursor
    params["cursor"] = json_cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/runs",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | RunPage | RunSummaryPage:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> RunPage | RunSummaryPage:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = RunPage.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = RunSummaryPage.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | RunPage | RunSummaryPage]:
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
    text_query: str | Unset | None = UNSET,
    agent_id: str | Unset | None = UNSET,
    session_id: str | Unset | None = UNSET,
    thread_id: str | Unset | None = UNSET,
    principal_id: str | Unset | None = UNSET,
    status: ListRunsApiV1RunsGetStatusType0 | Unset | None = UNSET,
    created_after: datetime.datetime | Unset | None = UNSET,
    created_before: datetime.datetime | Unset | None = UNSET,
    view: ListRunsApiV1RunsGetView | Unset = UNSET,
    limit: int | Unset | None = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | RunPage | RunSummaryPage]:
    """List Runs

    Args:
        text_query (None | str | Unset): All search terms must match one run's retained
            user/assistant text
        agent_id (None | str | Unset):
        session_id (None | str | Unset):
        thread_id (None | str | Unset):
        principal_id (None | str | Unset):
        status (ListRunsApiV1RunsGetStatusType0 | None | Unset):
        created_after (datetime.datetime | None | Unset):
        created_before (datetime.datetime | None | Unset):
        view (ListRunsApiV1RunsGetView | Unset):
        limit (int | None | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | RunPage | RunSummaryPage]
    """

    kwargs = build_request(
        text_query=text_query,
        agent_id=agent_id,
        session_id=session_id,
        thread_id=thread_id,
        principal_id=principal_id,
        status=status,
        created_after=created_after,
        created_before=created_before,
        view=view,
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
    text_query: str | Unset | None = UNSET,
    agent_id: str | Unset | None = UNSET,
    session_id: str | Unset | None = UNSET,
    thread_id: str | Unset | None = UNSET,
    principal_id: str | Unset | None = UNSET,
    status: ListRunsApiV1RunsGetStatusType0 | Unset | None = UNSET,
    created_after: datetime.datetime | Unset | None = UNSET,
    created_before: datetime.datetime | Unset | None = UNSET,
    view: ListRunsApiV1RunsGetView | Unset = UNSET,
    limit: int | Unset | None = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | RunPage | RunSummaryPage | None:
    """List Runs

    Args:
        text_query (None | str | Unset): All search terms must match one run's retained
            user/assistant text
        agent_id (None | str | Unset):
        session_id (None | str | Unset):
        thread_id (None | str | Unset):
        principal_id (None | str | Unset):
        status (ListRunsApiV1RunsGetStatusType0 | None | Unset):
        created_after (datetime.datetime | None | Unset):
        created_before (datetime.datetime | None | Unset):
        view (ListRunsApiV1RunsGetView | Unset):
        limit (int | None | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | RunPage | RunSummaryPage
    """

    return sync_detailed(
        client=client,
        text_query=text_query,
        agent_id=agent_id,
        session_id=session_id,
        thread_id=thread_id,
        principal_id=principal_id,
        status=status,
        created_after=created_after,
        created_before=created_before,
        view=view,
        limit=limit,
        cursor=cursor,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    text_query: str | Unset | None = UNSET,
    agent_id: str | Unset | None = UNSET,
    session_id: str | Unset | None = UNSET,
    thread_id: str | Unset | None = UNSET,
    principal_id: str | Unset | None = UNSET,
    status: ListRunsApiV1RunsGetStatusType0 | Unset | None = UNSET,
    created_after: datetime.datetime | Unset | None = UNSET,
    created_before: datetime.datetime | Unset | None = UNSET,
    view: ListRunsApiV1RunsGetView | Unset = UNSET,
    limit: int | Unset | None = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | RunPage | RunSummaryPage]:
    """List Runs

    Args:
        text_query (None | str | Unset): All search terms must match one run's retained
            user/assistant text
        agent_id (None | str | Unset):
        session_id (None | str | Unset):
        thread_id (None | str | Unset):
        principal_id (None | str | Unset):
        status (ListRunsApiV1RunsGetStatusType0 | None | Unset):
        created_after (datetime.datetime | None | Unset):
        created_before (datetime.datetime | None | Unset):
        view (ListRunsApiV1RunsGetView | Unset):
        limit (int | None | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | RunPage | RunSummaryPage]
    """

    kwargs = build_request(
        text_query=text_query,
        agent_id=agent_id,
        session_id=session_id,
        thread_id=thread_id,
        principal_id=principal_id,
        status=status,
        created_after=created_after,
        created_before=created_before,
        view=view,
        limit=limit,
        cursor=cursor,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    text_query: str | Unset | None = UNSET,
    agent_id: str | Unset | None = UNSET,
    session_id: str | Unset | None = UNSET,
    thread_id: str | Unset | None = UNSET,
    principal_id: str | Unset | None = UNSET,
    status: ListRunsApiV1RunsGetStatusType0 | Unset | None = UNSET,
    created_after: datetime.datetime | Unset | None = UNSET,
    created_before: datetime.datetime | Unset | None = UNSET,
    view: ListRunsApiV1RunsGetView | Unset = UNSET,
    limit: int | Unset | None = UNSET,
    cursor: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> ErrorEnvelope | RunPage | RunSummaryPage | None:
    """List Runs

    Args:
        text_query (None | str | Unset): All search terms must match one run's retained
            user/assistant text
        agent_id (None | str | Unset):
        session_id (None | str | Unset):
        thread_id (None | str | Unset):
        principal_id (None | str | Unset):
        status (ListRunsApiV1RunsGetStatusType0 | None | Unset):
        created_after (datetime.datetime | None | Unset):
        created_before (datetime.datetime | None | Unset):
        view (ListRunsApiV1RunsGetView | Unset):
        limit (int | None | Unset):
        cursor (None | str | Unset):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | RunPage | RunSummaryPage
    """

    return (
        await asyncio_detailed(
            client=client,
            text_query=text_query,
            agent_id=agent_id,
            session_id=session_id,
            thread_id=thread_id,
            principal_id=principal_id,
            status=status,
            created_after=created_after,
            created_before=created_before,
            view=view,
            limit=limit,
            cursor=cursor,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
