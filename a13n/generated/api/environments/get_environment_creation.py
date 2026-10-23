from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.creation_progress import CreationProgress
from ...models.error_envelope import ErrorEnvelope
from ...types import UNSET, Response, Unset


def build_request(
    environment_id: str,
    *,
    x_workspace_id: str | Unset | None = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(x_workspace_id, Unset):
        headers["X-Workspace-ID"] = x_workspace_id

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/environments/{environment_id}/creation".format(
            environment_id=quote(str(environment_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CreationProgress | ErrorEnvelope | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> CreationProgress | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = CreationProgress.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreationProgress | None, data)

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CreationProgress | ErrorEnvelope | None]:
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
    environment_id: str,
    *,
    client: AuthenticatedClient,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[CreationProgress | ErrorEnvelope | None]:
    """Get Environment Creation

    Args:
        environment_id (str):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreationProgress | None | ErrorEnvelope]
    """

    kwargs = build_request(
        environment_id=environment_id,
        x_workspace_id=x_workspace_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    x_workspace_id: str | Unset | None = UNSET,
) -> CreationProgress | None | ErrorEnvelope | None:
    """Get Environment Creation

    Args:
        environment_id (str):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreationProgress | None | ErrorEnvelope
    """

    return sync_detailed(
        environment_id=environment_id,
        client=client,
        x_workspace_id=x_workspace_id,
    ).parsed


async def asyncio_detailed(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    x_workspace_id: str | Unset | None = UNSET,
) -> Response[CreationProgress | ErrorEnvelope | None]:
    """Get Environment Creation

    Args:
        environment_id (str):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreationProgress | None | ErrorEnvelope]
    """

    kwargs = build_request(
        environment_id=environment_id,
        x_workspace_id=x_workspace_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    environment_id: str,
    *,
    client: AuthenticatedClient,
    x_workspace_id: str | Unset | None = UNSET,
) -> CreationProgress | None | ErrorEnvelope | None:
    """Get Environment Creation

    Args:
        environment_id (str):
        x_workspace_id (None | str | Unset): The workspace ID a login session acts in; required
            with a login session. An API key acts in its own workspace and needs none; naming another
            is forbidden.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreationProgress | None | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            environment_id=environment_id,
            client=client,
            x_workspace_id=x_workspace_id,
        )
    ).parsed
