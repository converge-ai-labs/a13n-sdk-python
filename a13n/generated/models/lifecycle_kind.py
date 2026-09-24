from enum import StrEnum


class LifecycleKind(StrEnum):
    RUN_ACCEPTED = "run.accepted"
    RUN_ATTEMPT_CANCELLED = "run_attempt.cancelled"
    RUN_ATTEMPT_FAILED = "run_attempt.failed"
    RUN_ATTEMPT_LEASED = "run_attempt.leased"
    RUN_ATTEMPT_RUNNING = "run_attempt.running"
    RUN_ATTEMPT_SUCCEEDED = "run_attempt.succeeded"
    RUN_ATTEMPT_YIELDED = "run_attempt.yielded"
    RUN_CANCELLED = "run.cancelled"
    RUN_COMPLETED = "run.completed"
    RUN_FAILED = "run.failed"
    RUN_RUNNING = "run.running"
    RUN_WAITING = "run.waiting"

    def __str__(self) -> str:
        return str(self.value)
