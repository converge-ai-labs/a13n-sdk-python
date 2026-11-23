from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.oidc_brand import OIDCBrand

T = TypeVar("T", bound="OIDCSignIn")


@_attrs_define(repr=False)
class OIDCSignIn:
    """
    Attributes:
        brand (OIDCBrand):
        id (str):
        label (str):
    """

    brand: OIDCBrand
    id: str
    label: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        brand = self.brand.value

        id = self.id

        label = self.label

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "brand": brand,
                "id": id,
                "label": label,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        brand = OIDCBrand(d.pop("brand"))

        id = d.pop("id")

        label = d.pop("label")

        oidc_sign_in = cls(
            brand=brand,
            id=id,
            label=label,
        )

        oidc_sign_in.additional_properties = d
        return oidc_sign_in

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
