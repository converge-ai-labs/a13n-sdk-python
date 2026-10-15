from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.environment_permission_set_input import EnvironmentPermissionSetInput


T = TypeVar("T", bound="MountUpdate")


@_attrs_define(repr=False)
class MountUpdate:
    """
    Attributes:
        permission_ceiling (EnvironmentPermissionSetInput):
    """

    permission_ceiling: EnvironmentPermissionSetInput

    def to_dict(self) -> dict[str, Any]:
        permission_ceiling = self.permission_ceiling.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "permission_ceiling": permission_ceiling,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.environment_permission_set_input import EnvironmentPermissionSetInput

        d = dict(src_dict)
        permission_ceiling = EnvironmentPermissionSetInput.from_dict(d.pop("permission_ceiling"))

        mount_update = cls(
            permission_ceiling=permission_ceiling,
        )

        return mount_update
