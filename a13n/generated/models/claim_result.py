from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.claim_result_state import ClaimResultState
from ..types import UNSET, Unset

T = TypeVar("T", bound="ClaimResult")


@_attrs_define(repr=False)
class ClaimResult:
    """
    Attributes:
        state (ClaimResultState):
        verification_code (str):
        connection_path (None | str | Unset):
        environment_id (None | str | Unset):
    """

    state: ClaimResultState
    verification_code: str
    connection_path: str | Unset | None = UNSET
    environment_id: str | Unset | None = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        state = self.state.value

        verification_code = self.verification_code

        connection_path: str | Unset | None
        if isinstance(self.connection_path, Unset):
            connection_path = UNSET
        else:
            connection_path = self.connection_path

        environment_id: str | Unset | None
        if isinstance(self.environment_id, Unset):
            environment_id = UNSET
        else:
            environment_id = self.environment_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "state": state,
                "verification_code": verification_code,
            }
        )
        if connection_path is not UNSET:
            field_dict["connection_path"] = connection_path
        if environment_id is not UNSET:
            field_dict["environment_id"] = environment_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        state = ClaimResultState(d.pop("state"))

        verification_code = d.pop("verification_code")

        def _parse_connection_path(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        connection_path = _parse_connection_path(d.pop("connection_path", UNSET))

        def _parse_environment_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        environment_id = _parse_environment_id(d.pop("environment_id", UNSET))

        claim_result = cls(
            state=state,
            verification_code=verification_code,
            connection_path=connection_path,
            environment_id=environment_id,
        )

        claim_result.additional_properties = d
        return claim_result

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
