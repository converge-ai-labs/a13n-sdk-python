from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.metrics_application_collection import MetricsApplicationCollection
from ..types import UNSET, Unset

T = TypeVar("T", bound="MetricsApplication")


@_attrs_define(repr=False)
class MetricsApplication:
    """The frozen sampler/exporter selection; applied_at confirms creation, not delivery.

    Attributes:
        collection (MetricsApplicationCollection):
        sample_interval_ms (int):
        source_id (str):
        source_version (int):
        applied_at (datetime.datetime | None | Unset):
    """

    collection: MetricsApplicationCollection
    sample_interval_ms: int
    source_id: str
    source_version: int
    applied_at: datetime.datetime | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        collection = self.collection.value

        sample_interval_ms = self.sample_interval_ms

        source_id = self.source_id

        source_version = self.source_version

        applied_at: str | Unset | None
        if isinstance(self.applied_at, Unset):
            applied_at = UNSET
        elif isinstance(self.applied_at, datetime.datetime):
            applied_at = self.applied_at.isoformat()
        else:
            applied_at = self.applied_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "collection": collection,
                "sample_interval_ms": sample_interval_ms,
                "source_id": source_id,
                "source_version": source_version,
            }
        )
        if applied_at is not UNSET:
            field_dict["applied_at"] = applied_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        collection = MetricsApplicationCollection(d.pop("collection"))

        sample_interval_ms = d.pop("sample_interval_ms")

        source_id = d.pop("source_id")

        source_version = d.pop("source_version")

        def _parse_applied_at(data: object) -> datetime.datetime | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                applied_at_type_0 = datetime.datetime.fromisoformat(data)

                return applied_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | Unset | None, data)

        applied_at = _parse_applied_at(d.pop("applied_at", UNSET))

        metrics_application = cls(
            collection=collection,
            sample_interval_ms=sample_interval_ms,
            source_id=source_id,
            source_version=source_version,
            applied_at=applied_at,
        )

        return metrics_application
