from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_ref import CatalogRef


T = TypeVar("T", bound="ModelSummary")


@_attrs_define(repr=False)
class ModelSummary:
    """
    Attributes:
        capabilities (list[str]):
        context_window_tokens (int | None):
        name (str):
        pricing_available (bool):
        ref (CatalogRef): A models.dev channel and the model ID it lists there.
        omitted_sections (list[str] | Unset):
        view (Literal['compact'] | Unset):
    """

    capabilities: list[str]
    context_window_tokens: int | None
    name: str
    pricing_available: bool
    ref: CatalogRef
    omitted_sections: list[str] | Unset = UNSET
    view: Literal["compact"] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        capabilities = self.capabilities

        context_window_tokens: int | None
        context_window_tokens = self.context_window_tokens

        name = self.name

        pricing_available = self.pricing_available

        ref = self.ref.to_dict()

        omitted_sections: list[str] | Unset = UNSET
        if not isinstance(self.omitted_sections, Unset):
            omitted_sections = self.omitted_sections

        view = self.view

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "capabilities": capabilities,
                "context_window_tokens": context_window_tokens,
                "name": name,
                "pricing_available": pricing_available,
                "ref": ref,
            }
        )
        if omitted_sections is not UNSET:
            field_dict["omitted_sections"] = omitted_sections
        if view is not UNSET:
            field_dict["view"] = view

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_ref import CatalogRef

        d = dict(src_dict)
        capabilities = cast(list[str], d.pop("capabilities"))

        def _parse_context_window_tokens(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        context_window_tokens = _parse_context_window_tokens(d.pop("context_window_tokens"))

        name = d.pop("name")

        pricing_available = d.pop("pricing_available")

        ref = CatalogRef.from_dict(d.pop("ref"))

        omitted_sections = cast(list[str], d.pop("omitted_sections", UNSET))

        view = cast(Literal["compact"] | Unset, d.pop("view", UNSET))
        if view != "compact" and not isinstance(view, Unset):
            raise ValueError(f"view must match const 'compact', got '{view}'")

        model_summary = cls(
            capabilities=capabilities,
            context_window_tokens=context_window_tokens,
            name=name,
            pricing_available=pricing_available,
            ref=ref,
            omitted_sections=omitted_sections,
            view=view,
        )

        model_summary.additional_properties = d
        return model_summary

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
