from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.template_config import TemplateConfig
    from ..models.template_create_labels import TemplateCreateLabels


T = TypeVar("T", bound="TemplateCreate")


@_attrs_define(repr=False)
class TemplateCreate:
    """
    Attributes:
        name (str):
        provider_id (str):
        config (TemplateConfig | Unset):
        description (None | str | Unset):
        labels (TemplateCreateLabels | Unset):
    """

    name: str
    provider_id: str
    config: TemplateConfig | Unset = UNSET
    description: str | Unset | None = UNSET
    labels: TemplateCreateLabels | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        provider_id = self.provider_id

        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        description: str | Unset | None
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = self.labels.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "provider_id": provider_id,
            }
        )
        if config is not UNSET:
            field_dict["config"] = config
        if description is not UNSET:
            field_dict["description"] = description
        if labels is not UNSET:
            field_dict["labels"] = labels

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.template_config import TemplateConfig
        from ..models.template_create_labels import TemplateCreateLabels

        d = dict(src_dict)
        name = d.pop("name")

        provider_id = d.pop("provider_id")

        _config = d.pop("config", UNSET)
        config: TemplateConfig | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = TemplateConfig.from_dict(_config)

        def _parse_description(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        description = _parse_description(d.pop("description", UNSET))

        _labels = d.pop("labels", UNSET)
        labels: TemplateCreateLabels | Unset
        if isinstance(_labels, Unset):
            labels = UNSET
        else:
            labels = TemplateCreateLabels.from_dict(_labels)

        template_create = cls(
            name=name,
            provider_id=provider_id,
            config=config,
            description=description,
            labels=labels,
        )

        return template_create
