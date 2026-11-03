from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..._validation import validate_model
from ..models.control_control import ControlControl

T = TypeVar("T", bound="Control")


@_attrs_define(repr=False)
class Control:
    """
    Attributes:
        control (ControlControl):
        controller_id (None | str):
        controller_thread_id (None | str):
        episode (int):
        expires_at (datetime.datetime | None):
        failure (None | str):
        generation (int):
        id (str):
        version (int):
    """

    control: ControlControl
    controller_id: str | None
    controller_thread_id: str | None
    episode: int
    expires_at: datetime.datetime | None
    failure: str | None
    generation: int
    id: str
    version: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        control = self.control.value

        controller_id: str | None
        controller_id = self.controller_id

        controller_thread_id: str | None
        controller_thread_id = self.controller_thread_id

        episode = self.episode

        expires_at: str | None
        if isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at

        failure: str | None
        failure = self.failure

        generation = self.generation

        id = self.id

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "control": control,
                "controller_id": controller_id,
                "controller_thread_id": controller_thread_id,
                "episode": episode,
                "expires_at": expires_at,
                "failure": failure,
                "generation": generation,
                "id": id,
                "version": version,
            }
        )

        validate_model("Control", field_dict)
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        validate_model("Control", src_dict)
        d = dict(src_dict)
        control = ControlControl(d.pop("control"))

        def _parse_controller_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        controller_id = _parse_controller_id(d.pop("controller_id"))

        def _parse_controller_thread_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        controller_thread_id = _parse_controller_thread_id(d.pop("controller_thread_id"))

        episode = d.pop("episode")

        def _parse_expires_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = datetime.datetime.fromisoformat(data)

                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        expires_at = _parse_expires_at(d.pop("expires_at"))

        def _parse_failure(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        failure = _parse_failure(d.pop("failure"))

        generation = d.pop("generation")

        id = d.pop("id")

        version = d.pop("version")

        control = cls(
            control=control,
            controller_id=controller_id,
            controller_thread_id=controller_thread_id,
            episode=episode,
            expires_at=expires_at,
            failure=failure,
            generation=generation,
            id=id,
            version=version,
        )

        control.additional_properties = d
        return control

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
