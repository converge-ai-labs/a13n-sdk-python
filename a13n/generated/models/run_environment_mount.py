from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.environment_access import EnvironmentAccess
from ..models.mount_application_status import MountApplicationStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.principal_ref import PrincipalRef
    from ..models.safe_failure import SafeFailure


T = TypeVar("T", bound="RunEnvironmentMount")


@_attrs_define(repr=False)
class RunEnvironmentMount:
    """
    Attributes:
        accepting_principal (PrincipalRef):
        access (EnvironmentAccess):
        created_at (datetime.datetime):
        environment_id (str):
        name (str):
        run_id (str):
        application_status (MountApplicationStatus | Unset):
        applied_attempt_fence (int | None | Unset):
        applied_attempt_id (None | str | Unset):
        error (None | SafeFailure | Unset):
        observed_at (datetime.datetime | None | Unset):
        use_started_at (datetime.datetime | None | Unset):
    """

    accepting_principal: PrincipalRef
    access: EnvironmentAccess
    created_at: datetime.datetime
    environment_id: str
    name: str
    run_id: str
    application_status: MountApplicationStatus | Unset = UNSET
    applied_attempt_fence: int | Unset | None = UNSET
    applied_attempt_id: str | Unset | None = UNSET
    error: SafeFailure | Unset | None = UNSET
    observed_at: datetime.datetime | Unset | None = UNSET
    use_started_at: datetime.datetime | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.safe_failure import SafeFailure

        accepting_principal = self.accepting_principal.to_dict()

        access = self.access.value

        created_at = self.created_at.isoformat()

        environment_id = self.environment_id

        name = self.name

        run_id = self.run_id

        application_status: str | Unset = UNSET
        if not isinstance(self.application_status, Unset):
            application_status = self.application_status.value

        applied_attempt_fence: int | Unset | None
        if isinstance(self.applied_attempt_fence, Unset):
            applied_attempt_fence = UNSET
        else:
            applied_attempt_fence = self.applied_attempt_fence

        applied_attempt_id: str | Unset | None
        if isinstance(self.applied_attempt_id, Unset):
            applied_attempt_id = UNSET
        else:
            applied_attempt_id = self.applied_attempt_id

        error: dict[str, Any] | Unset | None
        if isinstance(self.error, Unset):
            error = UNSET
        elif isinstance(self.error, SafeFailure):
            error = self.error.to_dict()
        else:
            error = self.error

        observed_at: str | Unset | None
        if isinstance(self.observed_at, Unset):
            observed_at = UNSET
        elif isinstance(self.observed_at, datetime.datetime):
            observed_at = self.observed_at.isoformat()
        else:
            observed_at = self.observed_at

        use_started_at: str | Unset | None
        if isinstance(self.use_started_at, Unset):
            use_started_at = UNSET
        elif isinstance(self.use_started_at, datetime.datetime):
            use_started_at = self.use_started_at.isoformat()
        else:
            use_started_at = self.use_started_at

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "accepting_principal": accepting_principal,
                "access": access,
                "created_at": created_at,
                "environment_id": environment_id,
                "name": name,
                "run_id": run_id,
            }
        )
        if application_status is not UNSET:
            field_dict["application_status"] = application_status
        if applied_attempt_fence is not UNSET:
            field_dict["applied_attempt_fence"] = applied_attempt_fence
        if applied_attempt_id is not UNSET:
            field_dict["applied_attempt_id"] = applied_attempt_id
        if error is not UNSET:
            field_dict["error"] = error
        if observed_at is not UNSET:
            field_dict["observed_at"] = observed_at
        if use_started_at is not UNSET:
            field_dict["use_started_at"] = use_started_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.principal_ref import PrincipalRef
        from ..models.safe_failure import SafeFailure

        d = dict(src_dict)
        accepting_principal = PrincipalRef.from_dict(d.pop("accepting_principal"))

        access = EnvironmentAccess(d.pop("access"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        environment_id = d.pop("environment_id")

        name = d.pop("name")

        run_id = d.pop("run_id")

        _application_status = d.pop("application_status", UNSET)
        application_status: MountApplicationStatus | Unset
        if isinstance(_application_status, Unset):
            application_status = UNSET
        else:
            application_status = MountApplicationStatus(_application_status)

        def _parse_applied_attempt_fence(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        applied_attempt_fence = _parse_applied_attempt_fence(d.pop("applied_attempt_fence", UNSET))

        def _parse_applied_attempt_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        applied_attempt_id = _parse_applied_attempt_id(d.pop("applied_attempt_id", UNSET))

        def _parse_error(data: object) -> SafeFailure | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_0 = SafeFailure.from_dict(data)

                return error_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(SafeFailure | Unset | None, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_observed_at(data: object) -> datetime.datetime | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                observed_at_type_0 = datetime.datetime.fromisoformat(data)

                return observed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | Unset | None, data)

        observed_at = _parse_observed_at(d.pop("observed_at", UNSET))

        def _parse_use_started_at(data: object) -> datetime.datetime | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                use_started_at_type_0 = datetime.datetime.fromisoformat(data)

                return use_started_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | Unset | None, data)

        use_started_at = _parse_use_started_at(d.pop("use_started_at", UNSET))

        run_environment_mount = cls(
            accepting_principal=accepting_principal,
            access=access,
            created_at=created_at,
            environment_id=environment_id,
            name=name,
            run_id=run_id,
            application_status=application_status,
            applied_attempt_fence=applied_attempt_fence,
            applied_attempt_id=applied_attempt_id,
            error=error,
            observed_at=observed_at,
            use_started_at=use_started_at,
        )

        return run_environment_mount
