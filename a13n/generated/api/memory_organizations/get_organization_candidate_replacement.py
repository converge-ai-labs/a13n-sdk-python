from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.candidate_replacement import CandidateReplacement
from ...models.error_envelope import ErrorEnvelope
from ...types import UNSET, Response, Unset


def build_request(
    organization_id: str,
    *,
    candidate_seq: int,
    target_seq: int,
    x_workspace_id: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-ID"] = x_workspace_id

    params: dict[str, Any] = {}

    params["candidate_seq"] = candidate_seq

    params["target_seq"] = target_seq

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/memory-organizations/{organization_id}/candidate/replacement".format(
            organization_id=quote(str(organization_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CandidateReplacement | ErrorEnvelope:
    if response.status_code == 200:
        response_200 = CandidateReplacement.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CandidateReplacement | ErrorEnvelope]:
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
    organization_id: str,
    *,
    client: AuthenticatedClient,
    candidate_seq: int,
    target_seq: int,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[CandidateReplacement | ErrorEnvelope]:
    """Get Organization Candidate Replacement

    Args:
        organization_id (str):
        candidate_seq (int):
        target_seq (int):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CandidateReplacement | ErrorEnvelope]
    """

    kwargs = build_request(
        organization_id=organization_id,
        candidate_seq=candidate_seq,
        target_seq=target_seq,
        x_workspace_id=x_workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    candidate_seq: int,
    target_seq: int,
    x_workspace_id: str | Unset | None = UNSET,
) -> CandidateReplacement | ErrorEnvelope | None:
    """Get Organization Candidate Replacement

    Args:
        organization_id (str):
        candidate_seq (int):
        target_seq (int):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CandidateReplacement | ErrorEnvelope
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        candidate_seq=candidate_seq,
        target_seq=target_seq,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    candidate_seq: int,
    target_seq: int,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[CandidateReplacement | ErrorEnvelope]:
    """Get Organization Candidate Replacement

    Args:
        organization_id (str):
        candidate_seq (int):
        target_seq (int):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CandidateReplacement | ErrorEnvelope]
    """

    kwargs = build_request(
        organization_id=organization_id,
        candidate_seq=candidate_seq,
        target_seq=target_seq,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    candidate_seq: int,
    target_seq: int,
    x_workspace_id: str | Unset | None = UNSET,
) -> CandidateReplacement | ErrorEnvelope | None:
    """Get Organization Candidate Replacement

    Args:
        organization_id (str):
        candidate_seq (int):
        target_seq (int):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CandidateReplacement | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            candidate_seq=candidate_seq,
            target_seq=target_seq,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
