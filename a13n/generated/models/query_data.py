from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.query_data_resulttype import QueryDataResulttype

T = TypeVar("T", bound="QueryData")


@_attrs_define(repr=False)
class QueryData:
    """
    Attributes:
        result (list[Any]):
        result_type (QueryDataResulttype):
    """

    result: list[Any]
    result_type: QueryDataResulttype
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        result = self.result

        result_type = self.result_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "result": result,
                "resultType": result_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        result = cast(list[Any], d.pop("result"))

        result_type = QueryDataResulttype(d.pop("resultType"))

        query_data = cls(
            result=result,
            result_type=result_type,
        )

        query_data.additional_properties = d
        return query_data

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
