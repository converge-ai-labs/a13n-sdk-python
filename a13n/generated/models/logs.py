from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Logs")


@_attrs_define(repr=False)
class Logs:
    """
    Attributes:
        container (str):
        pod_uid (str):
        previous (bool):
        text (str):
        limit_bytes (int | Unset):
    """

    container: str
    pod_uid: str
    previous: bool
    text: str
    limit_bytes: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        container = self.container

        pod_uid = self.pod_uid

        previous = self.previous

        text = self.text

        limit_bytes = self.limit_bytes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "container": container,
                "pod_uid": pod_uid,
                "previous": previous,
                "text": text,
            }
        )
        if limit_bytes is not UNSET:
            field_dict["limit_bytes"] = limit_bytes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        container = d.pop("container")

        pod_uid = d.pop("pod_uid")

        previous = d.pop("previous")

        text = d.pop("text")

        limit_bytes = d.pop("limit_bytes", UNSET)

        logs = cls(
            container=container,
            pod_uid=pod_uid,
            previous=previous,
            text=text,
            limit_bytes=limit_bytes,
        )

        logs.additional_properties = d
        return logs

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
