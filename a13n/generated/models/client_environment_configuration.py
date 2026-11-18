from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.environment_permission_set_output import EnvironmentPermissionSetOutput


T = TypeVar("T", bound="ClientEnvironmentConfiguration")


@_attrs_define(repr=False)
class ClientEnvironmentConfiguration:
    """
    Attributes:
        default_working_directory (str):
        declared_capabilities (EnvironmentPermissionSetOutput | None | Unset):
        description (None | str | Unset):
        permission_ceiling (EnvironmentPermissionSetOutput | Unset):
    """

    default_working_directory: str
    declared_capabilities: EnvironmentPermissionSetOutput | Unset | None = UNSET
    description: str | Unset | None = UNSET
    permission_ceiling: EnvironmentPermissionSetOutput | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.environment_permission_set_output import EnvironmentPermissionSetOutput

        default_working_directory = self.default_working_directory

        declared_capabilities: dict[str, Any] | Unset | None
        if isinstance(self.declared_capabilities, Unset):
            declared_capabilities = UNSET
        elif isinstance(self.declared_capabilities, EnvironmentPermissionSetOutput):
            declared_capabilities = self.declared_capabilities.to_dict()
        else:
            declared_capabilities = self.declared_capabilities

        description: str | Unset | None
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        permission_ceiling: dict[str, Any] | Unset = UNSET
        if not isinstance(self.permission_ceiling, Unset):
            permission_ceiling = self.permission_ceiling.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "default_working_directory": default_working_directory,
            }
        )
        if declared_capabilities is not UNSET:
            field_dict["declared_capabilities"] = declared_capabilities
        if description is not UNSET:
            field_dict["description"] = description
        if permission_ceiling is not UNSET:
            field_dict["permission_ceiling"] = permission_ceiling

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.environment_permission_set_output import EnvironmentPermissionSetOutput

        d = dict(src_dict)
        default_working_directory = d.pop("default_working_directory")

        def _parse_declared_capabilities(data: object) -> EnvironmentPermissionSetOutput | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                declared_capabilities_type_0 = EnvironmentPermissionSetOutput.from_dict(data)

                return declared_capabilities_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnvironmentPermissionSetOutput | Unset | None, data)

        declared_capabilities = _parse_declared_capabilities(d.pop("declared_capabilities", UNSET))

        def _parse_description(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        description = _parse_description(d.pop("description", UNSET))

        _permission_ceiling = d.pop("permission_ceiling", UNSET)
        permission_ceiling: EnvironmentPermissionSetOutput | Unset
        if isinstance(_permission_ceiling, Unset):
            permission_ceiling = UNSET
        else:
            permission_ceiling = EnvironmentPermissionSetOutput.from_dict(_permission_ceiling)

        client_environment_configuration = cls(
            default_working_directory=default_working_directory,
            declared_capabilities=declared_capabilities,
            description=description,
            permission_ceiling=permission_ceiling,
        )

        return client_environment_configuration
