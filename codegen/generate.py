"""Generate the Python SDK from its pinned local Service contract.

Generation does not import, check out, or execute the Service. Check mode compares
both bytes and file names without replacing the committed generated directory.
"""

import argparse
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

# Script execution and importlib-based generator tests use different roots.
if __name__ == "__main__":
    from resources import generate_resources
else:
    from codegen.resources import generate_resources

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "codegen"
TARGET = ROOT / "a13n/generated"


def run(*args: str, cwd: Path = ROOT) -> None:
    subprocess.run(args, cwd=cwd, check=True)


def prepare(document: dict) -> dict:
    """Generator-only annotations; the published 3.1 contract stays unchanged."""
    document = json.loads(json.dumps(document))
    schemas = document["components"]["schemas"]

    def strip_defaults(schema: dict) -> None:
        schema.pop("default", None)
        for keyword in ("properties", "patternProperties", "$defs"):
            for child in schema.get(keyword, {}).values():
                strip_defaults(child)
        for keyword in ("items", "additionalProperties", "not"):
            child = schema.get(keyword)
            if isinstance(child, dict):
                strip_defaults(child)
        for keyword in ("anyOf", "oneOf", "allOf", "prefixItems"):
            for child in schema.get(keyword, []):
                strip_defaults(child)

    for schema in schemas.values():
        strip_defaults(schema)

    def visit(value: object) -> None:
        if isinstance(value, dict):
            if isinstance(value.get("schema"), dict):
                strip_defaults(value["schema"])
            for child in list(value.values()):
                visit(child)
        elif isinstance(value, list):
            for child in value:
                visit(child)

    visit(document)
    # The pinned queue semantics explicitly specify 200 for submission_failed.
    # Adapt that known export omission without modifying the vendored evidence.
    consume = document.get("paths", {}).get("/api/v1/threads/{thread_id}/queued-submissions/consume", {}).get("post")
    if consume and "200" not in consume["responses"] and "202" in consume["responses"]:
        consume["responses"]["200"] = json.loads(json.dumps(consume["responses"]["202"]))
    # Two pinned binary routes lack response media annotations. These are
    # verified against the pinned skills/router.py and agents/router.py (which
    # uses http_images.image_response), not inferred from endpoint names.
    binary_responses = {
        "/api/v1/skill-revisions/{skill_revision_id}/content": "application/zip",
        "/api/v1/workspaces/{workspace}/agents/{agent}/avatar/{image_id}": "image/webp",
    }
    for path, media_type in binary_responses.items():
        response = document.get("paths", {}).get(path, {}).get("get", {}).get("responses", {}).get("200", {})
        if response.get("content") == {"application/json": {"schema": {}}}:
            response["content"] = {media_type: {"schema": {"type": "string", "format": "binary"}}}
    return document


def generate(document: dict, work: Path) -> Path:
    document = prepare(document)
    source = work / "openapi.json"
    source.write_text(json.dumps(document))
    output = work / "output"
    run(
        "uv",
        "tool",
        "run",
        "--from",
        "openapi-python-client==0.29.1",
        "openapi-python-client",
        "generate",
        "--fail-on-warning",
        "--path",
        str(source),
        "--output-path",
        str(output),
        "--meta",
        "none",
        "--config",
        str(CONFIG / "config.yaml"),
        "--custom-template-path",
        str(CONFIG / "templates"),
    )
    for path in output.rglob("*.py"):
        text = (
            path.read_text()
            .replace("import httpx\n", "import httpx2 as httpx\n")
            .replace("from httpx import ", "from httpx2 import ")
        )
        # Generated request models can contain write-only credentials. The
        # wire serializer remains unchanged; repr must not reveal their data.
        text = text.replace("@_attrs_define\n", "@_attrs_define(repr=False)\n").replace(
            "@define\n", "@define(repr=False)\n"
        )
        if '_kwargs["content"] = body.payload' in text:
            text = "from ...._binary import file_chunks\n" + text
            text = text.replace(
                "    response = await client.get_async_httpx_client().request(",
                '    kwargs["content"] = file_chunks(body.payload)\n\n    response = await client.get_async_httpx_client().request(',
            )
        text = text.replace("_get_kwargs", "build_request")
        if path.name == "client.py":
            text = text.replace("import ssl", "import ssl\nfrom types import TracebackType").replace(
                "@define\n", "@define(repr=False)\n"
            )
            text = (
                text.replace(
                    "self, *args: Any, **kwargs: Any",
                    "self, exc_type: type[BaseException] | None, exc_value: BaseException | None, traceback: TracebackType | None",
                )
                .replace("__exit__(*args, **kwargs)", "__exit__(exc_type, exc_value, traceback)")
                .replace("__aexit__(*args, **kwargs)", "__aexit__(exc_type, exc_value, traceback)")
            )
        path.write_text(text)
    generate_resources(document, output)
    run(
        "uv",
        "tool",
        "run",
        "--from",
        "ruff==0.16.3",
        "ruff",
        "check",
        "--fix",
        "--unsafe-fixes",
        "--config",
        str(ROOT / "pyproject.toml"),
        str(output),
    )
    run(
        "uv",
        "tool",
        "run",
        "--from",
        "ruff==0.16.3",
        "ruff",
        "format",
        "--config",
        str(ROOT / "pyproject.toml"),
        str(output),
    )
    # Tool-local caches are not part of the generated package.
    for cache in output.rglob(".ruff_cache"):
        shutil.rmtree(cache)
    return output


def files(path: Path) -> dict[str, bytes]:
    return {
        str(file.relative_to(path)): file.read_bytes()
        for file in path.rglob("*")
        if file.is_file() and "__pycache__" not in file.parts
    }


def install(output: Path, target: Path, *, check: bool) -> bool:
    actual, expected = files(target), files(output)
    changed = sorted(name for name in actual.keys() | expected.keys() if actual.get(name) != expected.get(name))
    if not changed:
        return True
    if check:
        print(f"Stale generated files in {target.relative_to(ROOT)}: " + ", ".join(changed[:20]))
        return False
    # Only generator-owned directories are replaced, including removed schemas.
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(output, target)
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    document = json.loads((ROOT / "contract/openapi.json").read_text())
    with tempfile.TemporaryDirectory(prefix="a13n-codegen-") as temp:
        output = generate(document, Path(temp))
        if not install(output, TARGET, check=args.check):
            parser.exit(1, "SDK bindings changed. Run make generate and commit the result.\n")


if __name__ == "__main__":
    main()
