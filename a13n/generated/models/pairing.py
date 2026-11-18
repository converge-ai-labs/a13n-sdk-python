from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.pairing_state import PairingState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.device_claim import DeviceClaim


T = TypeVar("T", bound="Pairing")


@_attrs_define(repr=False)
class Pairing:
    """
    Attributes:
        expires_at (datetime.datetime):
        host_name (str):
        id (str):
        owner_id (str):
        service_url (str):
        workspace_id (str):
        device (DeviceClaim | None | Unset):
        environment_id (None | str | Unset):
        reused (bool | Unset):
        state (PairingState | Unset):
        verification_code (None | str | Unset):
    """

    expires_at: datetime.datetime
    host_name: str
    id: str
    owner_id: str
    service_url: str
    workspace_id: str
    device: DeviceClaim | Unset | None = UNSET
    environment_id: str | Unset | None = UNSET
    reused: bool | Unset = UNSET
    state: PairingState | Unset = UNSET
    verification_code: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.device_claim import DeviceClaim

        expires_at = self.expires_at.isoformat()

        host_name = self.host_name

        id = self.id

        owner_id = self.owner_id

        service_url = self.service_url

        workspace_id = self.workspace_id

        device: dict[str, Any] | Unset | None
        if isinstance(self.device, Unset):
            device = UNSET
        elif isinstance(self.device, DeviceClaim):
            device = self.device.to_dict()
        else:
            device = self.device

        environment_id: str | Unset | None
        if isinstance(self.environment_id, Unset):
            environment_id = UNSET
        else:
            environment_id = self.environment_id

        reused = self.reused

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        verification_code: str | Unset | None
        if isinstance(self.verification_code, Unset):
            verification_code = UNSET
        else:
            verification_code = self.verification_code

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "expires_at": expires_at,
                "host_name": host_name,
                "id": id,
                "owner_id": owner_id,
                "service_url": service_url,
                "workspace_id": workspace_id,
            }
        )
        if device is not UNSET:
            field_dict["device"] = device
        if environment_id is not UNSET:
            field_dict["environment_id"] = environment_id
        if reused is not UNSET:
            field_dict["reused"] = reused
        if state is not UNSET:
            field_dict["state"] = state
        if verification_code is not UNSET:
            field_dict["verification_code"] = verification_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.device_claim import DeviceClaim

        d = dict(src_dict)
        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        host_name = d.pop("host_name")

        id = d.pop("id")

        owner_id = d.pop("owner_id")

        service_url = d.pop("service_url")

        workspace_id = d.pop("workspace_id")

        def _parse_device(data: object) -> DeviceClaim | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                device_type_0 = DeviceClaim.from_dict(data)

                return device_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DeviceClaim | Unset | None, data)

        device = _parse_device(d.pop("device", UNSET))

        def _parse_environment_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        environment_id = _parse_environment_id(d.pop("environment_id", UNSET))

        reused = d.pop("reused", UNSET)

        _state = d.pop("state", UNSET)
        state: PairingState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = PairingState(_state)

        def _parse_verification_code(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        verification_code = _parse_verification_code(d.pop("verification_code", UNSET))

        pairing = cls(
            expires_at=expires_at,
            host_name=host_name,
            id=id,
            owner_id=owner_id,
            service_url=service_url,
            workspace_id=workspace_id,
            device=device,
            environment_id=environment_id,
            reused=reused,
            state=state,
            verification_code=verification_code,
        )

        return pairing
