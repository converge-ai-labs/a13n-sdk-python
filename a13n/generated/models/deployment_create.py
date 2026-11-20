from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define

T = TypeVar("T", bound="DeploymentCreate")


@_attrs_define(repr=False)
class DeploymentCreate:
    """
    Attributes:
        account_id (str):
        api_token (str):
        name (str):
        request_id (UUID):
    """

    account_id: str
    api_token: str
    name: str
    request_id: UUID

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        api_token = self.api_token

        name = self.name

        request_id = str(self.request_id)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "account_id": account_id,
                "api_token": api_token,
                "name": name,
                "request_id": request_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id")

        api_token = d.pop("api_token")

        name = d.pop("name")

        request_id = UUID(d.pop("request_id"))

        deployment_create = cls(
            account_id=account_id,
            api_token=api_token,
            name=name,
            request_id=request_id,
        )

        return deployment_create
