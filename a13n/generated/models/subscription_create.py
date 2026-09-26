from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.lifecycle_kind import LifecycleKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subscription_filter import SubscriptionFilter


T = TypeVar("T", bound="SubscriptionCreate")


@_attrs_define(repr=False)
class SubscriptionCreate:
    """Without `signing_secret` the service generates one; either way it is returned only by this request.

    Attributes:
        kinds (list[LifecycleKind]):
        name (str):
        url (str):
        enabled (bool | Unset):
        filter_ (SubscriptionFilter | Unset): Absent fields match every run.
        signing_secret (None | str | Unset):
    """

    kinds: list[LifecycleKind]
    name: str
    url: str
    enabled: bool | Unset = UNSET
    filter_: SubscriptionFilter | Unset = UNSET
    signing_secret: str | Unset | None = UNSET

    def to_dict(self) -> dict[str, Any]:
        kinds = []
        for kinds_item_data in self.kinds:
            kinds_item = kinds_item_data.value
            kinds.append(kinds_item)

        name = self.name

        url = self.url

        enabled = self.enabled

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()

        signing_secret: str | Unset | None
        if isinstance(self.signing_secret, Unset):
            signing_secret = UNSET
        else:
            signing_secret = self.signing_secret

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "kinds": kinds,
                "name": name,
                "url": url,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if filter_ is not UNSET:
            field_dict["filter"] = filter_
        if signing_secret is not UNSET:
            field_dict["signing_secret"] = signing_secret

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subscription_filter import SubscriptionFilter

        d = dict(src_dict)
        kinds = []
        _kinds = d.pop("kinds")
        for kinds_item_data in _kinds:
            kinds_item = LifecycleKind(kinds_item_data)

            kinds.append(kinds_item)

        name = d.pop("name")

        url = d.pop("url")

        enabled = d.pop("enabled", UNSET)

        _filter_ = d.pop("filter", UNSET)
        filter_: SubscriptionFilter | Unset
        if isinstance(_filter_, Unset):
            filter_ = UNSET
        else:
            filter_ = SubscriptionFilter.from_dict(_filter_)

        def _parse_signing_secret(data: object) -> str | Unset | None:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(str | Unset | None, data)

        signing_secret = _parse_signing_secret(d.pop("signing_secret", UNSET))

        subscription_create = cls(
            kinds=kinds,
            name=name,
            url=url,
            enabled=enabled,
            filter_=filter_,
            signing_secret=signing_secret,
        )

        return subscription_create
