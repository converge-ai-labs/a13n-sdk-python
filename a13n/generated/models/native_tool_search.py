from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.automatic_tool_search import AutomaticToolSearch


T = TypeVar("T", bound="NativeToolSearch")


@_attrs_define(repr=False)
class NativeToolSearch:
    """Ungrouped native discovery of selected Service tools; plugins keep their own settings.

    Attributes:
        mode (Literal['native']):
        sources (AutomaticToolSearch | Unset): Select Service-owned sources for on-demand discovery.
    """

    mode: Literal["native"]
    sources: AutomaticToolSearch | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode

        sources: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sources, Unset):
            sources = self.sources.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "mode": mode,
            }
        )
        if sources is not UNSET:
            field_dict["sources"] = sources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.automatic_tool_search import AutomaticToolSearch

        d = dict(src_dict)
        mode = cast(Literal["native"], d.pop("mode"))
        if mode != "native":
            raise ValueError(f"mode must match const 'native', got '{mode}'")

        _sources = d.pop("sources", UNSET)
        sources: AutomaticToolSearch | Unset
        if isinstance(_sources, Unset):
            sources = UNSET
        else:
            sources = AutomaticToolSearch.from_dict(_sources)

        native_tool_search = cls(
            mode=mode,
            sources=sources,
        )

        return native_tool_search
