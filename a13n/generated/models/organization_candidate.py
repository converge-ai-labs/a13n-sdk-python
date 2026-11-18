from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.organization_candidate_status import OrganizationCandidateStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.candidate_application import CandidateApplication
    from ..models.candidate_change import CandidateChange


T = TypeVar("T", bound="OrganizationCandidate")


@_attrs_define(repr=False)
class OrganizationCandidate:
    """
    Attributes:
        baseline_seq (int):
        candidate_seq (int | None):
        changes (list[CandidateChange]):
        files (list[str]):
        memory_id (str):
        organization_id (str):
        status (OrganizationCandidateStatus):
        target_memory_id (str):
        target_seq (int | None):
        application (CandidateApplication | None | Unset):
    """

    baseline_seq: int
    candidate_seq: int | None
    changes: list[CandidateChange]
    files: list[str]
    memory_id: str
    organization_id: str
    status: OrganizationCandidateStatus
    target_memory_id: str
    target_seq: int | None
    application: CandidateApplication | Unset | None = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.candidate_application import CandidateApplication

        baseline_seq = self.baseline_seq

        candidate_seq: int | None
        candidate_seq = self.candidate_seq

        changes = []
        for changes_item_data in self.changes:
            changes_item = changes_item_data.to_dict()
            changes.append(changes_item)

        files = self.files

        memory_id = self.memory_id

        organization_id = self.organization_id

        status = self.status.value

        target_memory_id = self.target_memory_id

        target_seq: int | None
        target_seq = self.target_seq

        application: dict[str, Any] | Unset | None
        if isinstance(self.application, Unset):
            application = UNSET
        elif isinstance(self.application, CandidateApplication):
            application = self.application.to_dict()
        else:
            application = self.application

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "baseline_seq": baseline_seq,
                "candidate_seq": candidate_seq,
                "changes": changes,
                "files": files,
                "memory_id": memory_id,
                "organization_id": organization_id,
                "status": status,
                "target_memory_id": target_memory_id,
                "target_seq": target_seq,
            }
        )
        if application is not UNSET:
            field_dict["application"] = application

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.candidate_application import CandidateApplication
        from ..models.candidate_change import CandidateChange

        d = dict(src_dict)
        baseline_seq = d.pop("baseline_seq")

        def _parse_candidate_seq(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        candidate_seq = _parse_candidate_seq(d.pop("candidate_seq"))

        changes = []
        _changes = d.pop("changes")
        for changes_item_data in _changes:
            changes_item = CandidateChange.from_dict(changes_item_data)

            changes.append(changes_item)

        files = cast(list[str], d.pop("files"))

        memory_id = d.pop("memory_id")

        organization_id = d.pop("organization_id")

        status = OrganizationCandidateStatus(d.pop("status"))

        target_memory_id = d.pop("target_memory_id")

        def _parse_target_seq(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        target_seq = _parse_target_seq(d.pop("target_seq"))

        def _parse_application(data: object) -> CandidateApplication | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                application_type_0 = CandidateApplication.from_dict(data)

                return application_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CandidateApplication | Unset | None, data)

        application = _parse_application(d.pop("application", UNSET))

        organization_candidate = cls(
            baseline_seq=baseline_seq,
            candidate_seq=candidate_seq,
            changes=changes,
            files=files,
            memory_id=memory_id,
            organization_id=organization_id,
            status=status,
            target_memory_id=target_memory_id,
            target_seq=target_seq,
            application=application,
        )

        organization_candidate.additional_properties = d
        return organization_candidate

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
