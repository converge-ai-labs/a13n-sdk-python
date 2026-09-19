from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OrganizationStatus")


@_attrs_define(repr=False)
class OrganizationStatus:
    """
    Attributes:
        id (str):
        run_id (str):
        status (str):
        committed (int | Unset):
        deferred (int | Unset):
        error_code (None | str | Unset):
    """

    id: str
    run_id: str
    status: str
    committed: int | Unset = UNSET
    deferred: int | Unset = UNSET
    error_code: str | Unset | None = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        run_id = self.run_id

        status = self.status

        committed = self.committed

        deferred = self.deferred

        error_code: str | Unset | None
        if isinstance(self.error_code, Unset):
            error_code = UNSET
        else:
            error_code = self.error_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "run_id": run_id,
                "status": status,
            }
        )
        if committed is not UNSET:
            field_dict["committed"] = committed
        if deferred is not UNSET:
            field_dict["deferred"] = deferred
        if error_code is not UNSET:
            field_dict["error_code"] = error_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        run_id = d.pop("run_id")

        status = d.pop("status")

        committed = d.pop("committed", UNSET)

        deferred = d.pop("deferred", UNSET)

        def _parse_error_code(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        error_code = _parse_error_code(d.pop("error_code", UNSET))

        organization_status = cls(
            id=id,
            run_id=run_id,
            status=status,
            committed=committed,
            deferred=deferred,
            error_code=error_code,
        )

        organization_status.additional_properties = d
        return organization_status

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
