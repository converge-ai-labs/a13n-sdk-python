"""Wire regressions for the Service output-alternative contract."""

from a13n.generated import models as wire
from a13n.generated.types import UNSET


def test_output_alternative_variants_round_trip_without_losing_null_or_references() -> None:
    payload = {
        "alternatives": [
            "text",
            {"kind": "structured", "name": "answer", "schema": {"type": "object"}, "description": None},
            {"kind": "client_tool", "name": "confirm", "schema": {"type": "object"}},
        ]
    }
    output = wire.OutputSpec.from_dict(payload)
    assert isinstance(output.alternatives, list)
    assert output.alternatives[0] == "text"
    assert isinstance(output.alternatives[1], wire.StructuredOutputAlternative)
    assert isinstance(output.alternatives[2], wire.ClientOutputAlternative)
    assert output.alternatives[1].description is None
    assert output.alternatives[2].description is UNSET
    assert output.to_dict() == payload
