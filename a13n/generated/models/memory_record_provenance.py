from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.memory_record_source import MemoryRecordSource


T = TypeVar("T", bound="MemoryRecordProvenance")


@_attrs_define(repr=False)
class MemoryRecordProvenance:
    """
    Attributes:
        content_matches (bool):
        created (MemoryRecordSource | None):
        last_write (MemoryRecordSource): A platform-confirmed write, not an asserted source message or complete provider
            history.
    """

    content_matches: bool
    created: MemoryRecordSource | None
    last_write: MemoryRecordSource
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.memory_record_source import MemoryRecordSource

        content_matches = self.content_matches

        created: dict[str, Any] | None
        if isinstance(self.created, MemoryRecordSource):
            created = self.created.to_dict()
        else:
            created = self.created

        last_write = self.last_write.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content_matches": content_matches,
                "created": created,
                "last_write": last_write,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.memory_record_source import MemoryRecordSource

        d = dict(src_dict)
        content_matches = d.pop("content_matches")

        def _parse_created(data: object) -> MemoryRecordSource | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                created_type_0 = MemoryRecordSource.from_dict(data)

                return created_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MemoryRecordSource | None, data)

        created = _parse_created(d.pop("created"))

        last_write = MemoryRecordSource.from_dict(d.pop("last_write"))

        memory_record_provenance = cls(
            content_matches=content_matches,
            created=created,
            last_write=last_write,
        )

        memory_record_provenance.additional_properties = d
        return memory_record_provenance

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
