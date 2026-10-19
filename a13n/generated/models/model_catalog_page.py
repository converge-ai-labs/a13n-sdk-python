from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_catalog_page_status import ModelCatalogPageStatus

if TYPE_CHECKING:
    from ..models.catalog_model import CatalogModel
    from ..models.model_summary import ModelSummary


T = TypeVar("T", bound="ModelCatalogPage")


@_attrs_define(repr=False)
class ModelCatalogPage:
    """
    Attributes:
        items (list[CatalogModel | ModelSummary]):
        next_cursor (None | str):
        status (ModelCatalogPageStatus):
    """

    items: list[CatalogModel | ModelSummary]
    next_cursor: str | None
    status: ModelCatalogPageStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.model_summary import ModelSummary

        items = []
        for items_item_data in self.items:
            items_item: dict[str, Any]
            if isinstance(items_item_data, ModelSummary):
                items_item = items_item_data.to_dict()
            else:
                items_item = items_item_data.to_dict()

            items.append(items_item)

        next_cursor: str | None
        next_cursor = self.next_cursor

        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
                "next_cursor": next_cursor,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_model import CatalogModel
        from ..models.model_summary import ModelSummary

        d = dict(src_dict)
        items = []
        _items = d.pop("items")
        for items_item_data in _items:

            def _parse_items_item(data: object) -> CatalogModel | ModelSummary:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    items_item_type_0 = ModelSummary.from_dict(data)

                    return items_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                items_item_type_1 = CatalogModel.from_dict(data)

                return items_item_type_1

            items_item = _parse_items_item(items_item_data)

            items.append(items_item)

        def _parse_next_cursor(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        next_cursor = _parse_next_cursor(d.pop("next_cursor"))

        status = ModelCatalogPageStatus(d.pop("status"))

        model_catalog_page = cls(
            items=items,
            next_cursor=next_cursor,
            status=status,
        )

        model_catalog_page.additional_properties = d
        return model_catalog_page

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
