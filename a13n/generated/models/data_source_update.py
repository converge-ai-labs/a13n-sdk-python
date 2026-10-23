from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.configuration import Configuration
    from ..models.credentials import Credentials


T = TypeVar("T", bound="DataSourceUpdate")


@_attrs_define(repr=False)
class DataSourceUpdate:
    """
    Attributes:
        config (Configuration | None | Unset):
        enabled (bool | None | Unset):
        export_credentials (Credentials | None | Unset):
        name (None | str | Unset):
        query_credentials (Credentials | None | Unset):
    """

    config: Configuration | Unset | None = UNSET
    enabled: bool | Unset | None = UNSET
    export_credentials: Credentials | Unset | None = UNSET
    name: str | Unset | None = UNSET
    query_credentials: Credentials | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.configuration import Configuration
        from ..models.credentials import Credentials

        config: dict[str, Any] | Unset | None
        if isinstance(self.config, Unset):
            config = UNSET
        elif isinstance(self.config, Configuration):
            config = self.config.to_dict()
        else:
            config = self.config

        enabled: bool | Unset | None
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        export_credentials: dict[str, Any] | Unset | None
        if isinstance(self.export_credentials, Unset):
            export_credentials = UNSET
        elif isinstance(self.export_credentials, Credentials):
            export_credentials = self.export_credentials.to_dict()
        else:
            export_credentials = self.export_credentials

        name: str | Unset | None
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        query_credentials: dict[str, Any] | Unset | None
        if isinstance(self.query_credentials, Unset):
            query_credentials = UNSET
        elif isinstance(self.query_credentials, Credentials):
            query_credentials = self.query_credentials.to_dict()
        else:
            query_credentials = self.query_credentials

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if config is not UNSET:
            field_dict["config"] = config
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if export_credentials is not UNSET:
            field_dict["export_credentials"] = export_credentials
        if name is not UNSET:
            field_dict["name"] = name
        if query_credentials is not UNSET:
            field_dict["query_credentials"] = query_credentials

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.configuration import Configuration
        from ..models.credentials import Credentials

        d = dict(src_dict)

        def _parse_config(data: object) -> Configuration | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                config_type_0 = Configuration.from_dict(data)

                return config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Configuration | Unset | None, data)

        config = _parse_config(d.pop("config", UNSET))

        def _parse_enabled(data: object) -> bool | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | Unset | None, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        def _parse_export_credentials(data: object) -> Credentials | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                export_credentials_type_0 = Credentials.from_dict(data)

                return export_credentials_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Credentials | Unset | None, data)

        export_credentials = _parse_export_credentials(d.pop("export_credentials", UNSET))

        def _parse_name(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_query_credentials(data: object) -> Credentials | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                query_credentials_type_0 = Credentials.from_dict(data)

                return query_credentials_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Credentials | Unset | None, data)

        query_credentials = _parse_query_credentials(d.pop("query_credentials", UNSET))

        data_source_update = cls(
            config=config,
            enabled=enabled,
            export_credentials=export_credentials,
            name=name,
            query_credentials=query_credentials,
        )

        return data_source_update
