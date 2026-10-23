from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_data import QueryData


T = TypeVar("T", bound="QueryResult")


@_attrs_define(repr=False)
class QueryResult:
    """
    Attributes:
        data (QueryData):
        status (Literal['success']):
        infos (list[str] | Unset):
        warnings (list[str] | Unset):
    """

    data: QueryData
    status: Literal["success"]
    infos: list[str] | Unset = UNSET
    warnings: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        status = self.status

        infos: list[str] | Unset = UNSET
        if not isinstance(self.infos, Unset):
            infos = self.infos

        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "status": status,
            }
        )
        if infos is not UNSET:
            field_dict["infos"] = infos
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_data import QueryData

        d = dict(src_dict)
        data = QueryData.from_dict(d.pop("data"))

        status = cast(Literal["success"], d.pop("status"))
        if status != "success":
            raise ValueError(f"status must match const 'success', got '{status}'")

        infos = cast(list[str], d.pop("infos", UNSET))

        warnings = cast(list[str], d.pop("warnings", UNSET))

        query_result = cls(
            data=data,
            status=status,
            infos=infos,
            warnings=warnings,
        )

        query_result.additional_properties = d
        return query_result

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
