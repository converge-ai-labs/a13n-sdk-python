from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_output_alternative import ClientOutputAlternative
    from ..models.output_spec_resources import OutputSpecResources
    from ..models.output_spec_schema_type_0 import OutputSpecSchemaType0
    from ..models.output_variant import OutputVariant
    from ..models.structured_output_alternative import StructuredOutputAlternative


T = TypeVar("T", bound="OutputSpec")


@_attrs_define(repr=False)
class OutputSpec:
    """Plain text without a schema, one structured output, or at least two named variants.

    `resources` are the schemas `$ref`s may name besides the schema's own definitions.

        Attributes:
            alternatives (list[ClientOutputAlternative | str | StructuredOutputAlternative] | None | Unset):
            description (None | str | Unset):
            name (None | str | Unset):
            resources (OutputSpecResources | Unset):
            schema (None | OutputSpecSchemaType0 | Unset):
            variants (list[OutputVariant] | None | Unset):
    """

    alternatives: list[ClientOutputAlternative | str | StructuredOutputAlternative] | Unset | None = UNSET
    description: str | Unset | None = UNSET
    name: str | Unset | None = UNSET
    resources: OutputSpecResources | Unset = UNSET
    schema: OutputSpecSchemaType0 | Unset | None = UNSET
    variants: list[OutputVariant] | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.client_output_alternative import ClientOutputAlternative
        from ..models.output_spec_schema_type_0 import OutputSpecSchemaType0
        from ..models.structured_output_alternative import StructuredOutputAlternative

        alternatives: list[dict[str, Any] | str] | Unset | None
        if isinstance(self.alternatives, Unset):
            alternatives = UNSET
        elif isinstance(self.alternatives, list):
            alternatives = []
            for alternatives_type_0_item_data in self.alternatives:
                alternatives_type_0_item: dict[str, Any] | str
                if isinstance(alternatives_type_0_item_data, StructuredOutputAlternative):
                    alternatives_type_0_item = alternatives_type_0_item_data.to_dict()
                elif isinstance(alternatives_type_0_item_data, ClientOutputAlternative):
                    alternatives_type_0_item = alternatives_type_0_item_data.to_dict()
                else:
                    alternatives_type_0_item = alternatives_type_0_item_data
                alternatives.append(alternatives_type_0_item)

        else:
            alternatives = self.alternatives

        description: str | Unset | None
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        name: str | Unset | None
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        resources: dict[str, Any] | Unset = UNSET
        if not isinstance(self.resources, Unset):
            resources = self.resources.to_dict()

        schema: dict[str, Any] | Unset | None
        if isinstance(self.schema, Unset):
            schema = UNSET
        elif isinstance(self.schema, OutputSpecSchemaType0):
            schema = self.schema.to_dict()
        else:
            schema = self.schema

        variants: list[dict[str, Any]] | Unset | None
        if isinstance(self.variants, Unset):
            variants = UNSET
        elif isinstance(self.variants, list):
            variants = []
            for variants_type_0_item_data in self.variants:
                variants_type_0_item = variants_type_0_item_data.to_dict()
                variants.append(variants_type_0_item)

        else:
            variants = self.variants

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if alternatives is not UNSET:
            field_dict["alternatives"] = alternatives
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if resources is not UNSET:
            field_dict["resources"] = resources
        if schema is not UNSET:
            field_dict["schema"] = schema
        if variants is not UNSET:
            field_dict["variants"] = variants

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.client_output_alternative import ClientOutputAlternative
        from ..models.output_spec_resources import OutputSpecResources
        from ..models.output_spec_schema_type_0 import OutputSpecSchemaType0
        from ..models.output_variant import OutputVariant
        from ..models.structured_output_alternative import StructuredOutputAlternative

        d = dict(src_dict)

        def _parse_alternatives(
            data: object,
        ) -> list[ClientOutputAlternative | str | StructuredOutputAlternative] | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                alternatives_type_0 = []
                _alternatives_type_0 = data
                for alternatives_type_0_item_data in _alternatives_type_0:

                    def _parse_alternatives_type_0_item(
                        data: object,
                    ) -> ClientOutputAlternative | str | StructuredOutputAlternative:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_output_definition_type_0 = StructuredOutputAlternative.from_dict(data)

                            return componentsschemas_output_definition_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_output_definition_type_1 = ClientOutputAlternative.from_dict(data)

                            return componentsschemas_output_definition_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(ClientOutputAlternative | str | StructuredOutputAlternative, data)

                    alternatives_type_0_item = _parse_alternatives_type_0_item(alternatives_type_0_item_data)

                    alternatives_type_0.append(alternatives_type_0_item)

                return alternatives_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ClientOutputAlternative | str | StructuredOutputAlternative] | Unset | None, data)

        alternatives = _parse_alternatives(d.pop("alternatives", UNSET))

        def _parse_description(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_name(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        name = _parse_name(d.pop("name", UNSET))

        _resources = d.pop("resources", UNSET)
        resources: OutputSpecResources | Unset
        if isinstance(_resources, Unset):
            resources = UNSET
        else:
            resources = OutputSpecResources.from_dict(_resources)

        def _parse_schema(data: object) -> OutputSpecSchemaType0 | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                schema_type_0 = OutputSpecSchemaType0.from_dict(data)

                return schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(OutputSpecSchemaType0 | Unset | None, data)

        schema = _parse_schema(d.pop("schema", UNSET))

        def _parse_variants(data: object) -> list[OutputVariant] | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                variants_type_0 = []
                _variants_type_0 = data
                for variants_type_0_item_data in _variants_type_0:
                    variants_type_0_item = OutputVariant.from_dict(variants_type_0_item_data)

                    variants_type_0.append(variants_type_0_item)

                return variants_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[OutputVariant] | Unset | None, data)

        variants = _parse_variants(d.pop("variants", UNSET))

        output_spec = cls(
            alternatives=alternatives,
            description=description,
            name=name,
            resources=resources,
            schema=schema,
            variants=variants,
        )

        return output_spec
