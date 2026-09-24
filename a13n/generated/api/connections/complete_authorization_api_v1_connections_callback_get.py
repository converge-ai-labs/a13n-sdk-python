from http import HTTPStatus
from typing import Any, cast

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.callback_outcome import CallbackOutcome
from ...models.error_envelope import ErrorEnvelope
from ...types import UNSET, Response, Unset


def build_request(
    *,
    state: str,
    code: str | Unset | None = UNSET,
    error: str | Unset | None = UNSET,
    iss: str | Unset | None = UNSET,
    session_uri: str | Unset | None = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["state"] = state

    json_code: str | Unset | None
    if isinstance(code, Unset):
        json_code = UNSET
    else:
        json_code = code
    params["code"] = json_code

    json_error: str | Unset | None
    if isinstance(error, Unset):
        json_error = UNSET
    else:
        json_error = error
    params["error"] = json_error

    json_iss: str | Unset | None
    if isinstance(iss, Unset):
        json_iss = UNSET
    else:
        json_iss = iss
    params["iss"] = json_iss

    json_session_uri: str | Unset | None
    if isinstance(session_uri, Unset):
        json_session_uri = UNSET
    else:
        json_session_uri = session_uri
    params["session_uri"] = json_session_uri

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/connections/callback",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | CallbackOutcome | ErrorEnvelope:
    if response.status_code == 200:
        response_200 = CallbackOutcome.from_dict(response.json())

        return response_200

    if response.status_code == 303:
        response_303 = cast(Any, None)
        return response_303

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | CallbackOutcome | ErrorEnvelope]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    state: str,
    code: str | Unset | None = UNSET,
    error: str | Unset | None = UNSET,
    iss: str | Unset | None = UNSET,
    session_uri: str | Unset | None = UNSET,
) -> Response[Any | CallbackOutcome | ErrorEnvelope]:
    """Complete Authorization

     Public: the one-use state authenticates the browser that the authorization server sends back, and
    the flow
    cookie the browser that started the flow.

    Attempts per client address share the login flows' bound.

    Args:
        state (str):
        code (None | str | Unset):
        error (None | str | Unset):
        iss (None | str | Unset):
        session_uri (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CallbackOutcome | ErrorEnvelope]
    """

    kwargs = build_request(
        state=state,
        code=code,
        error=error,
        iss=iss,
        session_uri=session_uri,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    state: str,
    code: str | Unset | None = UNSET,
    error: str | Unset | None = UNSET,
    iss: str | Unset | None = UNSET,
    session_uri: str | Unset | None = UNSET,
) -> Any | CallbackOutcome | ErrorEnvelope | None:
    """Complete Authorization

     Public: the one-use state authenticates the browser that the authorization server sends back, and
    the flow
    cookie the browser that started the flow.

    Attempts per client address share the login flows' bound.

    Args:
        state (str):
        code (None | str | Unset):
        error (None | str | Unset):
        iss (None | str | Unset):
        session_uri (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CallbackOutcome | ErrorEnvelope
    """

    return sync_detailed(
        client=client,
        state=state,
        code=code,
        error=error,
        iss=iss,
        session_uri=session_uri,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    state: str,
    code: str | Unset | None = UNSET,
    error: str | Unset | None = UNSET,
    iss: str | Unset | None = UNSET,
    session_uri: str | Unset | None = UNSET,
) -> Response[Any | CallbackOutcome | ErrorEnvelope]:
    """Complete Authorization

     Public: the one-use state authenticates the browser that the authorization server sends back, and
    the flow
    cookie the browser that started the flow.

    Attempts per client address share the login flows' bound.

    Args:
        state (str):
        code (None | str | Unset):
        error (None | str | Unset):
        iss (None | str | Unset):
        session_uri (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CallbackOutcome | ErrorEnvelope]
    """

    kwargs = build_request(
        state=state,
        code=code,
        error=error,
        iss=iss,
        session_uri=session_uri,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    state: str,
    code: str | Unset | None = UNSET,
    error: str | Unset | None = UNSET,
    iss: str | Unset | None = UNSET,
    session_uri: str | Unset | None = UNSET,
) -> Any | CallbackOutcome | ErrorEnvelope | None:
    """Complete Authorization

     Public: the one-use state authenticates the browser that the authorization server sends back, and
    the flow
    cookie the browser that started the flow.

    Attempts per client address share the login flows' bound.

    Args:
        state (str):
        code (None | str | Unset):
        error (None | str | Unset):
        iss (None | str | Unset):
        session_uri (None | str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CallbackOutcome | ErrorEnvelope
    """

    return (
        await asyncio_detailed(
            client=client,
            state=state,
            code=code,
            error=error,
            iss=iss,
            session_uri=session_uri,
        )
    ).parsed
