from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.output_preview import OutputPreview
    from ..models.process_status_projection import ProcessStatusProjection


T = TypeVar("T", bound="ShellPreview")


@_attrs_define(repr=False)
class ShellPreview:
    """
    Attributes:
        status (ProcessStatusProjection):
        stderr (OutputPreview):
        stdout (OutputPreview):
    """

    status: ProcessStatusProjection
    stderr: OutputPreview
    stdout: OutputPreview
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.to_dict()

        stderr = self.stderr.to_dict()

        stdout = self.stdout.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "stderr": stderr,
                "stdout": stdout,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_preview import OutputPreview
        from ..models.process_status_projection import ProcessStatusProjection

        d = dict(src_dict)
        status = ProcessStatusProjection.from_dict(d.pop("status"))

        stderr = OutputPreview.from_dict(d.pop("stderr"))

        stdout = OutputPreview.from_dict(d.pop("stdout"))

        shell_preview = cls(
            status=status,
            stderr=stderr,
            stdout=stdout,
        )

        shell_preview.additional_properties = d
        return shell_preview

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
