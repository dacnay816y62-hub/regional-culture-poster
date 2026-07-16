#!/usr/bin/env python3
"""Lightweight public-repo validation for the regional culture poster skill.

This intentionally avoids third-party dependencies so GitHub Actions can run it
quickly on a clean checkout.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

TEXT_SUFFIXES = {
    ".md",
    ".yaml",
    ".yml",
    ".txt",
    ".json",
    ".py",
    ".gitignore",
    ".gitattributes",
}

SENSITIVE_PATTERNS = [
    re.compile(r"[A-Za-z]:\\"),
    re.compile("OPENAI" + r"_API_KEY", re.IGNORECASE),
    re.compile("api" + r"\.schyler", re.IGNORECASE),
    re.compile("Hi" + "Win11", re.IGNORECASE),
    re.compile("wxid" + "_", re.IGNORECASE),
    re.compile("WeChat" + " Files", re.IGNORECASE),
    re.compile("File" + "Storage", re.IGNORECASE),
]

SENSITIVE_IGNORE_FILES = {
    ".gitignore",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def iter_text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        if path.suffix in TEXT_SUFFIXES or path.name in TEXT_SUFFIXES:
            files.append(path)
    return files


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        fail(f"{path.relative_to(ROOT)} is not valid UTF-8: {exc}")


def check_skill_frontmatter() -> None:
    path = ROOT / "SKILL.md"
    text = read_text(path)
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        fail("SKILL.md frontmatter must close with ---")
    frontmatter = text[4:end]
    for field in ("name:", "description:"):
        if field not in frontmatter:
            fail(f"SKILL.md frontmatter missing {field}")
    if "regional-culture-poster" not in frontmatter:
        fail("SKILL.md frontmatter should identify regional-culture-poster")


def check_markdown_links() -> None:
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = read_text(path)
        for match in link_pattern.finditer(text):
            target = match.group(1).split("#", 1)[0].strip()
            if not target or "://" in target or target.startswith(("mailto:", "#")):
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                fail(f"{path.relative_to(ROOT)} links outside repo: {target}")
            if not resolved.exists():
                fail(f"{path.relative_to(ROOT)} has missing link target: {target}")


def check_sensitive_patterns() -> None:
    for path in iter_text_files():
        rel = path.relative_to(ROOT).as_posix()
        if path.name in SENSITIVE_IGNORE_FILES:
            continue
        text = read_text(path)
        for pattern in SENSITIVE_PATTERNS:
            if pattern.search(text):
                fail(f"{rel} contains sensitive/local pattern: {pattern.pattern}")


def check_version_consistency() -> None:
    version = read_text(ROOT / "VERSION").strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        fail("VERSION must use MAJOR.MINOR.PATCH")
    readme = read_text(ROOT / "README.md")
    changelog = read_text(ROOT / "CHANGELOG.md")
    if f"version-v{version}-" not in readme:
        fail("README version badge does not match VERSION")
    if f"## v{version}" not in changelog:
        fail("CHANGELOG missing current VERSION heading")


def check_required_files() -> None:
    required = [
        "README.md",
        "SKILL.md",
        "LICENSE",
        "CHANGELOG.md",
        "VERSION",
        ".gitignore",
        ".gitattributes",
        "references/mode-b-editorial.md",
    ]
    for item in required:
        if not (ROOT / item).exists():
            fail(f"missing required file: {item}")


def main() -> int:
    check_required_files()
    check_skill_frontmatter()
    check_markdown_links()
    check_sensitive_patterns()
    check_version_consistency()
    print("Public repo validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
