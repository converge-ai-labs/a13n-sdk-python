from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CompleteMCPOAuthRequest")


@_attrs_define(repr=False)
class CompleteMCPOAuthRequest:
    """
    Attributes:
        code (str):
        issuer (str):
        state (str):
    """

    code: str
    issuer: str
    state: str

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        issuer = self.issuer

        state = self.state

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
                "issuer": issuer,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        issuer = d.pop("issuer")

        state = d.pop("state")

        complete_mcpo_auth_request = cls(
            code=code,
            issuer=issuer,
            state=state,
        )

        return complete_mcpo_auth_request
