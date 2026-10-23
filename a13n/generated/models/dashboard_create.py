from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.dashboard_config import DashboardConfig


T = TypeVar("T", bound="DashboardCreate")


@_attrs_define(repr=False)
class DashboardCreate:
    """
    Attributes:
        config (DashboardConfig):
        name (str):
    """

    config: DashboardConfig
    name: str

    def to_dict(self) -> dict[str, Any]:
        config = self.config.to_dict()

        name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "config": config,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_config import DashboardConfig

        d = dict(src_dict)
        config = DashboardConfig.from_dict(d.pop("config"))

        name = d.pop("name")

        dashboard_create = cls(
            config=config,
            name=name,
        )

        return dashboard_create
