from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.egress_mode import EgressMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.disabled_sandbox import DisabledSandbox
    from ..models.egress_configuration import EgressConfiguration
    from ..models.native_isolation import NativeIsolation
    from ..models.restricted_sandbox import RestrictedSandbox
    from ..models.session_lifecycle_policy import SessionLifecyclePolicy
    from ..models.vm_isolation import VmIsolation


T = TypeVar("T", bound="SessionConfiguration")


@_attrs_define(repr=False)
class SessionConfiguration:
    """Tenant-authored Session policy; Service credentials are not process-environment references.

    Attributes:
        commands (bool | None | Unset):
        egress (EgressConfiguration | None | Unset):
        egress_mode (EgressMode | None | Unset):
        isolation (NativeIsolation | None | Unset | VmIsolation):
        lifecycle (None | SessionLifecyclePolicy | Unset):
        sandbox (DisabledSandbox | None | RestrictedSandbox | Unset):
        working_directory (None | str | Unset):
    """

    commands: bool | Unset | None = UNSET
    egress: EgressConfiguration | Unset | None = UNSET
    egress_mode: EgressMode | Unset | None = UNSET
    isolation: NativeIsolation | Unset | VmIsolation | None = UNSET
    lifecycle: SessionLifecyclePolicy | Unset | None = UNSET
    sandbox: DisabledSandbox | RestrictedSandbox | Unset | None = UNSET
    working_directory: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.disabled_sandbox import DisabledSandbox
        from ..models.egress_configuration import EgressConfiguration
        from ..models.native_isolation import NativeIsolation
        from ..models.restricted_sandbox import RestrictedSandbox
        from ..models.session_lifecycle_policy import SessionLifecyclePolicy
        from ..models.vm_isolation import VmIsolation

        commands: bool | Unset | None
        if isinstance(self.commands, Unset):
            commands = UNSET
        else:
            commands = self.commands

        egress: dict[str, Any] | Unset | None
        if isinstance(self.egress, Unset):
            egress = UNSET
        elif isinstance(self.egress, EgressConfiguration):
            egress = self.egress.to_dict()
        else:
            egress = self.egress

        egress_mode: str | Unset | None
        if isinstance(self.egress_mode, Unset):
            egress_mode = UNSET
        elif isinstance(self.egress_mode, EgressMode):
            egress_mode = self.egress_mode.value
        else:
            egress_mode = self.egress_mode

        isolation: dict[str, Any] | Unset | None
        if isinstance(self.isolation, Unset):
            isolation = UNSET
        elif isinstance(self.isolation, NativeIsolation):
            isolation = self.isolation.to_dict()
        elif isinstance(self.isolation, VmIsolation):
            isolation = self.isolation.to_dict()
        else:
            isolation = self.isolation

        lifecycle: dict[str, Any] | Unset | None
        if isinstance(self.lifecycle, Unset):
            lifecycle = UNSET
        elif isinstance(self.lifecycle, SessionLifecyclePolicy):
            lifecycle = self.lifecycle.to_dict()
        else:
            lifecycle = self.lifecycle

        sandbox: dict[str, Any] | Unset | None
        if isinstance(self.sandbox, Unset):
            sandbox = UNSET
        elif isinstance(self.sandbox, DisabledSandbox):
            sandbox = self.sandbox.to_dict()
        elif isinstance(self.sandbox, RestrictedSandbox):
            sandbox = self.sandbox.to_dict()
        else:
            sandbox = self.sandbox

        working_directory: str | Unset | None
        if isinstance(self.working_directory, Unset):
            working_directory = UNSET
        else:
            working_directory = self.working_directory

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if commands is not UNSET:
            field_dict["commands"] = commands
        if egress is not UNSET:
            field_dict["egress"] = egress
        if egress_mode is not UNSET:
            field_dict["egress_mode"] = egress_mode
        if isolation is not UNSET:
            field_dict["isolation"] = isolation
        if lifecycle is not UNSET:
            field_dict["lifecycle"] = lifecycle
        if sandbox is not UNSET:
            field_dict["sandbox"] = sandbox
        if working_directory is not UNSET:
            field_dict["working_directory"] = working_directory

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.disabled_sandbox import DisabledSandbox
        from ..models.egress_configuration import EgressConfiguration
        from ..models.native_isolation import NativeIsolation
        from ..models.restricted_sandbox import RestrictedSandbox
        from ..models.session_lifecycle_policy import SessionLifecyclePolicy
        from ..models.vm_isolation import VmIsolation

        d = dict(src_dict)

        def _parse_commands(data: object) -> bool | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | Unset | None, data)

        commands = _parse_commands(d.pop("commands", UNSET))

        def _parse_egress(data: object) -> EgressConfiguration | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                egress_type_0 = EgressConfiguration.from_dict(data)

                return egress_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EgressConfiguration | Unset | None, data)

        egress = _parse_egress(d.pop("egress", UNSET))

        def _parse_egress_mode(data: object) -> EgressMode | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                egress_mode_type_0 = EgressMode(data)

                return egress_mode_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(EgressMode | Unset | None, data)

        egress_mode = _parse_egress_mode(d.pop("egress_mode", UNSET))

        def _parse_isolation(data: object) -> NativeIsolation | Unset | VmIsolation | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_session_isolation_type_0 = NativeIsolation.from_dict(data)

                return componentsschemas_session_isolation_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_session_isolation_type_1 = VmIsolation.from_dict(data)

                return componentsschemas_session_isolation_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NativeIsolation | Unset | VmIsolation | None, data)

        isolation = _parse_isolation(d.pop("isolation", UNSET))

        def _parse_lifecycle(data: object) -> SessionLifecyclePolicy | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                lifecycle_type_0 = SessionLifecyclePolicy.from_dict(data)

                return lifecycle_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(SessionLifecyclePolicy | Unset | None, data)

        lifecycle = _parse_lifecycle(d.pop("lifecycle", UNSET))

        def _parse_sandbox(data: object) -> DisabledSandbox | RestrictedSandbox | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_sandbox_policy_type_0 = DisabledSandbox.from_dict(data)

                return componentsschemas_sandbox_policy_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_sandbox_policy_type_1 = RestrictedSandbox.from_dict(data)

                return componentsschemas_sandbox_policy_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DisabledSandbox | RestrictedSandbox | Unset | None, data)

        sandbox = _parse_sandbox(d.pop("sandbox", UNSET))

        def _parse_working_directory(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        working_directory = _parse_working_directory(d.pop("working_directory", UNSET))

        session_configuration = cls(
            commands=commands,
            egress=egress,
            egress_mode=egress_mode,
            isolation=isolation,
            lifecycle=lifecycle,
            sandbox=sandbox,
            working_directory=working_directory,
        )

        return session_configuration
