from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.item_kind import ItemKind
from ..models.item_state import ItemState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.item_content import ItemContent


T = TypeVar("T", bound="Item")


@_attrs_define(repr=False)
class Item:
    """
    Attributes:
        content (ItemContent):
        first_stream_id (str):
        id (str):
        kind (ItemKind):
        last_stream_id (str):
        ordinal (int):
        started_at (datetime.datetime):
        state (ItemState):
        ended_at (datetime.datetime | None | Unset):
    """

    content: ItemContent
    first_stream_id: str
    id: str
    kind: ItemKind
    last_stream_id: str
    ordinal: int
    started_at: datetime.datetime
    state: ItemState
    ended_at: datetime.datetime | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        content = self.content.to_dict()

        first_stream_id = self.first_stream_id

        id = self.id

        kind = self.kind.value

        last_stream_id = self.last_stream_id

        ordinal = self.ordinal

        started_at = self.started_at.isoformat()

        state = self.state.value

        ended_at: str | Unset | None
        if isinstance(self.ended_at, Unset):
            ended_at = UNSET
        elif isinstance(self.ended_at, datetime.datetime):
            ended_at = self.ended_at.isoformat()
        else:
            ended_at = self.ended_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "content": content,
                "first_stream_id": first_stream_id,
                "id": id,
                "kind": kind,
                "last_stream_id": last_stream_id,
                "ordinal": ordinal,
                "started_at": started_at,
                "state": state,
            }
        )
        if ended_at is not UNSET:
            field_dict["ended_at"] = ended_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.item_content import ItemContent

        d = dict(src_dict)
        content = ItemContent.from_dict(d.pop("content"))

        first_stream_id = d.pop("first_stream_id")

        id = d.pop("id")

        kind = ItemKind(d.pop("kind"))

        last_stream_id = d.pop("last_stream_id")

        ordinal = d.pop("ordinal")

        started_at = datetime.datetime.fromisoformat(d.pop("started_at"))

        state = ItemState(d.pop("state"))

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

        item = cls(
            content=content,
            first_stream_id=first_stream_id,
            id=id,
            kind=kind,
            last_stream_id=last_stream_id,
            ordinal=ordinal,
            started_at=started_at,
            state=state,
            ended_at=ended_at,
        )

        return item
