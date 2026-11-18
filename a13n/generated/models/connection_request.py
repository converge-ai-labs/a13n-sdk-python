from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.environment_permission_set_input import EnvironmentPermissionSetInput


T = TypeVar("T", bound="ConnectionRequest")


@_attrs_define(repr=False)
class ConnectionRequest:
    """
    Attributes:
        default_working_directory (str):
        device_id (str):
        name (str):
        declared_capabilities (EnvironmentPermissionSetInput | None | Unset):
        description (None | str | Unset):
        environment_id (None | str | Unset):
        permission_ceiling (EnvironmentPermissionSetInput | Unset):
    """

    default_working_directory: str
    device_id: str
    name: str
    declared_capabilities: EnvironmentPermissionSetInput | Unset | None = UNSET
    description: str | Unset | None = UNSET
    environment_id: str | Unset | None = UNSET
    permission_ceiling: EnvironmentPermissionSetInput | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.environment_permission_set_input import EnvironmentPermissionSetInput

        default_working_directory = self.default_working_directory

        device_id = self.device_id

        name = self.name

        declared_capabilities: dict[str, Any] | Unset | None
        if isinstance(self.declared_capabilities, Unset):
            declared_capabilities = UNSET
        elif isinstance(self.declared_capabilities, EnvironmentPermissionSetInput):
            declared_capabilities = self.declared_capabilities.to_dict()
        else:
            declared_capabilities = self.declared_capabilities

        description: str | Unset | None
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        environment_id: str | Unset | None
        if isinstance(self.environment_id, Unset):
            environment_id = UNSET
        else:
            environment_id = self.environment_id

        permission_ceiling: dict[str, Any] | Unset = UNSET
        if not isinstance(self.permission_ceiling, Unset):
            permission_ceiling = self.permission_ceiling.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "default_working_directory": default_working_directory,
                "device_id": device_id,
                "name": name,
            }
        )
        if declared_capabilities is not UNSET:
            field_dict["declared_capabilities"] = declared_capabilities
        if description is not UNSET:
            field_dict["description"] = description
        if environment_id is not UNSET:
            field_dict["environment_id"] = environment_id
        if permission_ceiling is not UNSET:
            field_dict["permission_ceiling"] = permission_ceiling

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.environment_permission_set_input import EnvironmentPermissionSetInput

        d = dict(src_dict)
        default_working_directory = d.pop("default_working_directory")

        device_id = d.pop("device_id")

        name = d.pop("name")

        def _parse_declared_capabilities(data: object) -> EnvironmentPermissionSetInput | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                declared_capabilities_type_0 = EnvironmentPermissionSetInput.from_dict(data)

                return declared_capabilities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnvironmentPermissionSetInput | Unset | None, data)

        declared_capabilities = _parse_declared_capabilities(d.pop("declared_capabilities", UNSET))

        def _parse_description(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_environment_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        environment_id = _parse_environment_id(d.pop("environment_id", UNSET))

        _permission_ceiling = d.pop("permission_ceiling", UNSET)
        permission_ceiling: EnvironmentPermissionSetInput | Unset
        if isinstance(_permission_ceiling, Unset):
            permission_ceiling = UNSET
        else:
            permission_ceiling = EnvironmentPermissionSetInput.from_dict(_permission_ceiling)

        connection_request = cls(
            default_working_directory=default_working_directory,
            device_id=device_id,
            name=name,
            declared_capabilities=declared_capabilities,
            description=description,
            environment_id=environment_id,
            permission_ceiling=permission_ceiling,
        )

        return connection_request
