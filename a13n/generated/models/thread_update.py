from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.execution_override import ExecutionOverride
    from ..models.mcp_headers import McpHeaders
    from ..models.thread_update_labels_type_0 import ThreadUpdateLabelsType0


T = TypeVar("T", bound="ThreadUpdate")


@_attrs_define(repr=False)
class ThreadUpdate:
    """
    Attributes:
        execution (ExecutionOverride | None | Unset):
        labels (None | ThreadUpdateLabelsType0 | Unset):
        mcp_headers (McpHeaders | None | Unset):
    """

    execution: ExecutionOverride | Unset | None = UNSET
    labels: ThreadUpdateLabelsType0 | Unset | None = UNSET
    mcp_headers: McpHeaders | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.execution_override import ExecutionOverride
        from ..models.mcp_headers import McpHeaders
        from ..models.thread_update_labels_type_0 import ThreadUpdateLabelsType0

        execution: dict[str, Any] | Unset | None
        if isinstance(self.execution, Unset):
            execution = UNSET
        elif isinstance(self.execution, ExecutionOverride):
            execution = self.execution.to_dict()
        else:
            execution = self.execution

        labels: dict[str, Any] | Unset | None
        if isinstance(self.labels, Unset):
            labels = UNSET
        elif isinstance(self.labels, ThreadUpdateLabelsType0):
            labels = self.labels.to_dict()
        else:
            labels = self.labels

        mcp_headers: dict[str, Any] | Unset | None
        if isinstance(self.mcp_headers, Unset):
            mcp_headers = UNSET
        elif isinstance(self.mcp_headers, McpHeaders):
            mcp_headers = self.mcp_headers.to_dict()
        else:
            mcp_headers = self.mcp_headers

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if execution is not UNSET:
            field_dict["execution"] = execution
        if labels is not UNSET:
            field_dict["labels"] = labels
        if mcp_headers is not UNSET:
            field_dict["mcp_headers"] = mcp_headers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.execution_override import ExecutionOverride
        from ..models.mcp_headers import McpHeaders
        from ..models.thread_update_labels_type_0 import ThreadUpdateLabelsType0

        d = dict(src_dict)

        def _parse_execution(data: object) -> ExecutionOverride | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                execution_type_0 = ExecutionOverride.from_dict(data)

                return execution_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExecutionOverride | Unset | None, data)

        execution = _parse_execution(d.pop("execution", UNSET))

        def _parse_labels(data: object) -> ThreadUpdateLabelsType0 | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                labels_type_0 = ThreadUpdateLabelsType0.from_dict(data)

                return labels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ThreadUpdateLabelsType0 | Unset | None, data)

        labels = _parse_labels(d.pop("labels", UNSET))

        def _parse_mcp_headers(data: object) -> McpHeaders | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mcp_headers_type_0 = McpHeaders.from_dict(data)

                return mcp_headers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(McpHeaders | Unset | None, data)

        mcp_headers = _parse_mcp_headers(d.pop("mcp_headers", UNSET))

        thread_update = cls(
            execution=execution,
            labels=labels,
            mcp_headers=mcp_headers,
        )

        return thread_update
