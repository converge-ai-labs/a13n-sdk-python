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
    SCHEDULE_ARCHIVED = "schedule.archived"
    SCHEDULE_COMPLETED = "schedule.completed"
    SCHEDULE_ENABLED = "schedule.enabled"
    SCHEDULE_OCCURRENCE_CANCELLED = "schedule_occurrence.cancelled"
    SCHEDULE_OCCURRENCE_COMPLETED = "schedule_occurrence.completed"
    SCHEDULE_OCCURRENCE_FAILED = "schedule_occurrence.failed"
    SCHEDULE_OCCURRENCE_SKIPPED = "schedule_occurrence.skipped"
    SCHEDULE_OCCURRENCE_SUBMITTED = "schedule_occurrence.submitted"
    SCHEDULE_PAUSED = "schedule.paused"

    def __str__(self) -> str:
        return str(self.value)
