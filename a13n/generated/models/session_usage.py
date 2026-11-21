from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_metrics import ModelMetrics
    from ..models.run_metrics import RunMetrics


T = TypeVar("T", bound="SessionUsage")


@_attrs_define(repr=False)
class SessionUsage:
    """
    Attributes:
        runs (RunMetrics):
        session_id (str):
        title (None | str):
        usage (ModelMetrics):
    """

    runs: RunMetrics
    session_id: str
    title: str | None
    usage: ModelMetrics
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        runs = self.runs.to_dict()

        session_id = self.session_id

        title: str | None
        title = self.title

        usage = self.usage.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "runs": runs,
                "session_id": session_id,
                "title": title,
                "usage": usage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_metrics import ModelMetrics
        from ..models.run_metrics import RunMetrics

        d = dict(src_dict)
        runs = RunMetrics.from_dict(d.pop("runs"))

        session_id = d.pop("session_id")

        def _parse_title(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        title = _parse_title(d.pop("title"))

        usage = ModelMetrics.from_dict(d.pop("usage"))

        session_usage = cls(
            runs=runs,
            session_id=session_id,
            title=title,
            usage=usage,
        )

        session_usage.additional_properties = d
        return session_usage

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
