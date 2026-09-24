from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.catalog_ref import CatalogRef
    from ..models.harness_model_characteristics_output import HarnessModelCharacteristicsOutput
    from ..models.model_pricing_entry_output import ModelPricingEntryOutput


T = TypeVar("T", bound="CatalogModel")


@_attrs_define(repr=False)
class CatalogModel:
    """A catalog model, with the characteristics and pricing a model created from it starts with.

    Attributes:
        characteristics (HarnessModelCharacteristicsOutput): Resolved Harness characteristics of the active Agent model.
        identity (str):
        name (str):
        pricing (ModelPricingEntryOutput | None):
        pricing_warning (None | str):
        provider_name (str):
        ref (CatalogRef): A models.dev channel and the model ID it lists there.
        release_date (datetime.date):
    """

    characteristics: HarnessModelCharacteristicsOutput
    identity: str
    name: str
    pricing: ModelPricingEntryOutput | None
    pricing_warning: str | None
    provider_name: str
    ref: CatalogRef
    release_date: datetime.date
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.model_pricing_entry_output import ModelPricingEntryOutput

        characteristics = self.characteristics.to_dict()

        identity = self.identity

        name = self.name

        pricing: dict[str, Any] | None
        if isinstance(self.pricing, ModelPricingEntryOutput):
            pricing = self.pricing.to_dict()
        else:
            pricing = self.pricing

        pricing_warning: str | None
        pricing_warning = self.pricing_warning

        provider_name = self.provider_name

        ref = self.ref.to_dict()

        release_date = self.release_date.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "characteristics": characteristics,
                "identity": identity,
                "name": name,
                "pricing": pricing,
                "pricing_warning": pricing_warning,
                "provider_name": provider_name,
                "ref": ref,
                "release_date": release_date,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_ref import CatalogRef
        from ..models.harness_model_characteristics_output import HarnessModelCharacteristicsOutput
        from ..models.model_pricing_entry_output import ModelPricingEntryOutput

        d = dict(src_dict)
        characteristics = HarnessModelCharacteristicsOutput.from_dict(d.pop("characteristics"))

        identity = d.pop("identity")

        name = d.pop("name")

        def _parse_pricing(data: object) -> ModelPricingEntryOutput | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pricing_type_0 = ModelPricingEntryOutput.from_dict(data)

                return pricing_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelPricingEntryOutput | None, data)

        pricing = _parse_pricing(d.pop("pricing"))

        def _parse_pricing_warning(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        pricing_warning = _parse_pricing_warning(d.pop("pricing_warning"))

        provider_name = d.pop("provider_name")

        ref = CatalogRef.from_dict(d.pop("ref"))

        release_date = datetime.date.fromisoformat(d.pop("release_date"))

        catalog_model = cls(
            characteristics=characteristics,
            identity=identity,
            name=name,
            pricing=pricing,
            pricing_warning=pricing_warning,
            provider_name=provider_name,
            ref=ref,
            release_date=release_date,
        )

        catalog_model.additional_properties = d
        return catalog_model

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
