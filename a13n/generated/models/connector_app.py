from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.connector_app_setup_schema import ConnectorAppSetupSchema


T = TypeVar("T", bound="ConnectorApp")


@_attrs_define(repr=False)
class ConnectorApp:
    """
    Attributes:
        authentication_methods (list[str]):
        description (None | str):
        key (str):
        logo_url (None | str):
        name (str):
        setup_schema (ConnectorAppSetupSchema):
        unavailable_reason (None | str):
    """

    authentication_methods: list[str]
    description: str | None
    key: str
    logo_url: str | None
    name: str
    setup_schema: ConnectorAppSetupSchema
    unavailable_reason: str | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authentication_methods = self.authentication_methods

        description: str | None
        description = self.description

        key = self.key

        logo_url: str | None
        logo_url = self.logo_url

        name = self.name

        setup_schema = self.setup_schema.to_dict()

        unavailable_reason: str | None
        unavailable_reason = self.unavailable_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authentication_methods": authentication_methods,
                "description": description,
                "key": key,
                "logo_url": logo_url,
                "name": name,
                "setup_schema": setup_schema,
                "unavailable_reason": unavailable_reason,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connector_app_setup_schema import ConnectorAppSetupSchema

        d = dict(src_dict)
        authentication_methods = cast(list[str], d.pop("authentication_methods"))

        def _parse_description(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        description = _parse_description(d.pop("description"))

        key = d.pop("key")

        def _parse_logo_url(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        logo_url = _parse_logo_url(d.pop("logo_url"))

        name = d.pop("name")

        setup_schema = ConnectorAppSetupSchema.from_dict(d.pop("setup_schema"))

        def _parse_unavailable_reason(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        unavailable_reason = _parse_unavailable_reason(d.pop("unavailable_reason"))

        connector_app = cls(
            authentication_methods=authentication_methods,
            description=description,
            key=key,
            logo_url=logo_url,
            name=name,
            setup_schema=setup_schema,
            unavailable_reason=unavailable_reason,
        )

        connector_app.additional_properties = d
        return connector_app

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
