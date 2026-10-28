from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.app_reference import AppReference


T = TypeVar("T", bound="AppReady")


@_attrs_define(repr=False)
class AppReady:
    """App originals and references are committed; opening still checks access and fetches current HTML.

    Attributes:
        apps (list[AppReference]):
        run_id (str):
        thread_id (str):
    """

    apps: list[AppReference]
    run_id: str
    thread_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        apps = []
        for apps_item_data in self.apps:
            apps_item = apps_item_data.to_dict()
            apps.append(apps_item)

        run_id = self.run_id

        thread_id = self.thread_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apps": apps,
                "run_id": run_id,
                "thread_id": thread_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_reference import AppReference

        d = dict(src_dict)
        apps = []
        _apps = d.pop("apps")
        for apps_item_data in _apps:
            apps_item = AppReference.from_dict(apps_item_data)

            apps.append(apps_item)

        run_id = d.pop("run_id")

        thread_id = d.pop("thread_id")

        app_ready = cls(
            apps=apps,
            run_id=run_id,
            thread_id=thread_id,
        )

        app_ready.additional_properties = d
        return app_ready

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
