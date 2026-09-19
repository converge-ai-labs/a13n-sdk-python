from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.managed_memory_document_kind import ManagedMemoryDocumentKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="ManagedMemoryDocument")


@_attrs_define(repr=False)
class ManagedMemoryDocument:
    """
    Attributes:
        created_at (datetime.datetime):
        description (str):
        id (str):
        kind (ManagedMemoryDocumentKind):
        path (str):
        saved_at (datetime.datetime):
        text (str):
        title (str):
        version (int):
        applicability (None | str | Unset):
        correction_of (None | str | Unset):
        effective_time (datetime.datetime | None | Unset):
        event_time (datetime.datetime | None | Unset):
        sources (list[str] | Unset):
    """

    created_at: datetime.datetime
    description: str
    id: str
    kind: ManagedMemoryDocumentKind
    path: str
    saved_at: datetime.datetime
    text: str
    title: str
    version: int
    applicability: str | Unset | None = UNSET
    correction_of: str | Unset | None = UNSET
    effective_time: datetime.datetime | Unset | None = UNSET
    event_time: datetime.datetime | Unset | None = UNSET
    sources: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        description = self.description

        id = self.id

        kind = self.kind.value

        path = self.path

        saved_at = self.saved_at.isoformat()

        text = self.text

        title = self.title

        version = self.version

        applicability: str | Unset | None
        if isinstance(self.applicability, Unset):
            applicability = UNSET
        else:
            applicability = self.applicability

        correction_of: str | Unset | None
        if isinstance(self.correction_of, Unset):
            correction_of = UNSET
        else:
            correction_of = self.correction_of

        effective_time: str | Unset | None
        if isinstance(self.effective_time, Unset):
            effective_time = UNSET
        elif isinstance(self.effective_time, datetime.datetime):
            effective_time = self.effective_time.isoformat()
        else:
            effective_time = self.effective_time

        event_time: str | Unset | None
        if isinstance(self.event_time, Unset):
            event_time = UNSET
        elif isinstance(self.event_time, datetime.datetime):
            event_time = self.event_time.isoformat()
        else:
            event_time = self.event_time

        sources: list[str] | Unset = UNSET
        if not isinstance(self.sources, Unset):
            sources = self.sources

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "created_at": created_at,
                "description": description,
                "id": id,
                "kind": kind,
                "path": path,
                "saved_at": saved_at,
                "text": text,
                "title": title,
                "version": version,
            }
        )
        if applicability is not UNSET:
            field_dict["applicability"] = applicability
        if correction_of is not UNSET:
            field_dict["correction_of"] = correction_of
        if effective_time is not UNSET:
            field_dict["effective_time"] = effective_time
        if event_time is not UNSET:
            field_dict["event_time"] = event_time
        if sources is not UNSET:
            field_dict["sources"] = sources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        description = d.pop("description")

        id = d.pop("id")

        kind = ManagedMemoryDocumentKind(d.pop("kind"))

        path = d.pop("path")

        saved_at = datetime.datetime.fromisoformat(d.pop("saved_at"))

        text = d.pop("text")

        title = d.pop("title")

        version = d.pop("version")

        def _parse_applicability(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        applicability = _parse_applicability(d.pop("applicability", UNSET))

        def _parse_correction_of(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        correction_of = _parse_correction_of(d.pop("correction_of", UNSET))

        def _parse_effective_time(data: object) -> datetime.datetime | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                effective_time_type_0 = datetime.datetime.fromisoformat(data)

                return effective_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | Unset | None, data)

        effective_time = _parse_effective_time(d.pop("effective_time", UNSET))

        def _parse_event_time(data: object) -> datetime.datetime | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                event_time_type_0 = datetime.datetime.fromisoformat(data)

                return event_time_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | Unset | None, data)

        event_time = _parse_event_time(d.pop("event_time", UNSET))

        sources = cast(list[str], d.pop("sources", UNSET))

        managed_memory_document = cls(
            created_at=created_at,
            description=description,
            id=id,
            kind=kind,
            path=path,
            saved_at=saved_at,
            text=text,
            title=title,
            version=version,
            applicability=applicability,
            correction_of=correction_of,
            effective_time=effective_time,
            event_time=event_time,
            sources=sources,
        )

        return managed_memory_document
