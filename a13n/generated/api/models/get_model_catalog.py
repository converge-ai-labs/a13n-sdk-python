from http import HTTPStatus
from typing import Any

import httpx2 as httpx

from ...client import AuthenticatedClient, Client
from ...models.error_envelope import ErrorEnvelope
from ...models.get_model_catalog_section_type_0 import GetModelCatalogSectionType0
from ...models.model_catalog import ModelCatalog
from ...models.model_catalog_page import ModelCatalogPage
from ...models.read_view import ReadView
from ...models.text_read import TextRead
from ...types import UNSET, Response, Unset


def build_request(
    *,
    provider: str | Unset | None = UNSET,
    model: str | Unset | None = UNSET,
    view: ReadView | Unset = UNSET,
    query: str | Unset | None = UNSET,
    capability: str | Unset | None = UNSET,
    limit: int | Unset | None = UNSET,
    cursor: str | Unset | None = UNSET,
    section: GetModelCatalogSectionType0 | Unset | None = UNSET,
    offset: int | Unset = UNSET,
    text_limit: int | Unset = UNSET,
    version: str | Unset | None = UNSET,
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

    json_view: str | Unset = UNSET
    if not isinstance(view, Unset):
        json_view = view.value

    params["view"] = json_view

    json_query: str | Unset | None
    if isinstance(query, Unset):
        json_query = UNSET
    else:
        json_query = query
    params["query"] = json_query

    json_capability: str | Unset | None
    if isinstance(capability, Unset):
        json_capability = UNSET
    else:
        json_capability = capability
    params["capability"] = json_capability

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

    json_section: str | Unset | None
    if isinstance(section, Unset):
        json_section = UNSET
    elif isinstance(section, GetModelCatalogSectionType0):
        json_section = section.value
    else:
        json_section = section
    params["section"] = json_section

    params["offset"] = offset

    params["text_limit"] = text_limit

    json_version: str | Unset | None
    if isinstance(version, Unset):
        json_version = UNSET
    else:
        json_version = version
    params["version"] = json_version

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/model-catalog",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorEnvelope | ModelCatalog | ModelCatalogPage | TextRead:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> ModelCatalog | ModelCatalogPage | TextRead:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = ModelCatalog.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = ModelCatalogPage.from_dict(data)

                return response_200_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_2 = TextRead.from_dict(data)

            return response_200_type_2

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorEnvelope.from_dict(response.json())

        return response_400

    response_default = ErrorEnvelope.from_dict(response.json())

    return response_default


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorEnvelope | ModelCatalog | ModelCatalogPage | TextRead]:
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
    view: ReadView | Unset = UNSET,
    query: str | Unset | None = UNSET,
    capability: str | Unset | None = UNSET,
    limit: int | Unset | None = UNSET,
    cursor: str | Unset | None = UNSET,
    section: GetModelCatalogSectionType0 | Unset | None = UNSET,
    offset: int | Unset = UNSET,
    text_limit: int | Unset = UNSET,
    version: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | ModelCatalog | ModelCatalogPage | TextRead]:
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
        view (ReadView | Unset):
        query (None | str | Unset): Case-insensitive substring of full names and descriptions.
        capability (None | str | Unset):
        limit (int | None | Unset):
        cursor (None | str | Unset):
        section (GetModelCatalogSectionType0 | None | Unset):
        offset (int | Unset): Unicode code-point offset; continue with next_offset.
        text_limit (int | Unset): Maximum Unicode code points in this fragment.
        version (None | str | Unset): Content version from the first read; required after offset
            0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ModelCatalog | ModelCatalogPage | TextRead]
    """

    kwargs = build_request(
        provider=provider,
        model=model,
        view=view,
        query=query,
        capability=capability,
        limit=limit,
        cursor=cursor,
        section=section,
        offset=offset,
        text_limit=text_limit,
        version=version,
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
    view: ReadView | Unset = UNSET,
    query: str | Unset | None = UNSET,
    capability: str | Unset | None = UNSET,
    limit: int | Unset | None = UNSET,
    cursor: str | Unset | None = UNSET,
    section: GetModelCatalogSectionType0 | Unset | None = UNSET,
    offset: int | Unset = UNSET,
    text_limit: int | Unset = UNSET,
    version: str | Unset | None = UNSET,
) -> ErrorEnvelope | ModelCatalog | ModelCatalogPage | TextRead | None:
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
        view (ReadView | Unset):
        query (None | str | Unset): Case-insensitive substring of full names and descriptions.
        capability (None | str | Unset):
        limit (int | None | Unset):
        cursor (None | str | Unset):
        section (GetModelCatalogSectionType0 | None | Unset):
        offset (int | Unset): Unicode code-point offset; continue with next_offset.
        text_limit (int | Unset): Maximum Unicode code points in this fragment.
        version (None | str | Unset): Content version from the first read; required after offset
            0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ModelCatalog | ModelCatalogPage | TextRead
    """

    return sync_detailed(
        client=client,
        provider=provider,
        model=model,
        view=view,
        query=query,
        capability=capability,
        limit=limit,
        cursor=cursor,
        section=section,
        offset=offset,
        text_limit=text_limit,
        version=version,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    provider: str | Unset | None = UNSET,
    model: str | Unset | None = UNSET,
    view: ReadView | Unset = UNSET,
    query: str | Unset | None = UNSET,
    capability: str | Unset | None = UNSET,
    limit: int | Unset | None = UNSET,
    cursor: str | Unset | None = UNSET,
    section: GetModelCatalogSectionType0 | Unset | None = UNSET,
    offset: int | Unset = UNSET,
    text_limit: int | Unset = UNSET,
    version: str | Unset | None = UNSET,
) -> Response[ErrorEnvelope | ModelCatalog | ModelCatalogPage | TextRead]:
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
        view (ReadView | Unset):
        query (None | str | Unset): Case-insensitive substring of full names and descriptions.
        capability (None | str | Unset):
        limit (int | None | Unset):
        cursor (None | str | Unset):
        section (GetModelCatalogSectionType0 | None | Unset):
        offset (int | Unset): Unicode code-point offset; continue with next_offset.
        text_limit (int | Unset): Maximum Unicode code points in this fragment.
        version (None | str | Unset): Content version from the first read; required after offset
            0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorEnvelope | ModelCatalog | ModelCatalogPage | TextRead]
    """

    kwargs = build_request(
        provider=provider,
        model=model,
        view=view,
        query=query,
        capability=capability,
        limit=limit,
        cursor=cursor,
        section=section,
        offset=offset,
        text_limit=text_limit,
        version=version,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    provider: str | Unset | None = UNSET,
    model: str | Unset | None = UNSET,
    view: ReadView | Unset = UNSET,
    query: str | Unset | None = UNSET,
    capability: str | Unset | None = UNSET,
    limit: int | Unset | None = UNSET,
    cursor: str | Unset | None = UNSET,
    section: GetModelCatalogSectionType0 | Unset | None = UNSET,
    offset: int | Unset = UNSET,
    text_limit: int | Unset = UNSET,
    version: str | Unset | None = UNSET,
) -> ErrorEnvelope | ModelCatalog | ModelCatalogPage | TextRead | None:
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
        view (ReadView | Unset):
        query (None | str | Unset): Case-insensitive substring of full names and descriptions.
        capability (None | str | Unset):
        limit (int | None | Unset):
        cursor (None | str | Unset):
        section (GetModelCatalogSectionType0 | None | Unset):
        offset (int | Unset): Unicode code-point offset; continue with next_offset.
        text_limit (int | Unset): Maximum Unicode code points in this fragment.
        version (None | str | Unset): Content version from the first read; required after offset
            0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorEnvelope | ModelCatalog | ModelCatalogPage | TextRead
    """

    return (
        await asyncio_detailed(
            client=client,
            provider=provider,
            model=model,
            view=view,
            query=query,
            capability=capability,
            limit=limit,
            cursor=cursor,
            section=section,
            offset=offset,
            text_limit=text_limit,
            version=version,
        )
    ).parsed
