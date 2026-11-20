from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_output_alternative_resources import ClientOutputAlternativeResources
    from ..models.client_output_alternative_schema import ClientOutputAlternativeSchema


T = TypeVar("T", bound="ClientOutputAlternative")


@_attrs_define(repr=False)
class ClientOutputAlternative:
    """
    Attributes:
        kind (Literal['client_tool']):
        name (str):
        schema (ClientOutputAlternativeSchema):
        description (None | str | Unset):
        resources (ClientOutputAlternativeResources | Unset):
    """

    kind: Literal["client_tool"]
    name: str
    schema: ClientOutputAlternativeSchema
    description: str | Unset | None = UNSET
    resources: ClientOutputAlternativeResources | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        kind = self.kind

        name = self.name

        schema = self.schema.to_dict()

        description: str | Unset | None
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        resources: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resources, Unset):
            resources = self.resources.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kind": kind,
                "name": name,
                "schema": schema,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if resources is not UNSET:
            field_dict["resources"] = resources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.client_output_alternative_resources import ClientOutputAlternativeResources
        from ..models.client_output_alternative_schema import ClientOutputAlternativeSchema

        d = dict(src_dict)
        kind = cast(Literal["client_tool"], d.pop("kind"))
        if kind != "client_tool":
            raise ValueError(f"kind must match const 'client_tool', got '{kind}'")

        name = d.pop("name")

        schema = ClientOutputAlternativeSchema.from_dict(d.pop("schema"))

        def _parse_description(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        description = _parse_description(d.pop("description", UNSET))

        _resources = d.pop("resources", UNSET)
        resources: ClientOutputAlternativeResources | Unset
        if isinstance(_resources, Unset):
            resources = UNSET
        else:
            resources = ClientOutputAlternativeResources.from_dict(_resources)

        client_output_alternative = cls(
            kind=kind,
            name=name,
            schema=schema,
            description=description,
            resources=resources,
        )

        return client_output_alternative
