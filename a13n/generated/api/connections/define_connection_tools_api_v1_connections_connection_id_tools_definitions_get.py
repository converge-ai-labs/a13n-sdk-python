from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.definitions import Definitions
from ...models.error_envelope import ErrorEnvelope
from ...models.text_read import TextRead
from ...types import UNSET, Response, Unset


def build_request(
    connection_id: str,
    *,
    name: list[str],
    offset: int | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    version: str | Unset | None = UNSET,
    query: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-ID"] = x_workspace_id

    params: dict[str, Any] = {}

    json_name = name

    params["name"] = json_name

    json_offset: int | Unset | None
    if isinstance(offset, Unset):
        json_offset = UNSET
    else:
        json_offset = offset
    params["offset"] = json_offset

    params["limit"] = limit

    json_version: str | Unset | None
    if isinstance(version, Unset):
        json_version = UNSET
    else:
        json_version = version
    params["version"] = json_version

    json_query: str | Unset | None
    if isinstance(query, Unset):
        json_query = UNSET
    else:
        json_query = query
    params["query"] = json_query

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/connections/{connection_id}/tools/definitions".format(
            connection_id=quote(str(connection_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Definitions | TextRead | ErrorEnvelope:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> Definitions | TextRead:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = Definitions.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = TextRead.from_dict(data)

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
) -> Response[Definitions | TextRead | ErrorEnvelope]:
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
    connection_id: str,
    *,
    client: AuthenticatedClient,
    name: list[str],
    offset: int | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    version: str | Unset | None = UNSET,
    query: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[Definitions | TextRead | ErrorEnvelope]:
    """Define Connection Tools

     Read up to five exact definitions. Oversized values provide a versioned fragment reference.

    Args:
        connection_id (str):
        name (list[str]): Exact names; repeat name to select up to five definitions.
        offset (int | None | Unset):
        limit (int | Unset): Maximum Unicode code points in this fragment.
        version (None | str | Unset): Content version from the first read; required after offset
            0.
        query (None | str | Unset): Case-sensitive literal text search.
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Definitions | TextRead | ErrorEnvelope]
    """

    kwargs = build_request(
        connection_id=connection_id,
        name=name,
        offset=offset,
        limit=limit,
        version=version,
        query=query,
        x_workspace_id=x_workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    connection_id: str,
    *,
    client: AuthenticatedClient,
    name: list[str],
    offset: int | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    version: str | Unset | None = UNSET,
    query: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Definitions | TextRead | ErrorEnvelope | None:
    """Define Connection Tools

     Read up to five exact definitions. Oversized values provide a versioned fragment reference.

    Args:
        connection_id (str):
        name (list[str]): Exact names; repeat name to select up to five definitions.
        offset (int | None | Unset):
        limit (int | Unset): Maximum Unicode code points in this fragment.
        version (None | str | Unset): Content version from the first read; required after offset
            0.
        query (None | str | Unset): Case-sensitive literal text search.
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Definitions | TextRead | ErrorEnvelope
    """

    return sync_detailed(
        connection_id=connection_id,
        client=client,
        name=name,
        offset=offset,
        limit=limit,
        version=version,
        query=query,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    connection_id: str,
    *,
    client: AuthenticatedClient,
    name: list[str],
    offset: int | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    version: str | Unset | None = UNSET,
    query: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[Definitions | TextRead | ErrorEnvelope]:
    """Define Connection Tools

     Read up to five exact definitions. Oversized values provide a versioned fragment reference.

    Args:
        connection_id (str):
        name (list[str]): Exact names; repeat name to select up to five definitions.
        offset (int | None | Unset):
        limit (int | Unset): Maximum Unicode code points in this fragment.
        version (None | str | Unset): Content version from the first read; required after offset
            0.
        query (None | str | Unset): Case-sensitive literal text search.
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Definitions | TextRead | ErrorEnvelope]
    """

    kwargs = build_request(
        connection_id=connection_id,
        name=name,
        offset=offset,
        limit=limit,
        version=version,
        query=query,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    connection_id: str,
    *,
    client: AuthenticatedClient,
    name: list[str],
    offset: int | Unset | None = UNSET,
    limit: int | Unset = UNSET,
    version: str | Unset | None = UNSET,
    query: str | Unset | None = UNSET,
    x_workspace_id: str | Unset | None = UNSET,
) -> Definitions | TextRead | ErrorEnvelope | None:
    """Define Connection Tools

     Read up to five exact definitions. Oversized values provide a versioned fragment reference.

    Args:
        connection_id (str):
        name (list[str]): Exact names; repeat name to select up to five definitions.
        offset (int | None | Unset):
        limit (int | Unset): Maximum Unicode code points in this fragment.
        version (None | str | Unset): Content version from the first read; required after offset
            0.
        query (None | str | Unset): Case-sensitive literal text search.
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Definitions | TextRead | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            connection_id=connection_id,
            client=client,
            name=name,
            offset=offset,
            limit=limit,
            version=version,
            query=query,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
