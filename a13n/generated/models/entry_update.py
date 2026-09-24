from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.delivery import Delivery
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.message_payload import MessagePayload
    from ..models.run_options_input import RunOptionsInput


T = TypeVar("T", bound="EntryUpdate")


@_attrs_define(repr=False)
class EntryUpdate:
    """Pending entries only; the original request digest never changes.

    Attributes:
        agent_revision_id (None | str | Unset):
        delivery (Delivery | None | Unset):
        options (None | RunOptionsInput | Unset):
        payload (MessagePayload | None | Unset):
    """

    agent_revision_id: str | Unset | None = UNSET
    delivery: Delivery | Unset | None = UNSET
    options: RunOptionsInput | Unset | None = UNSET
    payload: MessagePayload | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.message_payload import MessagePayload
        from ..models.run_options_input import RunOptionsInput

        agent_revision_id: str | Unset | None
        if isinstance(self.agent_revision_id, Unset):
            agent_revision_id = UNSET
        else:
            agent_revision_id = self.agent_revision_id

        delivery: str | Unset | None
        if isinstance(self.delivery, Unset):
            delivery = UNSET
        elif isinstance(self.delivery, Delivery):
            delivery = self.delivery.value
        else:
            delivery = self.delivery

        options: dict[str, Any] | Unset | None
        if isinstance(self.options, Unset):
            options = UNSET
        elif isinstance(self.options, RunOptionsInput):
            options = self.options.to_dict()
        else:
            options = self.options

        payload: dict[str, Any] | Unset | None
        if isinstance(self.payload, Unset):
            payload = UNSET
        elif isinstance(self.payload, MessagePayload):
            payload = self.payload.to_dict()
        else:
            payload = self.payload

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if agent_revision_id is not UNSET:
            field_dict["agent_revision_id"] = agent_revision_id
        if delivery is not UNSET:
            field_dict["delivery"] = delivery
        if options is not UNSET:
            field_dict["options"] = options
        if payload is not UNSET:
            field_dict["payload"] = payload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_payload import MessagePayload
        from ..models.run_options_input import RunOptionsInput

        d = dict(src_dict)

        def _parse_agent_revision_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        agent_revision_id = _parse_agent_revision_id(d.pop("agent_revision_id", UNSET))

        def _parse_delivery(data: object) -> Delivery | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                delivery_type_0 = Delivery(data)

                return delivery_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Delivery | Unset | None, data)

        delivery = _parse_delivery(d.pop("delivery", UNSET))

        def _parse_options(data: object) -> RunOptionsInput | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                options_type_0 = RunOptionsInput.from_dict(data)

                return options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(RunOptionsInput | Unset | None, data)

        options = _parse_options(d.pop("options", UNSET))

        def _parse_payload(data: object) -> MessagePayload | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payload_type_0 = MessagePayload.from_dict(data)

                return payload_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MessagePayload | Unset | None, data)

        payload = _parse_payload(d.pop("payload", UNSET))

        entry_update = cls(
            agent_revision_id=agent_revision_id,
            delivery=delivery,
            options=options,
            payload=payload,
        )

        return entry_update
