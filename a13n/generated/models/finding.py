from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.assessment import Assessment
from ..models.category import Category
from ..models.severity import Severity
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.evidence import Evidence


T = TypeVar("T", bound="Finding")


@_attrs_define(repr=False)
class Finding:
    """
    Attributes:
        agent_id (str):
        agent_revision_id (str):
        analysis_id (None | str):
        assessment (Assessment):
        assessment_note (str):
        category (Category):
        closed (bool):
        created_at (datetime.datetime):
        created_by_id (str):
        evidence (list[Evidence]):
        explanation (str):
        id (str):
        source_key (str):
        source_run_id (None | str):
        suggestion (str):
        title (str):
        updated_at (datetime.datetime):
        version (int):
        workspace_id (str):
        limitations (str | Unset):
        severity (Severity | Unset):
    """

    agent_id: str
    agent_revision_id: str
    analysis_id: str | None
    assessment: Assessment
    assessment_note: str
    category: Category
    closed: bool
    created_at: datetime.datetime
    created_by_id: str
    evidence: list[Evidence]
    explanation: str
    id: str
    source_key: str
    source_run_id: str | None
    suggestion: str
    title: str
    updated_at: datetime.datetime
    version: int
    workspace_id: str
    limitations: str | Unset = UNSET
    severity: Severity | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        agent_id = self.agent_id

        agent_revision_id = self.agent_revision_id

        analysis_id: str | None
        analysis_id = self.analysis_id

        assessment = self.assessment.value

        assessment_note = self.assessment_note

        category = self.category.value

        closed = self.closed

        created_at = self.created_at.isoformat()

        created_by_id = self.created_by_id

        evidence = []
        for evidence_item_data in self.evidence:
            evidence_item = evidence_item_data.to_dict()
            evidence.append(evidence_item)

        explanation = self.explanation

        id = self.id

        source_key = self.source_key

        source_run_id: str | None
        source_run_id = self.source_run_id

        suggestion = self.suggestion

        title = self.title

        updated_at = self.updated_at.isoformat()

        version = self.version

        workspace_id = self.workspace_id

        limitations = self.limitations

        severity: str | Unset = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "agent_id": agent_id,
                "agent_revision_id": agent_revision_id,
                "analysis_id": analysis_id,
                "assessment": assessment,
                "assessment_note": assessment_note,
                "category": category,
                "closed": closed,
                "created_at": created_at,
                "created_by_id": created_by_id,
                "evidence": evidence,
                "explanation": explanation,
                "id": id,
                "source_key": source_key,
                "source_run_id": source_run_id,
                "suggestion": suggestion,
                "title": title,
                "updated_at": updated_at,
                "version": version,
                "workspace_id": workspace_id,
            }
        )
        if limitations is not UNSET:
            field_dict["limitations"] = limitations
        if severity is not UNSET:
            field_dict["severity"] = severity

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.evidence import Evidence

        d = dict(src_dict)
        agent_id = d.pop("agent_id")

        agent_revision_id = d.pop("agent_revision_id")

        def _parse_analysis_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        analysis_id = _parse_analysis_id(d.pop("analysis_id"))

        assessment = Assessment(d.pop("assessment"))

        assessment_note = d.pop("assessment_note")

        category = Category(d.pop("category"))

        closed = d.pop("closed")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        created_by_id = d.pop("created_by_id")

        evidence = []
        _evidence = d.pop("evidence")
        for evidence_item_data in _evidence:
            evidence_item = Evidence.from_dict(evidence_item_data)

            evidence.append(evidence_item)

        explanation = d.pop("explanation")

        id = d.pop("id")

        source_key = d.pop("source_key")

        def _parse_source_run_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        source_run_id = _parse_source_run_id(d.pop("source_run_id"))

        suggestion = d.pop("suggestion")

        title = d.pop("title")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        version = d.pop("version")

        workspace_id = d.pop("workspace_id")

        limitations = d.pop("limitations", UNSET)

        _severity = d.pop("severity", UNSET)
        severity: Severity | Unset
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = Severity(_severity)

        finding = cls(
            agent_id=agent_id,
            agent_revision_id=agent_revision_id,
            analysis_id=analysis_id,
            assessment=assessment,
            assessment_note=assessment_note,
            category=category,
            closed=closed,
            created_at=created_at,
            created_by_id=created_by_id,
            evidence=evidence,
            explanation=explanation,
            id=id,
            source_key=source_key,
            source_run_id=source_run_id,
            suggestion=suggestion,
            title=title,
            updated_at=updated_at,
            version=version,
            workspace_id=workspace_id,
            limitations=limitations,
            severity=severity,
        )

        return finding
