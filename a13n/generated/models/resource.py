from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.resource_disposition import ResourceDisposition
from ..models.resource_kind import ResourceKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="Resource")


@_attrs_define(repr=False)
class Resource:
    """
    Attributes:
        kind (ResourceKind):
        name (str):
        disposition (ResourceDisposition | Unset):
        sub_paths (list[str] | Unset):
        uid (None | str | Unset):
    """

    kind: ResourceKind
    name: str
    disposition: ResourceDisposition | Unset = UNSET
    sub_paths: list[str] | Unset = UNSET
    uid: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind.value

        name = self.name

        disposition: str | Unset = UNSET
        if not isinstance(self.disposition, Unset):
            disposition = self.disposition.value

        sub_paths: list[str] | Unset = UNSET
        if not isinstance(self.sub_paths, Unset):
            sub_paths = self.sub_paths

        uid: str | Unset | None
        if isinstance(self.uid, Unset):
            uid = UNSET
        else:
            uid = self.uid

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "name": name,
            }
        )
        if disposition is not UNSET:
            field_dict["disposition"] = disposition
        if sub_paths is not UNSET:
            field_dict["sub_paths"] = sub_paths
        if uid is not UNSET:
            field_dict["uid"] = uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        kind = ResourceKind(d.pop("kind"))

        name = d.pop("name")

        _disposition = d.pop("disposition", UNSET)
        disposition: ResourceDisposition | Unset
        if isinstance(_disposition, Unset):
            disposition = UNSET
        else:
            disposition = ResourceDisposition(_disposition)

        sub_paths = cast(list[str], d.pop("sub_paths", UNSET))

        def _parse_uid(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        uid = _parse_uid(d.pop("uid", UNSET))

        resource = cls(
            kind=kind,
            name=name,
            disposition=disposition,
            sub_paths=sub_paths,
            uid=uid,
        )

        return resource
