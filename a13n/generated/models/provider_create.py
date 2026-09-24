from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.provider_create_config import ProviderCreateConfig
    from ..models.provider_create_credential_type_0 import ProviderCreateCredentialType0
    from ..models.provider_create_extra_headers import ProviderCreateExtraHeaders


T = TypeVar("T", bound="ProviderCreate")


@_attrs_define(repr=False)
class ProviderCreate:
    """
    Attributes:
        name (str):
        type_ (str):
        workspace_id (None | str):
        config (ProviderCreateConfig | Unset):
        credential (None | ProviderCreateCredentialType0 | Unset):
        enabled (bool | Unset):
        extra_headers (ProviderCreateExtraHeaders | Unset):
    """

    name: str
    type_: str
    workspace_id: str | None
    config: ProviderCreateConfig | Unset = UNSET
    credential: ProviderCreateCredentialType0 | Unset | None = UNSET
    enabled: bool | Unset = UNSET
    extra_headers: ProviderCreateExtraHeaders | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.provider_create_credential_type_0 import ProviderCreateCredentialType0

        name = self.name

        type_ = self.type_

        workspace_id: str | None
        workspace_id = self.workspace_id

        config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.config, Unset):
            config = self.config.to_dict()

        credential: dict[str, Any] | Unset | None
        if isinstance(self.credential, Unset):
            credential = UNSET
        elif isinstance(self.credential, ProviderCreateCredentialType0):
            credential = self.credential.to_dict()
        else:
            credential = self.credential

        enabled = self.enabled

        extra_headers: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extra_headers, Unset):
            extra_headers = self.extra_headers.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "type": type_,
                "workspace_id": workspace_id,
            }
        )
        if config is not UNSET:
            field_dict["config"] = config
        if credential is not UNSET:
            field_dict["credential"] = credential
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if extra_headers is not UNSET:
            field_dict["extra_headers"] = extra_headers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider_create_config import ProviderCreateConfig
        from ..models.provider_create_credential_type_0 import ProviderCreateCredentialType0
        from ..models.provider_create_extra_headers import ProviderCreateExtraHeaders

        d = dict(src_dict)
        name = d.pop("name")

        type_ = d.pop("type")

        def _parse_workspace_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        workspace_id = _parse_workspace_id(d.pop("workspace_id"))

        _config = d.pop("config", UNSET)
        config: ProviderCreateConfig | Unset
        if isinstance(_config, Unset):
            config = UNSET
        else:
            config = ProviderCreateConfig.from_dict(_config)

        def _parse_credential(data: object) -> ProviderCreateCredentialType0 | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                credential_type_0 = ProviderCreateCredentialType0.from_dict(data)

                return credential_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ProviderCreateCredentialType0 | Unset | None, data)

        credential = _parse_credential(d.pop("credential", UNSET))

        enabled = d.pop("enabled", UNSET)

        _extra_headers = d.pop("extra_headers", UNSET)
        extra_headers: ProviderCreateExtraHeaders | Unset
        if isinstance(_extra_headers, Unset):
            extra_headers = UNSET
        else:
            extra_headers = ProviderCreateExtraHeaders.from_dict(_extra_headers)

        provider_create = cls(
            name=name,
            type_=type_,
            workspace_id=workspace_id,
            config=config,
            credential=credential,
            enabled=enabled,
            extra_headers=extra_headers,
        )

        return provider_create
