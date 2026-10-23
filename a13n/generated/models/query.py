from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_scope_labels import QueryScopeLabels


T = TypeVar("T", bound="Query")


@_attrs_define(repr=False)
class Query:
    """
    Attributes:
        endpoint (str):
        scope_labels (QueryScopeLabels | Unset):
    """

    endpoint: str
    scope_labels: QueryScopeLabels | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        endpoint = self.endpoint

        scope_labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scope_labels, Unset):
            scope_labels = self.scope_labels.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "endpoint": endpoint,
            }
        )
        if scope_labels is not UNSET:
            field_dict["scope_labels"] = scope_labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_scope_labels import QueryScopeLabels

        d = dict(src_dict)
        endpoint = d.pop("endpoint")

        _scope_labels = d.pop("scope_labels", UNSET)
        scope_labels: QueryScopeLabels | Unset
        if isinstance(_scope_labels, Unset):
            scope_labels = UNSET
        else:
            scope_labels = QueryScopeLabels.from_dict(_scope_labels)

        query = cls(
            endpoint=endpoint,
            scope_labels=scope_labels,
        )

        return query
