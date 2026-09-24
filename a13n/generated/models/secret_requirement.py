from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.secret_scope import SecretScope
from ..types import UNSET, Unset

T = TypeVar("T", bound="SecretRequirement")


@_attrs_define(repr=False)
class SecretRequirement:
    """A secret an agent revision needs at execution; `user` resolves to the run principal's own secret.

    Attributes:
        key (str):
        scope (SecretScope | Unset):
    """

    key: str
    scope: SecretScope | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "key": key,
            }
        )
        if scope is not UNSET:
            field_dict["scope"] = scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        _scope = d.pop("scope", UNSET)
        scope: SecretScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = SecretScope(_scope)

        secret_requirement = cls(
            key=key,
            scope=scope,
        )

        return secret_requirement
