from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.bot_setup_reception_mode import BotSetupReceptionMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="BotSetup")


@_attrs_define(repr=False)
class BotSetup:
    """
    Attributes:
        account_id (str):
        event_path (None | str):
        event_url (None | str):
        poll_checked_at (datetime.datetime | None | Unset):
        poll_error_code (None | str | Unset):
        reception_mode (BotSetupReceptionMode | Unset):
    """

    account_id: str
    event_path: str | None
    event_url: str | None
    poll_checked_at: datetime.datetime | Unset | None = UNSET
    poll_error_code: str | Unset | None = UNSET
    reception_mode: BotSetupReceptionMode | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        event_path: str | None
        event_path = self.event_path

        event_url: str | None
        event_url = self.event_url

        poll_checked_at: str | Unset | None
        if isinstance(self.poll_checked_at, Unset):
            poll_checked_at = UNSET
        elif isinstance(self.poll_checked_at, datetime.datetime):
            poll_checked_at = self.poll_checked_at.isoformat()
        else:
            poll_checked_at = self.poll_checked_at

        poll_error_code: str | Unset | None
        if isinstance(self.poll_error_code, Unset):
            poll_error_code = UNSET
        else:
            poll_error_code = self.poll_error_code

        reception_mode: str | Unset = UNSET
        if not isinstance(self.reception_mode, Unset):
            reception_mode = self.reception_mode.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "account_id": account_id,
                "event_path": event_path,
                "event_url": event_url,
            }
        )
        if poll_checked_at is not UNSET:
            field_dict["poll_checked_at"] = poll_checked_at
        if poll_error_code is not UNSET:
            field_dict["poll_error_code"] = poll_error_code
        if reception_mode is not UNSET:
            field_dict["reception_mode"] = reception_mode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("account_id")

        def _parse_event_path(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        event_path = _parse_event_path(d.pop("event_path"))

        def _parse_event_url(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        event_url = _parse_event_url(d.pop("event_url"))

        def _parse_poll_checked_at(data: object) -> datetime.datetime | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                poll_checked_at_type_0 = datetime.datetime.fromisoformat(data)

                return poll_checked_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | Unset | None, data)

        poll_checked_at = _parse_poll_checked_at(d.pop("poll_checked_at", UNSET))

        def _parse_poll_error_code(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        poll_error_code = _parse_poll_error_code(d.pop("poll_error_code", UNSET))

        _reception_mode = d.pop("reception_mode", UNSET)
        reception_mode: BotSetupReceptionMode | Unset
        if isinstance(_reception_mode, Unset):
            reception_mode = UNSET
        else:
            reception_mode = BotSetupReceptionMode(_reception_mode)

        bot_setup = cls(
            account_id=account_id,
            event_path=event_path,
            event_url=event_url,
            poll_checked_at=poll_checked_at,
            poll_error_code=poll_error_code,
            reception_mode=reception_mode,
        )

        return bot_setup
