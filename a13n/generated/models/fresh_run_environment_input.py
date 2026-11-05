from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.environment_permission_set_input import EnvironmentPermissionSetInput


T = TypeVar("T", bound="FreshRunEnvironmentInput")


@_attrs_define(repr=False)
class FreshRunEnvironmentInput:
    """Reserve a primary instance for this accepted Run without changing Thread mounts.

    Attributes:
        mode (Literal['fresh']):
        template_id (str):
        permission_ceiling (EnvironmentPermissionSetInput | Unset):
        working_directory (None | str | Unset):
    """

    mode: Literal["fresh"]
    template_id: str
    permission_ceiling: EnvironmentPermissionSetInput | Unset = UNSET
    working_directory: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        template_id = self.template_id

        permission_ceiling: dict[str, Any] | Unset = UNSET
        if not isinstance(self.permission_ceiling, Unset):
            permission_ceiling = self.permission_ceiling.to_dict()

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
        if working_directory is not UNSET:
            field_dict["working_directory"] = working_directory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.environment_permission_set_input import EnvironmentPermissionSetInput

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
            working_directory=working_directory,
        )

        return fresh_run_environment_input
