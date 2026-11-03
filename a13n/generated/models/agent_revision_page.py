from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_revision import AgentRevision
    from ..models.unavailable_configuration import UnavailableConfiguration


T = TypeVar("T", bound="AgentRevisionPage")


@_attrs_define(repr=False)
class AgentRevisionPage:
    """
    Attributes:
        items (list[AgentRevision]):
        next_cursor (None | str):
        unavailable (list[UnavailableConfiguration] | Unset):
    """

    items: list[AgentRevision]
    next_cursor: str | None
    unavailable: list[UnavailableConfiguration] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        next_cursor: str | None
        next_cursor = self.next_cursor

        unavailable: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.unavailable, Unset):
            unavailable = []
            for unavailable_item_data in self.unavailable:
                unavailable_item = unavailable_item_data.to_dict()
                unavailable.append(unavailable_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
                "next_cursor": next_cursor,
            }
        )
        if unavailable is not UNSET:
            field_dict["unavailable"] = unavailable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_revision import AgentRevision
        from ..models.unavailable_configuration import UnavailableConfiguration

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = AgentRevision.from_dict(items_item_data)

            items.append(items_item)

        def _parse_next_cursor(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))

        _unavailable = d.pop("unavailable", UNSET)
        unavailable: list[UnavailableConfiguration] | Unset = UNSET
        if _unavailable is not UNSET:
            unavailable = []
            for unavailable_item_data in _unavailable:
                unavailable_item = UnavailableConfiguration.from_dict(unavailable_item_data)

                unavailable.append(unavailable_item)

        agent_revision_page = cls(
            items=items,
            next_cursor=next_cursor,
            unavailable=unavailable,
        )

        agent_revision_page.additional_properties = d
        return agent_revision_page

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
