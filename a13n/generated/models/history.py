from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.series import Series


T = TypeVar("T", bound="History")


@_attrs_define(repr=False)
class History:
    """
    Attributes:
        available_from (int | None):
        available_until (int | None):
        resolution_seconds (int):
        retention_seconds (int):
        series (list[Series]):
        inventory_truncated (bool | Unset):
        omitted_sources (int | Unset):
        source (Literal['temporary'] | Unset):
        temporary (bool | Unset):
    """

    available_from: int | None
    available_until: int | None
    resolution_seconds: int
    retention_seconds: int
    series: list[Series]
    inventory_truncated: bool | Unset = UNSET
    omitted_sources: int | Unset = UNSET
    source: Literal["temporary"] | Unset = UNSET
    temporary: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        available_from: int | None
        available_from = self.available_from

        available_until: int | None
        available_until = self.available_until

        resolution_seconds = self.resolution_seconds

        retention_seconds = self.retention_seconds

        series = []
        for series_item_data in self.series:
            series_item = series_item_data.to_dict()
            series.append(series_item)

        inventory_truncated = self.inventory_truncated

        omitted_sources = self.omitted_sources

        source = self.source

        temporary = self.temporary

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "available_from": available_from,
                "available_until": available_until,
                "resolution_seconds": resolution_seconds,
                "retention_seconds": retention_seconds,
                "series": series,
            }
        )
        if inventory_truncated is not UNSET:
            field_dict["inventory_truncated"] = inventory_truncated
        if omitted_sources is not UNSET:
            field_dict["omitted_sources"] = omitted_sources
        if source is not UNSET:
            field_dict["source"] = source
        if temporary is not UNSET:
            field_dict["temporary"] = temporary

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.series import Series

        d = dict(src_dict)

        def _parse_available_from(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        available_from = _parse_available_from(d.pop("available_from"))

        def _parse_available_until(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        available_until = _parse_available_until(d.pop("available_until"))

        resolution_seconds = d.pop("resolution_seconds")

        retention_seconds = d.pop("retention_seconds")

        series = []
        _series = d.pop("series")
        for series_item_data in _series:
            series_item = Series.from_dict(series_item_data)

            series.append(series_item)

        inventory_truncated = d.pop("inventory_truncated", UNSET)

        omitted_sources = d.pop("omitted_sources", UNSET)

        source = cast(Literal["temporary"] | Unset, d.pop("source", UNSET))
        if source != "temporary" and not isinstance(source, Unset):
            raise ValueError(f"source must match const 'temporary', got '{source}'")

        temporary = d.pop("temporary", UNSET)

        history = cls(
            available_from=available_from,
            available_until=available_until,
            resolution_seconds=resolution_seconds,
            retention_seconds=retention_seconds,
            series=series,
            inventory_truncated=inventory_truncated,
            omitted_sources=omitted_sources,
            source=source,
            temporary=temporary,
        )

        history.additional_properties = d
        return history

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
