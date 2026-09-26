from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="MemoryRecordSearch")


@_attrs_define(repr=False)
class MemoryRecordSearch:
    """
    Attributes:
        query (str):
        limit (int | Unset):
    """

    query: str
    limit: int | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        limit = self.limit

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "query": query,
            }
        )
        if limit is not UNSET:
            field_dict["limit"] = limit

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query = d.pop("query")

        limit = d.pop("limit", UNSET)

        memory_record_search = cls(
            query=query,
            limit=limit,
        )

        return memory_record_search
