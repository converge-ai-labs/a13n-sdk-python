from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.provider_connectivity_status import ProviderConnectivityStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ProviderConnectivity")


@_attrs_define(repr=False)
class ProviderConnectivity:
    """
    Attributes:
        status (ProviderConnectivityStatus):
        error (None | str | Unset):
    """

    status: ProviderConnectivityStatus
    error: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        error: str | Unset | None
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "status": status,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = ProviderConnectivityStatus(d.pop("status"))

        def _parse_error(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        error = _parse_error(d.pop("error", UNSET))

        provider_connectivity = cls(
            status=status,
            error=error,
        )

        return provider_connectivity
