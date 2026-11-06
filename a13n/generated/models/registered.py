from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.client_environment import ClientEnvironment


T = TypeVar("T", bound="Registered")


@_attrs_define(repr=False)
class Registered:
    """
    Attributes:
        client (ClientEnvironment):
        connection_path (str):
        token (None | str | Unset):
    """

    client: ClientEnvironment
    connection_path: str
    token: str | Unset | None = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        client = self.client.to_dict()

        connection_path = self.connection_path

        token: str | Unset | None
        if isinstance(self.token, Unset):
            token = UNSET
        else:
            token = self.token

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "client": client,
                "connection_path": connection_path,
            }
        )
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.client_environment import ClientEnvironment

        d = dict(src_dict)
        client = ClientEnvironment.from_dict(d.pop("client"))

        connection_path = d.pop("connection_path")

        def _parse_token(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        token = _parse_token(d.pop("token", UNSET))

        registered = cls(
            client=client,
            connection_path=connection_path,
            token=token,
        )

        registered.additional_properties = d
        return registered

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
