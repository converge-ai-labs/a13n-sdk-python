from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.frontend_view import FrontendView


T = TypeVar("T", bound="AppView")


@_attrs_define(repr=False)
class AppView:
    """
    Attributes:
        app_id (str):
        distribution (str):
        enabled (bool):
        factory_keys (list[str]):
        frontend (FrontendView | None):
        name (str):
        version (str):
    """

    app_id: str
    distribution: str
    enabled: bool
    factory_keys: list[str]
    frontend: FrontendView | None
    name: str
    version: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.frontend_view import FrontendView

        app_id = self.app_id

        distribution = self.distribution

        enabled = self.enabled

        factory_keys = self.factory_keys

        frontend: dict[str, Any] | None
        if isinstance(self.frontend, FrontendView):
            frontend = self.frontend.to_dict()
        else:
            frontend = self.frontend

        name = self.name

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app_id": app_id,
                "distribution": distribution,
                "enabled": enabled,
                "factory_keys": factory_keys,
                "frontend": frontend,
                "name": name,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.frontend_view import FrontendView

        d = dict(src_dict)
        app_id = d.pop("app_id")

        distribution = d.pop("distribution")

        enabled = d.pop("enabled")

        factory_keys = cast(list[str], d.pop("factory_keys"))

        def _parse_frontend(data: object) -> FrontendView | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                frontend_type_0 = FrontendView.from_dict(data)

                return frontend_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FrontendView | None, data)

        frontend = _parse_frontend(d.pop("frontend"))

        name = d.pop("name")

        version = d.pop("version")

        app_view = cls(
            app_id=app_id,
            distribution=distribution,
            enabled=enabled,
            factory_keys=factory_keys,
            frontend=frontend,
            name=name,
            version=version,
        )

        app_view.additional_properties = d
        return app_view

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
