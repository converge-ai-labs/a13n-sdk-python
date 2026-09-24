from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.environment_failure import EnvironmentFailure


T = TypeVar("T", bound="EnvironmentView")


@_attrs_define(repr=False)
class EnvironmentView:
    """
    Attributes:
        created_at (datetime.datetime):
        created_by_id (str):
        device_id (None | str):
        endpoint (None | str):
        failure (EnvironmentFailure | None):
        id (str):
        last_used_at (datetime.datetime | None):
        name (str):
        operation_id (None | str):
        operation_started_at (datetime.datetime | None):
        organization_id (str):
        owner_principal_id (None | str):
        provider_id (None | str):
        status (str):
        template_id (None | str):
        updated_at (datetime.datetime):
        version (int):
        workspace_id (str):
    """

    created_at: datetime.datetime
    created_by_id: str
    device_id: str | None
    endpoint: str | None
    failure: EnvironmentFailure | None
    id: str
    last_used_at: datetime.datetime | None
    name: str
    operation_id: str | None
    operation_started_at: datetime.datetime | None
    organization_id: str
    owner_principal_id: str | None
    provider_id: str | None
    status: str
    template_id: str | None
    updated_at: datetime.datetime
    version: int
    workspace_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.environment_failure import EnvironmentFailure

        created_at = self.created_at.isoformat()

        created_by_id = self.created_by_id

        device_id: str | None
        device_id = self.device_id

        endpoint: str | None
        endpoint = self.endpoint

        failure: dict[str, Any] | None
        if isinstance(self.failure, EnvironmentFailure):
            failure = self.failure.to_dict()
        else:
            failure = self.failure

        id = self.id

        last_used_at: str | None
        if isinstance(self.last_used_at, datetime.datetime):
            last_used_at = self.last_used_at.isoformat()
        else:
            last_used_at = self.last_used_at

        name = self.name

        operation_id: str | None
        operation_id = self.operation_id

        operation_started_at: str | None
        if isinstance(self.operation_started_at, datetime.datetime):
            operation_started_at = self.operation_started_at.isoformat()
        else:
            operation_started_at = self.operation_started_at

        organization_id = self.organization_id

        owner_principal_id: str | None
        owner_principal_id = self.owner_principal_id

        provider_id: str | None
        provider_id = self.provider_id

        status = self.status

        template_id: str | None
        template_id = self.template_id

        updated_at = self.updated_at.isoformat()

        version = self.version

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "created_by_id": created_by_id,
                "device_id": device_id,
                "endpoint": endpoint,
                "failure": failure,
                "id": id,
                "last_used_at": last_used_at,
                "name": name,
                "operation_id": operation_id,
                "operation_started_at": operation_started_at,
                "organization_id": organization_id,
                "owner_principal_id": owner_principal_id,
                "provider_id": provider_id,
                "status": status,
                "template_id": template_id,
                "updated_at": updated_at,
                "version": version,
                "workspace_id": workspace_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.environment_failure import EnvironmentFailure

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        created_by_id = d.pop("created_by_id")

        def _parse_device_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        device_id = _parse_device_id(d.pop("device_id"))

        def _parse_endpoint(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        endpoint = _parse_endpoint(d.pop("endpoint"))

        def _parse_failure(data: object) -> EnvironmentFailure | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                failure_type_0 = EnvironmentFailure.from_dict(data)

                return failure_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnvironmentFailure | None, data)

        failure = _parse_failure(d.pop("failure"))

        id = d.pop("id")

        def _parse_last_used_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_used_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_used_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_used_at = _parse_last_used_at(d.pop("last_used_at"))

        name = d.pop("name")

        def _parse_operation_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        operation_id = _parse_operation_id(d.pop("operation_id"))

        def _parse_operation_started_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                operation_started_at_type_0 = datetime.datetime.fromisoformat(data)

                return operation_started_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        operation_started_at = _parse_operation_started_at(d.pop("operation_started_at"))

        organization_id = d.pop("organization_id")

        def _parse_owner_principal_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        owner_principal_id = _parse_owner_principal_id(d.pop("owner_principal_id"))

        def _parse_provider_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        provider_id = _parse_provider_id(d.pop("provider_id"))

        status = d.pop("status")

        def _parse_template_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        template_id = _parse_template_id(d.pop("template_id"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        version = d.pop("version")

        workspace_id = d.pop("workspace_id")

        environment_view = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            device_id=device_id,
            endpoint=endpoint,
            failure=failure,
            id=id,
            last_used_at=last_used_at,
            name=name,
            operation_id=operation_id,
            operation_started_at=operation_started_at,
            organization_id=organization_id,
            owner_principal_id=owner_principal_id,
            provider_id=provider_id,
            status=status,
            template_id=template_id,
            updated_at=updated_at,
            version=version,
            workspace_id=workspace_id,
        )

        environment_view.additional_properties = d
        return environment_view

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
