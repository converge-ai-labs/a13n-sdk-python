from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.json_object import JsonObject


T = TypeVar("T", bound="ConnectorTool")


@_attrs_define(repr=False)
class ConnectorTool:
    """
    Attributes:
        description (str):
        input_schema (JsonObject):
        key (str):
        provider_version (str):
        annotations (JsonObject | Unset):
        output_schema (JsonObject | None | Unset):
    """

    description: str
    input_schema: JsonObject
    key: str
    provider_version: str
    annotations: JsonObject | Unset = UNSET
    output_schema: JsonObject | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.json_object import JsonObject

        description = self.description

        input_schema = self.input_schema.to_dict()

        key = self.key

        provider_version = self.provider_version

        annotations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = self.annotations.to_dict()

        output_schema: dict[str, Any] | Unset | None
        if isinstance(self.output_schema, Unset):
            output_schema = UNSET
        elif isinstance(self.output_schema, JsonObject):
            output_schema = self.output_schema.to_dict()
        else:
            output_schema = self.output_schema

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "description": description,
                "input_schema": input_schema,
                "key": key,
                "provider_version": provider_version,
            }
        )
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if output_schema is not UNSET:
            field_dict["output_schema"] = output_schema

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.json_object import JsonObject

        d = dict(src_dict)
        description = d.pop("description")

        input_schema = JsonObject.from_dict(d.pop("input_schema"))

        key = d.pop("key")

        provider_version = d.pop("provider_version")

        _annotations = d.pop("annotations", UNSET)
        annotations: JsonObject | Unset
        if isinstance(_annotations, Unset):
            annotations = UNSET
        else:
            annotations = JsonObject.from_dict(_annotations)

        def _parse_output_schema(data: object) -> JsonObject | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                output_schema_type_0 = JsonObject.from_dict(data)

                return output_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(JsonObject | Unset | None, data)

        output_schema = _parse_output_schema(d.pop("output_schema", UNSET))

        connector_tool = cls(
            description=description,
            input_schema=input_schema,
            key=key,
            provider_version=provider_version,
            annotations=annotations,
            output_schema=output_schema,
        )

        return connector_tool
