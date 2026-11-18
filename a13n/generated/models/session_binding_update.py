from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.session_configuration import SessionConfiguration


T = TypeVar("T", bound="SessionBindingUpdate")


@_attrs_define(repr=False)
class SessionBindingUpdate:
    """
    Attributes:
        configuration (SessionConfiguration): Tenant-authored Session policy; Service credentials are not process-
            environment references.
    """

    configuration: SessionConfiguration

    def to_dict(self) -> dict[str, Any]:
        configuration = self.configuration.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "configuration": configuration,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.session_configuration import SessionConfiguration

        d = dict(src_dict)
        configuration = SessionConfiguration.from_dict(d.pop("configuration"))

        session_binding_update = cls(
            configuration=configuration,
        )

        return session_binding_update
