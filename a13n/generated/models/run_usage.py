from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.model_usage import ModelUsage


T = TypeVar("T", bound="RunUsage")


@_attrs_define(repr=False)
class RunUsage:
    """
    Attributes:
        models (list[ModelUsage]):
        run_id (str):
        thread_id (str):
    """

    models: list[ModelUsage]
    run_id: str
    thread_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        models = []
        for models_item_data in self.models:
            models_item = models_item_data.to_dict()
            models.append(models_item)

        run_id = self.run_id

        thread_id = self.thread_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "models": models,
                "run_id": run_id,
                "thread_id": thread_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.model_usage import ModelUsage

        d = dict(src_dict)
        models = []
        _models = d.pop("models")
        for models_item_data in _models:
            models_item = ModelUsage.from_dict(models_item_data)

            models.append(models_item)

        run_id = d.pop("run_id")

        thread_id = d.pop("thread_id")

        run_usage = cls(
            models=models,
            run_id=run_id,
            thread_id=thread_id,
        )

        run_usage.additional_properties = d
        return run_usage

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
