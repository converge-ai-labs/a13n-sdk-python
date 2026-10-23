from enum import StrEnum


class TypedQueryMetricType0(StrEnum):
    CGROUP_MEMORY_CURRENT_BYTES = "cgroup_memory_current_bytes"
    CGROUP_PIDS_CURRENT = "cgroup_pids_current"
    DAEMON_CONNECTIONS = "daemon_connections"
    DAEMON_PROCESSES = "daemon_processes"
    DAEMON_RETAINED_OUTPUT_BYTES = "daemon_retained_output_bytes"
    DAEMON_SESSIONS = "daemon_sessions"
    DAEMON_TRANSFERS = "daemon_transfers"
    SYSTEM_COMMIT_LIMIT_BYTES = "system_commit_limit_bytes"
    SYSTEM_COMMIT_TOTAL_BYTES = "system_commit_total_bytes"
    SYSTEM_CPU_BUSY_RATIO = "system_cpu_busy_ratio"
    SYSTEM_HANDLES = "system_handles"
    SYSTEM_MEMORY_AVAILABLE_BYTES = "system_memory_available_bytes"
    SYSTEM_MEMORY_CACHE_BYTES = "system_memory_cache_bytes"
    SYSTEM_MEMORY_COMPRESSED_BYTES = "system_memory_compressed_bytes"
    SYSTEM_MEMORY_TOTAL_BYTES = "system_memory_total_bytes"
    SYSTEM_MEMORY_USED_BYTES = "system_memory_used_bytes"
    SYSTEM_MEMORY_WIRED_BYTES = "system_memory_wired_bytes"
    SYSTEM_PROCESSES = "system_processes"
    SYSTEM_SWAP_TOTAL_BYTES = "system_swap_total_bytes"
    SYSTEM_SWAP_USED_BYTES = "system_swap_used_bytes"
    SYSTEM_THREADS = "system_threads"
    TCP_CONNECTIONS = "tcp_connections"
    UDP_SOCKETS = "udp_sockets"

    def __str__(self) -> str:
        return str(self.value)
