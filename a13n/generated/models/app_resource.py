from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.app_resource_metadata import AppResourceMetadata


T = TypeVar("T", bound="AppResource")


@_attrs_define(repr=False)
class AppResource:
    """
    Attributes:
        html (str):
        metadata (AppResourceMetadata):
        mime_type (str):
        uri (str):
    """

    html: str
    metadata: AppResourceMetadata
    mime_type: str
    uri: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        html = self.html

        metadata = self.metadata.to_dict()

        mime_type = self.mime_type

        uri = self.uri

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "html": html,
                "metadata": metadata,
                "mime_type": mime_type,
                "uri": uri,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_resource_metadata import AppResourceMetadata

        d = dict(src_dict)
        html = d.pop("html")

        metadata = AppResourceMetadata.from_dict(d.pop("metadata"))

        mime_type = d.pop("mime_type")

        uri = d.pop("uri")

        app_resource = cls(
            html=html,
            metadata=metadata,
            mime_type=mime_type,
            uri=uri,
        )

        app_resource.additional_properties = d
        return app_resource

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
