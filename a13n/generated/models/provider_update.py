from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.provider_update_config_type_0 import ProviderUpdateConfigType0
    from ..models.provider_update_credential_type_0 import ProviderUpdateCredentialType0
    from ..models.provider_update_extra_headers import ProviderUpdateExtraHeaders


T = TypeVar("T", bound="ProviderUpdate")


@_attrs_define(repr=False)
class ProviderUpdate:
    """
    Attributes:
        config (None | ProviderUpdateConfigType0 | Unset):
        credential (None | ProviderUpdateCredentialType0 | Unset):
        enabled (bool | None | Unset):
        extra_headers (ProviderUpdateExtraHeaders | Unset):
        name (None | str | Unset):
    """

    config: ProviderUpdateConfigType0 | Unset | None = UNSET
    credential: ProviderUpdateCredentialType0 | Unset | None = UNSET
    enabled: bool | Unset | None = UNSET
    extra_headers: ProviderUpdateExtraHeaders | Unset = UNSET
    name: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.provider_update_config_type_0 import ProviderUpdateConfigType0
        from ..models.provider_update_credential_type_0 import ProviderUpdateCredentialType0

        config: dict[str, Any] | Unset | None
        if isinstance(self.config, Unset):
            config = UNSET
        elif isinstance(self.config, ProviderUpdateConfigType0):
            config = self.config.to_dict()
        else:
            config = self.config

        credential: dict[str, Any] | Unset | None
        if isinstance(self.credential, Unset):
            credential = UNSET
        elif isinstance(self.credential, ProviderUpdateCredentialType0):
            credential = self.credential.to_dict()
        else:
            credential = self.credential

        enabled: bool | Unset | None
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        extra_headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extra_headers, Unset):
            extra_headers = self.extra_headers.to_dict()

        name: str | Unset | None
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if credential is not UNSET:
            field_dict["credential"] = credential
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if extra_headers is not UNSET:
            field_dict["extra_headers"] = extra_headers
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider_update_config_type_0 import ProviderUpdateConfigType0
        from ..models.provider_update_credential_type_0 import ProviderUpdateCredentialType0
        from ..models.provider_update_extra_headers import ProviderUpdateExtraHeaders

        d = dict(src_dict)

        def _parse_config(data: object) -> ProviderUpdateConfigType0 | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0 = ProviderUpdateConfigType0.from_dict(data)

                return config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ProviderUpdateConfigType0 | Unset | None, data)

        config = _parse_config(d.pop("config", UNSET))

        def _parse_credential(data: object) -> ProviderUpdateCredentialType0 | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credential_type_0 = ProviderUpdateCredentialType0.from_dict(data)

                return credential_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ProviderUpdateCredentialType0 | Unset | None, data)

        credential = _parse_credential(d.pop("credential", UNSET))

        def _parse_enabled(data: object) -> bool | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | Unset | None, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        _extra_headers = d.pop("extra_headers", UNSET)
        extra_headers: ProviderUpdateExtraHeaders | Unset
        if isinstance(_extra_headers, Unset):
            extra_headers = UNSET
        else:
            extra_headers = ProviderUpdateExtraHeaders.from_dict(_extra_headers)

        def _parse_name(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        name = _parse_name(d.pop("name", UNSET))

        provider_update = cls(
            config=config,
            credential=credential,
            enabled=enabled,
            extra_headers=extra_headers,
            name=name,
        )

        return provider_update
