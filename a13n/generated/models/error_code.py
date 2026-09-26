from enum import StrEnum


class ErrorCode(StrEnum):
    ALREADY_EXISTS = "already_exists"
    CONFLICT = "conflict"
    DISABLED = "disabled"
    FORBIDDEN = "forbidden"
    INTERNAL = "internal"
    INVALID_ARGUMENT = "invalid_argument"
    INVALID_CURSOR = "invalid_cursor"
    NOT_FOUND = "not_found"
    PAYLOAD_TOO_LARGE = "payload_too_large"
    PRECONDITION_FAILED = "precondition_failed"
    PRECONDITION_REQUIRED = "precondition_required"
    RATE_LIMITED = "rate_limited"
    REQUEST_TIMEOUT = "request_timeout"
    UNAUTHENTICATED = "unauthenticated"
    UNAVAILABLE = "unavailable"

    def __str__(self) -> str:
        return str(self.value)
