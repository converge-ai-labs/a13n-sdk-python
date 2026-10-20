from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.preview import Preview


T = TypeVar("T", bound="ContentSummary")


@_attrs_define(repr=False)
class ContentSummary:
    """
    Attributes:
        id (str):
        media_type (str):
        size_chars (int):
        source_truncated (bool):
        value (Preview):
        omitted_sections (list[str] | Unset):
        view (Literal['compact'] | Unset):
    """

    id: str
    media_type: str
    size_chars: int
    source_truncated: bool
    value: Preview
    omitted_sections: list[str] | Unset = UNSET
    view: Literal["compact"] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        media_type = self.media_type

        size_chars = self.size_chars

        source_truncated = self.source_truncated

        value = self.value.to_dict()

        omitted_sections: list[str] | Unset = UNSET
        if not isinstance(self.omitted_sections, Unset):
            omitted_sections = self.omitted_sections

        view = self.view

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "media_type": media_type,
                "size_chars": size_chars,
                "source_truncated": source_truncated,
                "value": value,
            }
        )
        if omitted_sections is not UNSET:
            field_dict["omitted_sections"] = omitted_sections
        if view is not UNSET:
            field_dict["view"] = view

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.preview import Preview

        d = dict(src_dict)
        id = d.pop("id")

        media_type = d.pop("media_type")

        size_chars = d.pop("size_chars")

        source_truncated = d.pop("source_truncated")

        value = Preview.from_dict(d.pop("value"))

        omitted_sections = cast(list[str], d.pop("omitted_sections", UNSET))

        view = cast(Literal["compact"] | Unset, d.pop("view", UNSET))
        if view != "compact" and not isinstance(view, Unset):
            raise ValueError(f"view must match const 'compact', got '{view}'")

        content_summary = cls(
            id=id,
            media_type=media_type,
            size_chars=size_chars,
            source_truncated=source_truncated,
            value=value,
            omitted_sections=omitted_sections,
            view=view,
        )

        content_summary.additional_properties = d
        return content_summary

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
