from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.mcp_input_response_action import McpInputResponseAction
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mcp_input_response_content_type_0 import McpInputResponseContentType0


T = TypeVar("T", bound="McpInputResponse")


@_attrs_define(repr=False)
class McpInputResponse:
    """
    Attributes:
        action (McpInputResponseAction):
        content (McpInputResponseContentType0 | None | Unset):
    """

    action: McpInputResponseAction
    content: McpInputResponseContentType0 | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.mcp_input_response_content_type_0 import McpInputResponseContentType0

        action = self.action.value

        content: dict[str, Any] | Unset | None
        if isinstance(self.content, Unset):
            content = UNSET
        elif isinstance(self.content, McpInputResponseContentType0):
            content = self.content.to_dict()
        else:
            content = self.content

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "action": action,
            }
        )
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mcp_input_response_content_type_0 import McpInputResponseContentType0

        d = dict(src_dict)
        action = McpInputResponseAction(d.pop("action"))

        def _parse_content(data: object) -> McpInputResponseContentType0 | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                content_type_0 = McpInputResponseContentType0.from_dict(data)

                return content_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(McpInputResponseContentType0 | Unset | None, data)

        content = _parse_content(d.pop("content", UNSET))

        mcp_input_response = cls(
            action=action,
            content=content,
        )

        return mcp_input_response
