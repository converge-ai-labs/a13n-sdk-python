from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.model_catalog_collection_status import ModelCatalogCollectionStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_model import CatalogModel


T = TypeVar("T", bound="ModelCatalogCollection")


@_attrs_define(repr=False)
class ModelCatalogCollection:
    """
    Attributes:
        released_since (datetime.date):
        status (ModelCatalogCollectionStatus):
        items (list[CatalogModel] | Unset):
    """

    released_since: datetime.date
    status: ModelCatalogCollectionStatus
    items: list[CatalogModel] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        released_since = self.released_since.isoformat()

        status = self.status.value

        items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "released_since": released_since,
                "status": status,
            }
        )
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_model import CatalogModel

        d = dict(src_dict)
        released_since = datetime.date.fromisoformat(d.pop("released_since"))

        status = ModelCatalogCollectionStatus(d.pop("status"))

        _items = d.pop("items", UNSET)
        items: list[CatalogModel] | Unset = UNSET
        if _items is not UNSET:
            items = []
            for items_item_data in _items:
                items_item = CatalogModel.from_dict(items_item_data)

                items.append(items_item)

        model_catalog_collection = cls(
            released_since=released_since,
            status=status,
            items=items,
        )

        return model_catalog_collection
