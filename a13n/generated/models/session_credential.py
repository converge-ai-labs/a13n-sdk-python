from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.application_status import ApplicationStatus
from ..models.session_credential_credential_state import SessionCredentialCredentialState
from ..types import UNSET, Unset

T = TypeVar("T", bound="SessionCredential")


@_attrs_define(repr=False)
class SessionCredential:
    """
    Attributes:
        applied_at (datetime.datetime | None):
        applied_credential_version (int | None):
        applied_device_generation (None | str):
        applied_session_id (None | str):
        binding_name (str):
        credential_id (str):
        credential_name (str):
        credential_state (SessionCredentialCredentialState):
        credential_version (int):
        env (str):
        environment_id (str):
        environment_name (str):
        execution_active (bool):
        inject_hosts (list[str]):
        native_session_id (None | str):
        session_version (int):
        status (ApplicationStatus):
        thread_id (str):
        error_code (None | str | Unset):
        retry_at (datetime.datetime | None | Unset):
    """

    applied_at: datetime.datetime | None
    applied_credential_version: int | None
    applied_device_generation: str | None
    applied_session_id: str | None
    binding_name: str
    credential_id: str
    credential_name: str
    credential_state: SessionCredentialCredentialState
    credential_version: int
    env: str
    environment_id: str
    environment_name: str
    execution_active: bool
    inject_hosts: list[str]
    native_session_id: str | None
    session_version: int
    status: ApplicationStatus
    thread_id: str
    error_code: str | Unset | None = UNSET
    retry_at: datetime.datetime | Unset | None = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        applied_at: str | None
        if isinstance(self.applied_at, datetime.datetime):
            applied_at = self.applied_at.isoformat()
        else:
            applied_at = self.applied_at

        applied_credential_version: int | None
        applied_credential_version = self.applied_credential_version

        applied_device_generation: str | None
        applied_device_generation = self.applied_device_generation

        applied_session_id: str | None
        applied_session_id = self.applied_session_id

        binding_name = self.binding_name

        credential_id = self.credential_id

        credential_name = self.credential_name

        credential_state = self.credential_state.value

        credential_version = self.credential_version

        env = self.env

        environment_id = self.environment_id

        environment_name = self.environment_name

        execution_active = self.execution_active

        inject_hosts = self.inject_hosts

        native_session_id: str | None
        native_session_id = self.native_session_id

        session_version = self.session_version

        status = self.status.value

        thread_id = self.thread_id

        error_code: str | Unset | None
        if isinstance(self.error_code, Unset):
            error_code = UNSET
        else:
            error_code = self.error_code

        retry_at: str | Unset | None
        if isinstance(self.retry_at, Unset):
            retry_at = UNSET
        elif isinstance(self.retry_at, datetime.datetime):
            retry_at = self.retry_at.isoformat()
        else:
            retry_at = self.retry_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "applied_at": applied_at,
                "applied_credential_version": applied_credential_version,
                "applied_device_generation": applied_device_generation,
                "applied_session_id": applied_session_id,
                "binding_name": binding_name,
                "credential_id": credential_id,
                "credential_name": credential_name,
                "credential_state": credential_state,
                "credential_version": credential_version,
                "env": env,
                "environment_id": environment_id,
                "environment_name": environment_name,
                "execution_active": execution_active,
                "inject_hosts": inject_hosts,
                "native_session_id": native_session_id,
                "session_version": session_version,
                "status": status,
                "thread_id": thread_id,
            }
        )
        if error_code is not UNSET:
            field_dict["error_code"] = error_code
        if retry_at is not UNSET:
            field_dict["retry_at"] = retry_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_applied_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                applied_at_type_0 = datetime.datetime.fromisoformat(data)

                return applied_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        applied_at = _parse_applied_at(d.pop("applied_at"))

        def _parse_applied_credential_version(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        applied_credential_version = _parse_applied_credential_version(d.pop("applied_credential_version"))

        def _parse_applied_device_generation(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        applied_device_generation = _parse_applied_device_generation(d.pop("applied_device_generation"))

        def _parse_applied_session_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        applied_session_id = _parse_applied_session_id(d.pop("applied_session_id"))

        binding_name = d.pop("binding_name")

        credential_id = d.pop("credential_id")

        credential_name = d.pop("credential_name")

        credential_state = SessionCredentialCredentialState(d.pop("credential_state"))

        credential_version = d.pop("credential_version")

        env = d.pop("env")

        environment_id = d.pop("environment_id")

        environment_name = d.pop("environment_name")

        execution_active = d.pop("execution_active")

        inject_hosts = cast(list[str], d.pop("inject_hosts"))

        def _parse_native_session_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        native_session_id = _parse_native_session_id(d.pop("native_session_id"))

        session_version = d.pop("session_version")

        status = ApplicationStatus(d.pop("status"))

        thread_id = d.pop("thread_id")

        def _parse_error_code(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        error_code = _parse_error_code(d.pop("error_code", UNSET))

        def _parse_retry_at(data: object) -> datetime.datetime | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                retry_at_type_0 = datetime.datetime.fromisoformat(data)

                return retry_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | Unset | None, data)

        retry_at = _parse_retry_at(d.pop("retry_at", UNSET))

        session_credential = cls(
            applied_at=applied_at,
            applied_credential_version=applied_credential_version,
            applied_device_generation=applied_device_generation,
            applied_session_id=applied_session_id,
            binding_name=binding_name,
            credential_id=credential_id,
            credential_name=credential_name,
            credential_state=credential_state,
            credential_version=credential_version,
            env=env,
            environment_id=environment_id,
            environment_name=environment_name,
            execution_active=execution_active,
            inject_hosts=inject_hosts,
            native_session_id=native_session_id,
            session_version=session_version,
            status=status,
            thread_id=thread_id,
            error_code=error_code,
            retry_at=retry_at,
        )

        session_credential.additional_properties = d
        return session_credential

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
