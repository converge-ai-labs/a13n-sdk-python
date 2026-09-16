"""Local contract provenance, generation adapters, and output ownership."""

import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("sdk_codegen", ROOT / "codegen/generate.py")
assert SPEC and SPEC.loader
codegen = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(codegen)


def test_contract_source_matches_pinned_bytes() -> None:
    source = json.loads((ROOT / "contract/source.json").read_text())
    assert source["repository"] == "converge-ai-labs/agent-foundation"
    assert len(source["commit"]) == 40
    assert all(char in "0123456789abcdef" for char in source["commit"])
    vendored = {
        str(path.relative_to(ROOT / "contract"))
        for path in (ROOT / "contract").rglob("*")
        if path.is_file() and str(path.relative_to(ROOT / "contract")) not in {"source.json", "README.md"}
    }
    assert set(source["files"]) == vendored
    for name, entry in source["files"].items():
        assert hashlib.sha256((ROOT / "contract" / name).read_bytes()).hexdigest() == entry["sha256"]


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


def test_drift_checks_content_and_stale_files_without_mutation(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setattr(codegen, "ROOT", tmp_path)
    target, output = tmp_path / "committed", tmp_path / "regenerated"
    target.mkdir()
    output.mkdir()
    (target / "old.py").write_text("old")
    (target / "current.py").write_text("out of date")
    (output / "current.py").write_text("current")
    before = codegen.files(target)
    assert not codegen.install(output, target, check=True)
    assert codegen.files(target) == before
    assert codegen.install(output, target, check=False)
    assert codegen.files(target) == {"current.py": b"current"}
    assert codegen.install(output, target, check=True)


def test_missing_output_is_drift_without_creating_it(tmp_path: Path, monkeypatch) -> None:
    monkeypatch.setattr(codegen, "ROOT", tmp_path)
    output = tmp_path / "regenerated"
    output.mkdir()
    (output / "new.py").write_text("new")
    target = tmp_path / "missing"
    assert not codegen.install(output, target, check=True)
    assert not target.exists()


def test_all_native_operations_have_bindings() -> None:
    document = json.loads((ROOT / "contract/openapi.json").read_text())
    generated = {path.stem for path in (ROOT / "a13n/generated/api").rglob("*.py")}
    for path in document["paths"].values():
        for method, operation in path.items():
            if method in {"get", "post", "patch", "put", "delete", "head", "options"}:
                assert operation["operationId"] in generated


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
    initial, updated = tmp_path / "initial", tmp_path / "updated"
    initial.mkdir()
    updated.mkdir()
    before = codegen.files(codegen.generate(document, initial))
    document["paths"]["/api/v1/autogen-probe"]["get"]["parameters"] = [
        {"name": "autogen_probe_value", "in": "query", "schema": {"type": "string"}}
    ]
    source = json.dumps(document)
    output = codegen.generate(document, updated)
    after = codegen.files(output)
    assert before != after
    assert not any(b"autogen_probe_value" in value for value in before.values())
    assert any(b"autogen_probe_value" in value for value in after.values())
    assert json.dumps(document) == source
    target = tmp_path / "installed"
    assert codegen.install(output, target, check=False)
    assert codegen.install(output, target, check=True)
