from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.image_test_response_image_source_type_0 import ImageTestResponseImageSourceType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageTestResponse")


@_attrs_define(repr=False)
class ImageTestResponse:
    """
    Attributes:
        checks (list[str] | Unset):
        configuration_hash (None | str | Unset):
        error (None | str | Unset):
        image_id (None | str | Unset):
        image_source (ImageTestResponseImageSourceType0 | None | Unset):
    """

    checks: list[str] | Unset = UNSET
    configuration_hash: str | Unset | None = UNSET
    error: str | Unset | None = UNSET
    image_id: str | Unset | None = UNSET
    image_source: ImageTestResponseImageSourceType0 | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        checks: list[str] | Unset = UNSET
        if not isinstance(self.checks, Unset):
            checks = self.checks

        configuration_hash: str | Unset | None
        if isinstance(self.configuration_hash, Unset):
            configuration_hash = UNSET
        else:
            configuration_hash = self.configuration_hash

        error: str | Unset | None
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        image_id: str | Unset | None
        if isinstance(self.image_id, Unset):
            image_id = UNSET
        else:
            image_id = self.image_id

        image_source: str | Unset | None
        if isinstance(self.image_source, Unset):
            image_source = UNSET
        elif isinstance(self.image_source, ImageTestResponseImageSourceType0):
            image_source = self.image_source.value
        else:
            image_source = self.image_source

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if checks is not UNSET:
            field_dict["checks"] = checks
        if configuration_hash is not UNSET:
            field_dict["configuration_hash"] = configuration_hash
        if error is not UNSET:
            field_dict["error"] = error
        if image_id is not UNSET:
            field_dict["image_id"] = image_id
        if image_source is not UNSET:
            field_dict["image_source"] = image_source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        checks = cast(list[str], d.pop("checks", UNSET))

        def _parse_configuration_hash(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        configuration_hash = _parse_configuration_hash(d.pop("configuration_hash", UNSET))

        def _parse_error(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        error = _parse_error(d.pop("error", UNSET))

        def _parse_image_id(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        image_id = _parse_image_id(d.pop("image_id", UNSET))

        def _parse_image_source(data: object) -> ImageTestResponseImageSourceType0 | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                image_source_type_0 = ImageTestResponseImageSourceType0(data)

                return image_source_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImageTestResponseImageSourceType0 | Unset | None, data)

        image_source = _parse_image_source(d.pop("image_source", UNSET))

        image_test_response = cls(
            checks=checks,
            configuration_hash=configuration_hash,
            error=error,
            image_id=image_id,
            image_source=image_source,
        )

        return image_test_response
