from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CatalogRef")


@_attrs_define(repr=False)
class CatalogRef:
    """A models.dev channel and the model ID it lists there.

    Attributes:
        model (str):
        provider (str):
    """

    model: str
    provider: str

    def to_dict(self) -> dict[str, Any]:
        model = self.model

        provider = self.provider

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "model": model,
                "provider": provider,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        model = d.pop("model")

        provider = d.pop("provider")

        catalog_ref = cls(
            model=model,
            provider=provider,
        )

        return catalog_ref
