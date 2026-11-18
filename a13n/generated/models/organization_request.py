from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.organization_request_output import OrganizationRequestOutput
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_memory_target import FileMemoryTarget
    from ..models.organization_history import OrganizationHistory
    from ..models.space_target import SpaceTarget


T = TypeVar("T", bound="OrganizationRequest")


@_attrs_define(repr=False)
class OrganizationRequest:
    """
    Attributes:
        model (str):
        target (FileMemoryTarget | SpaceTarget):
        history (None | OrganizationHistory | Unset):
        instructions (str | Unset):
        output (OrganizationRequestOutput | Unset):
    """

    model: str
    target: FileMemoryTarget | SpaceTarget
    history: OrganizationHistory | Unset | None = UNSET
    instructions: str | Unset = UNSET
    output: OrganizationRequestOutput | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.file_memory_target import FileMemoryTarget
        from ..models.organization_history import OrganizationHistory

        model = self.model

        target: dict[str, Any]
        if isinstance(self.target, FileMemoryTarget):
            target = self.target.to_dict()
        else:
            target = self.target.to_dict()

        history: dict[str, Any] | Unset | None
        if isinstance(self.history, Unset):
            history = UNSET
        elif isinstance(self.history, OrganizationHistory):
            history = self.history.to_dict()
        else:
            history = self.history

        instructions = self.instructions

        output: str | Unset = UNSET
        if not isinstance(self.output, Unset):
            output = self.output.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "model": model,
                "target": target,
            }
        )
        if history is not UNSET:
            field_dict["history"] = history
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if output is not UNSET:
            field_dict["output"] = output

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_memory_target import FileMemoryTarget
        from ..models.organization_history import OrganizationHistory
        from ..models.space_target import SpaceTarget

        d = dict(src_dict)
        model = d.pop("model")

        def _parse_target(data: object) -> FileMemoryTarget | SpaceTarget:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_organization_target_type_0 = FileMemoryTarget.from_dict(data)

                return componentsschemas_organization_target_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_organization_target_type_1 = SpaceTarget.from_dict(data)

            return componentsschemas_organization_target_type_1

        target = _parse_target(d.pop("target"))

        def _parse_history(data: object) -> OrganizationHistory | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                history_type_0 = OrganizationHistory.from_dict(data)

                return history_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(OrganizationHistory | Unset | None, data)

        history = _parse_history(d.pop("history", UNSET))

        instructions = d.pop("instructions", UNSET)

        _output = d.pop("output", UNSET)
        output: OrganizationRequestOutput | Unset
        if isinstance(_output, Unset):
            output = UNSET
        else:
            output = OrganizationRequestOutput(_output)

        organization_request = cls(
            model=model,
            target=target,
            history=history,
            instructions=instructions,
            output=output,
        )

        return organization_request
