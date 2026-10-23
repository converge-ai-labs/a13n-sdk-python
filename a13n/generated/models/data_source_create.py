from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.configuration import Configuration
    from ..models.credentials import Credentials


T = TypeVar("T", bound="DataSourceCreate")


@_attrs_define(repr=False)
class DataSourceCreate:
    """
    Attributes:
        config (Configuration):
        name (str):
        deployment_preset_revision (None | str | Unset):
        enabled (bool | Unset):
        export_credentials (Credentials | None | Unset):
        query_credentials (Credentials | None | Unset):
        use_deployment_query_credentials (bool | Unset):
    """

    config: Configuration
    name: str
    deployment_preset_revision: str | Unset | None = UNSET
    enabled: bool | Unset = UNSET
    export_credentials: Credentials | Unset | None = UNSET
    query_credentials: Credentials | Unset | None = UNSET
    use_deployment_query_credentials: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.credentials import Credentials

        config = self.config.to_dict()

        name = self.name

        deployment_preset_revision: str | Unset | None
        if isinstance(self.deployment_preset_revision, Unset):
            deployment_preset_revision = UNSET
        else:
            deployment_preset_revision = self.deployment_preset_revision

        enabled = self.enabled

        export_credentials: dict[str, Any] | Unset | None
        if isinstance(self.export_credentials, Unset):
            export_credentials = UNSET
        elif isinstance(self.export_credentials, Credentials):
            export_credentials = self.export_credentials.to_dict()
        else:
            export_credentials = self.export_credentials

        query_credentials: dict[str, Any] | Unset | None
        if isinstance(self.query_credentials, Unset):
            query_credentials = UNSET
        elif isinstance(self.query_credentials, Credentials):
            query_credentials = self.query_credentials.to_dict()
        else:
            query_credentials = self.query_credentials

        use_deployment_query_credentials = self.use_deployment_query_credentials

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "config": config,
                "name": name,
            }
        )
        if deployment_preset_revision is not UNSET:
            field_dict["deployment_preset_revision"] = deployment_preset_revision
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if export_credentials is not UNSET:
            field_dict["export_credentials"] = export_credentials
        if query_credentials is not UNSET:
            field_dict["query_credentials"] = query_credentials
        if use_deployment_query_credentials is not UNSET:
            field_dict["use_deployment_query_credentials"] = use_deployment_query_credentials

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.configuration import Configuration
        from ..models.credentials import Credentials

        d = dict(src_dict)
        config = Configuration.from_dict(d.pop("config"))

        name = d.pop("name")

        def _parse_deployment_preset_revision(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        deployment_preset_revision = _parse_deployment_preset_revision(d.pop("deployment_preset_revision", UNSET))

        enabled = d.pop("enabled", UNSET)

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

        use_deployment_query_credentials = d.pop("use_deployment_query_credentials", UNSET)

        data_source_create = cls(
            config=config,
            name=name,
            deployment_preset_revision=deployment_preset_revision,
            enabled=enabled,
            export_credentials=export_credentials,
            query_credentials=query_credentials,
            use_deployment_query_credentials=use_deployment_query_credentials,
        )

        return data_source_create
