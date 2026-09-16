from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="TokenRatesInput")


@_attrs_define(repr=False)
class TokenRatesInput:
    """USD per million tokens; null is unknown, never free.

    Attributes:
        cache_read (float | None | str | Unset):
        cache_write (float | None | str | Unset):
        input_ (float | None | str | Unset):
        output (float | None | str | Unset):
    """

    cache_read: float | str | Unset | None = UNSET
    cache_write: float | str | Unset | None = UNSET
    input_: float | str | Unset | None = UNSET
    output: float | str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        cache_read: float | str | Unset | None
        if isinstance(self.cache_read, Unset):
            cache_read = UNSET
        else:
            cache_read = self.cache_read

        cache_write: float | str | Unset | None
        if isinstance(self.cache_write, Unset):
            cache_write = UNSET
        else:
            cache_write = self.cache_write

        input_: float | str | Unset | None
        if isinstance(self.input_, Unset):
            input_ = UNSET
        else:
            input_ = self.input_

        output: float | str | Unset | None
        if isinstance(self.output, Unset):
            output = UNSET
        else:
            output = self.output

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if cache_read is not UNSET:
            field_dict["cache_read"] = cache_read
        if cache_write is not UNSET:
            field_dict["cache_write"] = cache_write
        if input_ is not UNSET:
            field_dict["input"] = input_
        if output is not UNSET:
            field_dict["output"] = output

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_cache_read(data: object) -> float | str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset | None, data)

        cache_read = _parse_cache_read(d.pop("cache_read", UNSET))

        def _parse_cache_write(data: object) -> float | str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset | None, data)

        cache_write = _parse_cache_write(d.pop("cache_write", UNSET))

        def _parse_input_(data: object) -> float | str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset | None, data)

        input_ = _parse_input_(d.pop("input", UNSET))

        def _parse_output(data: object) -> float | str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | str | Unset | None, data)

        output = _parse_output(d.pop("output", UNSET))

        token_rates_input = cls(
            cache_read=cache_read,
            cache_write=cache_write,
            input_=input_,
            output=output,
        )

        return token_rates_input
