from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_request import OrganizationRequest
    from ..models.organization_source import OrganizationSource


T = TypeVar("T", bound="MemoryOrganization")


@_attrs_define(repr=False)
class MemoryOrganization:
    """
    Attributes:
        created_at (datetime.datetime):
        created_by_id (str):
        id (str):
        request (OrganizationRequest):
        run_id (str):
        session_id (str):
        sources (list[OrganizationSource]):
        thread_id (str):
        workspace_id (str):
        candidate_memory_id (None | str | Unset):
    """

    created_at: datetime.datetime
    created_by_id: str
    id: str
    request: OrganizationRequest
    run_id: str
    session_id: str
    sources: list[OrganizationSource]
    thread_id: str
    workspace_id: str
    candidate_memory_id: str | Unset | None = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at = self.created_at.isoformat()

        created_by_id = self.created_by_id

        id = self.id

        request = self.request.to_dict()

        run_id = self.run_id

        session_id = self.session_id

        sources = []
        for sources_item_data in self.sources:
            sources_item = sources_item_data.to_dict()
            sources.append(sources_item)

        thread_id = self.thread_id

        workspace_id = self.workspace_id

        candidate_memory_id: str | Unset | None
        if isinstance(self.candidate_memory_id, Unset):
            candidate_memory_id = UNSET
        else:
            candidate_memory_id = self.candidate_memory_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "created_by_id": created_by_id,
                "id": id,
                "request": request,
                "run_id": run_id,
                "session_id": session_id,
                "sources": sources,
                "thread_id": thread_id,
                "workspace_id": workspace_id,
            }
        )
        if candidate_memory_id is not UNSET:
            field_dict["candidate_memory_id"] = candidate_memory_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_request import OrganizationRequest
        from ..models.organization_source import OrganizationSource

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        created_by_id = d.pop("created_by_id")

        id = d.pop("id")

        request = OrganizationRequest.from_dict(d.pop("request"))

        run_id = d.pop("run_id")

        session_id = d.pop("session_id")

        sources = []
        _sources = d.pop("sources")
        for sources_item_data in _sources:
            sources_item = OrganizationSource.from_dict(sources_item_data)

            sources.append(sources_item)

        thread_id = d.pop("thread_id")

        workspace_id = d.pop("workspace_id")

        def _parse_candidate_memory_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        candidate_memory_id = _parse_candidate_memory_id(d.pop("candidate_memory_id", UNSET))

        memory_organization = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            id=id,
            request=request,
            run_id=run_id,
            session_id=session_id,
            sources=sources,
            thread_id=thread_id,
            workspace_id=workspace_id,
            candidate_memory_id=candidate_memory_id,
        )

        memory_organization.additional_properties = d
        return memory_organization

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
