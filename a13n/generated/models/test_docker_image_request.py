from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.test_docker_image_request_configuration import TestDockerImageRequestConfiguration


T = TypeVar("T", bound="TestDockerImageRequest")


@_attrs_define(repr=False)
class TestDockerImageRequest:
    """
    Attributes:
        configuration (TestDockerImageRequestConfiguration):
        request_id (str):
        workspace_id (None | str):
    """

    configuration: TestDockerImageRequestConfiguration
    request_id: str
    workspace_id: str | None

    def to_dict(self) -> dict[str, Any]:
        configuration = self.configuration.to_dict()

        request_id = self.request_id

        workspace_id: str | None
        workspace_id = self.workspace_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "configuration": configuration,
                "request_id": request_id,
                "workspace_id": workspace_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.test_docker_image_request_configuration import (
            TestDockerImageRequestConfiguration,
        )

        d = dict(src_dict)
        configuration = TestDockerImageRequestConfiguration.from_dict(d.pop("configuration"))

        request_id = d.pop("request_id")

        def _parse_workspace_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        workspace_id = _parse_workspace_id(d.pop("workspace_id"))

        test_docker_image_request = cls(
            configuration=configuration,
            request_id=request_id,
            workspace_id=workspace_id,
        )

        return test_docker_image_request
