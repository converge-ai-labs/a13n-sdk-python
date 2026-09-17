from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="GitHubCommentReceipt")


@_attrs_define(repr=False)
class GitHubCommentReceipt:
    """
    Attributes:
        comment_id (int):
        html_url (str):
        node_id (str):
        request_id (str):
    """

    comment_id: int
    html_url: str
    node_id: str
    request_id: str

    def to_dict(self) -> dict[str, Any]:
        comment_id = self.comment_id

        html_url = self.html_url

        node_id = self.node_id

        request_id = self.request_id

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "comment_id": comment_id,
                "html_url": html_url,
                "node_id": node_id,
                "request_id": request_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        comment_id = d.pop("comment_id")

        html_url = d.pop("html_url")

        node_id = d.pop("node_id")

        request_id = d.pop("request_id")

        git_hub_comment_receipt = cls(
            comment_id=comment_id,
            html_url=html_url,
            node_id=node_id,
            request_id=request_id,
        )

        return git_hub_comment_receipt
