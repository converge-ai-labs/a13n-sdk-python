from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.credential_mode import CredentialMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.authentication_case import AuthenticationCase


T = TypeVar("T", bound="Authentication")


@_attrs_define(repr=False)
class Authentication:
    """
    Attributes:
        cases (list[AuthenticationCase] | Unset):
        mode (CredentialMode | Unset):
    """

    cases: list[AuthenticationCase] | Unset = UNSET
    mode: CredentialMode | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        cases: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.cases, Unset):
            cases = []
            for cases_item_data in self.cases:
                cases_item = cases_item_data.to_dict()
                cases.append(cases_item)

        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if cases is not UNSET:
            field_dict["cases"] = cases
        if mode is not UNSET:
            field_dict["mode"] = mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.authentication_case import AuthenticationCase

        d = dict(src_dict)
        _cases = d.pop("cases", UNSET)
        cases: list[AuthenticationCase] | Unset = UNSET
        if _cases is not UNSET:
            cases = []
            for cases_item_data in _cases:
                cases_item = AuthenticationCase.from_dict(cases_item_data)

                cases.append(cases_item)

        _mode = d.pop("mode", UNSET)
        mode: CredentialMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = CredentialMode(_mode)

        authentication = cls(
            cases=cases,
            mode=mode,
        )

        return authentication
