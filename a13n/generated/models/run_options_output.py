from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_override_output import AgentOverrideOutput
    from ..models.run_options_output_labels import RunOptionsOutputLabels
    from ..models.usage_limit import UsageLimit


T = TypeVar("T", bound="RunOptionsOutput")


@_attrs_define(repr=False)
class RunOptionsOutput:
    """What a message may choose for the run it starts. A steer joins a run with the defaults or equal options.

    Attributes:
        labels (RunOptionsOutputLabels | Unset):
        max_usage (None | Unset | UsageLimit):
        overrides (AgentOverrideOutput | None | Unset):
    """

    labels: RunOptionsOutputLabels | Unset = UNSET
    max_usage: Unset | UsageLimit | None = UNSET
    overrides: AgentOverrideOutput | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_override_output import AgentOverrideOutput
        from ..models.usage_limit import UsageLimit

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        max_usage: dict[str, Any] | Unset | None
        if isinstance(self.max_usage, Unset):
            max_usage = UNSET
        elif isinstance(self.max_usage, UsageLimit):
            max_usage = self.max_usage.to_dict()
        else:
            max_usage = self.max_usage

        overrides: dict[str, Any] | Unset | None
        if isinstance(self.overrides, Unset):
            overrides = UNSET
        elif isinstance(self.overrides, AgentOverrideOutput):
            overrides = self.overrides.to_dict()
        else:
            overrides = self.overrides

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if labels is not UNSET:
            field_dict["labels"] = labels
        if max_usage is not UNSET:
            field_dict["max_usage"] = max_usage
        if overrides is not UNSET:
            field_dict["overrides"] = overrides

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_override_output import AgentOverrideOutput
        from ..models.run_options_output_labels import RunOptionsOutputLabels
        from ..models.usage_limit import UsageLimit

        d = dict(src_dict)
        _labels = d.pop("labels", UNSET)
        labels: RunOptionsOutputLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = RunOptionsOutputLabels.from_dict(_labels)

        def _parse_max_usage(data: object) -> Unset | UsageLimit | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                max_usage_type_0 = UsageLimit.from_dict(data)

                return max_usage_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Unset | UsageLimit | None, data)

        max_usage = _parse_max_usage(d.pop("max_usage", UNSET))

        def _parse_overrides(data: object) -> AgentOverrideOutput | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                overrides_type_0 = AgentOverrideOutput.from_dict(data)

                return overrides_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentOverrideOutput | Unset | None, data)

        overrides = _parse_overrides(d.pop("overrides", UNSET))

        run_options_output = cls(
            labels=labels,
            max_usage=max_usage,
            overrides=overrides,
        )

        return run_options_output
