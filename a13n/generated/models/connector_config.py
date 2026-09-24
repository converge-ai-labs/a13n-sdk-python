from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connector_config_setup import ConnectorConfigSetup


T = TypeVar("T", bound="ConnectorConfig")


@_attrs_define(repr=False)
class ConnectorConfig:
    """One app of a connector provider and the actions it exposes; `setup` is validated by the provider type.

    Attributes:
        actions (list[str]):
        app (str):
        setup (ConnectorConfigSetup | Unset):
    """

    actions: list[str]
    app: str
    setup: ConnectorConfigSetup | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        actions = self.actions

        app = self.app

        setup: dict[str, Any] | Unset = UNSET
        if not isinstance(self.setup, Unset):
            setup = self.setup.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "actions": actions,
                "app": app,
            }
        )
        if setup is not UNSET:
            field_dict["setup"] = setup

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connector_config_setup import ConnectorConfigSetup

        d = dict(src_dict)
        actions = cast(list[str], d.pop("actions"))

        app = d.pop("app")

        _setup = d.pop("setup", UNSET)
        setup: ConnectorConfigSetup | Unset
        if isinstance(_setup, Unset):
            setup = UNSET
        else:
            setup = ConnectorConfigSetup.from_dict(_setup)

        connector_config = cls(
            actions=actions,
            app=app,
            setup=setup,
        )

        return connector_config
