from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SharedSkillSync")


@_attrs_define(repr=False)
class SharedSkillSync:
    """Publish mutable conventional names; the last completed publication wins.

    Attributes:
        cleanup (bool | Unset):
        mode (Literal['shared'] | Unset):
        overwrite (bool | Unset):
    """

    cleanup: bool | Unset = UNSET
    mode: Literal["shared"] | Unset = UNSET
    overwrite: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        cleanup = self.cleanup

        mode = self.mode

        overwrite = self.overwrite

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if cleanup is not UNSET:
            field_dict["cleanup"] = cleanup
        if mode is not UNSET:
            field_dict["mode"] = mode
        if overwrite is not UNSET:
            field_dict["overwrite"] = overwrite

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cleanup = d.pop("cleanup", UNSET)

        mode = cast(Literal["shared"] | Unset, d.pop("mode", UNSET))
        if mode != "shared" and not isinstance(mode, Unset):
            raise ValueError(f"mode must match const 'shared', got '{mode}'")

        overwrite = d.pop("overwrite", UNSET)

        shared_skill_sync = cls(
            cleanup=cleanup,
            mode=mode,
            overwrite=overwrite,
        )

        return shared_skill_sync
