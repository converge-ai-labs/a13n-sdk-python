"""Generate static resource navigation from the existing typed HTTP bindings.

No runtime attribute synthesis or second serializer: signatures and calls come
from the pinned generator output. The route tree binds identity; small explicit
names select handwritten interaction behavior.
"""

import ast
import keyword
import re
from dataclasses import dataclass, field
from pathlib import Path

CORE = {
    (): "ServiceResources",
    ("workspaces", "{}"): "Workspace",
    ("organizations", "{}"): "Organization",
    ("workspaces", "{}", "agents", "{}"): "Agent",
    ("workspaces", "{}", "sessions", "{}"): "Session",
    ("workspaces", "{}", "threads", "{}"): "Thread",
    ("workspaces", "{}", "runs", "{}"): "Run",
    ("workspaces", "{}", "threads", "{}", "inbox", "{}"): "InboxEntry",
}
MIXINS = {
    "Workspace": "WorkspaceMethods",
    "Thread": "ThreadMethods",
    "Run": "RunMethods",
    "InboxEntry": "InboxEntryMethods",
}
VERBS = {
    "post": "create",
    "patch": "update",
    "put": "replace",
    "delete": "delete",
    "head": "head",
    "options": "options",
}


def snake(name: str) -> str:
    name = name.replace("-", "_")
    return name + "_" if keyword.iskeyword(name) else name


def pascal(name: str) -> str:
    return "".join(word.capitalize() for word in re.split(r"[-_]", name))


@dataclass
class Node:
    key: tuple[str, ...]
    segments: tuple[str, ...]
    children: dict[str, "Node"] = field(default_factory=dict)
    operations: dict[str, tuple[dict, tuple[str, ...]]] = field(default_factory=dict)

    @property
    def name(self) -> str:
        return CORE.get(self.key, "".join(pascal(s.strip("{}")) for s in self.segments))

    @property
    def bindings(self) -> dict[int, str]:
        return {i: s[1:-1] for i, s in enumerate(self.segments) if s.startswith("{")}


def success_type(annotation: ast.expr) -> str:
    assert isinstance(annotation, ast.Subscript)

    def parts(node: ast.expr) -> list[str]:
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.BitOr):
            return parts(node.left) + parts(node.right)
        return [] if ast.unparse(node) == "ErrorEnvelope" else [ast.unparse(node)]

    return " | ".join(parts(annotation.slice)) or "None"


