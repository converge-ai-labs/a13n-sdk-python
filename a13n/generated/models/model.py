from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.catalog_ref import CatalogRef
    from ..models.model_config_output import ModelConfigOutput
    from ..models.model_pricing_entry_output import ModelPricingEntryOutput


T = TypeVar("T", bound="Model")


@_attrs_define(repr=False)
class Model:
    """
    Attributes:
        catalog_ref (CatalogRef | None):
        config (ModelConfigOutput):
        created_at (datetime.datetime):
        created_by_id (str):
        description (str):
        enabled (bool):
        key (str):
        name (str):
        organization_id (str):
        pricing (ModelPricingEntryOutput | None):
        provider_id (str):
        updated_at (datetime.datetime):
        updated_by_id (str):
        version (int):
        workspace_id (str):
    """

    catalog_ref: CatalogRef | None
    config: ModelConfigOutput
    created_at: datetime.datetime
    created_by_id: str
    description: str
    enabled: bool
    key: str
    name: str
    organization_id: str
    pricing: ModelPricingEntryOutput | None
    provider_id: str
    updated_at: datetime.datetime
    updated_by_id: str
    version: int
    workspace_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.catalog_ref import CatalogRef
        from ..models.model_pricing_entry_output import ModelPricingEntryOutput

        catalog_ref: dict[str, Any] | None
        if isinstance(self.catalog_ref, CatalogRef):
            catalog_ref = self.catalog_ref.to_dict()
        else:
            catalog_ref = self.catalog_ref

        config = self.config.to_dict()

        created_at = self.created_at.isoformat()

        created_by_id = self.created_by_id

        description = self.description

        enabled = self.enabled

        key = self.key

        name = self.name

        organization_id = self.organization_id

        pricing: dict[str, Any] | None
        if isinstance(self.pricing, ModelPricingEntryOutput):
            pricing = self.pricing.to_dict()
        else:
            pricing = self.pricing

        provider_id = self.provider_id

        updated_at = self.updated_at.isoformat()

        updated_by_id = self.updated_by_id

        version = self.version

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "catalog_ref": catalog_ref,
                "config": config,
                "created_at": created_at,
                "created_by_id": created_by_id,
                "description": description,
                "enabled": enabled,
                "key": key,
                "name": name,
                "organization_id": organization_id,
                "pricing": pricing,
                "provider_id": provider_id,
                "updated_at": updated_at,
                "updated_by_id": updated_by_id,
                "version": version,
                "workspace_id": workspace_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_ref import CatalogRef
        from ..models.model_config_output import ModelConfigOutput
        from ..models.model_pricing_entry_output import ModelPricingEntryOutput

        d = dict(src_dict)

        def _parse_catalog_ref(data: object) -> CatalogRef | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                catalog_ref_type_0 = CatalogRef.from_dict(data)

                return catalog_ref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CatalogRef | None, data)

        catalog_ref = _parse_catalog_ref(d.pop("catalog_ref"))

        config = ModelConfigOutput.from_dict(d.pop("config"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        created_by_id = d.pop("created_by_id")

        description = d.pop("description")

        enabled = d.pop("enabled")

        key = d.pop("key")

        name = d.pop("name")

        organization_id = d.pop("organization_id")

        def _parse_pricing(data: object) -> ModelPricingEntryOutput | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                pricing_type_0 = ModelPricingEntryOutput.from_dict(data)

                return pricing_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ModelPricingEntryOutput | None, data)

        pricing = _parse_pricing(d.pop("pricing"))

        provider_id = d.pop("provider_id")

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        updated_by_id = d.pop("updated_by_id")

        version = d.pop("version")

        workspace_id = d.pop("workspace_id")

        model = cls(
            catalog_ref=catalog_ref,
            config=config,
            created_at=created_at,
            created_by_id=created_by_id,
            description=description,
            enabled=enabled,
            key=key,
            name=name,
            organization_id=organization_id,
            pricing=pricing,
            provider_id=provider_id,
            updated_at=updated_at,
            updated_by_id=updated_by_id,
            version=version,
            workspace_id=workspace_id,
        )

        model.additional_properties = d
        return model

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
