from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.session_view_purpose import SessionViewPurpose
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.session_memory_settings import SessionMemorySettings
    from ..models.session_origin import SessionOrigin
    from ..models.session_preview import SessionPreview
    from ..models.session_view_labels import SessionViewLabels


T = TypeVar("T", bound="SessionView")


@_attrs_define(repr=False)
class SessionView:
    """
    Attributes:
        cost (None | str):
        created_at (datetime.datetime):
        created_by_id (str):
        id (str):
        labels (SessionViewLabels):
        last_run_id (None | str):
        run_count (int):
        unpriced_requests (int):
        updated_at (datetime.datetime):
        version (int):
        workspace_id (str):
        memory (SessionMemorySettings | Unset): Participation and complete Space selection; policy belongs to each
            Space.
        origin (None | SessionOrigin | Unset):
        preview (None | SessionPreview | Unset):
        purpose (SessionViewPurpose | Unset):
        schedule_id (None | str | Unset):
        title (None | str | Unset):
    """

    cost: str | None
    created_at: datetime.datetime
    created_by_id: str
    id: str
    labels: SessionViewLabels
    last_run_id: str | None
    run_count: int
    unpriced_requests: int
    updated_at: datetime.datetime
    version: int
    workspace_id: str
    memory: SessionMemorySettings | Unset = UNSET
    origin: SessionOrigin | Unset | None = UNSET
    preview: SessionPreview | Unset | None = UNSET
    purpose: SessionViewPurpose | Unset = UNSET
    schedule_id: str | Unset | None = UNSET
    title: str | Unset | None = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.session_origin import SessionOrigin
        from ..models.session_preview import SessionPreview

        cost: str | None
        cost = self.cost

        created_at = self.created_at.isoformat()

        created_by_id = self.created_by_id

        id = self.id

        labels = self.labels.to_dict()

        last_run_id: str | None
        last_run_id = self.last_run_id

        run_count = self.run_count

        unpriced_requests = self.unpriced_requests

        updated_at = self.updated_at.isoformat()

        version = self.version

        workspace_id = self.workspace_id

        memory: dict[str, Any] | Unset = UNSET
        if not isinstance(self.memory, Unset):
            memory = self.memory.to_dict()

        origin: dict[str, Any] | Unset | None
        if isinstance(self.origin, Unset):
            origin = UNSET
        elif isinstance(self.origin, SessionOrigin):
            origin = self.origin.to_dict()
        else:
            origin = self.origin

        preview: dict[str, Any] | Unset | None
        if isinstance(self.preview, Unset):
            preview = UNSET
        elif isinstance(self.preview, SessionPreview):
            preview = self.preview.to_dict()
        else:
            preview = self.preview

        purpose: str | Unset = UNSET
        if not isinstance(self.purpose, Unset):
            purpose = self.purpose.value

        schedule_id: str | Unset | None
        if isinstance(self.schedule_id, Unset):
            schedule_id = UNSET
        else:
            schedule_id = self.schedule_id

        title: str | Unset | None
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cost": cost,
                "created_at": created_at,
                "created_by_id": created_by_id,
                "id": id,
                "labels": labels,
                "last_run_id": last_run_id,
                "run_count": run_count,
                "unpriced_requests": unpriced_requests,
                "updated_at": updated_at,
                "version": version,
                "workspace_id": workspace_id,
            }
        )
        if memory is not UNSET:
            field_dict["memory"] = memory
        if origin is not UNSET:
            field_dict["origin"] = origin
        if preview is not UNSET:
            field_dict["preview"] = preview
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if schedule_id is not UNSET:
            field_dict["schedule_id"] = schedule_id
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_memory_settings import SessionMemorySettings
        from ..models.session_origin import SessionOrigin
        from ..models.session_preview import SessionPreview
        from ..models.session_view_labels import SessionViewLabels

        d = dict(src_dict)

        def _parse_cost(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        cost = _parse_cost(d.pop("cost"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        created_by_id = d.pop("created_by_id")

        id = d.pop("id")

        labels = SessionViewLabels.from_dict(d.pop("labels"))

        def _parse_last_run_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        last_run_id = _parse_last_run_id(d.pop("last_run_id"))

        run_count = d.pop("run_count")

        unpriced_requests = d.pop("unpriced_requests")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        version = d.pop("version")

        workspace_id = d.pop("workspace_id")

        _memory = d.pop("memory", UNSET)
        memory: SessionMemorySettings | Unset
        if isinstance(_memory, Unset):
            memory = UNSET
        else:
            memory = SessionMemorySettings.from_dict(_memory)

        def _parse_origin(data: object) -> SessionOrigin | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                origin_type_0 = SessionOrigin.from_dict(data)

                return origin_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(SessionOrigin | Unset | None, data)

        origin = _parse_origin(d.pop("origin", UNSET))

        def _parse_preview(data: object) -> SessionPreview | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                preview_type_0 = SessionPreview.from_dict(data)

                return preview_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(SessionPreview | Unset | None, data)

        preview = _parse_preview(d.pop("preview", UNSET))

        _purpose = d.pop("purpose", UNSET)
        purpose: SessionViewPurpose | Unset
        if isinstance(_purpose, Unset):
            purpose = UNSET
        else:
            purpose = SessionViewPurpose(_purpose)

        def _parse_schedule_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        schedule_id = _parse_schedule_id(d.pop("schedule_id", UNSET))

        def _parse_title(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        title = _parse_title(d.pop("title", UNSET))

        session_view = cls(
            cost=cost,
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            labels=labels,
            last_run_id=last_run_id,
            run_count=run_count,
            unpriced_requests=unpriced_requests,
            updated_at=updated_at,
            version=version,
            workspace_id=workspace_id,
            memory=memory,
            origin=origin,
            preview=preview,
            purpose=purpose,
            schedule_id=schedule_id,
            title=title,
        )

        session_view.additional_properties = d
        return session_view

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
