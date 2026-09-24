from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.tool_info_annotations import ToolInfoAnnotations
    from ..models.tool_info_input_schema import ToolInfoInputSchema
    from ..models.tool_info_output_schema_type_0 import ToolInfoOutputSchemaType0


T = TypeVar("T", bound="ToolInfo")


@_attrs_define(repr=False)
class ToolInfo:
    """
    Attributes:
        description (None | str):
        input_schema (ToolInfoInputSchema):
        name (str):
        annotations (ToolInfoAnnotations | Unset):
        output_schema (None | ToolInfoOutputSchemaType0 | Unset):
        provider_version (None | str | Unset):
    """

    description: str | None
    input_schema: ToolInfoInputSchema
    name: str
    annotations: ToolInfoAnnotations | Unset = UNSET
    output_schema: ToolInfoOutputSchemaType0 | Unset | None = UNSET
    provider_version: str | Unset | None = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.tool_info_output_schema_type_0 import ToolInfoOutputSchemaType0

        description: str | None
        description = self.description

        input_schema = self.input_schema.to_dict()

        name = self.name

        annotations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = self.annotations.to_dict()

        output_schema: dict[str, Any] | Unset | None
        if isinstance(self.output_schema, Unset):
            output_schema = UNSET
        elif isinstance(self.output_schema, ToolInfoOutputSchemaType0):
            output_schema = self.output_schema.to_dict()
        else:
            output_schema = self.output_schema

        provider_version: str | Unset | None
        if isinstance(self.provider_version, Unset):
            provider_version = UNSET
        else:
            provider_version = self.provider_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "input_schema": input_schema,
                "name": name,
            }
        )
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if output_schema is not UNSET:
            field_dict["output_schema"] = output_schema
        if provider_version is not UNSET:
            field_dict["provider_version"] = provider_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tool_info_annotations import ToolInfoAnnotations
        from ..models.tool_info_input_schema import ToolInfoInputSchema
        from ..models.tool_info_output_schema_type_0 import ToolInfoOutputSchemaType0

        d = dict(src_dict)

        def _parse_description(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        description = _parse_description(d.pop("description"))

        input_schema = ToolInfoInputSchema.from_dict(d.pop("input_schema"))

        name = d.pop("name")

        _annotations = d.pop("annotations", UNSET)
        annotations: ToolInfoAnnotations | Unset
        if isinstance(_annotations, Unset):
            annotations = UNSET
        else:
            annotations = ToolInfoAnnotations.from_dict(_annotations)

        def _parse_output_schema(data: object) -> ToolInfoOutputSchemaType0 | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                output_schema_type_0 = ToolInfoOutputSchemaType0.from_dict(data)

                return output_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ToolInfoOutputSchemaType0 | Unset | None, data)

        output_schema = _parse_output_schema(d.pop("output_schema", UNSET))

        def _parse_provider_version(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        provider_version = _parse_provider_version(d.pop("provider_version", UNSET))

        tool_info = cls(
            description=description,
            input_schema=input_schema,
            name=name,
            annotations=annotations,
            output_schema=output_schema,
            provider_version=provider_version,
        )

        tool_info.additional_properties = d
        return tool_info

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
