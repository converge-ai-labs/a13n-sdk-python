from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="PairingApproval")


@_attrs_define(repr=False)
class PairingApproval:
    """
    Attributes:
        verification_code (str):
    """

    verification_code: str

    def to_dict(self) -> dict[str, Any]:
        verification_code = self.verification_code

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "verification_code": verification_code,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        verification_code = d.pop("verification_code")

        pairing_approval = cls(
            verification_code=verification_code,
        )

        return pairing_approval
