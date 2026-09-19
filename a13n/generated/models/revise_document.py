from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.append import Append
    from ..models.edit import Edit
    from ..models.patch import Patch
    from ..models.replace import Replace


T = TypeVar("T", bound="ReviseDocument")


@_attrs_define(repr=False)
class ReviseDocument:
    """
    Attributes:
        change (Append | Edit | Patch | Replace):
        expected_version (int):
    """

    change: Append | Edit | Patch | Replace
    expected_version: int

    def to_dict(self) -> dict[str, Any]:
        from ..models.append import Append
        from ..models.edit import Edit
        from ..models.replace import Replace

        change: dict[str, Any]
        if isinstance(self.change, Replace):
            change = self.change.to_dict()
        elif isinstance(self.change, Append):
            change = self.change.to_dict()
        elif isinstance(self.change, Edit):
            change = self.change.to_dict()
        else:
            change = self.change.to_dict()

        expected_version = self.expected_version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "change": change,
                "expected_version": expected_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.append import Append
        from ..models.edit import Edit
        from ..models.patch import Patch
        from ..models.replace import Replace

        d = dict(src_dict)

        def _parse_change(data: object) -> Append | Edit | Patch | Replace:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                change_type_0 = Replace.from_dict(data)

                return change_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                change_type_1 = Append.from_dict(data)

                return change_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                change_type_2 = Edit.from_dict(data)

                return change_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            change_type_3 = Patch.from_dict(data)

            return change_type_3

        change = _parse_change(d.pop("change"))

        expected_version = d.pop("expected_version")

        revise_document = cls(
            change=change,
            expected_version=expected_version,
        )

        return revise_document
