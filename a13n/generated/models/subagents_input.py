from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.subagents_input_mode import SubagentsInputMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.dynamic_subagents_input import DynamicSubagentsInput
    from ..models.subagents_input_named import SubagentsInputNamed


T = TypeVar("T", bound="SubagentsInput")


@_attrs_define(repr=False)
class SubagentsInput:
    """
    Attributes:
        dynamic (DynamicSubagentsInput | Unset): Root-only task-specific delegation within the parent's capability
            boundary.
        mode (SubagentsInputMode | Unset):
        named (SubagentsInputNamed | Unset):
    """

    dynamic: DynamicSubagentsInput | Unset = UNSET
    mode: SubagentsInputMode | Unset = UNSET
    named: SubagentsInputNamed | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        dynamic: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dynamic, Unset):
            dynamic = self.dynamic.to_dict()

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        named: dict[str, Any] | Unset = UNSET
        if not isinstance(self.named, Unset):
            named = self.named.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if dynamic is not UNSET:
            field_dict["dynamic"] = dynamic
        if mode is not UNSET:
            field_dict["mode"] = mode
        if named is not UNSET:
            field_dict["named"] = named

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dynamic_subagents_input import DynamicSubagentsInput
        from ..models.subagents_input_named import SubagentsInputNamed

        d = dict(src_dict)
        _dynamic = d.pop("dynamic", UNSET)
        dynamic: DynamicSubagentsInput | Unset
        if isinstance(_dynamic, Unset):
            dynamic = UNSET
        else:
            dynamic = DynamicSubagentsInput.from_dict(_dynamic)

        _mode = d.pop("mode", UNSET)
        mode: SubagentsInputMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = SubagentsInputMode(_mode)

        _named = d.pop("named", UNSET)
        named: SubagentsInputNamed | Unset
        if isinstance(_named, Unset):
            named = UNSET
        else:
            named = SubagentsInputNamed.from_dict(_named)

        subagents_input = cls(
            dynamic=dynamic,
            mode=mode,
            named=named,
        )

        return subagents_input
