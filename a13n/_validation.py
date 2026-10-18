"""Cached checks for schema-derived configuration and desktop/context wire values."""

import json
from functools import cache
from importlib.resources import files
from typing import Any

from jsonschema import Draft202012Validator, ValidationError


@cache
def _schemas() -> dict[str, Any]:
    return json.loads(files("a13n.generated").joinpath("validation.schema.json").read_bytes())


@cache
def _validator(name: str) -> Draft202012Validator:
    return Draft202012Validator({"$ref": f"#/components/schemas/{name}", **_schemas()})


def validate_model(name: str, value: Any) -> None:
    try:
        _validator(name).validate(value)
    except ValidationError:
        # Generated HTTP response parsing maps this to ProtocolError. Local
        # invalid inputs remain ValueError and are never dispatched or retried.
        raise ValueError(f"Invalid {name} wire value") from None
