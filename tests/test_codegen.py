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
    asset = "/api/v1/assets/{asset_id}/content"
    assert "*/*" in document["paths"][asset]["get"]["responses"]["200"]["content"]
    assert "application/octet-stream" in adapted["paths"][asset]["get"]["responses"]["200"]["content"]
    assert "*/*" not in adapted["paths"][asset]["get"]["responses"]["200"]["content"]
    image = "/api/v1/workspaces/{workspace_id}/icon"
    assert set(document["paths"][image]["put"]["requestBody"]["content"]) == {"image/jpeg", "image/png", "image/webp"}
    assert set(adapted["paths"][image]["put"]["requestBody"]["content"]) == {"application/octet-stream"}
    retained = "/api/v1/runs/{run_id}/images/{image_id}"
    assert set(document["paths"][retained]["get"]["responses"]["200"]["content"]) == {"image/jpeg", "image/png"}
    assert set(adapted["paths"][retained]["get"]["responses"]["200"]["content"]) == {"application/octet-stream"}


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


def test_every_pinned_named_model_and_inline_schema_has_generated_coverage() -> None:
    import re

    from a13n.generated import models as wire

    document = prepare(json.loads((ROOT / "contract/openapi.json").read_text()))
    schemas = document["components"]["schemas"]
    # Primitive aliases, arrays and unions are inlined into consuming signatures.
    inline = {
        "ApprovalDecision",
        "CallResult",
        "ConnectionConfig",
        "EnteredCredential",
        "InitialMounts",
        "JsonValue",
        "MessageHistory",
        "Part",
        "ToolCallId",
        "ToolPermissionSetting",
        "CpuLimit",
        "MemoryLimit",
        "PanelQuery",
        "ScheduleRule",
        "ToolsetKey",
    }
    named = set()
    for name, schema in schemas.items():
        title = schema.get("title", name)
        exported = "".join(part[0].upper() + part[1:] for part in re.split("[^A-Za-z0-9]+", title) if part)
        if name not in inline:
            assert exported in wire.__all__, name
            named.add(name)
    assert named | inline == schemas.keys()
    assert len(schemas) == 501
    for name in inline:
        reference = f"#/components/schemas/{name}"
        assert reference in json.dumps(document), name


def test_session_only_models_share_native_types_without_changing_native_inventory() -> None:
    from codegen.generate import with_session_models

    document = json.loads((ROOT / "contract/openapi.json").read_text())
    session = json.loads((ROOT / "contract/session-stream.schema.json").read_text())
    augmented = with_session_models(document, session)
    native = document["components"]["schemas"]
    combined = augmented["components"]["schemas"]
    assert len(native) == 501 and len(session["$defs"]) == 101
    assert combined.keys() - native.keys() == {
        "ScheduleConfiguration",
        "Progress",
        "ScheduleEvent",
        "OccurrenceEvent",
        "Delta",
        "Gap",
        "RunSnapshot",
        "ThreadState",
        "ItemRef",
        "MemorySource",
        "RecordSource",
        "FileSource",
        "DisplayContinuation",
        "FragmentState",
        "ObserverContinuation",
        "StreamPosition",
        "_Arguments",
        "_Assembly",
        "_ObserverState",
        "_PartCursor",
    }
    assert combined["RunSnapshot"]["properties"]["items"]["items"] == {"$ref": "#/components/schemas/Item"}
    assert combined["ThreadState"]["properties"]["thread"] == {"$ref": "#/components/schemas/ThreadView"}
    assert combined["RunView"] == native["RunView"]
    assert "continuation" not in native["RunItems"]["properties"]
    assert "DisplayContinuation" not in native
    broken = json.loads(json.dumps(session))
    broken["$defs"]["ThreadView"]["required"].append("new_required_field")
    import pytest

    with pytest.raises(ValueError, match="shared model: ThreadView"):
        with_session_models(document, broken)


def test_full_pinned_generation_matches_committed_owner(tmp_path: Path) -> None:
    document = json.loads((ROOT / "contract/openapi.json").read_text())
    output = generate(document, tmp_path, (ROOT / "contract/session-stream.schema.json").read_bytes())

    def files(root: Path) -> dict[str, bytes]:
        return {
            str(path.relative_to(root)): path.read_bytes()
            for path in root.rglob("*")
            if path.is_file() and "__pycache__" not in path.parts
        }

    assert files(output) == files(ROOT / "a13n/generated")


def test_boundary_validation_bundle_is_exact_reachable_pinned_subset() -> None:
    from codegen.generate import VALIDATED_MODELS, validation_schema

    document = json.loads((ROOT / "contract/openapi.json").read_text())
    source = document["components"]["schemas"]
    selected = validation_schema(document)["components"]["schemas"]
    assert set(selected) == VALIDATED_MODELS | {"ToolSearchConfig"}
    assert selected == {name: source[name] for name in selected}
    assert "AgentConfig-Input" not in selected  # Existing unrelated models retain their own codecs.
    assert json.loads((ROOT / "a13n/generated/validation.schema.json").read_text()) == validation_schema(document)


def test_boundary_adapter_rejects_only_selected_nullable_model_fallthrough() -> None:
    from codegen.generate import strict_wire_boundaries

    selected = "def _parse_value(data):\n    if data is None:\n        return data\n    return cast(ContextUsage | None, data)\n"
    result = strict_wire_boundaries(selected)
    assert "return data" in result
    assert 'raise ValueError("Invalid nullable model value")' in result
    unrelated = selected.replace("ContextUsage", "OldModel")
    assert strict_wire_boundaries(unrelated) == unrelated
