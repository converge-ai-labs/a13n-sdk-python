from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ProcessStatusProjection")


@_attrs_define(repr=False)
class ProcessStatusProjection:
    """
    Attributes:
        cleanup (None | str):
        exit_code (int | None):
        phase (str):
        signal (None | str):
        termination_reason (None | str):
    """

    cleanup: str | None
    exit_code: int | None
    phase: str
    signal: str | None
    termination_reason: str | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cleanup: str | None
        cleanup = self.cleanup

        exit_code: int | None
        exit_code = self.exit_code

        phase = self.phase

        signal: str | None
        signal = self.signal

        termination_reason: str | None
        termination_reason = self.termination_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cleanup": cleanup,
                "exit_code": exit_code,
                "phase": phase,
                "signal": signal,
                "termination_reason": termination_reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_cleanup(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        cleanup = _parse_cleanup(d.pop("cleanup"))

        def _parse_exit_code(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        exit_code = _parse_exit_code(d.pop("exit_code"))

        phase = d.pop("phase")

        def _parse_signal(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        signal = _parse_signal(d.pop("signal"))

        def _parse_termination_reason(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        termination_reason = _parse_termination_reason(d.pop("termination_reason"))

        process_status_projection = cls(
            cleanup=cleanup,
            exit_code=exit_code,
            phase=phase,
            signal=signal,
            termination_reason=termination_reason,
        )

        process_status_projection.additional_properties = d
        return process_status_projection

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
