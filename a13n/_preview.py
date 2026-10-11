"""Bounded best-effort root assistant preview, never a display reducer."""

from collections.abc import Mapping
from typing import NoReturn

from .errors import PreviewInterrupted
from .streaming import BoundaryFrame, DeltaFrame, ThreadFrame


class TextPreview:
    MAX_ACTIVE = 128

    def __init__(self, run_id: str) -> None:
        self.run_id = run_id
        self.active: dict[str, bool] = {}
        self.attempt: int | None = None
        self.sequence: int | None = None

    def interrupt(self, reason: str) -> NoReturn:
        raise PreviewInterrupted(reason, self.run_id)

    def apply(self, frame: ThreadFrame) -> str | None:
        if frame.event_type in {"gap", "reset"}:
            self.interrupt(frame.event_type)
        if frame.event_type == "changed":
            return None
        if not isinstance(frame, (DeltaFrame, BoundaryFrame)):
            return None
        if self.attempt is not None and frame.data["attempt"] != self.attempt:
            self.interrupt("attempt_changed")
        self.attempt = frame.data["attempt"]
        sequence = frame.data["sequence"]
        if self.sequence is not None:
            if frame.event_type == "delta" and sequence != self.sequence + 1:
                self.interrupt("sequence_gap")
            if frame.event_type == "boundary" and sequence > self.sequence:
                self.interrupt("sequence_gap")
        if frame.event_type == "delta" or self.sequence is None:
            self.sequence = sequence
        if frame.event_type != "delta":
            return None
        event = frame.data["event"]
        child = event.get("subagentRunId")
        if isinstance(child, str) and child:
            return None
        if child is not None:
            self.interrupt("ambiguous_attribution")
        metadata = event.get("metadata")
        hidden = isinstance(metadata, Mapping) and metadata.get("display") is False
        kind = event.get("type")
        if kind == "CUSTOM" and event.get("name") == "a13n.stream.fragment":
            if not hidden:
                self.interrupt("fragment")
            return None
        if kind not in {"TEXT_MESSAGE_START", "TEXT_MESSAGE_CONTENT", "TEXT_MESSAGE_END"}:
            return None
        identifier = event.get("messageId")
        if not isinstance(identifier, str) or not identifier:
            self.interrupt("missing_message_id")
        assert isinstance(identifier, str)
        if kind == "TEXT_MESSAGE_START":
            if identifier in self.active:
                self.interrupt("duplicate_start")
            if len(self.active) >= self.MAX_ACTIVE:
                self.interrupt("active_message_limit")
            role = event.get("role")
            if not isinstance(role, str):
                self.interrupt("ambiguous_role")
            self.active[identifier] = role == "assistant" and not hidden
            return None
        if hidden:
            if kind == "TEXT_MESSAGE_END":
                self.active.pop(identifier, None)
            return None
        if identifier not in self.active:
            self.interrupt("missing_start")
        visible = self.active[identifier]
        if kind == "TEXT_MESSAGE_END":
            del self.active[identifier]
            return None
        if not visible:
            return None
        delta = event.get("delta")
        if not isinstance(delta, str):
            self.interrupt("non_string_content")
        return delta
