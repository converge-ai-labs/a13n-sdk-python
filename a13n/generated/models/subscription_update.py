from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.lifecycle_kind import LifecycleKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subscription_filter import SubscriptionFilter


T = TypeVar("T", bound="SubscriptionUpdate")


@_attrs_define(repr=False)
class SubscriptionUpdate:
    """`signing_secret` replaces the secret for deliveries queued after this change.

    Attributes:
        enabled (bool | None | Unset):
        filter_ (None | SubscriptionFilter | Unset):
        kinds (list[LifecycleKind] | None | Unset):
        name (None | str | Unset):
        signing_secret (None | str | Unset):
        url (None | str | Unset):
    """

    enabled: bool | Unset | None = UNSET
    filter_: SubscriptionFilter | Unset | None = UNSET
    kinds: list[LifecycleKind] | Unset | None = UNSET
    name: str | Unset | None = UNSET
    signing_secret: str | Unset | None = UNSET
    url: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.subscription_filter import SubscriptionFilter

        enabled: bool | Unset | None
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        filter_: dict[str, Any] | Unset | None
        if isinstance(self.filter_, Unset):
            filter_ = UNSET
        elif isinstance(self.filter_, SubscriptionFilter):
            filter_ = self.filter_.to_dict()
        else:
            filter_ = self.filter_

        kinds: list[str] | Unset | None
        if isinstance(self.kinds, Unset):
            kinds = UNSET
        elif isinstance(self.kinds, list):
            kinds = []
            for kinds_type_0_item_data in self.kinds:
                kinds_type_0_item = kinds_type_0_item_data.value
                kinds.append(kinds_type_0_item)

        else:
            kinds = self.kinds

        name: str | Unset | None
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        signing_secret: str | Unset | None
        if isinstance(self.signing_secret, Unset):
            signing_secret = UNSET
        else:
            signing_secret = self.signing_secret

        url: str | Unset | None
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        field_dict: dict[str, Any] = {}

        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if kinds is not UNSET:
            field_dict["kinds"] = kinds
        if name is not UNSET:
            field_dict["name"] = name
        if signing_secret is not UNSET:
            field_dict["signing_secret"] = signing_secret
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subscription_filter import SubscriptionFilter

        d = dict(src_dict)

        def _parse_enabled(data: object) -> bool | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | Unset | None, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        def _parse_filter_(data: object) -> SubscriptionFilter | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                filter_type_0 = SubscriptionFilter.from_dict(data)

                return filter_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(SubscriptionFilter | Unset | None, data)

        filter_ = _parse_filter_(d.pop("filter", UNSET))

        def _parse_kinds(data: object) -> list[LifecycleKind] | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                kinds_type_0 = []
                _kinds_type_0 = data
                for kinds_type_0_item_data in _kinds_type_0:
                    kinds_type_0_item = LifecycleKind(kinds_type_0_item_data)

                    kinds_type_0.append(kinds_type_0_item)

                return kinds_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LifecycleKind] | Unset | None, data)

        kinds = _parse_kinds(d.pop("kinds", UNSET))

        def _parse_name(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_signing_secret(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        signing_secret = _parse_signing_secret(d.pop("signing_secret", UNSET))

        def _parse_url(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        url = _parse_url(d.pop("url", UNSET))

        subscription_update = cls(
            enabled=enabled,
            filter_=filter_,
            kinds=kinds,
            name=name,
            signing_secret=signing_secret,
            url=url,
        )

        return subscription_update
