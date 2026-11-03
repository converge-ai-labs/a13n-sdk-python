from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.browser_binding_preparation import BrowserBindingPreparation
from ..models.browser_binding_tab_access import BrowserBindingTabAccess
from ..types import UNSET, Unset

T = TypeVar("T", bound="BrowserBinding")


@_attrs_define(repr=False)
class BrowserBinding:
    """
    Attributes:
        browser_id (str):
        preparation (BrowserBindingPreparation | Unset):
        tab_access (BrowserBindingTabAccess | Unset):
    """

    browser_id: str
    preparation: BrowserBindingPreparation | Unset = UNSET
    tab_access: BrowserBindingTabAccess | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        browser_id = self.browser_id

        preparation: str | Unset = UNSET
        if not isinstance(self.preparation, Unset):
            preparation = self.preparation.value

        tab_access: str | Unset = UNSET
        if not isinstance(self.tab_access, Unset):
            tab_access = self.tab_access.value

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "browser_id": browser_id,
            }
        )
        if preparation is not UNSET:
            field_dict["preparation"] = preparation
        if tab_access is not UNSET:
            field_dict["tab_access"] = tab_access

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        browser_id = d.pop("browser_id")

        _preparation = d.pop("preparation", UNSET)
        preparation: BrowserBindingPreparation | Unset
        if isinstance(_preparation, Unset):
            preparation = UNSET
        else:
            preparation = BrowserBindingPreparation(_preparation)

        _tab_access = d.pop("tab_access", UNSET)
        tab_access: BrowserBindingTabAccess | Unset
        if isinstance(_tab_access, Unset):
            tab_access = UNSET
        else:
            tab_access = BrowserBindingTabAccess(_tab_access)

        browser_binding = cls(
            browser_id=browser_id,
            preparation=preparation,
            tab_access=tab_access,
        )

        return browser_binding
