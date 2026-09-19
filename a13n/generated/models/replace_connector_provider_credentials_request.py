from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.replace_connector_provider_credentials_request_credentials_type_0 import (
        ReplaceConnectorProviderCredentialsRequestCredentialsType0,
    )


T = TypeVar("T", bound="ReplaceConnectorProviderCredentialsRequest")


@_attrs_define(repr=False)
class ReplaceConnectorProviderCredentialsRequest:
    """
    Attributes:
        credentials (None | ReplaceConnectorProviderCredentialsRequestCredentialsType0):
        expected_version (int):
    """

    credentials: ReplaceConnectorProviderCredentialsRequestCredentialsType0 | None
    expected_version: int

    def to_dict(self) -> dict[str, Any]:
        from ..models.replace_connector_provider_credentials_request_credentials_type_0 import (
            ReplaceConnectorProviderCredentialsRequestCredentialsType0,
        )

        credentials: dict[str, Any] | None
        if isinstance(self.credentials, ReplaceConnectorProviderCredentialsRequestCredentialsType0):
            credentials = self.credentials.to_dict()
        else:
            credentials = self.credentials

        expected_version = self.expected_version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "credentials": credentials,
                "expected_version": expected_version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.replace_connector_provider_credentials_request_credentials_type_0 import (
            ReplaceConnectorProviderCredentialsRequestCredentialsType0,
        )

        d = dict(src_dict)

        def _parse_credentials(data: object) -> ReplaceConnectorProviderCredentialsRequestCredentialsType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credentials_type_0 = ReplaceConnectorProviderCredentialsRequestCredentialsType0.from_dict(data)

                return credentials_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ReplaceConnectorProviderCredentialsRequestCredentialsType0 | None, data)

        credentials = _parse_credentials(d.pop("credentials"))

        expected_version = d.pop("expected_version")

        replace_connector_provider_credentials_request = cls(
            credentials=credentials,
            expected_version=expected_version,
        )

        return replace_connector_provider_credentials_request
