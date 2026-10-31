#!/usr/bin/env python3
"""Build data.json from content/posts/*.md (1 item = 1 file).

Zero-dependency: frontmatter is simple 'key: value' lines, and the body
uses a small fixed Markdown subset (bullet fields, paragraphs, headings).
Run: python3 scripts/build.py   (from the repository root or anywhere)
"""
import json
import re
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POSTS = ROOT / "content" / "posts"
OUT = ROOT / "data.json"

STATUS_LABELS = {"stock": "ストック", "doing": "試作中", "done": "試作済み・見送り"}
FIELD_LABELS = ("元の情報", "要点", "面白いところ", "作れそうなもの", "扱い", "入口")


def parse_frontmatter(text):
    if not text.startswith("---\n"):
        return {}, text
    head, _, body = text[4:].partition("\n---\n")
    meta = {}
    for line in head.splitlines():
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        value = value.strip()
        if len(value) >= 2 and value[0] == "'" and value[-1] == "'":
            value = value[1:-1].replace("''", "'")
        elif len(value) >= 2 and value[0] == '"' and value[-1] == '"':
            value = value[1:-1]
        meta[key.strip()] = value
    return meta, body.strip("\n")


def inline(text):
    text = escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(https?://[^\s<）」]+)", r'<a href="\1" target="_blank" rel="noopener">\1</a>', text)
    return text


def md_to_html(md):
    out = []
    in_list = False

    def close_list():
        nonlocal in_list
        if in_list:
            out.append("</ul>")
            in_list = False

    for raw in md.splitlines():
        line = raw.rstrip()
        if line.startswith("- "):
            if not in_list:
                out.append("<ul>")
                in_list = True
            item = line[2:]
            label = None
            for cand in FIELD_LABELS:
                if item.startswith(cand + ": ") or item.startswith(cand + "："):
                    label = cand
                    item = item[len(cand) + 2:]
                    break
            else:
                m = re.match(r"^(追記（[^）]*）): (.*)$", item)
                if m:
                    label, item = m.group(1), m.group(2)
            if label:
                out.append("<li><strong>" + escape(label) + "</strong>: " + inline(item) + "</li>")
            else:
                out.append("<li>" + inline(item) + "</li>")
        elif line.startswith("### "):
            close_list()
            out.append("<h3>" + inline(line[4:]) + "</h3>")
        elif line.startswith("## "):
            close_list()
            out.append("<h2>" + inline(line[3:]) + "</h2>")
        elif not line.strip():
            close_list()
        else:
            close_list()
            out.append("<p>" + inline(line) + "</p>")
    close_list()
    return "\n".join(out)


def main():
    posts = []
    for path in sorted(POSTS.glob("*.md")):
        meta, body = parse_frontmatter(path.read_text(encoding="utf-8"))
        slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", path.stem)
        status = meta.get("status", "stock")
        posts.append({
            "id": "proto/" + slug,
            "slug": slug,
            "title": meta.get("title", path.stem),
            "date": meta.get("date", ""),
            "status": status,
            "status_label": STATUS_LABELS.get(status, status),
            "category": "試作ネタ",
            "summary": meta.get("summary", ""),
            "source": meta.get("source", ""),
            "entry": meta.get("entry", ""),
            "type": meta.get("type", "proto"),
            "markdown": body,
            "html": md_to_html(body),
        })
    posts.sort(key=lambda p: (p["date"], p["slug"]), reverse=True)
    data = {
        "schema": "proto-neta/v1",
        "site": {
            "id": "proto",
            "title": "試作ネタ帳",
            "subtitle": "この先、試作してみたいものの種",
            "updated": max((p["date"] for p in posts), default=""),
            "count": len(posts),
        },
        "posts": posts,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("built:", len(posts), "posts ->", OUT)


if __name__ == "__main__":
    main()
