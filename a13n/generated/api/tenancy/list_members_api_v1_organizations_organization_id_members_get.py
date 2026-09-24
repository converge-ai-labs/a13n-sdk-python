from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.list_members_api_v1_organizations_organization_id_members_get_kind_type_0 import (
    ListMembersApiV1OrganizationsOrganizationIdMembersGetKindType0,
)
from ...models.member_page import MemberPage
from ...types import UNSET, Response, Unset


def build_request(
    organization_id: str,
    *,
    kind: ListMembersApiV1OrganizationsOrganizationIdMembersGetKindType0 | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_kind: str | Unset | None
    if isinstance(kind, Unset):
        json_kind = UNSET
    elif isinstance(kind, ListMembersApiV1OrganizationsOrganizationIdMembersGetKindType0):
        json_kind = kind.value
    else:
        json_kind = kind
    params["kind"] = json_kind

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
        "url": "/api/v1/organizations/{organization_id}/members".format(
            organization_id=quote(str(organization_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | MemberPage:
    if response.status_code == 200:
        response_200 = MemberPage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | MemberPage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    kind: ListMembersApiV1OrganizationsOrganizationIdMembersGetKindType0 | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | MemberPage]:
    """List Members

    Args:
        organization_id (str):
        kind (ListMembersApiV1OrganizationsOrganizationIdMembersGetKindType0 | None | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | MemberPage]
    """

    kwargs = build_request(
        organization_id=organization_id,
        kind=kind,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    kind: ListMembersApiV1OrganizationsOrganizationIdMembersGetKindType0 | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
) -> ErrorEnvelope | MemberPage | None:
    """List Members

    Args:
        organization_id (str):
        kind (ListMembersApiV1OrganizationsOrganizationIdMembersGetKindType0 | None | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | MemberPage
    """

    return sync_detailed(
        organization_id=organization_id,
        client=client,
        kind=kind,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    kind: ListMembersApiV1OrganizationsOrganizationIdMembersGetKindType0 | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | MemberPage]:
    """List Members

    Args:
        organization_id (str):
        kind (ListMembersApiV1OrganizationsOrganizationIdMembersGetKindType0 | None | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | MemberPage]
    """

    kwargs = build_request(
        organization_id=organization_id,
        kind=kind,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    organization_id: str,
    *,
    client: AuthenticatedClient,
    kind: ListMembersApiV1OrganizationsOrganizationIdMembersGetKindType0 | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    cursor: str | Unset | None = UNSET,
) -> ErrorEnvelope | MemberPage | None:
    """List Members

    Args:
        organization_id (str):
        kind (ListMembersApiV1OrganizationsOrganizationIdMembersGetKindType0 | None | Unset):
        limit (int | Unset):
        cursor (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | MemberPage
    """

    return (
        await asyncio_detailed(
            organization_id=organization_id,
            client=client,
            kind=kind,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
