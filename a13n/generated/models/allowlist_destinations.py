from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="AllowlistDestinations")


@_attrs_define(repr=False)
class AllowlistDestinations:
    """
    Attributes:
        mode (Literal['allowlist']):
        hosts (list[str] | Unset):
    """

    mode: Literal["allowlist"]
    hosts: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        hosts: list[str] | Unset = UNSET
        if not isinstance(self.hosts, Unset):
            hosts = self.hosts

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "mode": mode,
            }
        )
        if hosts is not UNSET:
            field_dict["hosts"] = hosts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mode = cast(Literal["allowlist"], d.pop("mode"))
        if mode != "allowlist":
            raise ValueError(f"mode must match const 'allowlist', got '{mode}'")

        hosts = cast(list[str], d.pop("hosts", UNSET))

        allowlist_destinations = cls(
            mode=mode,
            hosts=hosts,
        )

        return allowlist_destinations
