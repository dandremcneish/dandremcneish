#!/usr/bin/env python3
"""Fetch real public GitHub activity and inject it into README.md between markers."""
import json
import re
import urllib.request
from datetime import datetime

USERNAME = "dandremcneish"
README_PATH = "README.md"
START_MARKER = "<!--START_SECTION:activity-->"
END_MARKER = "<!--END_SECTION:activity-->"
MAX_ITEMS = 5

EVENT_FORMATTERS = {
    "PushEvent": lambda e: f"Pushed {len(e['payload'].get('commits', [])) or 1} commit(s) to `{e['repo']['name']}`",
    "PullRequestEvent": lambda e: f"{e['payload'].get('action', 'updated').capitalize()} a pull request in `{e['repo']['name']}`",
    "IssuesEvent": lambda e: f"{e['payload'].get('action', 'updated').capitalize()} an issue in `{e['repo']['name']}`",
    "CreateEvent": lambda e: f"Created {e['payload'].get('ref_type', 'a ref')} in `{e['repo']['name']}`",
    "WatchEvent": lambda e: f"Starred `{e['repo']['name']}`",
    "ForkEvent": lambda e: f"Forked `{e['repo']['name']}`",
    "PublicEvent": lambda e: f"Made `{e['repo']['name']}` public",
    "ReleaseEvent": lambda e: f"Published a release in `{e['repo']['name']}`",
}


def fetch_events():
    url = f"https://api.github.com/users/{USERNAME}/events/public"
    req = urllib.request.Request(url, headers={"User-Agent": "readme-activity-script"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode())
    except Exception as exc:
        print(f"Failed to fetch events: {exc}")
        return []


def format_events(events):
    lines = []
    for e in events:
        fmt = EVENT_FORMATTERS.get(e.get("type"))
        if not fmt:
            continue
        try:
            text = fmt(e)
        except Exception:
            continue
        created = e.get("created_at", "")
        try:
            date_str = datetime.strptime(created, "%Y-%m-%dT%H:%M:%SZ").strftime("%b %d, %Y")
        except Exception:
            date_str = ""
        line = f"- {text} &mdash; {date_str}" if date_str else f"- {text}"
        lines.append(line)
        if len(lines) >= MAX_ITEMS:
            break
    return lines


def main():
    events = fetch_events()
    lines = format_events(events)
    if not lines:
        lines = [
            "- No public GitHub events in the last 90 days &mdash; recent build activity has "
            "been in private WGU environments and on [GitLab](https://gitlab.com/dmcnei29)."
        ]

    block = "\n".join(lines)

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(
        re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER), re.DOTALL
    )
    replacement = f"{START_MARKER}\n{block}\n{END_MARKER}"

    if pattern.search(content):
        new_content = pattern.sub(replacement, content)
    else:
        new_content = content

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)


if __name__ == "__main__":
    main()
