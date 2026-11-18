from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.environment_permission_set_input import EnvironmentPermissionSetInput
    from ..models.session_configuration import SessionConfiguration


T = TypeVar("T", bound="FreshRunEnvironmentInput")


@_attrs_define(repr=False)
class FreshRunEnvironmentInput:
    """Reserve a primary instance for this accepted Run without changing Thread mounts.

    Attributes:
        mode (Literal['fresh']):
        template_id (str):
        permission_ceiling (EnvironmentPermissionSetInput | Unset):
        session_binding (str | Unset):
        session_configuration (None | SessionConfiguration | Unset):
        working_directory (None | str | Unset):
    """

    mode: Literal["fresh"]
    template_id: str
    permission_ceiling: EnvironmentPermissionSetInput | Unset = UNSET
    session_binding: str | Unset = UNSET
    session_configuration: SessionConfiguration | Unset | None = UNSET
    working_directory: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.session_configuration import SessionConfiguration

        mode = self.mode

        template_id = self.template_id

        permission_ceiling: dict[str, Any] | Unset = UNSET
        if not isinstance(self.permission_ceiling, Unset):
            permission_ceiling = self.permission_ceiling.to_dict()

        session_binding = self.session_binding

        session_configuration: dict[str, Any] | Unset | None
        if isinstance(self.session_configuration, Unset):
            session_configuration = UNSET
        elif isinstance(self.session_configuration, SessionConfiguration):
            session_configuration = self.session_configuration.to_dict()
        else:
            session_configuration = self.session_configuration

        working_directory: str | Unset | None
        if isinstance(self.working_directory, Unset):
            working_directory = UNSET
        else:
            working_directory = self.working_directory

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "mode": mode,
                "template_id": template_id,
            }
        )
        if permission_ceiling is not UNSET:
            field_dict["permission_ceiling"] = permission_ceiling
        if session_binding is not UNSET:
            field_dict["session_binding"] = session_binding
        if session_configuration is not UNSET:
            field_dict["session_configuration"] = session_configuration
        if working_directory is not UNSET:
            field_dict["working_directory"] = working_directory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.environment_permission_set_input import EnvironmentPermissionSetInput
        from ..models.session_configuration import SessionConfiguration

        d = dict(src_dict)
        mode = cast(Literal["fresh"], d.pop("mode"))
        if mode != "fresh":
            raise ValueError(f"mode must match const 'fresh', got '{mode}'")

        template_id = d.pop("template_id")

        _permission_ceiling = d.pop("permission_ceiling", UNSET)
        permission_ceiling: EnvironmentPermissionSetInput | Unset
        if isinstance(_permission_ceiling, Unset):
            permission_ceiling = UNSET
        else:
            permission_ceiling = EnvironmentPermissionSetInput.from_dict(_permission_ceiling)

        session_binding = d.pop("session_binding", UNSET)

        def _parse_session_configuration(data: object) -> SessionConfiguration | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                session_configuration_type_0 = SessionConfiguration.from_dict(data)

                return session_configuration_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(SessionConfiguration | Unset | None, data)

        session_configuration = _parse_session_configuration(d.pop("session_configuration", UNSET))

        def _parse_working_directory(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        working_directory = _parse_working_directory(d.pop("working_directory", UNSET))

        fresh_run_environment_input = cls(
            mode=mode,
            template_id=template_id,
            permission_ceiling=permission_ceiling,
            session_binding=session_binding,
            session_configuration=session_configuration,
            working_directory=working_directory,
        )

        return fresh_run_environment_input
