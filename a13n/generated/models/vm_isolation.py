from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..models.vm_backend import VmBackend
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.vm_mount import VmMount


T = TypeVar("T", bound="VmIsolation")


@_attrs_define(repr=False)
class VmIsolation:
    """
    Attributes:
        backend (VmBackend):
        cpus (int):
        image (str):
        memory_mib (int):
        mode (Literal['vm']):
        mounts (list[VmMount] | Unset):
    """

    backend: VmBackend
    cpus: int
    image: str
    memory_mib: int
    mode: Literal["vm"]
    mounts: list[VmMount] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        backend = self.backend.value

        cpus = self.cpus

        image = self.image

        memory_mib = self.memory_mib

        mode = self.mode

        mounts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.mounts, Unset):
            mounts = []
            for mounts_item_data in self.mounts:
                mounts_item = mounts_item_data.to_dict()
                mounts.append(mounts_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "backend": backend,
                "cpus": cpus,
                "image": image,
                "memory_mib": memory_mib,
                "mode": mode,
            }
        )
        if mounts is not UNSET:
            field_dict["mounts"] = mounts

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.vm_mount import VmMount

        d = dict(src_dict)
        backend = VmBackend(d.pop("backend"))

        cpus = d.pop("cpus")

        image = d.pop("image")

        memory_mib = d.pop("memory_mib")

        mode = cast(Literal["vm"], d.pop("mode"))
        if mode != "vm":
            raise ValueError(f"mode must match const 'vm', got '{mode}'")

        _mounts = d.pop("mounts", UNSET)
        mounts: list[VmMount] | Unset = UNSET
        if _mounts is not UNSET:
            mounts = []
            for mounts_item_data in _mounts:
                mounts_item = VmMount.from_dict(mounts_item_data)

                mounts.append(mounts_item)

        vm_isolation = cls(
            backend=backend,
            cpus=cpus,
            image=image,
            memory_mib=memory_mib,
            mode=mode,
            mounts=mounts,
        )

        return vm_isolation
