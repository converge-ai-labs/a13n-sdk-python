from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mcp_elicitation_mode import McpElicitationMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mcp_elicitation_schema_type_0 import McpElicitationSchemaType0


T = TypeVar("T", bound="McpElicitation")


@_attrs_define(repr=False)
class McpElicitation:
    """
    Attributes:
        expires_at (datetime.datetime):
        message (str):
        mode (McpElicitationMode):
        request_id (str):
        server_id (str):
        thread_id (str):
        kind (Literal['mcp_elicitation'] | Unset):
        run_id (None | str | Unset):
        schema (McpElicitationSchemaType0 | None | Unset):
        server_name (None | str | Unset):
        tool_call_id (None | str | Unset):
        url (None | str | Unset):
        url_host (None | str | Unset):
    """

    expires_at: datetime.datetime
    message: str
    mode: McpElicitationMode
    request_id: str
    server_id: str
    thread_id: str
    kind: Literal["mcp_elicitation"] | Unset = UNSET
    run_id: str | Unset | None = UNSET
    schema: McpElicitationSchemaType0 | Unset | None = UNSET
    server_name: str | Unset | None = UNSET
    tool_call_id: str | Unset | None = UNSET
    url: str | Unset | None = UNSET
    url_host: str | Unset | None = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.mcp_elicitation_schema_type_0 import McpElicitationSchemaType0

        expires_at = self.expires_at.isoformat()

        message = self.message

        mode = self.mode.value

        request_id = self.request_id

        server_id = self.server_id

        thread_id = self.thread_id

        kind = self.kind

        run_id: str | Unset | None
        if isinstance(self.run_id, Unset):
            run_id = UNSET
        else:
            run_id = self.run_id

        schema: dict[str, Any] | Unset | None
        if isinstance(self.schema, Unset):
            schema = UNSET
        elif isinstance(self.schema, McpElicitationSchemaType0):
            schema = self.schema.to_dict()
        else:
            schema = self.schema

        server_name: str | Unset | None
        if isinstance(self.server_name, Unset):
            server_name = UNSET
        else:
            server_name = self.server_name

        tool_call_id: str | Unset | None
        if isinstance(self.tool_call_id, Unset):
            tool_call_id = UNSET
        else:
            tool_call_id = self.tool_call_id

        url: str | Unset | None
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        url_host: str | Unset | None
        if isinstance(self.url_host, Unset):
            url_host = UNSET
        else:
            url_host = self.url_host

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "expires_at": expires_at,
                "message": message,
                "mode": mode,
                "request_id": request_id,
                "server_id": server_id,
                "thread_id": thread_id,
            }
        )
        if kind is not UNSET:
            field_dict["kind"] = kind
        if run_id is not UNSET:
            field_dict["run_id"] = run_id
        if schema is not UNSET:
            field_dict["schema"] = schema
        if server_name is not UNSET:
            field_dict["server_name"] = server_name
        if tool_call_id is not UNSET:
            field_dict["tool_call_id"] = tool_call_id
        if url is not UNSET:
            field_dict["url"] = url
        if url_host is not UNSET:
            field_dict["url_host"] = url_host

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mcp_elicitation_schema_type_0 import McpElicitationSchemaType0

        d = dict(src_dict)
        expires_at = datetime.datetime.fromisoformat(d.pop("expires_at"))

        message = d.pop("message")

        mode = McpElicitationMode(d.pop("mode"))

        request_id = d.pop("request_id")

        server_id = d.pop("server_id")

        thread_id = d.pop("thread_id")

        kind = cast(Literal["mcp_elicitation"] | Unset, d.pop("kind", UNSET))
        if kind != "mcp_elicitation" and not isinstance(kind, Unset):
            raise ValueError(f"kind must match const 'mcp_elicitation', got '{kind}'")

        def _parse_run_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        run_id = _parse_run_id(d.pop("run_id", UNSET))

        def _parse_schema(data: object) -> McpElicitationSchemaType0 | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                schema_type_0 = McpElicitationSchemaType0.from_dict(data)

                return schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(McpElicitationSchemaType0 | Unset | None, data)

        schema = _parse_schema(d.pop("schema", UNSET))

        def _parse_server_name(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        server_name = _parse_server_name(d.pop("server_name", UNSET))

        def _parse_tool_call_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        tool_call_id = _parse_tool_call_id(d.pop("tool_call_id", UNSET))

        def _parse_url(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        url = _parse_url(d.pop("url", UNSET))

        def _parse_url_host(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        url_host = _parse_url_host(d.pop("url_host", UNSET))

        mcp_elicitation = cls(
            expires_at=expires_at,
            message=message,
            mode=mode,
            request_id=request_id,
            server_id=server_id,
            thread_id=thread_id,
            kind=kind,
            run_id=run_id,
            schema=schema,
            server_name=server_name,
            tool_call_id=tool_call_id,
            url=url,
            url_host=url_host,
        )

        mcp_elicitation.additional_properties = d
        return mcp_elicitation

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
