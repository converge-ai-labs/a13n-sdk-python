from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.child_environment_policy import ChildEnvironmentPolicy
    from ..models.delegation_context_policy import DelegationContextPolicy
    from ..models.usage_limits_output import UsageLimitsOutput


T = TypeVar("T", bound="SubagentSelectionOutput")


@_attrs_define(repr=False)
class SubagentSelectionOutput:
    """
    Attributes:
        agent_id (str):
        context (DelegationContextPolicy | Unset):
        description (None | str | Unset):
        environment (ChildEnvironmentPolicy | Unset): What a child run mounts: no environment, the parent's, or a new
            one from `template_id`.
        revision_id (None | str | Unset):
        usage_limits (None | Unset | UsageLimitsOutput):
    """

    agent_id: str
    context: DelegationContextPolicy | Unset = UNSET
    description: str | Unset | None = UNSET
    environment: ChildEnvironmentPolicy | Unset = UNSET
    revision_id: str | Unset | None = UNSET
    usage_limits: Unset | UsageLimitsOutput | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.usage_limits_output import UsageLimitsOutput

        agent_id = self.agent_id

        context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.to_dict()

        description: str | Unset | None
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        environment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.environment, Unset):
            environment = self.environment.to_dict()

        revision_id: str | Unset | None
        if isinstance(self.revision_id, Unset):
            revision_id = UNSET
        else:
            revision_id = self.revision_id

        usage_limits: dict[str, Any] | Unset | None
        if isinstance(self.usage_limits, Unset):
            usage_limits = UNSET
        elif isinstance(self.usage_limits, UsageLimitsOutput):
            usage_limits = self.usage_limits.to_dict()
        else:
            usage_limits = self.usage_limits

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "agent_id": agent_id,
            }
        )
        if context is not UNSET:
            field_dict["context"] = context
        if description is not UNSET:
            field_dict["description"] = description
        if environment is not UNSET:
            field_dict["environment"] = environment
        if revision_id is not UNSET:
            field_dict["revision_id"] = revision_id
        if usage_limits is not UNSET:
            field_dict["usage_limits"] = usage_limits

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.child_environment_policy import ChildEnvironmentPolicy
        from ..models.delegation_context_policy import DelegationContextPolicy
        from ..models.usage_limits_output import UsageLimitsOutput

        d = dict(src_dict)
        agent_id = d.pop("agent_id")

        _context = d.pop("context", UNSET)
        context: DelegationContextPolicy | Unset
        if isinstance(_context, Unset):
            context = UNSET
        else:
            context = DelegationContextPolicy.from_dict(_context)

        def _parse_description(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        description = _parse_description(d.pop("description", UNSET))

        _environment = d.pop("environment", UNSET)
        environment: ChildEnvironmentPolicy | Unset
        if isinstance(_environment, Unset):
            environment = UNSET
        else:
            environment = ChildEnvironmentPolicy.from_dict(_environment)

        def _parse_revision_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        revision_id = _parse_revision_id(d.pop("revision_id", UNSET))

        def _parse_usage_limits(data: object) -> Unset | UsageLimitsOutput | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                usage_limits_type_0 = UsageLimitsOutput.from_dict(data)

                return usage_limits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Unset | UsageLimitsOutput | None, data)

        usage_limits = _parse_usage_limits(d.pop("usage_limits", UNSET))

        subagent_selection_output = cls(
            agent_id=agent_id,
            context=context,
            description=description,
            environment=environment,
            revision_id=revision_id,
            usage_limits=usage_limits,
        )

        return subagent_selection_output
