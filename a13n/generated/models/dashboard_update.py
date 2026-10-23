from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dashboard_config import DashboardConfig


T = TypeVar("T", bound="DashboardUpdate")


@_attrs_define(repr=False)
class DashboardUpdate:
    """
    Attributes:
        config (DashboardConfig | None | Unset):
        name (None | str | Unset):
    """

    config: DashboardConfig | Unset | None = UNSET
    name: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.dashboard_config import DashboardConfig

        config: dict[str, Any] | Unset | None
        if isinstance(self.config, Unset):
            config = UNSET
        elif isinstance(self.config, DashboardConfig):
            config = self.config.to_dict()
        else:
            config = self.config

        name: str | Unset | None
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dashboard_config import DashboardConfig

        d = dict(src_dict)

        def _parse_config(data: object) -> DashboardConfig | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0 = DashboardConfig.from_dict(data)

                return config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DashboardConfig | Unset | None, data)

        config = _parse_config(d.pop("config", UNSET))

        def _parse_name(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        name = _parse_name(d.pop("name", UNSET))

        dashboard_update = cls(
            config=config,
            name=name,
        )

        return dashboard_update
