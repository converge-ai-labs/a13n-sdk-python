from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_ref import CatalogRef
    from ..models.model_config_input import ModelConfigInput
    from ..models.model_pricing_entry_input import ModelPricingEntryInput


T = TypeVar("T", bound="ModelCreate")


@_attrs_define(repr=False)
class ModelCreate:
    """
    Attributes:
        config (ModelConfigInput):
        name (str):
        provider_id (str):
        catalog_ref (CatalogRef | None | Unset):
        description (str | Unset):
        enabled (bool | Unset):
        key (None | str | Unset):
        pricing (ModelPricingEntryInput | None | Unset):
    """

    config: ModelConfigInput
    name: str
    provider_id: str
    catalog_ref: CatalogRef | Unset | None = UNSET
    description: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    key: str | Unset | None = UNSET
    pricing: ModelPricingEntryInput | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.catalog_ref import CatalogRef
        from ..models.model_pricing_entry_input import ModelPricingEntryInput

        config = self.config.to_dict()

        name = self.name

        provider_id = self.provider_id

        catalog_ref: dict[str, Any] | Unset | None
        if isinstance(self.catalog_ref, Unset):
            catalog_ref = UNSET
        elif isinstance(self.catalog_ref, CatalogRef):
            catalog_ref = self.catalog_ref.to_dict()
        else:
            catalog_ref = self.catalog_ref

        description = self.description

        enabled = self.enabled

        key: str | Unset | None
        if isinstance(self.key, Unset):
            key = UNSET
        else:
            key = self.key

        pricing: dict[str, Any] | Unset | None
        if isinstance(self.pricing, Unset):
            pricing = UNSET
        elif isinstance(self.pricing, ModelPricingEntryInput):
            pricing = self.pricing.to_dict()
        else:
            pricing = self.pricing

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "config": config,
                "name": name,
                "provider_id": provider_id,
            }
        )
        if catalog_ref is not UNSET:
            field_dict["catalog_ref"] = catalog_ref
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if key is not UNSET:
            field_dict["key"] = key
        if pricing is not UNSET:
            field_dict["pricing"] = pricing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_ref import CatalogRef
        from ..models.model_config_input import ModelConfigInput
        from ..models.model_pricing_entry_input import ModelPricingEntryInput

        d = dict(src_dict)
        config = ModelConfigInput.from_dict(d.pop("config"))

        name = d.pop("name")

        provider_id = d.pop("provider_id")

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

        description = d.pop("description", UNSET)

        enabled = d.pop("enabled", UNSET)

        def _parse_key(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        key = _parse_key(d.pop("key", UNSET))

        def _parse_pricing(data: object) -> ModelPricingEntryInput | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pricing_type_0 = ModelPricingEntryInput.from_dict(data)

                return pricing_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelPricingEntryInput | Unset | None, data)

        pricing = _parse_pricing(d.pop("pricing", UNSET))

        model_create = cls(
            config=config,
            name=name,
            provider_id=provider_id,
            catalog_ref=catalog_ref,
            description=description,
            enabled=enabled,
            key=key,
            pricing=pricing,
        )

        return model_create
