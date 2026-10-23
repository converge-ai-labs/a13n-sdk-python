from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..models.dashboard_config_refresh_seconds import DashboardConfigRefreshSeconds
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.panel import Panel


T = TypeVar("T", bound="DashboardConfig")


@_attrs_define(repr=False)
class DashboardConfig:
    """
    Attributes:
        panels (list[Panel] | Unset):
        range_seconds (int | Unset):
        refresh_seconds (DashboardConfigRefreshSeconds | Unset):
        schema_version (Literal[1] | Unset):
    """

    panels: list[Panel] | Unset = UNSET
    range_seconds: int | Unset = UNSET
    refresh_seconds: DashboardConfigRefreshSeconds | Unset = UNSET
    schema_version: Literal[1] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        panels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.panels, Unset):
            panels = []
            for panels_item_data in self.panels:
                panels_item = panels_item_data.to_dict()
                panels.append(panels_item)

        range_seconds = self.range_seconds

        refresh_seconds: int | Unset = UNSET
        if not isinstance(self.refresh_seconds, Unset):
            refresh_seconds = self.refresh_seconds.value

        schema_version = self.schema_version

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if panels is not UNSET:
            field_dict["panels"] = panels
        if range_seconds is not UNSET:
            field_dict["range_seconds"] = range_seconds
        if refresh_seconds is not UNSET:
            field_dict["refresh_seconds"] = refresh_seconds
        if schema_version is not UNSET:
            field_dict["schema_version"] = schema_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.panel import Panel

        d = dict(src_dict)
        _panels = d.pop("panels", UNSET)
        panels: list[Panel] | Unset = UNSET
        if _panels is not UNSET:
            panels = []
            for panels_item_data in _panels:
                panels_item = Panel.from_dict(panels_item_data)

                panels.append(panels_item)

        range_seconds = d.pop("range_seconds", UNSET)

        _refresh_seconds = d.pop("refresh_seconds", UNSET)
        refresh_seconds: DashboardConfigRefreshSeconds | Unset
        if isinstance(_refresh_seconds, Unset):
            refresh_seconds = UNSET
        else:
            refresh_seconds = DashboardConfigRefreshSeconds(_refresh_seconds)

        schema_version = cast(Literal[1] | Unset, d.pop("schema_version", UNSET))
        if schema_version != 1 and not isinstance(schema_version, Unset):
            raise ValueError(f"schema_version must match const 1, got '{schema_version}'")

        dashboard_config = cls(
            panels=panels,
            range_seconds=range_seconds,
            refresh_seconds=refresh_seconds,
            schema_version=schema_version,
        )

        return dashboard_config
