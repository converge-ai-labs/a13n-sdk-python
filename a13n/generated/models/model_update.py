from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_ref import CatalogRef
    from ..models.model_config_input import ModelConfigInput
    from ..models.model_pricing_entry_input import ModelPricingEntryInput


T = TypeVar("T", bound="ModelUpdate")


@_attrs_define(repr=False)
class ModelUpdate:
    """
    Attributes:
        catalog_ref (CatalogRef | None | Unset):
        config (ModelConfigInput | None | Unset):
        description (None | str | Unset):
        enabled (bool | None | Unset):
        name (None | str | Unset):
        pricing (ModelPricingEntryInput | None | Unset):
    """

    catalog_ref: CatalogRef | Unset | None = UNSET
    config: ModelConfigInput | Unset | None = UNSET
    description: str | Unset | None = UNSET
    enabled: bool | Unset | None = UNSET
    name: str | Unset | None = UNSET
    pricing: ModelPricingEntryInput | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.catalog_ref import CatalogRef
        from ..models.model_config_input import ModelConfigInput
        from ..models.model_pricing_entry_input import ModelPricingEntryInput

        catalog_ref: dict[str, Any] | Unset | None
        if isinstance(self.catalog_ref, Unset):
            catalog_ref = UNSET
        elif isinstance(self.catalog_ref, CatalogRef):
            catalog_ref = self.catalog_ref.to_dict()
        else:
            catalog_ref = self.catalog_ref

        config: dict[str, Any] | Unset | None
        if isinstance(self.config, Unset):
            config = UNSET
        elif isinstance(self.config, ModelConfigInput):
            config = self.config.to_dict()
        else:
            config = self.config

        description: str | Unset | None
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        enabled: bool | Unset | None
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        name: str | Unset | None
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        pricing: dict[str, Any] | Unset | None
        if isinstance(self.pricing, Unset):
            pricing = UNSET
        elif isinstance(self.pricing, ModelPricingEntryInput):
            pricing = self.pricing.to_dict()
        else:
            pricing = self.pricing

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if catalog_ref is not UNSET:
            field_dict["catalog_ref"] = catalog_ref
        if config is not UNSET:
            field_dict["config"] = config
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if name is not UNSET:
            field_dict["name"] = name
        if pricing is not UNSET:
            field_dict["pricing"] = pricing

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_ref import CatalogRef
        from ..models.model_config_input import ModelConfigInput
        from ..models.model_pricing_entry_input import ModelPricingEntryInput

        d = dict(src_dict)

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

        def _parse_config(data: object) -> ModelConfigInput | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0 = ModelConfigInput.from_dict(data)

                return config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelConfigInput | Unset | None, data)

        config = _parse_config(d.pop("config", UNSET))

        def _parse_description(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_enabled(data: object) -> bool | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | Unset | None, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        def _parse_name(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        name = _parse_name(d.pop("name", UNSET))

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

        model_update = cls(
            catalog_ref=catalog_ref,
            config=config,
            description=description,
            enabled=enabled,
            name=name,
            pricing=pricing,
        )

        return model_update