def generate_resources(document: dict, output: Path) -> None:
    root = Node((), ())
    nodes: dict[tuple[str, ...], Node] = {(): root}
    for path, operations in document["paths"].items():
        if path.startswith("/api/v1/"):
            segments = tuple(path.removeprefix("/api/v1/").split("/"))
        elif path in {"/healthz", "/readyz"}:
            segments = (path.lstrip("/"),)
        else:
            raise ValueError(f"Unsupported resource path: {path}")
        node = root
        for segment in segments:
            key = "{}" if segment.startswith("{") else segment
            if key not in node.children:
                child = Node((*node.key, key), (*node.segments, segment))
                node.children[key] = child
                nodes[child.key] = child
            node = node.children[key]
        for http_method, operation in operations.items():
            if http_method in {"get", *VERBS}:
                node.operations[http_method] = (operation, segments)

    modules = {file.stem: file for file in (output / "api").rglob("*.py") if file.name != "__init__.py"}
    imports: set[str] = set()
    model_names: set[str] = set()
    endpoints: set[str] = set()

    def typed(code: str) -> str:
        return re.sub(
            r"\b[A-Za-z_][A-Za-z_0-9]*\b",
            lambda match: "wire." + match[0] if match[0] in model_names else match[0],
            code,
        )

    classes: list[str] = []

    def endpoint(operation: dict) -> tuple[ast.AsyncFunctionDef, str]:
        module = modules[operation["operationId"].replace("__", "_")]
        tree = ast.parse(module.read_text())
        for imp in tree.body:
            if isinstance(imp, ast.ImportFrom) and imp.module:
                if imp.module.startswith("models."):
                    model_names.update(a.name for a in imp.names)
                elif imp.module == "types":
                    names = [ast.unparse(a) for a in imp.names if a.name != "Response"]
                    if names:
                        imports.add("from .types import " + ", ".join(names))
            elif isinstance(imp, ast.Import):
                for alias in imp.names:
                    if alias.name == "datetime":
                        imports.add("import datetime")
        function = next(n for n in tree.body if isinstance(n, ast.AsyncFunctionDef) and n.name == "asyncio_detailed")
        mod = module.relative_to(output).with_suffix("").as_posix().replace("/", ".")
        alias = operation["operationId"].replace("__", "_")
        endpoints.add(f"from .{mod.rsplit('.', 1)[0]} import {alias}")
        return function, alias

    def method(node: Node, verb: str, op: dict, segments: tuple[str, ...], name: str) -> list[str]:
        fn, alias = endpoint(op)
        assert fn.returns is not None
        successful = [response for code, response in op["responses"].items() if code.startswith("2")]
        raw_result = (
            "None"
            if successful and all(not response.get("content") for response in successful)
            else success_type(fn.returns)
        )
        result = typed(raw_result)
        bound = {
            segment[1:-1]: node.bindings[i]
            for i, segment in enumerate(segments)
            if segment.startswith("{") and i in node.bindings
        }
        args = fn.args
        arguments: list[tuple[ast.arg, ast.expr | None]] = [
            *zip(args.args, [None] * (len(args.args) - len(args.defaults)) + list(args.defaults), strict=True),
            *zip(args.kwonlyargs, args.kw_defaults, strict=True),
        ]
        exposed = [(arg, default) for arg, default in arguments if arg.arg not in {"client", *bound}]
        signature = ", ".join(
            typed(ast.unparse(arg)) + (f" = {ast.unparse(default)}" if default else "") for arg, default in exposed
        )
        signature = "self" + (", *, " + signature if signature else "")
        argument_types = {arg.arg: typed(ast.unparse(arg.annotation)) for arg, _ in arguments if arg.annotation}
        call_args = []
        for wire_name, binding in bound.items():
            value = f"self._bindings[{binding!r}]"
            if argument_types[wire_name] != "str":
                value = f"{argument_types[wire_name]}({value})"
            call_args.append(f"{wire_name}={value}")
        call_args += [f"{arg.arg}={arg.arg}" for arg, _ in exposed]
        call = ", ".join(["client=client", *call_args])
        lines = [
            f"    async def {name}({signature}) -> Result[{result}]:",
            f'        """{op.get("summary", alias)}. One HTTP request; no automatic replay."""',
            f"        return await self._call(lambda client: {alias}.asyncio_detailed({call}))",
            "",
        ]
        # Preserve specialized page values and metadata. Only ordinary opaque
        # cursor collections get this helper; queue/resource-sequence reads do not.
        if name == "list" and any(arg.arg == "cursor" for arg, _ in exposed):
            models = output / "models"
            model_file = next((p for p in models.glob("*.py") if f"class {raw_result}:" in p.read_text()), None)
            if model_file and "next_cursor:" in model_file.read_text():
                page_args = [f"{arg.arg}={arg.arg}" for arg, _ in exposed if arg.arg != "cursor"]
                page_args.append("cursor=next_cursor")
                snapshots = [
                    f"        {arg.arg} = {arg.arg}.copy() if isinstance({arg.arg}, list) else {arg.arg}"
                    for arg, _ in exposed
                    if arg.annotation is not None
                    and any(
                        isinstance(part, ast.Subscript) and isinstance(part.value, ast.Name) and part.value.id == "list"
                        for part in ast.walk(arg.annotation)
                    )
                ]
                lines += [
                    f"    def pages({signature}) -> AsyncIterator[Result[{result}]]:",
                    '        """Iterate lazily with a filter snapshot, retaining each page and HTTP evidence."""',
                    *snapshots,
                    f"        return pages(lambda next_cursor: self.list({', '.join(page_args)}), lambda value: value.next_cursor, cursor)",
                    "",
                ]
                page_tree = ast.parse(model_file.read_text())
                page_class = next(n for n in page_tree.body if isinstance(n, ast.ClassDef))
                item_field = next(
                    (
                        n
                        for n in page_class.body
                        if isinstance(n, ast.AnnAssign) and isinstance(n.target, ast.Name) and n.target.id == "items"
                    ),
                    None,
                )
                # Projection snapshots retain page-level coverage; flatten only ordinary collections.
                if (
                    item_field is not None
                    and isinstance(item_field.annotation, ast.Subscript)
                    and "snapshot_version:" not in model_file.read_text()
                ):
                    item_type = ast.unparse(item_field.annotation.slice)
                    item_type = re.sub(r"\b([A-Z][A-Za-z_0-9]*)\b", r"wire.\1", item_type)
                    forward = ", ".join(f"{arg.arg}={arg.arg}" for arg, _ in exposed)
                    lines += [
                        f"    def iter({signature}) -> AsyncIterator[{item_type}]:",
                        '        """Yield ordinary wire values lazily with a filter snapshot and server order."""',
                        f"        return (item async for page in self.pages({forward}) for item in page.value.items)",
                        "",
                    ]
        media = {
            media
            for code, response in op["responses"].items()
            if code.startswith("2")
            for media in response.get("content", {})
        }
        if media and not media <= {"application/json", "text/event-stream"}:
            stream_args = ", ".join(call_args)
            lines += [
                f"    def {name}_stream({signature}) -> AbstractAsyncContextManager[httpx2.Response]:",
                '        """Unbuffered response; caller checks status and consumes within the context."""',
                f"        return self._stream({alias}.build_request({stream_args}))",
                "",
            ]
        return lines

    def flattened(node: Node) -> bool:
        return (
            not node.children
            and len(node.operations) == 1
            and set(node.operations) == {"post"}
            and not node.segments[-1].endswith("s")
        )

    for node in nodes.values():
        if node is not root and flattened(node) and node.key[-1] != "{}":
            continue
        name = "_" + node.name + "Resource" if node.name in MIXINS else node.name
        lines = [
            f"class {name}(Resource):",
            f'    """Bound Native resource: /{" / ".join(node.segments) or "api/v1"}."""',
            "",
        ]
        members: set[str] = set()
        for verb, (op, segments) in node.operations.items():
            is_collection = any(
                marker in str(response.get("content", {}))
                for code, response in op["responses"].items()
                if code.startswith("2")
                for marker in ("Collection", "Page")
            )
            method_name = ("list" if is_collection else "get") if verb == "get" else VERBS[verb]
            members.add(method_name)
            lines += method(node, verb, op, segments, method_name)
        for key, child in node.children.items():
            if key == "{}":
                selector = snake(child.segments[-1][1:-1])
                param = child.segments[-1][1:-1]
                selector_type = "str"
                for child_op, child_segments in child.operations.values():
                    child_fn, _ = endpoint(child_op)
                    original_param = child_segments[-1][1:-1]
                    for argument in child_fn.args.args:
                        if argument.arg == original_param and argument.annotation:
                            selector_type = typed(ast.unparse(argument.annotation))
                    break
                lines += [
                    f"    def __call__(self, {selector}: {selector_type}) -> {child.name}:",
                    f"        return {child.name}(self._client, self._bind({param!r}, {selector}))",
                    "",
                ]
                continue
            member = snake(key)
            if node.name == "Run" and member in {"fork", "resume", "interrupt"}:
                member += "_receipt"
            elif node.name == "Thread" and member == "stream":
                member = "stream_response"
            elif node.name == "Thread" and member == "inbox":
                member = "inbox_entries"
            if member in members:
                raise ValueError(f"Resource member collision: {node.name}.{member}")
            if flattened(child):
                op, segments = child.operations["post"]
                lines += method(node, "post", op, segments, member)
            else:
                lines += [
                    "    @property",
                    f"    def {member}(self) -> {child.name}:",
                    f"        return {child.name}(self._client, self._bindings)",
                    "",
                ]
        classes.append("\n".join(lines))

    for name, mixin in MIXINS.items():
        if name in {node.name for node in nodes.values()}:
            classes.append(
                f'class {name}({mixin}, _{name}Resource):\n    """Managed {name} reference with bounded interaction helpers."""\n'
            )
    prelude = '''"""Generated typed Native resource navigation. Do not edit; run make generate."""
from __future__ import annotations
from collections.abc import AsyncIterator
from contextlib import AbstractAsyncContextManager
from typing import Any, Literal
import httpx2
from . import models as wire
from .._resources import Resource, Result, pages
from .._interaction import WorkspaceMethods, ThreadMethods, RunMethods, InboxEntryMethods
'''
    source = prelude + "\n".join(sorted(imports | endpoints)) + "\n\n" + "\n\n".join(classes)
    (output / "resources.py").write_text(source)
