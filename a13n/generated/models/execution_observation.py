from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.execution_observation_source import ExecutionObservationSource
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execution_view import ExecutionView
    from ..models.shell_preview import ShellPreview


T = TypeVar("T", bound="ExecutionObservation")


@_attrs_define(repr=False)
class ExecutionObservation:
    """
    Attributes:
        execution (ExecutionView): Run identity is the Service Run; attempt and worker identify the retained owner.
        source (ExecutionObservationSource):
        shell (None | ShellPreview | Unset):
    """

    execution: ExecutionView
    source: ExecutionObservationSource
    shell: ShellPreview | Unset | None = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.shell_preview import ShellPreview

        execution = self.execution.to_dict()

        source = self.source.value

        shell: dict[str, Any] | Unset | None
        if isinstance(self.shell, Unset):
            shell = UNSET
        elif isinstance(self.shell, ShellPreview):
            shell = self.shell.to_dict()
        else:
            shell = self.shell

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "execution": execution,
                "source": source,
            }
        )
        if shell is not UNSET:
            field_dict["shell"] = shell

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_view import ExecutionView
        from ..models.shell_preview import ShellPreview

        d = dict(src_dict)
        execution = ExecutionView.from_dict(d.pop("execution"))

        source = ExecutionObservationSource(d.pop("source"))

        def _parse_shell(data: object) -> ShellPreview | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                shell_type_0 = ShellPreview.from_dict(data)

                return shell_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ShellPreview | Unset | None, data)

        shell = _parse_shell(d.pop("shell", UNSET))

        execution_observation = cls(
            execution=execution,
            source=source,
            shell=shell,
        )

        execution_observation.additional_properties = d
        return execution_observation

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
