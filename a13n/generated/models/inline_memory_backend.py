from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.inline_memory_backend_configuration import InlineMemoryBackendConfiguration


T = TypeVar("T", bound="InlineMemoryBackend")


@_attrs_define(repr=False)
class InlineMemoryBackend:
    """
    Attributes:
        type_ (Literal['a13n.filesystem']):
        configuration (InlineMemoryBackendConfiguration | Unset):
    """

    type_: Literal["a13n.filesystem"]
    configuration: InlineMemoryBackendConfiguration | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        configuration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configuration, Unset):
            configuration = self.configuration.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "type": type_,
            }
        )
        if configuration is not UNSET:
            field_dict["configuration"] = configuration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inline_memory_backend_configuration import InlineMemoryBackendConfiguration

        d = dict(src_dict)
        type_ = cast(Literal["a13n.filesystem"], d.pop("type"))
        if type_ != "a13n.filesystem":
            raise ValueError(f"type must match const 'a13n.filesystem', got '{type_}'")

        _configuration = d.pop("configuration", UNSET)
        configuration: InlineMemoryBackendConfiguration | Unset
        if isinstance(_configuration, Unset):
            configuration = UNSET
        else:
            configuration = InlineMemoryBackendConfiguration.from_dict(_configuration)

        inline_memory_backend = cls(
            type_=type_,
            configuration=configuration,
        )

        return inline_memory_backend
