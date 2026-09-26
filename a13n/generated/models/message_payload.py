from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.asset_part import AssetPart
    from ..models.json_part import JsonPart
    from ..models.text_part import TextPart
    from ..models.url_part import UrlPart


T = TypeVar("T", bound="MessagePayload")


@_attrs_define(repr=False)
class MessagePayload:
    """
    Attributes:
        content (list[AssetPart | JsonPart | TextPart | UrlPart]):
    """

    content: list[AssetPart | JsonPart | TextPart | UrlPart]

    def to_dict(self) -> dict[str, Any]:
        from ..models.asset_part import AssetPart
        from ..models.text_part import TextPart
        from ..models.url_part import UrlPart

        content = []
        for content_item_data in self.content:
            content_item: dict[str, Any]
            if isinstance(content_item_data, TextPart):
                content_item = content_item_data.to_dict()
            elif isinstance(content_item_data, AssetPart):
                content_item = content_item_data.to_dict()
            elif isinstance(content_item_data, UrlPart):
                content_item = content_item_data.to_dict()
            else:
                content_item = content_item_data.to_dict()

            content.append(content_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "content": content,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.asset_part import AssetPart
        from ..models.json_part import JsonPart
        from ..models.text_part import TextPart
        from ..models.url_part import UrlPart

        d = dict(src_dict)
        content = []
        _content = d.pop("content")
        for content_item_data in _content:

            def _parse_content_item(data: object) -> AssetPart | JsonPart | TextPart | UrlPart:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_part_type_0 = TextPart.from_dict(data)

                    return componentsschemas_part_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_part_type_1 = AssetPart.from_dict(data)

                    return componentsschemas_part_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_part_type_2 = UrlPart.from_dict(data)

                    return componentsschemas_part_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_part_type_3 = JsonPart.from_dict(data)

                return componentsschemas_part_type_3

            content_item = _parse_content_item(content_item_data)

            content.append(content_item)

        message_payload = cls(
            content=content,
        )

        return message_payload
