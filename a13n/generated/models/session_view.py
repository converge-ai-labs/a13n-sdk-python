from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.session_preview import SessionPreview
    from ..models.session_view_labels import SessionViewLabels


T = TypeVar("T", bound="SessionView")


@_attrs_define(repr=False)
class SessionView:
    """
    Attributes:
        created_at (datetime.datetime):
        created_by_id (str):
        id (str):
        labels (SessionViewLabels):
        last_run_id (None | str):
        updated_at (datetime.datetime):
        version (int):
        workspace_id (str):
        preview (None | SessionPreview | Unset):
        run_count (int | Unset):
    """

    created_at: datetime.datetime
    created_by_id: str
    id: str
    labels: SessionViewLabels
    last_run_id: str | None
    updated_at: datetime.datetime
    version: int
    workspace_id: str
    preview: SessionPreview | Unset | None = UNSET
    run_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.session_preview import SessionPreview

        created_at = self.created_at.isoformat()

        created_by_id = self.created_by_id

        id = self.id

        labels = self.labels.to_dict()

        last_run_id: str | None
        last_run_id = self.last_run_id

        updated_at = self.updated_at.isoformat()

        version = self.version

        workspace_id = self.workspace_id

        preview: dict[str, Any] | Unset | None
        if isinstance(self.preview, Unset):
            preview = UNSET
        elif isinstance(self.preview, SessionPreview):
            preview = self.preview.to_dict()
        else:
            preview = self.preview

        run_count = self.run_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "created_by_id": created_by_id,
                "id": id,
                "labels": labels,
                "last_run_id": last_run_id,
                "updated_at": updated_at,
                "version": version,
                "workspace_id": workspace_id,
            }
        )
        if preview is not UNSET:
            field_dict["preview"] = preview
        if run_count is not UNSET:
            field_dict["run_count"] = run_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_preview import SessionPreview
        from ..models.session_view_labels import SessionViewLabels

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        created_by_id = d.pop("created_by_id")

        id = d.pop("id")

        labels = SessionViewLabels.from_dict(d.pop("labels"))

        def _parse_last_run_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        last_run_id = _parse_last_run_id(d.pop("last_run_id"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        version = d.pop("version")

        workspace_id = d.pop("workspace_id")

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

        run_count = d.pop("run_count", UNSET)

        session_view = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            labels=labels,
            last_run_id=last_run_id,
            updated_at=updated_at,
            version=version,
            workspace_id=workspace_id,
            preview=preview,
            run_count=run_count,
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
