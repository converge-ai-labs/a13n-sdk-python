from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.git_hub_reception_policy import GitHubReceptionPolicy
    from ..models.messaging_policy import MessagingPolicy


T = TypeVar("T", bound="ActivateBotRequest")


@_attrs_define(repr=False)
class ActivateBotRequest:
    """
    Attributes:
        agent_id (str):
        conversation_id (str):
        execution_service_account_id (str):
        expected_version (int):
        policy (GitHubReceptionPolicy | MessagingPolicy):
        target_id (str):
        target_version (int):
    """

    agent_id: str
    conversation_id: str
    execution_service_account_id: str
    expected_version: int
    policy: GitHubReceptionPolicy | MessagingPolicy
    target_id: str
    target_version: int

    def to_dict(self) -> dict[str, Any]:
        from ..models.messaging_policy import MessagingPolicy

        agent_id = self.agent_id

        conversation_id = self.conversation_id

        execution_service_account_id = self.execution_service_account_id

        expected_version = self.expected_version

        policy: dict[str, Any]
        if isinstance(self.policy, MessagingPolicy):
            policy = self.policy.to_dict()
        else:
            policy = self.policy.to_dict()

        target_id = self.target_id

        target_version = self.target_version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "agent_id": agent_id,
                "conversation_id": conversation_id,
                "execution_service_account_id": execution_service_account_id,
                "expected_version": expected_version,
                "policy": policy,
                "target_id": target_id,
                "target_version": target_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.git_hub_reception_policy import GitHubReceptionPolicy
        from ..models.messaging_policy import MessagingPolicy

        d = dict(src_dict)
        agent_id = d.pop("agent_id")

        conversation_id = d.pop("conversation_id")

        execution_service_account_id = d.pop("execution_service_account_id")

        expected_version = d.pop("expected_version")

        def _parse_policy(data: object) -> GitHubReceptionPolicy | MessagingPolicy:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                policy_type_0 = MessagingPolicy.from_dict(data)

                return policy_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            policy_type_1 = GitHubReceptionPolicy.from_dict(data)

            return policy_type_1

        policy = _parse_policy(d.pop("policy"))

        target_id = d.pop("target_id")

        target_version = d.pop("target_version")

        activate_bot_request = cls(
            agent_id=agent_id,
            conversation_id=conversation_id,
            execution_service_account_id=execution_service_account_id,
            expected_version=expected_version,
            policy=policy,
            target_id=target_id,
            target_version=target_version,
        )

        return activate_bot_request
