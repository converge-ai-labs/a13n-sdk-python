from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.deployment_operation import DeploymentOperation
from ..models.deployment_status import DeploymentStatus

if TYPE_CHECKING:
    from ..models.deployment_cleanup import DeploymentCleanup


T = TypeVar("T", bound="Deployment")


@_attrs_define(repr=False)
class Deployment:
    """
    Attributes:
        account_id (str):
        cleanup (DeploymentCleanup):
        endpoint (None | str):
        error (None | str):
        id (str):
        name (str):
        operation (DeploymentOperation):
        provider_id (None | str):
        source_image (str):
        stage (str):
        status (DeploymentStatus):
        version (int):
        worker_name (str):
    """

    account_id: str
    cleanup: DeploymentCleanup
    endpoint: str | None
    error: str | None
    id: str
    name: str
    operation: DeploymentOperation
    provider_id: str | None
    source_image: str
    stage: str
    status: DeploymentStatus
    version: int
    worker_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        cleanup = self.cleanup.to_dict()

        endpoint: str | None
        endpoint = self.endpoint

        error: str | None
        error = self.error

        id = self.id

        name = self.name

        operation = self.operation.value

        provider_id: str | None
        provider_id = self.provider_id

        source_image = self.source_image

        stage = self.stage

        status = self.status.value

        version = self.version

        worker_name = self.worker_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "cleanup": cleanup,
                "endpoint": endpoint,
                "error": error,
                "id": id,
                "name": name,
                "operation": operation,
                "provider_id": provider_id,
                "source_image": source_image,
                "stage": stage,
                "status": status,
                "version": version,
                "worker_name": worker_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.deployment_cleanup import DeploymentCleanup

        d = dict(src_dict)
        account_id = d.pop("account_id")

        cleanup = DeploymentCleanup.from_dict(d.pop("cleanup"))

        def _parse_endpoint(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        endpoint = _parse_endpoint(d.pop("endpoint"))

        def _parse_error(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        error = _parse_error(d.pop("error"))

        id = d.pop("id")

        name = d.pop("name")

        operation = DeploymentOperation(d.pop("operation"))

        def _parse_provider_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        provider_id = _parse_provider_id(d.pop("provider_id"))

        source_image = d.pop("source_image")

        stage = d.pop("stage")

        status = DeploymentStatus(d.pop("status"))

        version = d.pop("version")

        worker_name = d.pop("worker_name")

        deployment = cls(
            account_id=account_id,
            cleanup=cleanup,
            endpoint=endpoint,
            error=error,
            id=id,
            name=name,
            operation=operation,
            provider_id=provider_id,
            source_image=source_image,
            stage=stage,
            status=status,
            version=version,
            worker_name=worker_name,
        )

        deployment.additional_properties = d
        return deployment

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
