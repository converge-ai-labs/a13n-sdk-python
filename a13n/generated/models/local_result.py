from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.export_health import ExportHealth
    from ..models.history import History
    from ..models.observation import Observation


T = TypeVar("T", bound="LocalResult")


@_attrs_define(repr=False)
class LocalResult:
    """
    Attributes:
        history (History):
        observation (Observation):
        export (ExportHealth | None | Unset):
        source (Literal['temporary'] | Unset):
    """

    history: History
    observation: Observation
    export: ExportHealth | Unset | None = UNSET
    source: Literal["temporary"] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.export_health import ExportHealth

        history = self.history.to_dict()

        observation = self.observation.to_dict()

        export: dict[str, Any] | Unset | None
        if isinstance(self.export, Unset):
            export = UNSET
        elif isinstance(self.export, ExportHealth):
            export = self.export.to_dict()
        else:
            export = self.export

        source = self.source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "history": history,
                "observation": observation,
            }
        )
        if export is not UNSET:
            field_dict["export"] = export
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.export_health import ExportHealth
        from ..models.history import History
        from ..models.observation import Observation

        d = dict(src_dict)
        history = History.from_dict(d.pop("history"))

        observation = Observation.from_dict(d.pop("observation"))

        def _parse_export(data: object) -> ExportHealth | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                export_type_0 = ExportHealth.from_dict(data)

                return export_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ExportHealth | Unset | None, data)

        export = _parse_export(d.pop("export", UNSET))

        source = cast(Literal["temporary"] | Unset, d.pop("source", UNSET))
        if source != "temporary" and not isinstance(source, Unset):
            raise ValueError(f"source must match const 'temporary', got '{source}'")

        local_result = cls(
            history=history,
            observation=observation,
            export=export,
            source=source,
        )

        local_result.additional_properties = d
        return local_result

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
