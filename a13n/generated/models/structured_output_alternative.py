from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.structured_output_alternative_resources import StructuredOutputAlternativeResources
    from ..models.structured_output_alternative_schema import StructuredOutputAlternativeSchema


T = TypeVar("T", bound="StructuredOutputAlternative")


@_attrs_define(repr=False)
class StructuredOutputAlternative:
    """
    Attributes:
        kind (Literal['structured']):
        name (str):
        schema (StructuredOutputAlternativeSchema):
        description (None | str | Unset):
        resources (StructuredOutputAlternativeResources | Unset):
    """

    kind: Literal["structured"]
    name: str
    schema: StructuredOutputAlternativeSchema
    description: str | Unset | None = UNSET
    resources: StructuredOutputAlternativeResources | Unset = UNSET

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
        from ..models.structured_output_alternative_resources import (
            StructuredOutputAlternativeResources,
        )
        from ..models.structured_output_alternative_schema import StructuredOutputAlternativeSchema

        d = dict(src_dict)
        kind = cast(Literal["structured"], d.pop("kind"))
        if kind != "structured":
            raise ValueError(f"kind must match const 'structured', got '{kind}'")

        name = d.pop("name")

        schema = StructuredOutputAlternativeSchema.from_dict(d.pop("schema"))

        def _parse_description(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        description = _parse_description(d.pop("description", UNSET))

        _resources = d.pop("resources", UNSET)
        resources: StructuredOutputAlternativeResources | Unset
        if isinstance(_resources, Unset):
            resources = UNSET
        else:
            resources = StructuredOutputAlternativeResources.from_dict(_resources)

        structured_output_alternative = cls(
            kind=kind,
            name=name,
            schema=schema,
            description=description,
            resources=resources,
        )

        return structured_output_alternative
