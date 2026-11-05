from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.environment_failure import EnvironmentFailure
    from ..models.environment_state import EnvironmentState
    from ..models.environment_view_metrics_labels import EnvironmentViewMetricsLabels
    from ..models.metrics_application import MetricsApplication
    from ..models.reclamation import Reclamation


T = TypeVar("T", bound="EnvironmentView")


@_attrs_define(repr=False)
class EnvironmentView:
    """
    Attributes:
        created_at (datetime.datetime):
        created_by_id (str):
        device_id (None | str):
        endpoint (None | str):
        failure (EnvironmentFailure | None):
        id (str):
        last_used_at (datetime.datetime | None):
        name (str):
        operation_id (None | str):
        operation_started_at (datetime.datetime | None):
        organization_id (str):
        owner_principal_id (None | str):
        provider_id (None | str):
        status (str):
        template_id (None | str):
        updated_at (datetime.datetime):
        version (int):
        workspace_id (str):
        debug_hold_until (datetime.datetime | None | Unset):
        metrics_application (MetricsApplication | None | Unset):
        metrics_data_source_id (None | str | Unset):
        metrics_labels (EnvironmentViewMetricsLabels | Unset):
        preparation_deadline (datetime.datetime | None | Unset):
        preparation_failed_at (datetime.datetime | None | Unset):
        reclamation (None | Reclamation | Unset):
        retirement_state (EnvironmentState | None | Unset):
    """

    created_at: datetime.datetime
    created_by_id: str
    device_id: str | None
    endpoint: str | None
    failure: EnvironmentFailure | None
    id: str
    last_used_at: datetime.datetime | None
    name: str
    operation_id: str | None
    operation_started_at: datetime.datetime | None
    organization_id: str
    owner_principal_id: str | None
    provider_id: str | None
    status: str
    template_id: str | None
    updated_at: datetime.datetime
    version: int
    workspace_id: str
    debug_hold_until: datetime.datetime | Unset | None = UNSET
    metrics_application: MetricsApplication | Unset | None = UNSET
    metrics_data_source_id: str | Unset | None = UNSET
    metrics_labels: EnvironmentViewMetricsLabels | Unset = UNSET
    preparation_deadline: datetime.datetime | Unset | None = UNSET
    preparation_failed_at: datetime.datetime | Unset | None = UNSET
    reclamation: Reclamation | Unset | None = UNSET
    retirement_state: EnvironmentState | Unset | None = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.environment_failure import EnvironmentFailure
        from ..models.environment_state import EnvironmentState
        from ..models.metrics_application import MetricsApplication
        from ..models.reclamation import Reclamation

        created_at = self.created_at.isoformat()

        created_by_id = self.created_by_id

        device_id: str | None
        device_id = self.device_id

        endpoint: str | None
        endpoint = self.endpoint

        failure: dict[str, Any] | None
        if isinstance(self.failure, EnvironmentFailure):
            failure = self.failure.to_dict()
        else:
            failure = self.failure

        id = self.id

        last_used_at: str | None
        if isinstance(self.last_used_at, datetime.datetime):
            last_used_at = self.last_used_at.isoformat()
        else:
            last_used_at = self.last_used_at

        name = self.name

        operation_id: str | None
        operation_id = self.operation_id

        operation_started_at: str | None
        if isinstance(self.operation_started_at, datetime.datetime):
            operation_started_at = self.operation_started_at.isoformat()
        else:
            operation_started_at = self.operation_started_at

        organization_id = self.organization_id

        owner_principal_id: str | None
        owner_principal_id = self.owner_principal_id

        provider_id: str | None
        provider_id = self.provider_id

        status = self.status

        template_id: str | None
        template_id = self.template_id

        updated_at = self.updated_at.isoformat()

        version = self.version

        workspace_id = self.workspace_id

        debug_hold_until: str | Unset | None
        if isinstance(self.debug_hold_until, Unset):
            debug_hold_until = UNSET
        elif isinstance(self.debug_hold_until, datetime.datetime):
            debug_hold_until = self.debug_hold_until.isoformat()
        else:
            debug_hold_until = self.debug_hold_until

        metrics_application: dict[str, Any] | Unset | None
        if isinstance(self.metrics_application, Unset):
            metrics_application = UNSET
        elif isinstance(self.metrics_application, MetricsApplication):
            metrics_application = self.metrics_application.to_dict()
        else:
            metrics_application = self.metrics_application

        metrics_data_source_id: str | Unset | None
        if isinstance(self.metrics_data_source_id, Unset):
            metrics_data_source_id = UNSET
        else:
            metrics_data_source_id = self.metrics_data_source_id

        metrics_labels: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metrics_labels, Unset):
            metrics_labels = self.metrics_labels.to_dict()

        preparation_deadline: str | Unset | None
        if isinstance(self.preparation_deadline, Unset):
            preparation_deadline = UNSET
        elif isinstance(self.preparation_deadline, datetime.datetime):
            preparation_deadline = self.preparation_deadline.isoformat()
        else:
            preparation_deadline = self.preparation_deadline

        preparation_failed_at: str | Unset | None
        if isinstance(self.preparation_failed_at, Unset):
            preparation_failed_at = UNSET
        elif isinstance(self.preparation_failed_at, datetime.datetime):
            preparation_failed_at = self.preparation_failed_at.isoformat()
        else:
            preparation_failed_at = self.preparation_failed_at

        reclamation: dict[str, Any] | Unset | None
        if isinstance(self.reclamation, Unset):
            reclamation = UNSET
        elif isinstance(self.reclamation, Reclamation):
            reclamation = self.reclamation.to_dict()
        else:
            reclamation = self.reclamation

        retirement_state: dict[str, Any] | Unset | None
        if isinstance(self.retirement_state, Unset):
            retirement_state = UNSET
        elif isinstance(self.retirement_state, EnvironmentState):
            retirement_state = self.retirement_state.to_dict()
        else:
            retirement_state = self.retirement_state

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "created_by_id": created_by_id,
                "device_id": device_id,
                "endpoint": endpoint,
                "failure": failure,
                "id": id,
                "last_used_at": last_used_at,
                "name": name,
                "operation_id": operation_id,
                "operation_started_at": operation_started_at,
                "organization_id": organization_id,
                "owner_principal_id": owner_principal_id,
                "provider_id": provider_id,
                "status": status,
                "template_id": template_id,
                "updated_at": updated_at,
                "version": version,
                "workspace_id": workspace_id,
            }
        )
        if debug_hold_until is not UNSET:
            field_dict["debug_hold_until"] = debug_hold_until
        if metrics_application is not UNSET:
            field_dict["metrics_application"] = metrics_application
        if metrics_data_source_id is not UNSET:
            field_dict["metrics_data_source_id"] = metrics_data_source_id
        if metrics_labels is not UNSET:
            field_dict["metrics_labels"] = metrics_labels
        if preparation_deadline is not UNSET:
            field_dict["preparation_deadline"] = preparation_deadline
        if preparation_failed_at is not UNSET:
            field_dict["preparation_failed_at"] = preparation_failed_at
        if reclamation is not UNSET:
            field_dict["reclamation"] = reclamation
        if retirement_state is not UNSET:
            field_dict["retirement_state"] = retirement_state

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.environment_failure import EnvironmentFailure
        from ..models.environment_state import EnvironmentState
        from ..models.environment_view_metrics_labels import EnvironmentViewMetricsLabels
        from ..models.metrics_application import MetricsApplication
        from ..models.reclamation import Reclamation

        d = dict(src_dict)
        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        created_by_id = d.pop("created_by_id")

        def _parse_device_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        device_id = _parse_device_id(d.pop("device_id"))

        def _parse_endpoint(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        endpoint = _parse_endpoint(d.pop("endpoint"))

        def _parse_failure(data: object) -> EnvironmentFailure | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                failure_type_0 = EnvironmentFailure.from_dict(data)

                return failure_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnvironmentFailure | None, data)

        failure = _parse_failure(d.pop("failure"))

        id = d.pop("id")

        def _parse_last_used_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_used_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_used_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_used_at = _parse_last_used_at(d.pop("last_used_at"))

        name = d.pop("name")

        def _parse_operation_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        operation_id = _parse_operation_id(d.pop("operation_id"))

        def _parse_operation_started_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                operation_started_at_type_0 = datetime.datetime.fromisoformat(data)

                return operation_started_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        operation_started_at = _parse_operation_started_at(d.pop("operation_started_at"))

        organization_id = d.pop("organization_id")

        def _parse_owner_principal_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        owner_principal_id = _parse_owner_principal_id(d.pop("owner_principal_id"))

        def _parse_provider_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        provider_id = _parse_provider_id(d.pop("provider_id"))

        status = d.pop("status")

        def _parse_template_id(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        template_id = _parse_template_id(d.pop("template_id"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        version = d.pop("version")

        workspace_id = d.pop("workspace_id")

        def _parse_debug_hold_until(data: object) -> datetime.datetime | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                debug_hold_until_type_0 = datetime.datetime.fromisoformat(data)

                return debug_hold_until_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | Unset | None, data)

        debug_hold_until = _parse_debug_hold_until(d.pop("debug_hold_until", UNSET))

        def _parse_metrics_application(data: object) -> MetricsApplication | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metrics_application_type_0 = MetricsApplication.from_dict(data)

                return metrics_application_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MetricsApplication | Unset | None, data)

        metrics_application = _parse_metrics_application(d.pop("metrics_application", UNSET))

        def _parse_metrics_data_source_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        metrics_data_source_id = _parse_metrics_data_source_id(d.pop("metrics_data_source_id", UNSET))

        _metrics_labels = d.pop("metrics_labels", UNSET)
        metrics_labels: EnvironmentViewMetricsLabels | Unset
        if isinstance(_metrics_labels, Unset):
            metrics_labels = UNSET
        else:
            metrics_labels = EnvironmentViewMetricsLabels.from_dict(_metrics_labels)

        def _parse_preparation_deadline(data: object) -> datetime.datetime | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                preparation_deadline_type_0 = datetime.datetime.fromisoformat(data)

                return preparation_deadline_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | Unset | None, data)

        preparation_deadline = _parse_preparation_deadline(d.pop("preparation_deadline", UNSET))

        def _parse_preparation_failed_at(data: object) -> datetime.datetime | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                preparation_failed_at_type_0 = datetime.datetime.fromisoformat(data)

                return preparation_failed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | Unset | None, data)

        preparation_failed_at = _parse_preparation_failed_at(d.pop("preparation_failed_at", UNSET))

        def _parse_reclamation(data: object) -> Reclamation | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                reclamation_type_0 = Reclamation.from_dict(data)

                return reclamation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(Reclamation | Unset | None, data)

        reclamation = _parse_reclamation(d.pop("reclamation", UNSET))

        def _parse_retirement_state(data: object) -> EnvironmentState | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                retirement_state_type_0 = EnvironmentState.from_dict(data)

                return retirement_state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EnvironmentState | Unset | None, data)

        retirement_state = _parse_retirement_state(d.pop("retirement_state", UNSET))

        environment_view = cls(
            created_at=created_at,
            created_by_id=created_by_id,
            device_id=device_id,
            endpoint=endpoint,
            failure=failure,
            id=id,
            last_used_at=last_used_at,
            name=name,
            operation_id=operation_id,
            operation_started_at=operation_started_at,
            organization_id=organization_id,
            owner_principal_id=owner_principal_id,
            provider_id=provider_id,
            status=status,
            template_id=template_id,
            updated_at=updated_at,
            version=version,
            workspace_id=workspace_id,
            debug_hold_until=debug_hold_until,
            metrics_application=metrics_application,
            metrics_data_source_id=metrics_data_source_id,
            metrics_labels=metrics_labels,
            preparation_deadline=preparation_deadline,
            preparation_failed_at=preparation_failed_at,
            reclamation=reclamation,
            retirement_state=retirement_state,
        )

        environment_view.additional_properties = d
        return environment_view

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
