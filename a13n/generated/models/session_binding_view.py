from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.session_configuration import SessionConfiguration


T = TypeVar("T", bound="SessionBindingView")


@_attrs_define(repr=False)
class SessionBindingView:
    """
    Attributes:
        configuration (SessionConfiguration): Tenant-authored Session policy; Service credentials are not process-
            environment references.
        environment_id (str):
        name (str):
        version (int):
    """

    configuration: SessionConfiguration
    environment_id: str
    name: str
    version: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configuration = self.configuration.to_dict()

        environment_id = self.environment_id

        name = self.name

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "configuration": configuration,
                "environment_id": environment_id,
                "name": name,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_configuration import SessionConfiguration

        d = dict(src_dict)
        configuration = SessionConfiguration.from_dict(d.pop("configuration"))

        environment_id = d.pop("environment_id")

        name = d.pop("name")

        version = d.pop("version")

        session_binding_view = cls(
            configuration=configuration,
            environment_id=environment_id,
            name=name,
            version=version,
        )

        session_binding_view.additional_properties = d
        return session_binding_view

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
