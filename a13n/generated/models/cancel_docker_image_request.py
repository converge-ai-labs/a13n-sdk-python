from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="CancelDockerImageRequest")


@_attrs_define(repr=False)
class CancelDockerImageRequest:
    """
    Attributes:
        workspace_id (None | str):
    """

    workspace_id: str | None

    def to_dict(self) -> dict[str, Any]:
        workspace_id: str | None
        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "workspace_id": workspace_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_workspace_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        workspace_id = _parse_workspace_id(d.pop("workspace_id"))

        cancel_docker_image_request = cls(
            workspace_id=workspace_id,
        )

        return cancel_docker_image_request
