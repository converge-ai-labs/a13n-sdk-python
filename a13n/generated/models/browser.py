from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.browser_source import BrowserSource
from ..models.browser_status import BrowserStatus
from ..models.control_status import ControlStatus

T = TypeVar("T", bound="Browser")


@_attrs_define(repr=False)
class Browser:
    """
    Attributes:
        control (ControlStatus):
        control_expires_at (datetime.datetime | None):
        created_at (datetime.datetime):
        episode (int):
        expires_at (datetime.datetime | None):
        failure (None | str):
        generation (int):
        id (str):
        idle_seconds (int | None):
        name (str):
        organization_id (str):
        provider_id (None | str):
        source (BrowserSource):
        status (BrowserStatus):
        updated_at (datetime.datetime):
        version (int):
        workspace_id (str):
    """

    control: ControlStatus
    control_expires_at: datetime.datetime | None
    created_at: datetime.datetime
    episode: int
    expires_at: datetime.datetime | None
    failure: str | None
    generation: int
    id: str
    idle_seconds: int | None
    name: str
    organization_id: str
    provider_id: str | None
    source: BrowserSource
    status: BrowserStatus
    updated_at: datetime.datetime
    version: int
    workspace_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        control = self.control.value

        control_expires_at: str | None
        if isinstance(self.control_expires_at, datetime.datetime):
            control_expires_at = self.control_expires_at.isoformat()
        else:
            control_expires_at = self.control_expires_at

        created_at = self.created_at.isoformat()

        episode = self.episode

        expires_at: str | None
        if isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        failure: str | None
        failure = self.failure

        generation = self.generation

        id = self.id

        idle_seconds: int | None
        idle_seconds = self.idle_seconds

        name = self.name

        organization_id = self.organization_id

        provider_id: str | None
        provider_id = self.provider_id

        source = self.source.value

        status = self.status.value

        updated_at = self.updated_at.isoformat()

        version = self.version

        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "control": control,
                "control_expires_at": control_expires_at,
                "created_at": created_at,
                "episode": episode,
                "expires_at": expires_at,
                "failure": failure,
                "generation": generation,
                "id": id,
                "idle_seconds": idle_seconds,
                "name": name,
                "organization_id": organization_id,
                "provider_id": provider_id,
                "source": source,
                "status": status,
                "updated_at": updated_at,
                "version": version,
                "workspace_id": workspace_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        control = ControlStatus(d.pop("control"))

        def _parse_control_expires_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                control_expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return control_expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        control_expires_at = _parse_control_expires_at(d.pop("control_expires_at"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        episode = d.pop("episode")

        def _parse_expires_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        expires_at = _parse_expires_at(d.pop("expires_at"))

        def _parse_failure(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        failure = _parse_failure(d.pop("failure"))

        generation = d.pop("generation")

        id = d.pop("id")

        def _parse_idle_seconds(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        idle_seconds = _parse_idle_seconds(d.pop("idle_seconds"))

        name = d.pop("name")

        organization_id = d.pop("organization_id")

        def _parse_provider_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        provider_id = _parse_provider_id(d.pop("provider_id"))

        source = BrowserSource(d.pop("source"))

        status = BrowserStatus(d.pop("status"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        version = d.pop("version")

        workspace_id = d.pop("workspace_id")

        browser = cls(
            control=control,
            control_expires_at=control_expires_at,
            created_at=created_at,
            episode=episode,
            expires_at=expires_at,
            failure=failure,
            generation=generation,
            id=id,
            idle_seconds=idle_seconds,
            name=name,
            organization_id=organization_id,
            provider_id=provider_id,
            source=source,
            status=status,
            updated_at=updated_at,
            version=version,
            workspace_id=workspace_id,
        )

        browser.additional_properties = d
        return browser

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
