from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cgroup_metrics import CgroupMetrics
    from ..models.connection_metrics import ConnectionMetrics
    from ..models.daemon_metrics import DaemonMetrics
    from ..models.disk_metrics import DiskMetrics
    from ..models.filesystem_inventory import FilesystemInventory
    from ..models.metrics_sample_filesystems import MetricsSampleFilesystems
    from ..models.network_metrics import NetworkMetrics
    from ..models.system_metrics import SystemMetrics


T = TypeVar("T", bound="MetricsSample")


@_attrs_define(repr=False)
class MetricsSample:
    """
    Attributes:
        collection_duration_ms (int):
        sample_age_ms (int):
        sampled_at (datetime.datetime):
        sequence (int):
        system (SystemMetrics):
        cgroup_v2 (CgroupMetrics | None | Unset):
        connections (ConnectionMetrics | None | Unset):
        daemon (DaemonMetrics | None | Unset):
        disks (DiskMetrics | None | Unset):
        filesystems (MetricsSampleFilesystems | Unset):
        local_filesystems (FilesystemInventory | None | Unset):
        network (NetworkMetrics | None | Unset):
    """

    collection_duration_ms: int
    sample_age_ms: int
    sampled_at: datetime.datetime
    sequence: int
    system: SystemMetrics
    cgroup_v2: CgroupMetrics | Unset | None = UNSET
    connections: ConnectionMetrics | Unset | None = UNSET
    daemon: DaemonMetrics | Unset | None = UNSET
    disks: DiskMetrics | Unset | None = UNSET
    filesystems: MetricsSampleFilesystems | Unset = UNSET
    local_filesystems: FilesystemInventory | Unset | None = UNSET
    network: NetworkMetrics | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.cgroup_metrics import CgroupMetrics
        from ..models.connection_metrics import ConnectionMetrics
        from ..models.daemon_metrics import DaemonMetrics
        from ..models.disk_metrics import DiskMetrics
        from ..models.filesystem_inventory import FilesystemInventory
        from ..models.network_metrics import NetworkMetrics

        collection_duration_ms = self.collection_duration_ms

        sample_age_ms = self.sample_age_ms

        sampled_at = self.sampled_at.isoformat()

        sequence = self.sequence

        system = self.system.to_dict()

        cgroup_v2: dict[str, Any] | Unset | None
        if isinstance(self.cgroup_v2, Unset):
            cgroup_v2 = UNSET
        elif isinstance(self.cgroup_v2, CgroupMetrics):
            cgroup_v2 = self.cgroup_v2.to_dict()
        else:
            cgroup_v2 = self.cgroup_v2

        connections: dict[str, Any] | Unset | None
        if isinstance(self.connections, Unset):
            connections = UNSET
        elif isinstance(self.connections, ConnectionMetrics):
            connections = self.connections.to_dict()
        else:
            connections = self.connections

        daemon: dict[str, Any] | Unset | None
        if isinstance(self.daemon, Unset):
            daemon = UNSET
        elif isinstance(self.daemon, DaemonMetrics):
            daemon = self.daemon.to_dict()
        else:
            daemon = self.daemon

        disks: dict[str, Any] | Unset | None
        if isinstance(self.disks, Unset):
            disks = UNSET
        elif isinstance(self.disks, DiskMetrics):
            disks = self.disks.to_dict()
        else:
            disks = self.disks

        filesystems: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filesystems, Unset):
            filesystems = self.filesystems.to_dict()

        local_filesystems: dict[str, Any] | Unset | None
        if isinstance(self.local_filesystems, Unset):
            local_filesystems = UNSET
        elif isinstance(self.local_filesystems, FilesystemInventory):
            local_filesystems = self.local_filesystems.to_dict()
        else:
            local_filesystems = self.local_filesystems

        network: dict[str, Any] | Unset | None
        if isinstance(self.network, Unset):
            network = UNSET
        elif isinstance(self.network, NetworkMetrics):
            network = self.network.to_dict()
        else:
            network = self.network

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "collection_duration_ms": collection_duration_ms,
                "sample_age_ms": sample_age_ms,
                "sampled_at": sampled_at,
                "sequence": sequence,
                "system": system,
            }
        )
        if cgroup_v2 is not UNSET:
            field_dict["cgroup_v2"] = cgroup_v2
        if connections is not UNSET:
            field_dict["connections"] = connections
        if daemon is not UNSET:
            field_dict["daemon"] = daemon
        if disks is not UNSET:
            field_dict["disks"] = disks
        if filesystems is not UNSET:
            field_dict["filesystems"] = filesystems
        if local_filesystems is not UNSET:
            field_dict["local_filesystems"] = local_filesystems
        if network is not UNSET:
            field_dict["network"] = network

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cgroup_metrics import CgroupMetrics
        from ..models.connection_metrics import ConnectionMetrics
        from ..models.daemon_metrics import DaemonMetrics
        from ..models.disk_metrics import DiskMetrics
        from ..models.filesystem_inventory import FilesystemInventory
        from ..models.metrics_sample_filesystems import MetricsSampleFilesystems
        from ..models.network_metrics import NetworkMetrics
        from ..models.system_metrics import SystemMetrics

        d = dict(src_dict)
        collection_duration_ms = d.pop("collection_duration_ms")

        sample_age_ms = d.pop("sample_age_ms")

        sampled_at = datetime.datetime.fromisoformat(d.pop("sampled_at"))

        sequence = d.pop("sequence")

        system = SystemMetrics.from_dict(d.pop("system"))

        def _parse_cgroup_v2(data: object) -> CgroupMetrics | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                cgroup_v2_type_0 = CgroupMetrics.from_dict(data)

                return cgroup_v2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CgroupMetrics | Unset | None, data)

        cgroup_v2 = _parse_cgroup_v2(d.pop("cgroup_v2", UNSET))

        def _parse_connections(data: object) -> ConnectionMetrics | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                connections_type_0 = ConnectionMetrics.from_dict(data)

                return connections_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ConnectionMetrics | Unset | None, data)

        connections = _parse_connections(d.pop("connections", UNSET))

        def _parse_daemon(data: object) -> DaemonMetrics | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                daemon_type_0 = DaemonMetrics.from_dict(data)

                return daemon_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DaemonMetrics | Unset | None, data)

        daemon = _parse_daemon(d.pop("daemon", UNSET))

        def _parse_disks(data: object) -> DiskMetrics | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                disks_type_0 = DiskMetrics.from_dict(data)

                return disks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DiskMetrics | Unset | None, data)

        disks = _parse_disks(d.pop("disks", UNSET))

        _filesystems = d.pop("filesystems", UNSET)
        filesystems: MetricsSampleFilesystems | Unset
        if isinstance(_filesystems, Unset):
            filesystems = UNSET
        else:
            filesystems = MetricsSampleFilesystems.from_dict(_filesystems)

        def _parse_local_filesystems(data: object) -> FilesystemInventory | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                local_filesystems_type_0 = FilesystemInventory.from_dict(data)

                return local_filesystems_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(FilesystemInventory | Unset | None, data)

        local_filesystems = _parse_local_filesystems(d.pop("local_filesystems", UNSET))

        def _parse_network(data: object) -> NetworkMetrics | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                network_type_0 = NetworkMetrics.from_dict(data)

                return network_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NetworkMetrics | Unset | None, data)

        network = _parse_network(d.pop("network", UNSET))

        metrics_sample = cls(
            collection_duration_ms=collection_duration_ms,
            sample_age_ms=sample_age_ms,
            sampled_at=sampled_at,
            sequence=sequence,
            system=system,
            cgroup_v2=cgroup_v2,
            connections=connections,
            daemon=daemon,
            disks=disks,
            filesystems=filesystems,
            local_filesystems=local_filesystems,
            network=network,
        )

        return metrics_sample
