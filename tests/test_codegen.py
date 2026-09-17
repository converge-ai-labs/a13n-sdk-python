"""Generator adapters and generated binding behavior."""

import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("sdk_codegen", ROOT / "codegen/generate.py")
assert SPEC and SPEC.loader
codegen = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(codegen)


def test_adapter_preserves_unions_and_omission_without_mutating_contract() -> None:
    document = json.loads((ROOT / "contract/openapi.json").read_text())
    before = json.dumps(document)
    adapted = codegen.prepare(document)
    assert json.dumps(document) == before
    schemas = adapted["components"]["schemas"]
    for name in ["ActorRef", "EnvironmentSelection"]:
        assert schemas[name] == document["components"]["schemas"][name]
    assert schemas["UpdateAgentRequest"]["properties"]["name"]["anyOf"] == [{"type": "string"}, {"type": "null"}]
    assert "default" not in schemas["ThreadRunSubmissionRequest"]["properties"]["environment"]


def test_default_response_and_property_named_default_are_not_annotations() -> None:
    document = {
        "components": {
            "schemas": {
                "Object": {
                    "type": "object",
                    "properties": {
                        "default": {"type": "string", "default": "server-value"},
                    },
                }
            }
        },
        "paths": {
            "/resource": {
                "get": {
                    "responses": {
                        "default": {"content": {"application/json": {"schema": {"type": "object"}}}},
                    }
                }
            }
        },
    }
    projected = codegen.prepare(document)
    assert projected["components"]["schemas"]["Object"]["properties"]["default"] == {"type": "string"}
    assert projected["paths"] == document["paths"]


def test_changed_http_contract_regenerates_bindings(tmp_path: Path) -> None:
    """Exercise the real pinned generator, not the sync test's fake make."""
    document = {
        "openapi": "3.1.0",
        "info": {"title": "Autogen fixture", "version": "1"},
        "components": {"schemas": {"RunStatus": {"type": "string", "enum": ["queued", "running"]}}},
        "paths": {
            "/api/v1/autogen-probe": {
                "get": {"operationId": "autogen_probe", "responses": {"204": {"description": "No content"}}}
            }
        },
    }
    document["paths"]["/api/v1/autogen-probe"]["get"]["parameters"] = [
        {"name": "autogen_probe_value", "in": "query", "schema": {"type": "string"}}
    ]
    output = codegen.generate(document, tmp_path)
    target = tmp_path / "installed"
    target.mkdir()
    (target / "obsolete.txt").write_text("old generated output")
    codegen.install(output, target)
    assert not (target / "obsolete.txt").exists()
    assert "autogen_probe_value" in (target / "api/default/autogen_probe.py").read_text()
