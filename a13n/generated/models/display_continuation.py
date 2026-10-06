from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.arguments import Arguments
    from ..models.display_continuation_response_groups import DisplayContinuationResponseGroups
    from ..models.fragment_state import FragmentState
    from ..models.observer_continuation import ObserverContinuation
    from ..models.stream_position import StreamPosition


T = TypeVar("T", bound="DisplayContinuation")


@_attrs_define(repr=False)
class DisplayContinuation:
    """Parsing state at a semantic cut; Host paging may retire only immutable items.

    Attributes:
        next_ordinal (int):
        position (StreamPosition):
        run_id (str):
        arguments (Arguments | None | Unset):
        fragments (FragmentState | Unset): Incomplete custom payloads, not a journal of completed events.
        full_content (bool | Unset):
        observer (ObserverContinuation | Unset): Native conversion cursors required to resume mid-part, without raw
            history.
        response_groups (DisplayContinuationResponseGroups | Unset):
    """

    next_ordinal: int
    position: StreamPosition
    run_id: str
    arguments: Arguments | Unset | None = UNSET
    fragments: FragmentState | Unset = UNSET
    full_content: bool | Unset = UNSET
    observer: ObserverContinuation | Unset = UNSET
    response_groups: DisplayContinuationResponseGroups | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.arguments import Arguments

        next_ordinal = self.next_ordinal

        position = self.position.to_dict()

        run_id = self.run_id

        arguments: dict[str, Any] | Unset | None
        if isinstance(self.arguments, Unset):
            arguments = UNSET
        elif isinstance(self.arguments, Arguments):
            arguments = self.arguments.to_dict()
        else:
            arguments = self.arguments

        fragments: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fragments, Unset):
            fragments = self.fragments.to_dict()

        full_content = self.full_content

        observer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.observer, Unset):
            observer = self.observer.to_dict()

        response_groups: dict[str, Any] | Unset = UNSET
        if not isinstance(self.response_groups, Unset):
            response_groups = self.response_groups.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "next_ordinal": next_ordinal,
                "position": position,
                "run_id": run_id,
            }
        )
        if arguments is not UNSET:
            field_dict["arguments"] = arguments
        if fragments is not UNSET:
            field_dict["fragments"] = fragments
        if full_content is not UNSET:
            field_dict["full_content"] = full_content
        if observer is not UNSET:
            field_dict["observer"] = observer
        if response_groups is not UNSET:
            field_dict["response_groups"] = response_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.arguments import Arguments
        from ..models.display_continuation_response_groups import DisplayContinuationResponseGroups
        from ..models.fragment_state import FragmentState
        from ..models.observer_continuation import ObserverContinuation
        from ..models.stream_position import StreamPosition

        d = dict(src_dict)
        next_ordinal = d.pop("next_ordinal")

        position = StreamPosition.from_dict(d.pop("position"))

        run_id = d.pop("run_id")

        def _parse_arguments(data: object) -> Arguments | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                arguments_type_0 = Arguments.from_dict(data)

                return arguments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Arguments | Unset | None, data)

        arguments = _parse_arguments(d.pop("arguments", UNSET))

        _fragments = d.pop("fragments", UNSET)
        fragments: FragmentState | Unset
        if isinstance(_fragments, Unset):
            fragments = UNSET
        else:
            fragments = FragmentState.from_dict(_fragments)

        full_content = d.pop("full_content", UNSET)

        _observer = d.pop("observer", UNSET)
        observer: ObserverContinuation | Unset
        if isinstance(_observer, Unset):
            observer = UNSET
        else:
            observer = ObserverContinuation.from_dict(_observer)

        _response_groups = d.pop("response_groups", UNSET)
        response_groups: DisplayContinuationResponseGroups | Unset
        if isinstance(_response_groups, Unset):
            response_groups = UNSET
        else:
            response_groups = DisplayContinuationResponseGroups.from_dict(_response_groups)

        display_continuation = cls(
            next_ordinal=next_ordinal,
            position=position,
            run_id=run_id,
            arguments=arguments,
            fragments=fragments,
            full_content=full_content,
            observer=observer,
            response_groups=response_groups,
        )

        return display_continuation
