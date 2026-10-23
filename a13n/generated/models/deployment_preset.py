from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.configuration import Configuration


T = TypeVar("T", bound="DeploymentPreset")


@_attrs_define(repr=False)
class DeploymentPreset:
    """
    Attributes:
        config (Configuration):
        has_query_credentials (bool):
        name (str):
        revision (str):
    """

    config: Configuration
    has_query_credentials: bool
    name: str
    revision: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        config = self.config.to_dict()

        has_query_credentials = self.has_query_credentials

        name = self.name

        revision = self.revision

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "config": config,
                "has_query_credentials": has_query_credentials,
                "name": name,
                "revision": revision,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.configuration import Configuration

        d = dict(src_dict)
        config = Configuration.from_dict(d.pop("config"))

        has_query_credentials = d.pop("has_query_credentials")

        name = d.pop("name")

        revision = d.pop("revision")

        deployment_preset = cls(
            config=config,
            has_query_credentials=has_query_credentials,
            name=name,
            revision=revision,
        )

        deployment_preset.additional_properties = d
        return deployment_preset

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
