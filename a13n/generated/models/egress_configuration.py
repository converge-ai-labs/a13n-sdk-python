from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.allowlist_destinations import AllowlistDestinations
    from ..models.public_destinations import PublicDestinations
    from ..models.secret_reference import SecretReference


T = TypeVar("T", bound="EgressConfiguration")


@_attrs_define(repr=False)
class EgressConfiguration:
    """
    Attributes:
        destinations (AllowlistDestinations | PublicDestinations):
        secrets (list[SecretReference] | Unset):
    """

    destinations: AllowlistDestinations | PublicDestinations
    secrets: list[SecretReference] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.public_destinations import PublicDestinations

        destinations: dict[str, Any]
        if isinstance(self.destinations, PublicDestinations):
            destinations = self.destinations.to_dict()
        else:
            destinations = self.destinations.to_dict()

        secrets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.secrets, Unset):
            secrets = []
            for secrets_item_data in self.secrets:
                secrets_item = secrets_item_data.to_dict()
                secrets.append(secrets_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "destinations": destinations,
            }
        )
        if secrets is not UNSET:
            field_dict["secrets"] = secrets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.allowlist_destinations import AllowlistDestinations
        from ..models.public_destinations import PublicDestinations
        from ..models.secret_reference import SecretReference

        d = dict(src_dict)

        def _parse_destinations(data: object) -> AllowlistDestinations | PublicDestinations:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_egress_destinations_type_0 = PublicDestinations.from_dict(data)

                return componentsschemas_egress_destinations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_egress_destinations_type_1 = AllowlistDestinations.from_dict(data)

            return componentsschemas_egress_destinations_type_1

        destinations = _parse_destinations(d.pop("destinations"))

        _secrets = d.pop("secrets", UNSET)
        secrets: list[SecretReference] | Unset = UNSET
        if _secrets is not UNSET:
            secrets = []
            for secrets_item_data in _secrets:
                secrets_item = SecretReference.from_dict(secrets_item_data)

                secrets.append(secrets_item)

        egress_configuration = cls(
            destinations=destinations,
            secrets=secrets,
        )

        return egress_configuration
