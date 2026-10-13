from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.principal_summary import PrincipalSummary


T = TypeVar("T", bound="MessageAuthor")


@_attrs_define(repr=False)
class MessageAuthor:
    """
    Attributes:
        entry_id (str):
        principal (None | PrincipalSummary):
        principal_id (str):
        submitted_at (datetime.datetime):
    """

    entry_id: str
    principal: PrincipalSummary | None
    principal_id: str
    submitted_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        from ..models.principal_summary import PrincipalSummary

        entry_id = self.entry_id

        principal: dict[str, Any] | None
        if isinstance(self.principal, PrincipalSummary):
            principal = self.principal.to_dict()
        else:
            principal = self.principal

        principal_id = self.principal_id

        submitted_at = self.submitted_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "entry_id": entry_id,
                "principal": principal,
                "principal_id": principal_id,
                "submitted_at": submitted_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.principal_summary import PrincipalSummary

        d = dict(src_dict)
        entry_id = d.pop("entry_id")

        def _parse_principal(data: object) -> PrincipalSummary | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                principal_type_0 = PrincipalSummary.from_dict(data)

                return principal_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(PrincipalSummary | None, data)

        principal = _parse_principal(d.pop("principal"))

        principal_id = d.pop("principal_id")

        submitted_at = datetime.datetime.fromisoformat(d.pop("submitted_at"))

        message_author = cls(
            entry_id=entry_id,
            principal=principal,
            principal_id=principal_id,
            submitted_at=submitted_at,
        )

        return message_author
