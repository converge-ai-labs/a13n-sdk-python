from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.asset_source_type_0 import AssetSourceType0


T = TypeVar("T", bound="Asset")


@_attrs_define(repr=False)
class Asset:
    """
    Attributes:
        content_type (str):
        created_at (datetime.datetime):
        created_by_id (str):
        digest (str):
        id (str):
        name (str):
        retired_at (datetime.datetime | None):
        size (int):
        source (AssetSourceType0 | None):
        updated_at (datetime.datetime):
        version (int):
        workspace_id (str):
    """

    content_type: str
    created_at: datetime.datetime
    created_by_id: str
    digest: str
    id: str
    name: str
    retired_at: datetime.datetime | None
    size: int
    source: AssetSourceType0 | None
    updated_at: datetime.datetime
    version: int
    workspace_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.asset_source_type_0 import AssetSourceType0

        content_type = self.content_type

        created_at = self.created_at.isoformat()

        created_by_id = self.created_by_id

        digest = self.digest

        id = self.id

        name = self.name

        retired_at: str | None
        if isinstance(self.retired_at, datetime.datetime):
            retired_at = self.retired_at.isoformat()
        else:
            retired_at = self.retired_at

        size = self.size

        source: dict[str, Any] | None
        if isinstance(self.source, AssetSourceType0):
            source = self.source.to_dict()
        else:
            source = self.source

        updated_at = self.updated_at.isoformat()

        version = self.version

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content_type": content_type,
                "created_at": created_at,
                "created_by_id": created_by_id,
                "digest": digest,
                "id": id,
                "name": name,
                "retired_at": retired_at,
                "size": size,
                "source": source,
                "updated_at": updated_at,
                "version": version,
                "workspace_id": workspace_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_source_type_0 import AssetSourceType0

        d = dict(src_dict)
        content_type = d.pop("content_type")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        created_by_id = d.pop("created_by_id")

        digest = d.pop("digest")

        id = d.pop("id")

        name = d.pop("name")

        def _parse_retired_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                retired_at_type_0 = datetime.datetime.fromisoformat(data)

                return retired_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        retired_at = _parse_retired_at(d.pop("retired_at"))

        size = d.pop("size")

        def _parse_source(data: object) -> AssetSourceType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                source_type_0 = AssetSourceType0.from_dict(data)

                return source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AssetSourceType0 | None, data)

        source = _parse_source(d.pop("source"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        version = d.pop("version")

        workspace_id = d.pop("workspace_id")

        asset = cls(
            content_type=content_type,
            created_at=created_at,
            created_by_id=created_by_id,
            digest=digest,
            id=id,
            name=name,
            retired_at=retired_at,
            size=size,
            source=source,
            updated_at=updated_at,
            version=version,
            workspace_id=workspace_id,
        )

        asset.additional_properties = d
        return asset

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
