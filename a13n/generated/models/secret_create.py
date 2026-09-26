from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.secret_scope import SecretScope
from ..types import UNSET, Unset

T = TypeVar("T", bound="SecretCreate")


@_attrs_define(repr=False)
class SecretCreate:
    """`user` creates a secret private to the caller.

    Attributes:
        key (str):
        value (str):
        scope (SecretScope | Unset):
    """

    key: str
    value: str
    scope: SecretScope | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        value = self.value

        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
                "value": value,
            }
        )
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        value = d.pop("value")

        _scope = d.pop("scope", UNSET)
        scope: SecretScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = SecretScope(_scope)

        secret_create = cls(
            key=key,
            value=value,
            scope=scope,
        )

        return secret_create
