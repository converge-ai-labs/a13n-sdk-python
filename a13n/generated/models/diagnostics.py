from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.diagnostics_envd import DiagnosticsEnvd

if TYPE_CHECKING:
    from ..models.diagnostics_rendered_item import DiagnosticsRenderedItem
    from ..models.event import Event
    from ..models.resource_observation import ResourceObservation


T = TypeVar("T", bound="Diagnostics")


@_attrs_define(repr=False)
class Diagnostics:
    """
    Attributes:
        cluster (str):
        commands (list[str]):
        connection (str):
        envd (DiagnosticsEnvd):
        errors (list[str]):
        events (list[Event]):
        events_truncated (bool):
        namespace (str):
        observed_at (datetime.datetime):
        ownership_id (str):
        pod_name (str):
        pod_uid (None | str):
        rendered (list[DiagnosticsRenderedItem]):
        resources (list[ResourceObservation]):
        stage (str):
    """

    cluster: str
    commands: list[str]
    connection: str
    envd: DiagnosticsEnvd
    errors: list[str]
    events: list[Event]
    events_truncated: bool
    namespace: str
    observed_at: datetime.datetime
    ownership_id: str
    pod_name: str
    pod_uid: str | None
    rendered: list[DiagnosticsRenderedItem]
    resources: list[ResourceObservation]
    stage: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cluster = self.cluster

        commands = self.commands

        connection = self.connection

        envd = self.envd.value

        errors = self.errors

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.to_dict()
            events.append(events_item)

        events_truncated = self.events_truncated

        namespace = self.namespace

        observed_at = self.observed_at.isoformat()

        ownership_id = self.ownership_id

        pod_name = self.pod_name

        pod_uid: str | None
        pod_uid = self.pod_uid

        rendered = []
        for rendered_item_data in self.rendered:
            rendered_item = rendered_item_data.to_dict()
            rendered.append(rendered_item)

        resources = []
        for resources_item_data in self.resources:
            resources_item = resources_item_data.to_dict()
            resources.append(resources_item)

        stage = self.stage

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cluster": cluster,
                "commands": commands,
                "connection": connection,
                "envd": envd,
                "errors": errors,
                "events": events,
                "events_truncated": events_truncated,
                "namespace": namespace,
                "observed_at": observed_at,
                "ownership_id": ownership_id,
                "pod_name": pod_name,
                "pod_uid": pod_uid,
                "rendered": rendered,
                "resources": resources,
                "stage": stage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.diagnostics_rendered_item import DiagnosticsRenderedItem
        from ..models.event import Event
        from ..models.resource_observation import ResourceObservation

        d = dict(src_dict)
        cluster = d.pop("cluster")

        commands = cast(list[str], d.pop("commands"))

        connection = d.pop("connection")

        envd = DiagnosticsEnvd(d.pop("envd"))

        errors = cast(list[str], d.pop("errors"))

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = Event.from_dict(events_item_data)

            events.append(events_item)

        events_truncated = d.pop("events_truncated")

        namespace = d.pop("namespace")

        observed_at = datetime.datetime.fromisoformat(d.pop("observed_at"))

        ownership_id = d.pop("ownership_id")

        pod_name = d.pop("pod_name")

        def _parse_pod_uid(data: object) -> str | None:
            if data is None:
                return data
            return cast(str | None, data)

        pod_uid = _parse_pod_uid(d.pop("pod_uid"))

        rendered = []
        _rendered = d.pop("rendered")
        for rendered_item_data in _rendered:
            rendered_item = DiagnosticsRenderedItem.from_dict(rendered_item_data)

            rendered.append(rendered_item)

        resources = []
        _resources = d.pop("resources")
        for resources_item_data in _resources:
            resources_item = ResourceObservation.from_dict(resources_item_data)

            resources.append(resources_item)

        stage = d.pop("stage")

        diagnostics = cls(
            cluster=cluster,
            commands=commands,
            connection=connection,
            envd=envd,
            errors=errors,
            events=events,
            events_truncated=events_truncated,
            namespace=namespace,
            observed_at=observed_at,
            ownership_id=ownership_id,
            pod_name=pod_name,
            pod_uid=pod_uid,
            rendered=rendered,
            resources=resources,
            stage=stage,
        )

        diagnostics.additional_properties = d
        return diagnostics

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
