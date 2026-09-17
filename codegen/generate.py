"""Generate the Python SDK from its pinned local Service contract.

Generation does not import, check out, or execute the Service.
"""

import json
import shutil
import subprocess
import tempfile
from pathlib import Path

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
    return document


def generate(document: dict, work: Path) -> Path:
    source = work / "openapi.json"
    source.write_text(json.dumps(prepare(document)))
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


def install(output: Path, target: Path) -> None:
    # Only generator-owned directories are replaced, including removed schemas.
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(output, target)


def main() -> None:
    document = json.loads((ROOT / "contract/openapi.json").read_text())
    with tempfile.TemporaryDirectory(prefix="a13n-codegen-") as temp:
        output = generate(document, Path(temp))
        install(output, TARGET)


if __name__ == "__main__":
    main()
