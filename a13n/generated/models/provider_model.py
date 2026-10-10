from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.harness_model_characteristics_output import HarnessModelCharacteristicsOutput


T = TypeVar("T", bound="ProviderModel")


@_attrs_define(repr=False)
class ProviderModel:
    """An upstream choice; wire names retain the original account-discovery contract.

    Attributes:
        display_name (str):
        slug (str):
        characteristics (HarnessModelCharacteristicsOutput | None | Unset):
    """

    display_name: str
    slug: str
    characteristics: HarnessModelCharacteristicsOutput | Unset | None = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.harness_model_characteristics_output import HarnessModelCharacteristicsOutput

        display_name = self.display_name

        slug = self.slug

        characteristics: dict[str, Any] | Unset | None
        if isinstance(self.characteristics, Unset):
            characteristics = UNSET
        elif isinstance(self.characteristics, HarnessModelCharacteristicsOutput):
            characteristics = self.characteristics.to_dict()
        else:
            characteristics = self.characteristics

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "display_name": display_name,
                "slug": slug,
            }
        )
        if characteristics is not UNSET:
            field_dict["characteristics"] = characteristics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.harness_model_characteristics_output import HarnessModelCharacteristicsOutput

        d = dict(src_dict)
        display_name = d.pop("display_name")

        slug = d.pop("slug")

        def _parse_characteristics(data: object) -> HarnessModelCharacteristicsOutput | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                characteristics_type_0 = HarnessModelCharacteristicsOutput.from_dict(data)

                return characteristics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HarnessModelCharacteristicsOutput | Unset | None, data)

        characteristics = _parse_characteristics(d.pop("characteristics", UNSET))

        provider_model = cls(
            display_name=display_name,
            slug=slug,
            characteristics=characteristics,
        )

        provider_model.additional_properties = d
        return provider_model

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
