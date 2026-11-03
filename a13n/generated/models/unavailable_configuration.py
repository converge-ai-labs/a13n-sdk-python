from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UnavailableConfiguration")


@_attrs_define(repr=False)
class UnavailableConfiguration:
    """A collection member whose stored configuration requires operator repair.

    Attributes:
        id (str):
        kind (str):
        reason (Literal['configuration_unavailable'] | Unset):
    """

    id: str
    kind: str
    reason: Literal["configuration_unavailable"] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        kind = self.kind

        reason = self.reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "kind": kind,
            }
        )
        if reason is not UNSET:
            field_dict["reason"] = reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        kind = d.pop("kind")

        reason = cast(Literal["configuration_unavailable"] | Unset, d.pop("reason", UNSET))
        if reason != "configuration_unavailable" and not isinstance(reason, Unset):
            raise ValueError(f"reason must match const 'configuration_unavailable', got '{reason}'")

        unavailable_configuration = cls(
            id=id,
            kind=kind,
            reason=reason,
        )

        unavailable_configuration.additional_properties = d
        return unavailable_configuration

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
