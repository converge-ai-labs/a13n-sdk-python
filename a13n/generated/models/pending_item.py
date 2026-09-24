from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.pending_kind import PendingKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pending_item_arguments import PendingItemArguments
    from ..models.pending_item_presentation_type_0 import PendingItemPresentationType0


T = TypeVar("T", bound="PendingItem")


@_attrs_define(repr=False)
class PendingItem:
    """
    Attributes:
        arguments (PendingItemArguments):
        kind (PendingKind):
        tool_call_id (str):
        tool_name (str):
        presentation (None | PendingItemPresentationType0 | Unset):
    """

    arguments: PendingItemArguments
    kind: PendingKind
    tool_call_id: str
    tool_name: str
    presentation: PendingItemPresentationType0 | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.pending_item_presentation_type_0 import PendingItemPresentationType0

        arguments = self.arguments.to_dict()

        kind = self.kind.value

        tool_call_id = self.tool_call_id

        tool_name = self.tool_name

        presentation: dict[str, Any] | Unset | None
        if isinstance(self.presentation, Unset):
            presentation = UNSET
        elif isinstance(self.presentation, PendingItemPresentationType0):
            presentation = self.presentation.to_dict()
        else:
            presentation = self.presentation

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "arguments": arguments,
                "kind": kind,
                "tool_call_id": tool_call_id,
                "tool_name": tool_name,
            }
        )
        if presentation is not UNSET:
            field_dict["presentation"] = presentation

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pending_item_arguments import PendingItemArguments
        from ..models.pending_item_presentation_type_0 import PendingItemPresentationType0

        d = dict(src_dict)
        arguments = PendingItemArguments.from_dict(d.pop("arguments"))

        kind = PendingKind(d.pop("kind"))

        tool_call_id = d.pop("tool_call_id")

        tool_name = d.pop("tool_name")

        def _parse_presentation(data: object) -> PendingItemPresentationType0 | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                presentation_type_0 = PendingItemPresentationType0.from_dict(data)

                return presentation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(PendingItemPresentationType0 | Unset | None, data)

        presentation = _parse_presentation(d.pop("presentation", UNSET))

        pending_item = cls(
            arguments=arguments,
            kind=kind,
            tool_call_id=tool_call_id,
            tool_name=tool_name,
            presentation=presentation,
        )

        return pending_item
