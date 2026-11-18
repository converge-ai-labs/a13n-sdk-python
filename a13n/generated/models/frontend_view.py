from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="FrontendView")


@_attrs_define(repr=False)
class FrontendView:
    """
    Attributes:
        bridge (int):
        entry (str):
        styles (list[str]):
    """

    bridge: int
    entry: str
    styles: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bridge = self.bridge

        entry = self.entry

        styles = self.styles

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "bridge": bridge,
                "entry": entry,
                "styles": styles,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bridge = d.pop("bridge")

        entry = d.pop("entry")

        styles = cast(list[str], d.pop("styles"))

        frontend_view = cls(
            bridge=bridge,
            entry=entry,
            styles=styles,
        )

        frontend_view.additional_properties = d
        return frontend_view

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
