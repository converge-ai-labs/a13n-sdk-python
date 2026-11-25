from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.security_advisory import SecurityAdvisory
    from ..models.stable_release import StableRelease


T = TypeVar("T", bound="UpdateNotices")


@_attrs_define(repr=False)
class UpdateNotices:
    """
    Attributes:
        advisories (list[SecurityAdvisory]):
        current_version (str):
        latest_stable (None | StableRelease):
    """

    advisories: list[SecurityAdvisory]
    current_version: str
    latest_stable: StableRelease | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.stable_release import StableRelease

        advisories = []
        for advisories_item_data in self.advisories:
            advisories_item = advisories_item_data.to_dict()
            advisories.append(advisories_item)

        current_version = self.current_version

        latest_stable: dict[str, Any] | None
        if isinstance(self.latest_stable, StableRelease):
            latest_stable = self.latest_stable.to_dict()
        else:
            latest_stable = self.latest_stable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "advisories": advisories,
                "current_version": current_version,
                "latest_stable": latest_stable,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.security_advisory import SecurityAdvisory
        from ..models.stable_release import StableRelease

        d = dict(src_dict)
        advisories = []
        _advisories = d.pop("advisories")
        for advisories_item_data in _advisories:
            advisories_item = SecurityAdvisory.from_dict(advisories_item_data)

            advisories.append(advisories_item)

        current_version = d.pop("current_version")

        def _parse_latest_stable(data: object) -> StableRelease | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                latest_stable_type_0 = StableRelease.from_dict(data)

                return latest_stable_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(StableRelease | None, data)

        latest_stable = _parse_latest_stable(d.pop("latest_stable"))

        update_notices = cls(
            advisories=advisories,
            current_version=current_version,
            latest_stable=latest_stable,
        )

        update_notices.additional_properties = d
        return update_notices

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
