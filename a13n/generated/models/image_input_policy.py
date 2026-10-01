from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ImageInputPolicy")


@_attrs_define(repr=False)
class ImageInputPolicy:
    """Preparation limits for one model's image input, not native ModelSettings.

    Attributes:
        image_split_max_height (int | Unset):
        image_split_overlap (int | Unset):
        max_image_bytes (int | Unset): Maximum base64-encoded bytes per image; zero disables this byte limit.
        max_image_dimension (int | Unset): Maximum image axis; zero disables this limit.
        max_images (int | Unset): Keep the newest images; zero removes all image input.
        split_large_images (bool | Unset):
        support_gif (bool | Unset):
    """

    image_split_max_height: int | Unset = UNSET
    image_split_overlap: int | Unset = UNSET
    max_image_bytes: int | Unset = UNSET
    max_image_dimension: int | Unset = UNSET
    max_images: int | Unset = UNSET
    split_large_images: bool | Unset = UNSET
    support_gif: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        image_split_max_height = self.image_split_max_height

        image_split_overlap = self.image_split_overlap

        max_image_bytes = self.max_image_bytes

        max_image_dimension = self.max_image_dimension

        max_images = self.max_images

        split_large_images = self.split_large_images

        support_gif = self.support_gif

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if image_split_max_height is not UNSET:
            field_dict["image_split_max_height"] = image_split_max_height
        if image_split_overlap is not UNSET:
            field_dict["image_split_overlap"] = image_split_overlap
        if max_image_bytes is not UNSET:
            field_dict["max_image_bytes"] = max_image_bytes
        if max_image_dimension is not UNSET:
            field_dict["max_image_dimension"] = max_image_dimension
        if max_images is not UNSET:
            field_dict["max_images"] = max_images
        if split_large_images is not UNSET:
            field_dict["split_large_images"] = split_large_images
        if support_gif is not UNSET:
            field_dict["support_gif"] = support_gif

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        image_split_max_height = d.pop("image_split_max_height", UNSET)

        image_split_overlap = d.pop("image_split_overlap", UNSET)

        max_image_bytes = d.pop("max_image_bytes", UNSET)

        max_image_dimension = d.pop("max_image_dimension", UNSET)

        max_images = d.pop("max_images", UNSET)

        split_large_images = d.pop("split_large_images", UNSET)

        support_gif = d.pop("support_gif", UNSET)

        image_input_policy = cls(
            image_split_max_height=image_split_max_height,
            image_split_overlap=image_split_overlap,
            max_image_bytes=max_image_bytes,
            max_image_dimension=max_image_dimension,
            max_images=max_images,
            split_large_images=split_large_images,
            support_gif=support_gif,
        )

        return image_input_policy
