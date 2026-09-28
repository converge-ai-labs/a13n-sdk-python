from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_metrics import ModelMetrics


T = TypeVar("T", bound="ModelUsageGroup")


@_attrs_define(repr=False)
class ModelUsageGroup:
    """
    Attributes:
        model (None | str):
        name (None | str):
        usage (ModelMetrics):
    """

    model: str | None
    name: str | None
    usage: ModelMetrics
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        model: str | None
        model = self.model

        name: str | None
        name = self.name

        usage = self.usage.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "model": model,
                "name": name,
                "usage": usage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_metrics import ModelMetrics

        d = dict(src_dict)

        def _parse_model(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        model = _parse_model(d.pop("model"))

        def _parse_name(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        name = _parse_name(d.pop("name"))

        usage = ModelMetrics.from_dict(d.pop("usage"))

        model_usage_group = cls(
            model=model,
            name=name,
            usage=usage,
        )

        model_usage_group.additional_properties = d
        return model_usage_group

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
