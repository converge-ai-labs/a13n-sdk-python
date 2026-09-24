from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.client_authentication import ClientAuthentication
from ..models.o_auth_grant import OAuthGrant
from ..types import UNSET, Unset

T = TypeVar("T", bound="OAuthSettings")


@_attrs_define(repr=False)
class OAuthSettings:
    """
    Attributes:
        client_id (None | str | Unset):
        grant_type (OAuthGrant | Unset):
        scopes (list[str] | Unset):
        token_endpoint_auth_method (ClientAuthentication | Unset):
    """

    client_id: str | Unset | None = UNSET
    grant_type: OAuthGrant | Unset = UNSET
    scopes: list[str] | Unset = UNSET
    token_endpoint_auth_method: ClientAuthentication | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        client_id: str | Unset | None
        if isinstance(self.client_id, Unset):
            client_id = UNSET
        else:
            client_id = self.client_id

        grant_type: str | Unset = UNSET
        if not isinstance(self.grant_type, Unset):
            grant_type = self.grant_type.value

        scopes: list[str] | Unset = UNSET
        if not isinstance(self.scopes, Unset):
            scopes = self.scopes

        token_endpoint_auth_method: str | Unset = UNSET
        if not isinstance(self.token_endpoint_auth_method, Unset):
            token_endpoint_auth_method = self.token_endpoint_auth_method.value

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if client_id is not UNSET:
            field_dict["client_id"] = client_id
        if grant_type is not UNSET:
            field_dict["grant_type"] = grant_type
        if scopes is not UNSET:
            field_dict["scopes"] = scopes
        if token_endpoint_auth_method is not UNSET:
            field_dict["token_endpoint_auth_method"] = token_endpoint_auth_method

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_client_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        client_id = _parse_client_id(d.pop("client_id", UNSET))

        _grant_type = d.pop("grant_type", UNSET)
        grant_type: OAuthGrant | Unset
        if isinstance(_grant_type, Unset):
            grant_type = UNSET
        else:
            grant_type = OAuthGrant(_grant_type)

        scopes = cast(list[str], d.pop("scopes", UNSET))

        _token_endpoint_auth_method = d.pop("token_endpoint_auth_method", UNSET)
        token_endpoint_auth_method: ClientAuthentication | Unset
        if isinstance(_token_endpoint_auth_method, Unset):
            token_endpoint_auth_method = UNSET
        else:
            token_endpoint_auth_method = ClientAuthentication(_token_endpoint_auth_method)

        o_auth_settings = cls(
            client_id=client_id,
            grant_type=grant_type,
            scopes=scopes,
            token_endpoint_auth_method=token_endpoint_auth_method,
        )

        return o_auth_settings
