from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_type_config_schema import EventTypeConfigSchema
    from ..models.event_type_payload_schema_type_0 import EventTypePayloadSchemaType0


T = TypeVar("T", bound="EventType")


@_attrs_define(repr=False)
class EventType:
    """
    Attributes:
        app (str):
        config_schema (EventTypeConfigSchema):
        key (str):
        name (str):
        description (str | Unset):
        instructions (str | Unset):
        payload_schema (EventTypePayloadSchemaType0 | None | Unset):
        requires_provider_setup (bool | Unset):
        version (None | str | Unset):
    """

    app: str
    config_schema: EventTypeConfigSchema
    key: str
    name: str
    description: str | Unset = UNSET
    instructions: str | Unset = UNSET
    payload_schema: EventTypePayloadSchemaType0 | Unset | None = UNSET
    requires_provider_setup: bool | Unset = UNSET
    version: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.event_type_payload_schema_type_0 import EventTypePayloadSchemaType0

        app = self.app

        config_schema = self.config_schema.to_dict()

        key = self.key

        name = self.name

        description = self.description

        instructions = self.instructions

        payload_schema: dict[str, Any] | Unset | None
        if isinstance(self.payload_schema, Unset):
            payload_schema = UNSET
        elif isinstance(self.payload_schema, EventTypePayloadSchemaType0):
            payload_schema = self.payload_schema.to_dict()
        else:
            payload_schema = self.payload_schema

        requires_provider_setup = self.requires_provider_setup

        version: str | Unset | None
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "app": app,
                "config_schema": config_schema,
                "key": key,
                "name": name,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if payload_schema is not UNSET:
            field_dict["payload_schema"] = payload_schema
        if requires_provider_setup is not UNSET:
            field_dict["requires_provider_setup"] = requires_provider_setup
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_type_config_schema import EventTypeConfigSchema
        from ..models.event_type_payload_schema_type_0 import EventTypePayloadSchemaType0

        d = dict(src_dict)
        app = d.pop("app")

        config_schema = EventTypeConfigSchema.from_dict(d.pop("config_schema"))

        key = d.pop("key")

        name = d.pop("name")

        description = d.pop("description", UNSET)

        instructions = d.pop("instructions", UNSET)

        def _parse_payload_schema(data: object) -> EventTypePayloadSchemaType0 | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payload_schema_type_0 = EventTypePayloadSchemaType0.from_dict(data)

                return payload_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EventTypePayloadSchemaType0 | Unset | None, data)

        payload_schema = _parse_payload_schema(d.pop("payload_schema", UNSET))

        requires_provider_setup = d.pop("requires_provider_setup", UNSET)

        def _parse_version(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        version = _parse_version(d.pop("version", UNSET))

        event_type = cls(
            app=app,
            config_schema=config_schema,
            key=key,
            name=name,
            description=description,
            instructions=instructions,
            payload_schema=payload_schema,
            requires_provider_setup=requires_provider_setup,
            version=version,
        )

        return event_type
