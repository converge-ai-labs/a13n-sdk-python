from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.category import Category
from ..models.severity import Severity
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.evidence import Evidence


T = TypeVar("T", bound="FindingCreate")


@_attrs_define(repr=False)
class FindingCreate:
    """
    Attributes:
        agent_id (str):
        agent_revision_id (str):
        category (Category):
        evidence (list[Evidence]):
        explanation (str):
        source_key (str):
        suggestion (str):
        title (str):
        limitations (str | Unset):
        severity (Severity | Unset):
    """

    agent_id: str
    agent_revision_id: str
    category: Category
    evidence: list[Evidence]
    explanation: str
    source_key: str
    suggestion: str
    title: str
    limitations: str | Unset = UNSET
    severity: Severity | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        agent_id = self.agent_id

        agent_revision_id = self.agent_revision_id

        category = self.category.value

        evidence = []
        for evidence_item_data in self.evidence:
            evidence_item = evidence_item_data.to_dict()
            evidence.append(evidence_item)

        explanation = self.explanation

        source_key = self.source_key

        suggestion = self.suggestion

        title = self.title

        limitations = self.limitations

        severity: str | Unset = UNSET
        if not isinstance(self.severity, Unset):
            severity = self.severity.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "agent_id": agent_id,
                "agent_revision_id": agent_revision_id,
                "category": category,
                "evidence": evidence,
                "explanation": explanation,
                "source_key": source_key,
                "suggestion": suggestion,
                "title": title,
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

        category = Category(d.pop("category"))

        evidence = []
        _evidence = d.pop("evidence")
        for evidence_item_data in _evidence:
            evidence_item = Evidence.from_dict(evidence_item_data)

            evidence.append(evidence_item)

        explanation = d.pop("explanation")

        source_key = d.pop("source_key")

        suggestion = d.pop("suggestion")

        title = d.pop("title")

        limitations = d.pop("limitations", UNSET)

        _severity = d.pop("severity", UNSET)
        severity: Severity | Unset
        if isinstance(_severity, Unset):
            severity = UNSET
        else:
            severity = Severity(_severity)

        finding_create = cls(
            agent_id=agent_id,
            agent_revision_id=agent_revision_id,
            category=category,
            evidence=evidence,
            explanation=explanation,
            source_key=source_key,
            suggestion=suggestion,
            title=title,
            limitations=limitations,
            severity=severity,
        )

        return finding_create
