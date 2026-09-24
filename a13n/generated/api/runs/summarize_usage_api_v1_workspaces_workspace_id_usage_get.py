import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.usage_summary import UsageSummary
from ...types import UNSET, Response, Unset


def build_request(
    workspace_id: str,
    *,
    run_id: str | Unset | None = UNSET,
    thread_id: str | Unset | None = UNSET,
    session_id: str | Unset | None = UNSET,
    ingested_after: datetime.datetime | Unset | None = UNSET,
    ingested_before: datetime.datetime | Unset | None = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_run_id: str | Unset | None
    if isinstance(run_id, Unset):
        json_run_id = UNSET
    else:
        json_run_id = run_id
    params["run_id"] = json_run_id

    json_thread_id: str | Unset | None
    if isinstance(thread_id, Unset):
        json_thread_id = UNSET
    else:
        json_thread_id = thread_id
    params["thread_id"] = json_thread_id

    json_session_id: str | Unset | None
    if isinstance(session_id, Unset):
        json_session_id = UNSET
    else:
        json_session_id = session_id
    params["session_id"] = json_session_id

    json_ingested_after: str | Unset | None
    if isinstance(ingested_after, Unset):
        json_ingested_after = UNSET
    elif isinstance(ingested_after, datetime.datetime):
        json_ingested_after = ingested_after.isoformat()
    else:
        json_ingested_after = ingested_after
    params["ingested_after"] = json_ingested_after

    json_ingested_before: str | Unset | None
    if isinstance(ingested_before, Unset):
        json_ingested_before = UNSET
    elif isinstance(ingested_before, datetime.datetime):
        json_ingested_before = ingested_before.isoformat()
    else:
        json_ingested_before = ingested_before
    params["ingested_before"] = json_ingested_before

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/workspaces/{workspace_id}/usage".format(
            workspace_id=quote(str(workspace_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | UsageSummary:
    if response.status_code == 200:
        response_200 = UsageSummary.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | UsageSummary]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    run_id: str | Unset | None = UNSET,
    thread_id: str | Unset | None = UNSET,
    session_id: str | Unset | None = UNSET,
    ingested_after: datetime.datetime | Unset | None = UNSET,
    ingested_before: datetime.datetime | Unset | None = UNSET,
) -> Response[ErrorEnvelope | UsageSummary]:
    """Summarize Usage

    Args:
        workspace_id (str):
        run_id (None | str | Unset):
        thread_id (None | str | Unset):
        session_id (None | str | Unset):
        ingested_after (datetime.datetime | None | Unset):
        ingested_before (datetime.datetime | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | UsageSummary]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        run_id=run_id,
        thread_id=thread_id,
        session_id=session_id,
        ingested_after=ingested_after,
        ingested_before=ingested_before,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    run_id: str | Unset | None = UNSET,
    thread_id: str | Unset | None = UNSET,
    session_id: str | Unset | None = UNSET,
    ingested_after: datetime.datetime | Unset | None = UNSET,
    ingested_before: datetime.datetime | Unset | None = UNSET,
) -> ErrorEnvelope | UsageSummary | None:
    """Summarize Usage

    Args:
        workspace_id (str):
        run_id (None | str | Unset):
        thread_id (None | str | Unset):
        session_id (None | str | Unset):
        ingested_after (datetime.datetime | None | Unset):
        ingested_before (datetime.datetime | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | UsageSummary
    """

    return sync_detailed(
        workspace_id=workspace_id,
        client=client,
        run_id=run_id,
        thread_id=thread_id,
        session_id=session_id,
        ingested_after=ingested_after,
        ingested_before=ingested_before,
    ).parsed


async def asyncio_detailed(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    run_id: str | Unset | None = UNSET,
    thread_id: str | Unset | None = UNSET,
    session_id: str | Unset | None = UNSET,
    ingested_after: datetime.datetime | Unset | None = UNSET,
    ingested_before: datetime.datetime | Unset | None = UNSET,
) -> Response[ErrorEnvelope | UsageSummary]:
    """Summarize Usage

    Args:
        workspace_id (str):
        run_id (None | str | Unset):
        thread_id (None | str | Unset):
        session_id (None | str | Unset):
        ingested_after (datetime.datetime | None | Unset):
        ingested_before (datetime.datetime | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | UsageSummary]
    """

    kwargs = build_request(
        workspace_id=workspace_id,
        run_id=run_id,
        thread_id=thread_id,
        session_id=session_id,
        ingested_after=ingested_after,
        ingested_before=ingested_before,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workspace_id: str,
    *,
    client: AuthenticatedClient,
    run_id: str | Unset | None = UNSET,
    thread_id: str | Unset | None = UNSET,
    session_id: str | Unset | None = UNSET,
    ingested_after: datetime.datetime | Unset | None = UNSET,
    ingested_before: datetime.datetime | Unset | None = UNSET,
) -> ErrorEnvelope | UsageSummary | None:
    """Summarize Usage

    Args:
        workspace_id (str):
        run_id (None | str | Unset):
        thread_id (None | str | Unset):
        session_id (None | str | Unset):
        ingested_after (datetime.datetime | None | Unset):
        ingested_before (datetime.datetime | None | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | UsageSummary
    """

    return (
        await asyncio_detailed(
            workspace_id=workspace_id,
            client=client,
            run_id=run_id,
            thread_id=thread_id,
            session_id=session_id,
            ingested_after=ingested_after,
            ingested_before=ingested_before,
        )
    ).parsed
