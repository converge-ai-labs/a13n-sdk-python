from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.failed import Failed
    from ..models.returned import Returned


T = TypeVar("T", bound="PendingAnswerCalls")


@_attrs_define(repr=False)
class PendingAnswerCalls:
    additional_properties: dict[str, Failed | Returned] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.returned import Returned

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, Returned):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.failed import Failed
        from ..models.returned import Returned

        d = dict(src_dict)
        pending_answer_calls = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(data: object) -> Failed | Returned:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_call_result_type_0 = Returned.from_dict(data)

                    return componentsschemas_call_result_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_call_result_type_1 = Failed.from_dict(data)

                return componentsschemas_call_result_type_1

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        pending_answer_calls.additional_properties = additional_properties
        return pending_answer_calls

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Failed | Returned:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Failed | Returned) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
