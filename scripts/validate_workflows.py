#!/usr/bin/env python3
"""Validate example n8n workflow templates against the repository schema."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, Tuple

REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = REPO_ROOT / "schema" / "workflow.schema.json"
EXAMPLES_DIR = REPO_ROOT / "examples"


class ValidationError(Exception):
    """Raised when a document fails schema validation."""


Schema = Dict[str, Any]


def load_schema() -> Schema:
    if not SCHEMA_PATH.exists():
        raise FileNotFoundError(f"Schema not found: {SCHEMA_PATH}")
    with SCHEMA_PATH.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def iter_workflow_paths(patterns: Iterable[str]) -> Iterable[Path]:
    if not EXAMPLES_DIR.exists():
        return []
    if patterns:
        for pattern in patterns:
            yield from EXAMPLES_DIR.glob(pattern)
    else:
        yield from EXAMPLES_DIR.glob("*.json")


def validate(data: Any, schema: Schema, path: str = "$") -> None:
    schema_type = schema.get("type")
    if schema_type:
        if schema_type == "object" and not isinstance(data, dict):
            raise ValidationError(f"{path} should be an object")
        if schema_type == "array" and not isinstance(data, list):
            raise ValidationError(f"{path} should be an array")
        if schema_type == "string" and not isinstance(data, str):
            raise ValidationError(f"{path} should be a string")
        if schema_type == "number" and not isinstance(data, (int, float)):
            raise ValidationError(f"{path} should be a number")

    if isinstance(data, dict):
        required = schema.get("required", [])
        for key in required:
            if key not in data:
                raise ValidationError(f"{path}.{key} is required")
        properties = schema.get("properties", {})
        for key, value in data.items():
            if key in properties:
                validate(value, properties[key], f"{path}.{key}")
    elif isinstance(data, list):
        min_items = schema.get("minItems")
        max_items = schema.get("maxItems")
        if min_items is not None and len(data) < min_items:
            raise ValidationError(f"{path} should contain at least {min_items} items")
        if max_items is not None and len(data) > max_items:
            raise ValidationError(f"{path} should contain no more than {max_items} items")
        items_schema = schema.get("items")
        if items_schema:
            for idx, item in enumerate(data):
                validate(item, items_schema, f"{path}[{idx}]")



def validate_file(path: Path, schema: Schema) -> Tuple[Path, str]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    validate(data, schema)
    return path, "ok"


def main(argv: Iterable[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "patterns",
        nargs="*",
        help="Glob patterns (relative to examples/) for selecting workflows",
    )
    args = parser.parse_args(list(argv))

    schema = load_schema()
    failures = []
    for workflow_path in iter_workflow_paths(args.patterns):
        try:
            validate_file(workflow_path, schema)
            print(f"✅ {workflow_path.relative_to(REPO_ROOT)}")
        except Exception as exc:  # noqa: BLE001
            failures.append((workflow_path, str(exc)))
            print(f"❌ {workflow_path.relative_to(REPO_ROOT)} -> {exc}")

    if failures:
        print(f"\n{len(failures)} workflow(s) failed validation.")
        return 1
    print("All workflows passed schema validation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
