from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_ref import CatalogRef
    from ..models.create_model_request_settings import CreateModelRequestSettings
    from ..models.model_declarations_input import ModelDeclarationsInput


T = TypeVar("T", bound="CreateModelRequest")


@_attrs_define(repr=False)
class CreateModelRequest:
    """
    Attributes:
        key (str):
        model_api (str):
        name (str):
        provider_id (str):
        upstream_model (str):
        catalog_ref (CatalogRef | None | Unset):
        declarations (ModelDeclarationsInput | Unset): Harness-facing facts and authoring choices declared for one saved
            Model.
        description (None | str | Unset):
        enabled (bool | Unset):
        settings (CreateModelRequestSettings | Unset):
    """

    key: str
    model_api: str
    name: str
    provider_id: str
    upstream_model: str
    catalog_ref: CatalogRef | Unset | None = UNSET
    declarations: ModelDeclarationsInput | Unset = UNSET
    description: str | Unset | None = UNSET
    enabled: bool | Unset = UNSET
    settings: CreateModelRequestSettings | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.catalog_ref import CatalogRef

        key = self.key

        model_api = self.model_api

        name = self.name

        provider_id = self.provider_id

        upstream_model = self.upstream_model

        catalog_ref: dict[str, Any] | Unset | None
        if isinstance(self.catalog_ref, Unset):
            catalog_ref = UNSET
        elif isinstance(self.catalog_ref, CatalogRef):
            catalog_ref = self.catalog_ref.to_dict()
        else:
            catalog_ref = self.catalog_ref

        declarations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.declarations, Unset):
            declarations = self.declarations.to_dict()

        description: str | Unset | None
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        enabled = self.enabled

        settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "model_api": model_api,
                "name": name,
                "provider_id": provider_id,
                "upstream_model": upstream_model,
            }
        )
        if catalog_ref is not UNSET:
            field_dict["catalog_ref"] = catalog_ref
        if declarations is not UNSET:
            field_dict["declarations"] = declarations
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_ref import CatalogRef
        from ..models.create_model_request_settings import CreateModelRequestSettings
        from ..models.model_declarations_input import ModelDeclarationsInput

        d = dict(src_dict)
        key = d.pop("key")

        model_api = d.pop("model_api")

        name = d.pop("name")

        provider_id = d.pop("provider_id")

        upstream_model = d.pop("upstream_model")

        def _parse_catalog_ref(data: object) -> CatalogRef | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                catalog_ref_type_0 = CatalogRef.from_dict(data)

                return catalog_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CatalogRef | Unset | None, data)

        catalog_ref = _parse_catalog_ref(d.pop("catalog_ref", UNSET))

        _declarations = d.pop("declarations", UNSET)
        declarations: ModelDeclarationsInput | Unset
        if isinstance(_declarations, Unset):
            declarations = UNSET
        else:
            declarations = ModelDeclarationsInput.from_dict(_declarations)

        def _parse_description(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        description = _parse_description(d.pop("description", UNSET))

        enabled = d.pop("enabled", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: CreateModelRequestSettings | Unset
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = CreateModelRequestSettings.from_dict(_settings)

        create_model_request = cls(
            key=key,
            model_api=model_api,
            name=name,
            provider_id=provider_id,
            upstream_model=upstream_model,
            catalog_ref=catalog_ref,
            declarations=declarations,
            description=description,
            enabled=enabled,
            settings=settings,
        )

        return create_model_request
