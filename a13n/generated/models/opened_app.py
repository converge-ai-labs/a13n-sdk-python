from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.app_reference import AppReference
    from ..models.app_resource import AppResource
    from ..models.opened_app_arguments import OpenedAppArguments
    from ..models.opened_app_result import OpenedAppResult
    from ..models.opened_app_tool import OpenedAppTool


T = TypeVar("T", bound="OpenedApp")


@_attrs_define(repr=False)
class OpenedApp:
    """
    Attributes:
        arguments (OpenedAppArguments):
        reference (AppReference):
        resource (AppResource):
        result (OpenedAppResult):
        tool (OpenedAppTool):
    """

    arguments: OpenedAppArguments
    reference: AppReference
    resource: AppResource
    result: OpenedAppResult
    tool: OpenedAppTool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        arguments = self.arguments.to_dict()

        reference = self.reference.to_dict()

        resource = self.resource.to_dict()

        result = self.result.to_dict()

        tool = self.tool.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "arguments": arguments,
                "reference": reference,
                "resource": resource,
                "result": result,
                "tool": tool,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_reference import AppReference
        from ..models.app_resource import AppResource
        from ..models.opened_app_arguments import OpenedAppArguments
        from ..models.opened_app_result import OpenedAppResult
        from ..models.opened_app_tool import OpenedAppTool

        d = dict(src_dict)
        arguments = OpenedAppArguments.from_dict(d.pop("arguments"))

        reference = AppReference.from_dict(d.pop("reference"))

        resource = AppResource.from_dict(d.pop("resource"))

        result = OpenedAppResult.from_dict(d.pop("result"))

        tool = OpenedAppTool.from_dict(d.pop("tool"))

        opened_app = cls(
            arguments=arguments,
            reference=reference,
            resource=resource,
            result=result,
            tool=tool,
        )

        opened_app.additional_properties = d
        return opened_app

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
