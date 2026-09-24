from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.subscription_filter import SubscriptionFilter


T = TypeVar("T", bound="Subscription")


@_attrs_define(repr=False)
class Subscription:
    """
    Attributes:
        created_at (datetime.datetime):
        created_by_id (str):
        enabled (bool):
        filter_ (SubscriptionFilter): Absent fields match every run.
        id (str):
        kinds (list[str]):
        name (str):
        updated_at (datetime.datetime):
        updated_by_id (str):
        url (str):
        version (int):
        workspace_id (str):
    """

    created_at: datetime.datetime
    created_by_id: str
    enabled: bool
    filter_: SubscriptionFilter
    id: str
    kinds: list[str]
    name: str
    updated_at: datetime.datetime
    updated_by_id: str
    url: str
    version: int
    workspace_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        created_by_id = self.created_by_id

        enabled = self.enabled

        filter_ = self.filter_.to_dict()

        id = self.id

        kinds = self.kinds

        name = self.name

        updated_at = self.updated_at.isoformat()

        updated_by_id = self.updated_by_id

        url = self.url

        version = self.version

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "created_by_id": created_by_id,
                "enabled": enabled,
                "filter": filter_,
                "id": id,
                "kinds": kinds,
                "name": name,
                "updated_at": updated_at,
                "updated_by_id": updated_by_id,
                "url": url,
                "version": version,
                "workspace_id": workspace_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subscription_filter import SubscriptionFilter

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        created_by_id = d.pop("created_by_id")

        enabled = d.pop("enabled")

        filter_ = SubscriptionFilter.from_dict(d.pop("filter"))

        id = d.pop("id")

        kinds = cast(list[str], d.pop("kinds"))

        name = d.pop("name")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        updated_by_id = d.pop("updated_by_id")

        url = d.pop("url")

        version = d.pop("version")

        workspace_id = d.pop("workspace_id")

        subscription = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            enabled=enabled,
            filter_=filter_,
            id=id,
            kinds=kinds,
            name=name,
            updated_at=updated_at,
            updated_by_id=updated_by_id,
            url=url,
            version=version,
            workspace_id=workspace_id,
        )

        subscription.additional_properties = d
        return subscription

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
