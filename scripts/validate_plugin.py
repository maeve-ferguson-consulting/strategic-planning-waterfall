#!/usr/bin/env python3
"""Validate the public skill contract for this plugin."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / ".claude-plugin" / "plugin.json"
README = ROOT / "README.md"
LANDING_PAGE = ROOT / "docs" / "index.html"
SETUP_GUIDE = ROOT / "docs" / "setup-guide.pdf"
EXPECTED_PLUGIN_VERSION = "2.1.0"
EXPECTED_SKILLS = (
    ("./skills/brand", "brand"),
    ("./skills/plan-year", "plan-year"),
    ("./skills/plan-quarter", "plan-quarter"),
    ("./skills/plan-month", "plan-month"),
    ("./skills/plan-week", "plan-week"),
)


def frontmatter_fields(skill_file: Path) -> dict[str, object] | None:
    text = skill_file.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", text, re.DOTALL)
    if match is None:
        return None

    fields: dict[str, object] = {}
    for line in match.group(1).splitlines():
        field = re.fullmatch(r"([a-z][a-z0-9_-]*):\s*(.*?)\s*", line)
        if field is None:
            continue

        key, source_value = field.groups()
        if source_value.startswith('"'):
            try:
                value: object = json.loads(source_value)
            except json.JSONDecodeError:
                value = None
        elif source_value.startswith("'"):
            value = (
                source_value[1:-1].replace("''", "'")
                if source_value.endswith("'")
                else None
            )
        elif source_value.lower() in {"", "null", "~", "true", "false"}:
            value = None
        else:
            try:
                decoded_value = json.loads(source_value)
            except json.JSONDecodeError:
                value = source_value.partition(" #")[0].rstrip()
            else:
                value = decoded_value if isinstance(decoded_value, str) else None

        if key in fields:
            fields[key] = None
        else:
            fields[key] = value

    return fields


def contains_in_order(text: str, phrases: tuple[str, ...]) -> bool:
    position = 0
    for phrase in phrases:
        position = text.find(phrase, position)
        if position == -1:
            return False
        position += len(phrase)
    return True


def main() -> int:
    errors: list[str] = []

    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        print(f"ERROR: cannot read {MANIFEST.relative_to(ROOT)}: {error}", file=sys.stderr)
        return 1

    expected_paths = [path for path, _ in EXPECTED_SKILLS]
    if manifest.get("skills") != expected_paths:
        errors.append(
            f"{MANIFEST.relative_to(ROOT)} must declare exactly these skills in order: "
            + ", ".join(expected_paths)
        )
    if manifest.get("version") != EXPECTED_PLUGIN_VERSION:
        errors.append(
            f"{MANIFEST.relative_to(ROOT)} version must be "
            f"{EXPECTED_PLUGIN_VERSION!r}, got {manifest.get('version')!r}"
        )

    schema_files: list[Path] = []
    for relative_path, command in EXPECTED_SKILLS:
        skill_dir = ROOT / relative_path.removeprefix("./")
        skill_file = skill_dir / "SKILL.md"
        schema_file = skill_dir / "references" / "brand-schema.md"

        if not skill_dir.is_dir():
            errors.append(f"declared skill directory is missing: {relative_path}")
            continue
        if not skill_file.is_file():
            errors.append(f"declared skill file is missing: {skill_file.relative_to(ROOT)}")
        else:
            frontmatter = frontmatter_fields(skill_file)
            actual_name = frontmatter.get("name") if frontmatter is not None else None
            if actual_name != command:
                errors.append(
                    f"{skill_file.relative_to(ROOT)} frontmatter name must be "
                    f"{command!r}, got {actual_name!r}"
                )
            description = (
                frontmatter.get("description") if frontmatter is not None else None
            )
            if not isinstance(description, str):
                errors.append(
                    f"{skill_file.relative_to(ROOT)} frontmatter description must be a string"
                )
            elif not 1 <= len(description) <= 1024:
                errors.append(
                    f"{skill_file.relative_to(ROOT)} frontmatter description must be "
                    f"1-1024 characters, got {len(description)}"
                )

        if not schema_file.is_file():
            errors.append(f"brand schema copy is missing: {schema_file.relative_to(ROOT)}")
        else:
            schema_files.append(schema_file)

    if len(schema_files) == len(EXPECTED_SKILLS):
        canonical = schema_files[0].read_bytes()
        for schema_file in schema_files[1:]:
            if schema_file.read_bytes() != canonical:
                errors.append(
                    "brand schema copies must be byte-identical: "
                    f"{schema_file.relative_to(ROOT)} differs from "
                    f"{schema_files[0].relative_to(ROOT)}"
                )

    readme = re.sub(r"\s+", " ", README.read_text(encoding="utf-8"))
    cowork_flow = (
        "Canonical maintainer source:",
        "Customize → Plugins",
        "Personal plugins",
        "Add marketplace → Add from a repository",
        "https://github.com/maeve-ferguson-consulting/strategic-planning-waterfall",
        "Sync",
        "The Strategic Planning Waterfall",
        "Add",
        "Install",
        "Update",
        "Unknown skill: plugin",
        "new conversation",
    )
    if not contains_in_order(readme, cowork_flow):
        errors.append("README.md must retain the canonical Cowork install and update flow")

    check_installation = readme.partition("### Check the installation")[2].partition(
        "## Step 2"
    )[0]
    documented_commands = re.findall(r"`(/(?:brand|plan-[a-z]+))`", check_installation)
    expected_commands = [f"/{command}" for _, command in EXPECTED_SKILLS]
    if documented_commands != expected_commands:
        errors.append(
            "README.md installation check must list exactly these commands in order: "
            + ", ".join(expected_commands)
        )

    brand_setup = readme.partition("## Step 2")[2].partition("## Step 3")[0]
    if re.search(r"(?<![\w-])/brand(?![\w-])", brand_setup) is None:
        errors.append("README.md must direct customers to start with /brand")

    landing_page = LANDING_PAGE.read_text(encoding="utf-8")
    if 'href="setup-guide.pdf"' not in landing_page:
        errors.append("docs/index.html must link to the same-site setup guide PDF")
    if not SETUP_GUIDE.is_file():
        errors.append("customer setup guide is missing: docs/setup-guide.pdf")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("Plugin contract and canonical documentation checks valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
