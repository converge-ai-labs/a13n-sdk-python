from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="GitHubReceptionPolicy")


@_attrs_define(repr=False)
class GitHubReceptionPolicy:
    """
    Attributes:
        allowed_senders (list[str] | Unset):
        event_actions (list[str] | Unset):
    """

    allowed_senders: list[str] | Unset = UNSET
    event_actions: list[str] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        allowed_senders: list[str] | Unset = UNSET
        if not isinstance(self.allowed_senders, Unset):
            allowed_senders = self.allowed_senders

        event_actions: list[str] | Unset = UNSET
        if not isinstance(self.event_actions, Unset):
            event_actions = self.event_actions

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if allowed_senders is not UNSET:
            field_dict["allowed_senders"] = allowed_senders
        if event_actions is not UNSET:
            field_dict["event_actions"] = event_actions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        allowed_senders = cast(list[str], d.pop("allowed_senders", UNSET))

        event_actions = cast(list[str], d.pop("event_actions", UNSET))

        git_hub_reception_policy = cls(
            allowed_senders=allowed_senders,
            event_actions=event_actions,
        )

        return git_hub_reception_policy
