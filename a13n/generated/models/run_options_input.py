from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.agent_override_input import AgentOverrideInput
    from ..models.run_configuration_input import RunConfigurationInput
    from ..models.run_options_input_labels import RunOptionsInputLabels
    from ..models.usage_limit import UsageLimit


T = TypeVar("T", bound="RunOptionsInput")


@_attrs_define(repr=False)
class RunOptionsInput:
    """What a message may choose for the run it starts. A steer joins a run with the defaults or equal options.

    Attributes:
        configuration (None | RunConfigurationInput | Unset):
        labels (RunOptionsInputLabels | Unset):
        max_usage (None | Unset | UsageLimit):
        overrides (AgentOverrideInput | None | Unset):
    """

    configuration: RunConfigurationInput | Unset | None = UNSET
    labels: RunOptionsInputLabels | Unset = UNSET
    max_usage: Unset | UsageLimit | None = UNSET
    overrides: AgentOverrideInput | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.agent_override_input import AgentOverrideInput
        from ..models.run_configuration_input import RunConfigurationInput
        from ..models.usage_limit import UsageLimit

        configuration: dict[str, Any] | Unset | None
        if isinstance(self.configuration, Unset):
            configuration = UNSET
        elif isinstance(self.configuration, RunConfigurationInput):
            configuration = self.configuration.to_dict()
        else:
            configuration = self.configuration

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
        elif isinstance(self.overrides, AgentOverrideInput):
            overrides = self.overrides.to_dict()
        else:
            overrides = self.overrides

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if configuration is not UNSET:
            field_dict["configuration"] = configuration
        if labels is not UNSET:
            field_dict["labels"] = labels
        if max_usage is not UNSET:
            field_dict["max_usage"] = max_usage
        if overrides is not UNSET:
            field_dict["overrides"] = overrides

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.agent_override_input import AgentOverrideInput
        from ..models.run_configuration_input import RunConfigurationInput
        from ..models.run_options_input_labels import RunOptionsInputLabels
        from ..models.usage_limit import UsageLimit

        d = dict(src_dict)

        def _parse_configuration(data: object) -> RunConfigurationInput | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                configuration_type_0 = RunConfigurationInput.from_dict(data)

                return configuration_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(RunConfigurationInput | Unset | None, data)

        configuration = _parse_configuration(d.pop("configuration", UNSET))

        _labels = d.pop("labels", UNSET)
        labels: RunOptionsInputLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = RunOptionsInputLabels.from_dict(_labels)

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

        def _parse_overrides(data: object) -> AgentOverrideInput | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                overrides_type_0 = AgentOverrideInput.from_dict(data)

                return overrides_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AgentOverrideInput | Unset | None, data)

        overrides = _parse_overrides(d.pop("overrides", UNSET))

        run_options_input = cls(
            configuration=configuration,
            labels=labels,
            max_usage=max_usage,
            overrides=overrides,
        )

        return run_options_input
