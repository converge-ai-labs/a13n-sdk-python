from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.model_capability import ModelCapability
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image_input_policy import ImageInputPolicy
    from ..models.url_input_support_input import UrlInputSupportInput
    from ..models.video_input_policy import VideoInputPolicy


T = TypeVar("T", bound="HarnessModelCharacteristicsInput")


@_attrs_define(repr=False)
class HarnessModelCharacteristicsInput:
    """Resolved Harness characteristics of the active Agent model.

    Attributes:
        capabilities (list[ModelCapability] | Unset):
        compact_threshold (float | Unset):
        context_window_tokens (int | None | Unset):
        image_input (ImageInputPolicy | None | Unset): Image preparation policy; omitted uses native defaults, null
            disables automatic preparation.
        proactive_context_management_threshold (float | None | Unset):
        url_input (UrlInputSupportInput | Unset): URL subtypes consumed natively by the selected transport.
        video_input (VideoInputPolicy | Unset): Base64-after byte budget for both one video and all inline videos in a
            request.
    """

    capabilities: list[ModelCapability] | Unset = UNSET
    compact_threshold: float | Unset = UNSET
    context_window_tokens: int | Unset | None = UNSET
    image_input: ImageInputPolicy | Unset | None = UNSET
    proactive_context_management_threshold: float | Unset | None = UNSET
    url_input: UrlInputSupportInput | Unset = UNSET
    video_input: VideoInputPolicy | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.image_input_policy import ImageInputPolicy

        capabilities: list[str] | Unset = UNSET
        if not isinstance(self.capabilities, Unset):
            capabilities = []
            for capabilities_item_data in self.capabilities:
                capabilities_item = capabilities_item_data.value
                capabilities.append(capabilities_item)

        compact_threshold = self.compact_threshold

        context_window_tokens: int | Unset | None
        if isinstance(self.context_window_tokens, Unset):
            context_window_tokens = UNSET
        else:
            context_window_tokens = self.context_window_tokens

        image_input: dict[str, Any] | Unset | None
        if isinstance(self.image_input, Unset):
            image_input = UNSET
        elif isinstance(self.image_input, ImageInputPolicy):
            image_input = self.image_input.to_dict()
        else:
            image_input = self.image_input

        proactive_context_management_threshold: float | Unset | None
        if isinstance(self.proactive_context_management_threshold, Unset):
            proactive_context_management_threshold = UNSET
        else:
            proactive_context_management_threshold = self.proactive_context_management_threshold

        url_input: dict[str, Any] | Unset = UNSET
        if not isinstance(self.url_input, Unset):
            url_input = self.url_input.to_dict()

        video_input: dict[str, Any] | Unset = UNSET
        if not isinstance(self.video_input, Unset):
            video_input = self.video_input.to_dict()

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if capabilities is not UNSET:
            field_dict["capabilities"] = capabilities
        if compact_threshold is not UNSET:
            field_dict["compact_threshold"] = compact_threshold
        if context_window_tokens is not UNSET:
            field_dict["context_window_tokens"] = context_window_tokens
        if image_input is not UNSET:
            field_dict["image_input"] = image_input
        if proactive_context_management_threshold is not UNSET:
            field_dict["proactive_context_management_threshold"] = proactive_context_management_threshold
        if url_input is not UNSET:
            field_dict["url_input"] = url_input
        if video_input is not UNSET:
            field_dict["video_input"] = video_input

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image_input_policy import ImageInputPolicy
        from ..models.url_input_support_input import UrlInputSupportInput
        from ..models.video_input_policy import VideoInputPolicy

        d = dict(src_dict)
        _capabilities = d.pop("capabilities", UNSET)
        capabilities: list[ModelCapability] | Unset = UNSET
        if _capabilities is not UNSET:
            capabilities = []
            for capabilities_item_data in _capabilities:
                capabilities_item = ModelCapability(capabilities_item_data)

                capabilities.append(capabilities_item)

        compact_threshold = d.pop("compact_threshold", UNSET)

        def _parse_context_window_tokens(data: object) -> int | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | Unset | None, data)

        context_window_tokens = _parse_context_window_tokens(d.pop("context_window_tokens", UNSET))

        def _parse_image_input(data: object) -> ImageInputPolicy | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                image_input_type_0 = ImageInputPolicy.from_dict(data)

                return image_input_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImageInputPolicy | Unset | None, data)

        image_input = _parse_image_input(d.pop("image_input", UNSET))

        def _parse_proactive_context_management_threshold(data: object) -> float | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | Unset | None, data)

        proactive_context_management_threshold = _parse_proactive_context_management_threshold(
            d.pop("proactive_context_management_threshold", UNSET)
        )

        _url_input = d.pop("url_input", UNSET)
        url_input: UrlInputSupportInput | Unset
        if isinstance(_url_input, Unset):
            url_input = UNSET
        else:
            url_input = UrlInputSupportInput.from_dict(_url_input)

        _video_input = d.pop("video_input", UNSET)
        video_input: VideoInputPolicy | Unset
        if isinstance(_video_input, Unset):
            video_input = UNSET
        else:
            video_input = VideoInputPolicy.from_dict(_video_input)

        harness_model_characteristics_input = cls(
            capabilities=capabilities,
            compact_threshold=compact_threshold,
            context_window_tokens=context_window_tokens,
            image_input=image_input,
            proactive_context_management_threshold=proactive_context_management_threshold,
            url_input=url_input,
            video_input=video_input,
        )

        return harness_model_characteristics_input
