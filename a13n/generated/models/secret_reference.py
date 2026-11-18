from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="SecretReference")


@_attrs_define(repr=False)
class SecretReference:
    """
    Attributes:
        credential_id (str):
        env (str):
        inject_hosts (list[str]):
    """

    credential_id: str
    env: str
    inject_hosts: list[str]

    def to_dict(self) -> dict[str, Any]:
        credential_id = self.credential_id

        env = self.env

        inject_hosts = self.inject_hosts

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "credential_id": credential_id,
                "env": env,
                "inject_hosts": inject_hosts,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        credential_id = d.pop("credential_id")

        env = d.pop("env")

        inject_hosts = cast(list[str], d.pop("inject_hosts"))

        secret_reference = cls(
            credential_id=credential_id,
            env=env,
            inject_hosts=inject_hosts,
        )

        return secret_reference
