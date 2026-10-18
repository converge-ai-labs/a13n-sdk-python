"""Small authored workflow values; the generated models own wire serialization."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass, fields
from typing import Any, ClassVar, Literal

from pydantic import JsonValue

from .generated import models as wire
from .generated.types import UNSET, Unset


@dataclass(frozen=True)
class _Value:
    _tag: ClassVar[dict[str, str]] = {}

    def to_dict(self) -> dict[str, Any]:
        return {
            **self._tag,
            **{
                field.name: _json(value)
                for field in fields(self)
                if not isinstance(value := getattr(self, field.name), Unset)
            },
        }


def _json(value: Any) -> Any:
    if isinstance(value, (_Value, wire.ToolSearch)):
        return value.to_dict()
    if isinstance(value, Mapping):
        return {key: _json(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json(item) for item in value]
    return value


@dataclass(frozen=True)
class TextPart(_Value):
    text: str
    _tag: ClassVar[dict[str, str]] = {"type": "text"}


@dataclass(frozen=True)
class JsonPart(_Value):
    value: JsonValue
    _tag: ClassVar[dict[str, str]] = {"type": "json"}


@dataclass(frozen=True)
class UrlPart(_Value):
    url: str
    _tag: ClassVar[dict[str, str]] = {"type": "url"}


@dataclass(frozen=True)
class AssetPart(_Value):
    asset_id: str
    _tag: ClassVar[dict[str, str]] = {"type": "asset"}


type Input = str | Sequence[str | TextPart | JsonPart | UrlPart | AssetPart]


def payload(value: Input) -> wire.MessagePayload:
    parts = [value] if isinstance(value, str) else value
    if not isinstance(parts, Sequence):
        raise TypeError("input must be text or an ordered sequence of public parts")
    content: list[dict[str, Any]] = []
    for part in parts:
        if isinstance(part, str):
            part = TextPart(part)
        if not isinstance(part, (TextPart, JsonPart, UrlPart, AssetPart)):
            raise TypeError("input contains an unsupported part")
        content.append(part.to_dict())
    return wire.MessagePayload.from_dict({"content": content})


@dataclass(frozen=True, kw_only=True)
class RunConfiguration(_Value):
    allowed_hosts: list[str] | Unset | None = UNSET
    extensions: Mapping[str, JsonValue] | Unset = UNSET


@dataclass(frozen=True, kw_only=True)
class AgentOverride(_Value):
    """All selectable overrides; nested schema objects use native JSON mappings."""

    builtin_skills: list[Literal["platform-operations"]] | Unset | None = UNSET
    client_tools: list[dict[str, JsonValue]] | Unset | None = UNSET
    connection_tools: list[dict[str, JsonValue]] | Unset | None = UNSET
    instructions: str | Unset | None = UNSET
    lazy_environment: bool | Unset | None = UNSET
    media_understanding: Mapping[str, JsonValue] | Unset | None = UNSET
    model: str | Unset | None = UNSET
    model_characteristics: Mapping[str, JsonValue] | Unset | None = UNSET
    model_settings: Mapping[str, JsonValue] | Unset | None = UNSET
    output_spec: Mapping[str, JsonValue] | Unset | None = UNSET
    platform_tools: Mapping[str, JsonValue] | Unset | None = UNSET
    plugins: list[dict[str, JsonValue]] | Unset | None = UNSET
    retries: Mapping[str, JsonValue] | Unset | None = UNSET
    reviewer: Mapping[str, JsonValue] | Unset | None = UNSET
    skill_sync: Mapping[str, JsonValue] | Unset | None = UNSET
    skills: list[dict[str, JsonValue]] | Unset | None = UNSET
    subagents: Mapping[str, JsonValue] | Unset | None = UNSET
    toolsets: Mapping[str, JsonValue] | Unset | None = UNSET
    tool_search: wire.ToolSearch | Unset | None = UNSET


@dataclass(frozen=True)
class UsageLimit(_Value):
    requests: int


@dataclass(frozen=True, kw_only=True)
class RunOptions(_Value):
    configuration: RunConfiguration | Unset | None = UNSET
    overrides: AgentOverride | Unset | None = UNSET
    labels: Mapping[str, str] | Unset = UNSET
    max_usage: UsageLimit | Unset | None = UNSET

    def into_wire(self) -> wire.RunOptionsInput:
        return wire.RunOptionsInput.from_dict(self.to_dict())


@dataclass(frozen=True)
class MountCreate(_Value):
    name: str
    environment_id: str
    working_directory: str | Unset | None = UNSET
    permission_ceiling: Mapping[str, JsonValue] | Unset = UNSET


@dataclass(frozen=True)
class MemoryMount(_Value):
    name: str
    memory_id: str
    access: Literal["read", "write"]
    recall: bool | Unset = UNSET


@dataclass(frozen=True)
class Approve(_Value):
    _tag: ClassVar[dict[str, str]] = {"action": "approve"}


@dataclass(frozen=True)
class Deny(_Value):
    reason: str | Unset | None = UNSET
    _tag: ClassVar[dict[str, str]] = {"action": "deny"}


@dataclass(frozen=True)
class Returned(_Value):
    value: JsonValue
    _tag: ClassVar[dict[str, str]] = {"status": "returned"}


@dataclass(frozen=True)
class Failed(_Value):
    message: str
    _tag: ClassVar[dict[str, str]] = {"status": "failed"}


type Answer = Approve | Deny | Returned | Failed


@dataclass(frozen=True)
class PendingRequest:
    tool_call_id: str
    tool_name: str
    arguments: dict[str, JsonValue]
    presentation: dict[str, JsonValue] | Unset | None = UNSET

    @classmethod
    def from_wire(cls, value: wire.PendingCall) -> PendingRequest:
        presentation = value.presentation
        return cls(
            value.tool_call_id,
            value.tool_name,
            value.arguments.to_dict(),
            presentation if isinstance(presentation, Unset) or presentation is None else presentation.to_dict(),
        )


@dataclass(frozen=True)
class Pending:
    approvals: tuple[PendingRequest, ...]
    calls: tuple[PendingRequest, ...]
    desktop_control_id: str | Unset | None = UNSET

    @classmethod
    def from_wire(cls, value: wire.Pending) -> Pending:
        return cls(
            tuple(PendingRequest.from_wire(item) for item in value.approvals),
            tuple(PendingRequest.from_wire(item) for item in value.calls),
            value.desktop_control_id,
        )


@dataclass(frozen=True)
class Failure:
    code: str
    message: str
