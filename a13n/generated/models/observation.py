from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.status import Status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.metrics_sample import MetricsSample
    from ..models.system_info import SystemInfo


T = TypeVar("T", bound="Observation")


@_attrs_define(repr=False)
class Observation:
    """
    Attributes:
        device_id (str):
        status (Status):
        age_ms (int | None | Unset):
        generation (int | None | Unset):
        last_sample_at (datetime.datetime | None | Unset):
        received_at (datetime.datetime | None | Unset):
        sample (MetricsSample | None | Unset):
        sample_interval_ms (int | None | Unset):
        system_info (None | SystemInfo | Unset):
    """

    device_id: str
    status: Status
    age_ms: int | Unset | None = UNSET
    generation: int | Unset | None = UNSET
    last_sample_at: datetime.datetime | Unset | None = UNSET
    received_at: datetime.datetime | Unset | None = UNSET
    sample: MetricsSample | Unset | None = UNSET
    sample_interval_ms: int | Unset | None = UNSET
    system_info: SystemInfo | Unset | None = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.metrics_sample import MetricsSample
        from ..models.system_info import SystemInfo

        device_id = self.device_id

        status = self.status.value

        age_ms: int | Unset | None
        if isinstance(self.age_ms, Unset):
            age_ms = UNSET
        else:
            age_ms = self.age_ms

        generation: int | Unset | None
        if isinstance(self.generation, Unset):
            generation = UNSET
        else:
            generation = self.generation

        last_sample_at: str | Unset | None
        if isinstance(self.last_sample_at, Unset):
            last_sample_at = UNSET
        elif isinstance(self.last_sample_at, datetime.datetime):
            last_sample_at = self.last_sample_at.isoformat()
        else:
            last_sample_at = self.last_sample_at

        received_at: str | Unset | None
        if isinstance(self.received_at, Unset):
            received_at = UNSET
        elif isinstance(self.received_at, datetime.datetime):
            received_at = self.received_at.isoformat()
        else:
            received_at = self.received_at

        sample: dict[str, Any] | Unset | None
        if isinstance(self.sample, Unset):
            sample = UNSET
        elif isinstance(self.sample, MetricsSample):
            sample = self.sample.to_dict()
        else:
            sample = self.sample

        sample_interval_ms: int | Unset | None
        if isinstance(self.sample_interval_ms, Unset):
            sample_interval_ms = UNSET
        else:
            sample_interval_ms = self.sample_interval_ms

        system_info: dict[str, Any] | Unset | None
        if isinstance(self.system_info, Unset):
            system_info = UNSET
        elif isinstance(self.system_info, SystemInfo):
            system_info = self.system_info.to_dict()
        else:
            system_info = self.system_info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "device_id": device_id,
                "status": status,
            }
        )
        if age_ms is not UNSET:
            field_dict["age_ms"] = age_ms
        if generation is not UNSET:
            field_dict["generation"] = generation
        if last_sample_at is not UNSET:
            field_dict["last_sample_at"] = last_sample_at
        if received_at is not UNSET:
            field_dict["received_at"] = received_at
        if sample is not UNSET:
            field_dict["sample"] = sample
        if sample_interval_ms is not UNSET:
            field_dict["sample_interval_ms"] = sample_interval_ms
        if system_info is not UNSET:
            field_dict["system_info"] = system_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metrics_sample import MetricsSample
        from ..models.system_info import SystemInfo

        d = dict(src_dict)
        device_id = d.pop("device_id")

        status = Status(d.pop("status"))

        def _parse_age_ms(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        age_ms = _parse_age_ms(d.pop("age_ms", UNSET))

        def _parse_generation(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        generation = _parse_generation(d.pop("generation", UNSET))

        def _parse_last_sample_at(data: object) -> datetime.datetime | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_sample_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_sample_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | Unset | None, data)

        last_sample_at = _parse_last_sample_at(d.pop("last_sample_at", UNSET))

        def _parse_received_at(data: object) -> datetime.datetime | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                received_at_type_0 = datetime.datetime.fromisoformat(data)

                return received_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | Unset | None, data)

        received_at = _parse_received_at(d.pop("received_at", UNSET))

        def _parse_sample(data: object) -> MetricsSample | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sample_type_0 = MetricsSample.from_dict(data)

                return sample_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MetricsSample | Unset | None, data)

        sample = _parse_sample(d.pop("sample", UNSET))

        def _parse_sample_interval_ms(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        sample_interval_ms = _parse_sample_interval_ms(d.pop("sample_interval_ms", UNSET))

        def _parse_system_info(data: object) -> SystemInfo | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                system_info_type_0 = SystemInfo.from_dict(data)

                return system_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(SystemInfo | Unset | None, data)

        system_info = _parse_system_info(d.pop("system_info", UNSET))

        observation = cls(
            device_id=device_id,
            status=status,
            age_ms=age_ms,
            generation=generation,
            last_sample_at=last_sample_at,
            received_at=received_at,
            sample=sample,
            sample_interval_ms=sample_interval_ms,
            system_info=system_info,
        )

        observation.additional_properties = d
        return observation

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
