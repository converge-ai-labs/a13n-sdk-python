from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.approve import Approve
    from ..models.deny import Deny


T = TypeVar("T", bound="PendingAnswerApprovals")


@_attrs_define(repr=False)
class PendingAnswerApprovals:
    additional_properties: dict[str, Approve | Deny] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.approve import Approve

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, Approve):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.approve import Approve
        from ..models.deny import Deny

        d = dict(src_dict)
        pending_answer_approvals = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(data: object) -> Approve | Deny:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_approval_decision_type_0 = Approve.from_dict(data)

                    return componentsschemas_approval_decision_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_approval_decision_type_1 = Deny.from_dict(data)

                return componentsschemas_approval_decision_type_1

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        pending_answer_approvals.additional_properties = additional_properties
        return pending_answer_approvals

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Approve | Deny:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Approve | Deny) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
