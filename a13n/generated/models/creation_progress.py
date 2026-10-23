from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.creation_progress_stage import CreationProgressStage
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreationProgress")


@_attrs_define(repr=False)
class CreationProgress:
    """
    Attributes:
        observed_at (datetime.datetime):
        stage (CreationProgressStage):
        started_at (datetime.datetime):
        ended_at (datetime.datetime | None | Unset):
        retryable (bool | Unset):
    """

    observed_at: datetime.datetime
    stage: CreationProgressStage
    started_at: datetime.datetime
    ended_at: datetime.datetime | Unset | None = UNSET
    retryable: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        observed_at = self.observed_at.isoformat()

        stage = self.stage.value

        started_at = self.started_at.isoformat()

        ended_at: str | Unset | None
        if isinstance(self.ended_at, Unset):
            ended_at = UNSET
        elif isinstance(self.ended_at, datetime.datetime):
            ended_at = self.ended_at.isoformat()
        else:
            ended_at = self.ended_at

        retryable = self.retryable

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "observed_at": observed_at,
                "stage": stage,
                "started_at": started_at,
            }
        )
        if ended_at is not UNSET:
            field_dict["ended_at"] = ended_at
        if retryable is not UNSET:
            field_dict["retryable"] = retryable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        observed_at = datetime.datetime.fromisoformat(d.pop("observed_at"))

        stage = CreationProgressStage(d.pop("stage"))

        started_at = datetime.datetime.fromisoformat(d.pop("started_at"))

        def _parse_ended_at(data: object) -> datetime.datetime | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                ended_at_type_0 = datetime.datetime.fromisoformat(data)

                return ended_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | Unset | None, data)

        ended_at = _parse_ended_at(d.pop("ended_at", UNSET))

        retryable = d.pop("retryable", UNSET)

        creation_progress = cls(
            observed_at=observed_at,
            stage=stage,
            started_at=started_at,
            ended_at=ended_at,
            retryable=retryable,
        )

        creation_progress.additional_properties = d
        return creation_progress

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
