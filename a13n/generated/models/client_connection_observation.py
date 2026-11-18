from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.client_connection_observation_state import ClientConnectionObservationState

T = TypeVar("T", bound="ClientConnectionObservation")


@_attrs_define(repr=False)
class ClientConnectionObservation:
    """
    Attributes:
        observed_at (datetime.datetime):
        state (ClientConnectionObservationState):
    """

    observed_at: datetime.datetime
    state: ClientConnectionObservationState
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        observed_at = self.observed_at.isoformat()

        state = self.state.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "observed_at": observed_at,
                "state": state,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        observed_at = datetime.datetime.fromisoformat(d.pop("observed_at"))

        state = ClientConnectionObservationState(d.pop("state"))

        client_connection_observation = cls(
            observed_at=observed_at,
            state=state,
        )

        client_connection_observation.additional_properties = d
        return client_connection_observation

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
