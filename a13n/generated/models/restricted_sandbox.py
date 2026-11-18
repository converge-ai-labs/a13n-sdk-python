from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sandbox_grant import SandboxGrant


T = TypeVar("T", bound="RestrictedSandbox")


@_attrs_define(repr=False)
class RestrictedSandbox:
    """
    Attributes:
        mode (Literal['restricted']):
        full_disk_read (bool | Unset):
        grants (list[SandboxGrant] | Unset):
    """

    mode: Literal["restricted"]
    full_disk_read: bool | Unset = UNSET
    grants: list[SandboxGrant] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        full_disk_read = self.full_disk_read

        grants: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.grants, Unset):
            grants = []
            for grants_item_data in self.grants:
                grants_item = grants_item_data.to_dict()
                grants.append(grants_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "mode": mode,
            }
        )
        if full_disk_read is not UNSET:
            field_dict["full_disk_read"] = full_disk_read
        if grants is not UNSET:
            field_dict["grants"] = grants

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sandbox_grant import SandboxGrant

        d = dict(src_dict)
        mode = cast(Literal["restricted"], d.pop("mode"))
        if mode != "restricted":
            raise ValueError(f"mode must match const 'restricted', got '{mode}'")

        full_disk_read = d.pop("full_disk_read", UNSET)

        _grants = d.pop("grants", UNSET)
        grants: list[SandboxGrant] | Unset = UNSET
        if _grants is not UNSET:
            grants = []
            for grants_item_data in _grants:
                grants_item = SandboxGrant.from_dict(grants_item_data)

                grants.append(grants_item)

        restricted_sandbox = cls(
            mode=mode,
            full_disk_read=full_disk_read,
            grants=grants,
        )

        return restricted_sandbox
