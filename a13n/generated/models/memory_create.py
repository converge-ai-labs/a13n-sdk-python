from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.memory_create_labels import MemoryCreateLabels


T = TypeVar("T", bound="MemoryCreate")


@_attrs_define(repr=False)
class MemoryCreate:
    """`postgres` makes a file memory the Service stores; a Memory Provider's type makes a record memory in that
    provider's backend, under a new namespace or the existing one `namespace` adopts.

        Attributes:
            key (str):
            name (str):
            always_load (list[str] | Unset):
            description (None | str | Unset):
            guide (None | str | Unset):
            labels (MemoryCreateLabels | Unset):
            namespace (None | str | Unset):
            provider_id (None | str | Unset):
            type_ (str | Unset):
    """

    key: str
    name: str
    always_load: list[str] | Unset = UNSET
    description: str | Unset | None = UNSET
    guide: str | Unset | None = UNSET
    labels: MemoryCreateLabels | Unset = UNSET
    namespace: str | Unset | None = UNSET
    provider_id: str | Unset | None = UNSET
    type_: str | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        name = self.name

        always_load: list[str] | Unset = UNSET
        if not isinstance(self.always_load, Unset):
            always_load = self.always_load

        description: str | Unset | None
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        guide: str | Unset | None
        if isinstance(self.guide, Unset):
            guide = UNSET
        else:
            guide = self.guide

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        namespace: str | Unset | None
        if isinstance(self.namespace, Unset):
            namespace = UNSET
        else:
            namespace = self.namespace

        provider_id: str | Unset | None
        if isinstance(self.provider_id, Unset):
            provider_id = UNSET
        else:
            provider_id = self.provider_id

        type_ = self.type_

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "name": name,
            }
        )
        if always_load is not UNSET:
            field_dict["always_load"] = always_load
        if description is not UNSET:
            field_dict["description"] = description
        if guide is not UNSET:
            field_dict["guide"] = guide
        if labels is not UNSET:
            field_dict["labels"] = labels
        if namespace is not UNSET:
            field_dict["namespace"] = namespace
        if provider_id is not UNSET:
            field_dict["provider_id"] = provider_id
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.memory_create_labels import MemoryCreateLabels

        d = dict(src_dict)
        key = d.pop("key")

        name = d.pop("name")

        always_load = cast(list[str], d.pop("always_load", UNSET))

        def _parse_description(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_guide(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        guide = _parse_guide(d.pop("guide", UNSET))

        _labels = d.pop("labels", UNSET)
        labels: MemoryCreateLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = MemoryCreateLabels.from_dict(_labels)

        def _parse_namespace(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        namespace = _parse_namespace(d.pop("namespace", UNSET))

        def _parse_provider_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        provider_id = _parse_provider_id(d.pop("provider_id", UNSET))

        type_ = d.pop("type", UNSET)

        memory_create = cls(
            key=key,
            name=name,
            always_load=always_load,
            description=description,
            guide=guide,
            labels=labels,
            namespace=namespace,
            provider_id=provider_id,
            type_=type_,
        )

        return memory_create
