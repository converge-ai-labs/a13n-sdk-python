from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.template_config import TemplateConfig
    from ..models.template_update_labels_type_0 import TemplateUpdateLabelsType0


T = TypeVar("T", bound="TemplateUpdate")


@_attrs_define(repr=False)
class TemplateUpdate:
    """Fields left out stay unchanged; `description: null` clears it.

    A new provider or recipe needs `write` on the provider and applies to environments created afterwards;
    existing ones keep what they were built with, and the idle policy applies to all of them. `enabled: false`
    refuses new environments, including reserved ones never created; created ones keep working.

        Attributes:
            config (None | TemplateConfig | Unset):
            description (None | str | Unset):
            enabled (bool | None | Unset):
            labels (None | TemplateUpdateLabelsType0 | Unset):
            name (None | str | Unset):
            provider_id (None | str | Unset):
    """

    config: TemplateConfig | Unset | None = UNSET
    description: str | Unset | None = UNSET
    enabled: bool | Unset | None = UNSET
    labels: TemplateUpdateLabelsType0 | Unset | None = UNSET
    name: str | Unset | None = UNSET
    provider_id: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.template_config import TemplateConfig
        from ..models.template_update_labels_type_0 import TemplateUpdateLabelsType0

        config: dict[str, Any] | Unset | None
        if isinstance(self.config, Unset):
            config = UNSET
        elif isinstance(self.config, TemplateConfig):
            config = self.config.to_dict()
        else:
            config = self.config

        description: str | Unset | None
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        enabled: bool | Unset | None
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        labels: dict[str, Any] | Unset | None
        if isinstance(self.labels, Unset):
            labels = UNSET
        elif isinstance(self.labels, TemplateUpdateLabelsType0):
            labels = self.labels.to_dict()
        else:
            labels = self.labels

        name: str | Unset | None
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        provider_id: str | Unset | None
        if isinstance(self.provider_id, Unset):
            provider_id = UNSET
        else:
            provider_id = self.provider_id

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if labels is not UNSET:
            field_dict["labels"] = labels
        if name is not UNSET:
            field_dict["name"] = name
        if provider_id is not UNSET:
            field_dict["provider_id"] = provider_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_config import TemplateConfig
        from ..models.template_update_labels_type_0 import TemplateUpdateLabelsType0

        d = dict(src_dict)

        def _parse_config(data: object) -> TemplateConfig | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0 = TemplateConfig.from_dict(data)

                return config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(TemplateConfig | Unset | None, data)

        config = _parse_config(d.pop("config", UNSET))

        def _parse_description(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_enabled(data: object) -> bool | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | Unset | None, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        def _parse_labels(data: object) -> TemplateUpdateLabelsType0 | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                labels_type_0 = TemplateUpdateLabelsType0.from_dict(data)

                return labels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(TemplateUpdateLabelsType0 | Unset | None, data)

        labels = _parse_labels(d.pop("labels", UNSET))

        def _parse_name(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_provider_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        provider_id = _parse_provider_id(d.pop("provider_id", UNSET))

        template_update = cls(
            config=config,
            description=description,
            enabled=enabled,
            labels=labels,
            name=name,
            provider_id=provider_id,
        )

        return template_update
