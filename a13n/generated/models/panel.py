from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..models.panel_unit import PanelUnit
from ..models.panel_visualization import PanelVisualization
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.position import Position
    from ..models.prom_ql_query import PromQLQuery
    from ..models.typed_query import TypedQuery


T = TypeVar("T", bound="Panel")


@_attrs_define(repr=False)
class Panel:
    """
    Attributes:
        id (str):
        position (Position):
        queries (list[PromQLQuery | TypedQuery]):
        title (str):
        description (str | Unset):
        legend (bool | Unset):
        unit (PanelUnit | Unset):
        visualization (PanelVisualization | Unset):
    """

    id: str
    position: Position
    queries: list[PromQLQuery | TypedQuery]
    title: str
    description: str | Unset = UNSET
    legend: bool | Unset = UNSET
    unit: PanelUnit | Unset = UNSET
    visualization: PanelVisualization | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.typed_query import TypedQuery

        id = self.id

        position = self.position.to_dict()

        queries = []
        for queries_item_data in self.queries:
            queries_item: dict[str, Any]
            if isinstance(queries_item_data, TypedQuery):
                queries_item = queries_item_data.to_dict()
            else:
                queries_item = queries_item_data.to_dict()

            queries.append(queries_item)

        title = self.title

        description = self.description

        legend = self.legend

        unit: str | Unset = UNSET
        if not isinstance(self.unit, Unset):
            unit = self.unit.value

        visualization: str | Unset = UNSET
        if not isinstance(self.visualization, Unset):
            visualization = self.visualization.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "position": position,
                "queries": queries,
                "title": title,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if legend is not UNSET:
            field_dict["legend"] = legend
        if unit is not UNSET:
            field_dict["unit"] = unit
        if visualization is not UNSET:
            field_dict["visualization"] = visualization

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.position import Position
        from ..models.prom_ql_query import PromQLQuery
        from ..models.typed_query import TypedQuery

        d = dict(src_dict)
        id = d.pop("id")

        position = Position.from_dict(d.pop("position"))

        queries = []
        _queries = d.pop("queries")
        for queries_item_data in _queries:

            def _parse_queries_item(data: object) -> PromQLQuery | TypedQuery:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_panel_query_type_0 = TypedQuery.from_dict(data)

                    return componentsschemas_panel_query_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_panel_query_type_1 = PromQLQuery.from_dict(data)

                return componentsschemas_panel_query_type_1

            queries_item = _parse_queries_item(queries_item_data)

            queries.append(queries_item)

        title = d.pop("title")

        description = d.pop("description", UNSET)

        legend = d.pop("legend", UNSET)

        _unit = d.pop("unit", UNSET)
        unit: PanelUnit | Unset
        if isinstance(_unit, Unset):
            unit = UNSET
        else:
            unit = PanelUnit(_unit)

        _visualization = d.pop("visualization", UNSET)
        visualization: PanelVisualization | Unset
        if isinstance(_visualization, Unset):
            visualization = UNSET
        else:
            visualization = PanelVisualization(_visualization)

        panel = cls(
            id=id,
            position=position,
            queries=queries,
            title=title,
            description=description,
            legend=legend,
            unit=unit,
            visualization=visualization,
        )

        return panel
