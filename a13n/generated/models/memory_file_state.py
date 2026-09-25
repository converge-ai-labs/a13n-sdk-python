from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.memory_file import MemoryFile


T = TypeVar("T", bound="MemoryFileState")


@_attrs_define(repr=False)
class MemoryFileState:
    """A path after a restore: its file, or null when the restored state is no file.

    Attributes:
        file (MemoryFile | None):
        path (str):
    """

    file: MemoryFile | None
    path: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.memory_file import MemoryFile

        file: dict[str, Any] | None
        if isinstance(self.file, MemoryFile):
            file = self.file.to_dict()
        else:
            file = self.file

        path = self.path

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "file": file,
                "path": path,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.memory_file import MemoryFile

        d = dict(src_dict)

        def _parse_file(data: object) -> MemoryFile | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                file_type_0 = MemoryFile.from_dict(data)

                return file_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MemoryFile | None, data)

        file = _parse_file(d.pop("file"))

        path = d.pop("path")

        memory_file_state = cls(
            file=file,
            path=path,
        )

        memory_file_state.additional_properties = d
        return memory_file_state

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
