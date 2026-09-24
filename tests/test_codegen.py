import json
from pathlib import Path

from codegen.generate import generate, install, prepare

ROOT = Path(__file__).resolve().parents[1]


def test_adapter_preserves_pinned_contract_and_normalizes_generator_only_shapes() -> None:
    document = json.loads((ROOT / "contract/openapi.json").read_text())
    original = json.dumps(document)
    adapted = prepare(document)
    assert json.dumps(document) == original
    assert adapted["components"]["schemas"]["AgentConfig-Output"].get("title") is None
    assert document["components"]["schemas"]["AgentConfig-Output"]["title"] == "AgentConfig"
    asset = "/api/v1/workspaces/{workspace_id}/assets/{asset_id}/content"
    assert "*/*" in document["paths"][asset]["get"]["responses"]["200"]["content"]
    assert "application/octet-stream" in adapted["paths"][asset]["get"]["responses"]["200"]["content"]
    assert "*/*" not in adapted["paths"][asset]["get"]["responses"]["200"]["content"]


def test_default_response_and_property_named_default_are_not_annotations() -> None:
    document = {
        "components": {
            "schemas": {
                "Object": {"type": "object", "properties": {"default": {"type": "string", "default": "server-value"}}}
            }
        },
        "paths": {
            "/resource": {
                "get": {"responses": {"default": {"content": {"application/json": {"schema": {"type": "object"}}}}}}
            }
        },
    }
    projected = prepare(document)
    assert projected["components"]["schemas"]["Object"]["properties"]["default"] == {"type": "string"}
    assert projected["paths"] == document["paths"]


def test_changed_http_contract_regenerates_bindings(tmp_path: Path) -> None:
    document = {
        "openapi": "3.1.0",
        "info": {"title": "Autogen fixture", "version": "1"},
        "components": {"schemas": {"RunStatus": {"type": "string", "enum": ["queued", "running"]}}},
        "paths": {
            "/api/v1/autogen-probe": {
                "get": {
                    "operationId": "autogen_probe",
                    "responses": {"204": {"description": "No content"}},
                    "parameters": [{"name": "autogen_probe_value", "in": "query", "schema": {"type": "string"}}],
                }
            }
        },
    }
    output = generate(document, tmp_path)
    target = tmp_path / "installed"
    target.mkdir()
    (target / "obsolete.txt").write_text("old generated output")
    install(output, target)
    assert not (target / "obsolete.txt").exists()
    assert "autogen_probe_value" in (target / "api/default/autogen_probe.py").read_text()
