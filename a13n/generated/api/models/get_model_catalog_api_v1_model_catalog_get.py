from http import HTTPStatus
from typing import Any

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.model_catalog import ModelCatalog
from ...types import UNSET, Response, Unset


def build_request(
    *,
    provider: str | Unset | None = UNSET,
    model: str | Unset | None = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_provider: str | Unset | None
    if isinstance(provider, Unset):
        json_provider = UNSET
    else:
        json_provider = provider
    params["provider"] = json_provider

    json_model: str | Unset | None
    if isinstance(model, Unset):
        json_model = UNSET
    else:
        json_model = model
    params["model"] = json_model

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/model-catalog",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorEnvelope | ModelCatalog:
    if response.status_code == 200:
        response_200 = ModelCatalog.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | ModelCatalog]:
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
    provider: str | Unset | None = UNSET,
    model: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | ModelCatalog]:
    """Get Model Catalog

     Read public model metadata and prices. Filter by provider and model to avoid a large full-catalog
    response.

    Both filters match exactly and combine with AND; omitted filters leave that dimension unrestricted.
    No match returns empty items with the catalog status. Refreshes always fetch the full catalog when
    due.
    Copy the selected item's characteristics, pricing and ref into model config, pricing and catalog_ref
    when saving.

    Args:
        provider (None | str | Unset): Exact catalog channel ID, such as openrouter.
        model (None | str | Unset): Exact, case-sensitive model ID within the catalog channel.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ModelCatalog]
    """

    kwargs = build_request(
        provider=provider,
        model=model,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    provider: str | Unset | None = UNSET,
    model: str | Unset | None = UNSET,
) -> ErrorEnvelope | ModelCatalog | None:
    """Get Model Catalog

     Read public model metadata and prices. Filter by provider and model to avoid a large full-catalog
    response.

    Both filters match exactly and combine with AND; omitted filters leave that dimension unrestricted.
    No match returns empty items with the catalog status. Refreshes always fetch the full catalog when
    due.
    Copy the selected item's characteristics, pricing and ref into model config, pricing and catalog_ref
    when saving.

    Args:
        provider (None | str | Unset): Exact catalog channel ID, such as openrouter.
        model (None | str | Unset): Exact, case-sensitive model ID within the catalog channel.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ModelCatalog
    """

    return sync_detailed(
        client=client,
        provider=provider,
        model=model,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    provider: str | Unset | None = UNSET,
    model: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | ModelCatalog]:
    """Get Model Catalog

     Read public model metadata and prices. Filter by provider and model to avoid a large full-catalog
    response.

    Both filters match exactly and combine with AND; omitted filters leave that dimension unrestricted.
    No match returns empty items with the catalog status. Refreshes always fetch the full catalog when
    due.
    Copy the selected item's characteristics, pricing and ref into model config, pricing and catalog_ref
    when saving.

    Args:
        provider (None | str | Unset): Exact catalog channel ID, such as openrouter.
        model (None | str | Unset): Exact, case-sensitive model ID within the catalog channel.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ModelCatalog]
    """

    kwargs = build_request(
        provider=provider,
        model=model,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    provider: str | Unset | None = UNSET,
    model: str | Unset | None = UNSET,
) -> ErrorEnvelope | ModelCatalog | None:
    """Get Model Catalog

     Read public model metadata and prices. Filter by provider and model to avoid a large full-catalog
    response.

    Both filters match exactly and combine with AND; omitted filters leave that dimension unrestricted.
    No match returns empty items with the catalog status. Refreshes always fetch the full catalog when
    due.
    Copy the selected item's characteristics, pricing and ref into model config, pricing and catalog_ref
    when saving.

    Args:
        provider (None | str | Unset): Exact catalog channel ID, such as openrouter.
        model (None | str | Unset): Exact, case-sensitive model ID within the catalog channel.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ModelCatalog
    """

    return (
        await asyncio_detailed(
            client=client,
            provider=provider,
            model=model,
        )
    ).parsed
