from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PrincipalSummary")


@_attrs_define(repr=False)
class PrincipalSummary:
    """
    Attributes:
        email (None | str):
        id (str):
        image_url (None | str):
        kind (str):
        name (str):
        status (str):
        oidc_email (None | str | Unset):
    """

    email: str | None
    id: str
    image_url: str | None
    kind: str
    name: str
    status: str
    oidc_email: str | Unset | None = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email: str | None
        email = self.email

        id = self.id

        image_url: str | None
        image_url = self.image_url

        kind = self.kind

        name = self.name

        status = self.status

        oidc_email: str | Unset | None
        if isinstance(self.oidc_email, Unset):
            oidc_email = UNSET
        else:
            oidc_email = self.oidc_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "id": id,
                "image_url": image_url,
                "kind": kind,
                "name": name,
                "status": status,
            }
        )
        if oidc_email is not UNSET:
            field_dict["oidc_email"] = oidc_email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_email(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        email = _parse_email(d.pop("email"))

        id = d.pop("id")

        def _parse_image_url(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        image_url = _parse_image_url(d.pop("image_url"))

        kind = d.pop("kind")

        name = d.pop("name")

        status = d.pop("status")

        def _parse_oidc_email(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        oidc_email = _parse_oidc_email(d.pop("oidc_email", UNSET))

        principal_summary = cls(
            email=email,
            id=id,
            image_url=image_url,
            kind=kind,
            name=name,
            status=status,
            oidc_email=oidc_email,
        )

        principal_summary.additional_properties = d
        return principal_summary

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
