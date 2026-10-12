"""Per-task dispatch provenance for authored mutation acknowledgements."""

from collections.abc import Iterator
from contextlib import contextmanager
from contextvars import ContextVar
from dataclasses import dataclass

from .errors import ApiError, UnknownOutcomeError


@dataclass
class _Mutation:
    dispatched: bool = False
    evidence: object | None = None


_current: ContextVar[_Mutation | None] = ContextVar("a13n_mutation", default=None)


def mark_dispatch() -> None:
    state = _current.get()
    if state is not None:
        state.dispatched = True


@contextmanager
def mutation(
    key: str, operation: str, *, thread_id: str | None = None, run_id: str | None = None
) -> Iterator[_Mutation]:
    state = _Mutation()
    token = _current.set(state)
    try:
        yield state
    except ApiError:
        raise
    except Exception as cause:
        if not state.dispatched:
            raise
        raise UnknownOutcomeError(key, operation, thread_id, run_id, state.evidence) from cause
    finally:
        _current.reset(token)
