from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.replacement import Replacement


T = TypeVar("T", bound="Edit")


@_attrs_define(repr=False)
class Edit:
    """
    Attributes:
        edits (list[Replacement]):
        type_ (Literal['edit']):
    """

    edits: list[Replacement]
    type_: Literal["edit"]

    def to_dict(self) -> dict[str, Any]:
        edits = []
        for edits_item_data in self.edits:
            edits_item = edits_item_data.to_dict()
            edits.append(edits_item)

        type_ = self.type_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "edits": edits,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.replacement import Replacement

        d = dict(src_dict)
        edits = []
        _edits = d.pop("edits")
        for edits_item_data in _edits:
            edits_item = Replacement.from_dict(edits_item_data)

            edits.append(edits_item)

        type_ = cast(Literal["edit"], d.pop("type"))
        if type_ != "edit":
            raise ValueError(f"type must match const 'edit', got '{type_}'")

        edit = cls(
            edits=edits,
            type_=type_,
        )

        return edit
