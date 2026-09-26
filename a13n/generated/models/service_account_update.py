from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.service_account_update_status_type_0 import ServiceAccountUpdateStatusType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceAccountUpdate")


@_attrs_define(repr=False)
class ServiceAccountUpdate:
    """
    Attributes:
        description (None | str | Unset):
        name (None | str | Unset):
        role (None | str | Unset):
        status (None | ServiceAccountUpdateStatusType0 | Unset):
    """

    description: str | Unset | None = UNSET
    name: str | Unset | None = UNSET
    role: str | Unset | None = UNSET
    status: ServiceAccountUpdateStatusType0 | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        description: str | Unset | None
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        name: str | Unset | None
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        role: str | Unset | None
        if isinstance(self.role, Unset):
            role = UNSET
        else:
            role = self.role

        status: str | Unset | None
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, ServiceAccountUpdateStatusType0):
            status = self.status.value
        else:
            status = self.status

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if role is not UNSET:
            field_dict["role"] = role
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_description(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_name(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_role(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        role = _parse_role(d.pop("role", UNSET))

        def _parse_status(data: object) -> ServiceAccountUpdateStatusType0 | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = ServiceAccountUpdateStatusType0(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ServiceAccountUpdateStatusType0 | Unset | None, data)

        status = _parse_status(d.pop("status", UNSET))

        service_account_update = cls(
            description=description,
            name=name,
            role=role,
            status=status,
        )

        return service_account_update
