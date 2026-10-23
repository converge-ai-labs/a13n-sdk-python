from enum import StrEnum


class EnvironmentQueryMetricType1(StrEnum):
    CGROUP_IO_READ_BYTES_PER_SECOND = "cgroup_io_read_bytes_per_second"
    CGROUP_IO_READ_OPERATIONS_PER_SECOND = "cgroup_io_read_operations_per_second"
    CGROUP_IO_WRITE_OPERATIONS_PER_SECOND = "cgroup_io_write_operations_per_second"
    CGROUP_IO_WRITTEN_BYTES_PER_SECOND = "cgroup_io_written_bytes_per_second"
    DISK_READ_BYTES_PER_SECOND = "disk_read_bytes_per_second"
    DISK_READ_OPERATIONS_PER_SECOND = "disk_read_operations_per_second"
    DISK_WRITE_OPERATIONS_PER_SECOND = "disk_write_operations_per_second"
    DISK_WRITTEN_BYTES_PER_SECOND = "disk_written_bytes_per_second"
    NETWORK_RECEIVED_BYTES_PER_SECOND = "network_received_bytes_per_second"
    NETWORK_TRANSMITTED_BYTES_PER_SECOND = "network_transmitted_bytes_per_second"

    def __str__(self) -> str:
        return str(self.value)
