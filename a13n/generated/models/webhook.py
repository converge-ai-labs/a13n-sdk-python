from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="Webhook")


@_attrs_define(repr=False)
class Webhook:
    """
    Attributes:
        configured (bool):
        failure (None | str):
        operation (None | str):
        provider_id (str):
        remote_id (None | str):
        retryable (bool):
        secret_version (int):
        url (None | str):
        version (int):
    """

    configured: bool
    failure: str | None
    operation: str | None
    provider_id: str
    remote_id: str | None
    retryable: bool
    secret_version: int
    url: str | None
    version: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        configured = self.configured

        failure: str | None
        failure = self.failure

        operation: str | None
        operation = self.operation

        provider_id = self.provider_id

        remote_id: str | None
        remote_id = self.remote_id

        retryable = self.retryable

        secret_version = self.secret_version

        url: str | None
        url = self.url

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "configured": configured,
                "failure": failure,
                "operation": operation,
                "provider_id": provider_id,
                "remote_id": remote_id,
                "retryable": retryable,
                "secret_version": secret_version,
                "url": url,
                "version": version,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        configured = d.pop("configured")

        def _parse_failure(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        failure = _parse_failure(d.pop("failure"))

        def _parse_operation(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        operation = _parse_operation(d.pop("operation"))

        provider_id = d.pop("provider_id")

        def _parse_remote_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        remote_id = _parse_remote_id(d.pop("remote_id"))

        retryable = d.pop("retryable")

        secret_version = d.pop("secret_version")

        def _parse_url(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        url = _parse_url(d.pop("url"))

        version = d.pop("version")

        webhook = cls(
            configured=configured,
            failure=failure,
            operation=operation,
            provider_id=provider_id,
            remote_id=remote_id,
            retryable=retryable,
            secret_version=secret_version,
            url=url,
            version=version,
        )

        webhook.additional_properties = d
        return webhook

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
