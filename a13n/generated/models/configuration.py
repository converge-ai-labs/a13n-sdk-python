from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.collection import Collection
from ..models.collector import Collector
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.export import Export
    from ..models.query import Query


T = TypeVar("T", bound="Configuration")


@_attrs_define(repr=False)
class Configuration:
    """
    Attributes:
        collection (Collection):
        collector (Collector | None | Unset):
        export (Export | None | Unset):
        query (None | Query | Unset):
    """

    collection: Collection
    collector: Collector | Unset | None = UNSET
    export: Export | Unset | None = UNSET
    query: Query | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.export import Export
        from ..models.query import Query

        collection = self.collection.value

        collector: str | Unset | None
        if isinstance(self.collector, Unset):
            collector = UNSET
        elif isinstance(self.collector, Collector):
            collector = self.collector.value
        else:
            collector = self.collector

        export: dict[str, Any] | Unset | None
        if isinstance(self.export, Unset):
            export = UNSET
        elif isinstance(self.export, Export):
            export = self.export.to_dict()
        else:
            export = self.export

        query: dict[str, Any] | Unset | None
        if isinstance(self.query, Unset):
            query = UNSET
        elif isinstance(self.query, Query):
            query = self.query.to_dict()
        else:
            query = self.query

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "collection": collection,
            }
        )
        if collector is not UNSET:
            field_dict["collector"] = collector
        if export is not UNSET:
            field_dict["export"] = export
        if query is not UNSET:
            field_dict["query"] = query

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.export import Export
        from ..models.query import Query

        d = dict(src_dict)
        collection = Collection(d.pop("collection"))

        def _parse_collector(data: object) -> Collector | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                collector_type_0 = Collector(data)

                return collector_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Collector | Unset | None, data)

        collector = _parse_collector(d.pop("collector", UNSET))

        def _parse_export(data: object) -> Export | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                export_type_0 = Export.from_dict(data)

                return export_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Export | Unset | None, data)

        export = _parse_export(d.pop("export", UNSET))

        def _parse_query(data: object) -> Query | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                query_type_0 = Query.from_dict(data)

                return query_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Query | Unset | None, data)

        query = _parse_query(d.pop("query", UNSET))

        configuration = cls(
            collection=collection,
            collector=collector,
            export=export,
            query=query,
        )

        return configuration
