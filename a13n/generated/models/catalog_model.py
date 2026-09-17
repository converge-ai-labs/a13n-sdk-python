from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.catalog_ref import CatalogRef
    from ..models.model_declarations_output import ModelDeclarationsOutput


T = TypeVar("T", bound="CatalogModel")


@_attrs_define(repr=False)
class CatalogModel:
    """
    Attributes:
        declarations (ModelDeclarationsOutput): Harness-facing facts and authoring choices declared for one saved Model.
        identity (str):
        name (str):
        provider_name (str):
        ref (CatalogRef): A models.dev provider-qualified identity, independent of the outbound ID.
        release_date (datetime.date):
        pricing_warning (None | str | Unset):
    """

    declarations: ModelDeclarationsOutput
    identity: str
    name: str
    provider_name: str
    ref: CatalogRef
    release_date: datetime.date
    pricing_warning: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        declarations = self.declarations.to_dict()

        identity = self.identity

        name = self.name

        provider_name = self.provider_name

        ref = self.ref.to_dict()

        release_date = self.release_date.isoformat()

        pricing_warning: str | Unset | None
        if isinstance(self.pricing_warning, Unset):
            pricing_warning = UNSET
        else:
            pricing_warning = self.pricing_warning

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "declarations": declarations,
                "identity": identity,
                "name": name,
                "provider_name": provider_name,
                "ref": ref,
                "release_date": release_date,
            }
        )
        if pricing_warning is not UNSET:
            field_dict["pricing_warning"] = pricing_warning

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.catalog_ref import CatalogRef
        from ..models.model_declarations_output import ModelDeclarationsOutput

        d = dict(src_dict)
        declarations = ModelDeclarationsOutput.from_dict(d.pop("declarations"))

        identity = d.pop("identity")

        name = d.pop("name")

        provider_name = d.pop("provider_name")

        ref = CatalogRef.from_dict(d.pop("ref"))

        release_date = datetime.date.fromisoformat(d.pop("release_date"))

        def _parse_pricing_warning(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        pricing_warning = _parse_pricing_warning(d.pop("pricing_warning", UNSET))

        catalog_model = cls(
            declarations=declarations,
            identity=identity,
            name=name,
            provider_name=provider_name,
            ref=ref,
            release_date=release_date,
            pricing_warning=pricing_warning,
        )

        return catalog_model
