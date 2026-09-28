"""Generate the Python SDK from its pinned local Service contract.

Generation does not import, check out, or execute the Service.
"""

import ast
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

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

    for name, schema in schemas.items():
        strip_defaults(schema)
        # Pydantic gives its distinct input/output components the same title;
        # the generator otherwise collides their names and drops response refs.
        if name.endswith(("-Input", "-Output")):
            schema.pop("title", None)
        if name == "UploadCreate":
            file_part = schema["properties"]["file"]
            if file_part.get("contentMediaType") != "application/octet-stream" or file_part.get("type") != "string":
                raise ValueError("Unsupported Service upload part schema")
            file_part["format"] = "binary"

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
    for operations in document["paths"].values():
        for operation in operations.values():
            if not isinstance(operation, dict) or "responses" not in operation:
                continue
            for response in operation["responses"].values():
                if isinstance(response, dict) and response.get("content", {}).get("*/*"):
                    response["content"]["application/octet-stream"] = response["content"].pop("*/*")
            request = operation.get("requestBody", {})
            content = request.get("content", {})
            if len(content) > 1 and all(
                entry.get("schema") == {"type": "string", "format": "binary"} for entry in content.values()
            ):
                # Generate one File parameter; restore all declared media choices
                # in build_request rather than silently choosing one wire format.
                request["content"] = {"application/octet-stream": next(iter(content.values()))}
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
    binary_media = {
        operation["operationId"].replace("__", "_"): tuple(content)
        for operations in document["paths"].values()
        for operation in operations.values()
        if isinstance(operation, dict) and "operationId" in operation
        if (content := operation.get("requestBody", {}).get("content", {}))
        and len(content) > 1
        and all(entry.get("schema") == {"type": "string", "format": "binary"} for entry in content.values())
    }
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
        if path.stem in binary_media:
            media = binary_media[path.stem]
            text = text.replace(
                '    headers["Content-Type"] = "application/octet-stream"',
                f"    if body.mime_type not in {media!r}:\n"
                f'        raise ValueError("File.mime_type must be one of: {", ".join(media)}")\n'
                '    headers["Content-Type"] = body.mime_type',
            )
        if '_kwargs["content"] = body.payload' in text:
            text = "from ...._binary import file_chunks\n" + text
            text = text.replace(
                "    response = await client.get_async_httpx_client().request(",
                '    kwargs["content"] = file_chunks(body.payload)\n\n    response = await client.get_async_httpx_client().request(',
            )
        if '_kwargs["files"] = body.to_multipart()' in text:
            # httpx constructs a fresh multipart boundary. The generator's
            # literal +++ header does not match the serialized file body.
            text = text.replace('    headers["Content-Type"] = "multipart/form-data; boundary=+++"\n', "")
        text = text.replace("_get_kwargs", "build_request")
        # Classify failures at the response parser, not around request building,
        # so invalid local inputs retain their original exception and no I/O claim.
        for node in ast.parse(text).body:
            if isinstance(node, ast.FunctionDef) and node.name == "_build_response":
                lines = text.splitlines(keepends=True)
                start, end = node.body[0].lineno - 1, node.end_lineno
                body = "".join("    " + line if line.strip() else line for line in lines[start:end])
                lines[start:end] = [
                    "    from ....errors import ProtocolError\n\n",
                    "    try:\n",
                    body,
                    "    except (ValueError, KeyError, TypeError, AttributeError):\n",
                    '        raise ProtocolError("Malformed Service response") from None\n',
                ]
                text = "".join(lines)
                break
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
    scoped_paths = sorted(
        path
        for path, operations in document["paths"].items()
        if any(
            any(parameter.get("name") == "X-Workspace-ID" for parameter in operation.get("parameters", []))
            for operation in operations.values()
            if isinstance(operation, dict)
        )
    )
    patterns = [re.sub(r"\\\{[^{}]+\\\}", r"[^/]+", re.escape(path)) + r"\Z" for path in scoped_paths]
    (output / "workspace_routes.py").write_text(
        '"""Generated workspace-scoped routes for session credential headers."""\n'
        "import re\n\n"
        "WORKSPACE_PATHS = (\n" + "".join(f"    re.compile({pattern!r}),\n" for pattern in patterns) + ")\n"
    )
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
