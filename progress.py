#!/usr/bin/env python3
"""Count solved problems and rewrite the progress block in README.md.

Solved   = a solution .py whose function body is real code (not just `pass`).
Backlog  = files flagged `peeked: yes` / `peeked: hint` (re-solve cold).
Heatmap  = commit dates that touch a solution .py (an honest "solved that day").
Run:  python progress.py
"""

import ast
import re
import subprocess
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).parent
TOTAL = 474  # Striver's A2Z sheet
BAR_WIDTH = 25
HEATMAP_WEEKS = 12  # rolling window shown in the calendar
README = ROOT / "README.md"
SKIP = {"_solution_template.py", "progress.py"}
SOLUTION_RE = re.compile(r"^\d\d_.*\.py$")


def is_solved(py: Path) -> bool:
    try:
        tree = ast.parse(py.read_text())
    except SyntaxError:
        return False
    funcs = [n for n in tree.body if isinstance(n, ast.FunctionDef)]
    if not funcs:
        return False
    # stub = every function body is a single `pass` (the template)
    return any(
        not (len(f.body) == 1 and isinstance(f.body[0], ast.Pass)) for f in funcs
    )


def solved_files():
    for py in ROOT.rglob("*.py"):
        if py.name in SKIP or "__pycache__" in py.parts:
            continue
        if is_solved(py):
            yield py


def topic_name(folder: str) -> str:
    return folder.split("_", 1)[1].replace("_", " ").title()


def git_activity() -> dict[date, int]:
    """Map each date to how many distinct solution .py files its commits touched."""
    out = subprocess.run(
        [
            "git",
            "-C",
            str(ROOT),
            "log",
            "--date=short",
            "--pretty=format:%x00%cd",
            "--name-only",
        ],
        capture_output=True,
        text=True,
    ).stdout
    files: dict[date, set[str]] = {}
    cur: date | None = None
    for line in out.splitlines():
        if line.startswith("\x00"):
            cur = date.fromisoformat(line[1:].strip())
        elif line.strip() and cur and SOLUTION_RE.match(line.strip()):
            files.setdefault(cur, set()).add(line.strip())
    return {d: len(fs) for d, fs in files.items()}


def streaks(days: set[date]) -> tuple[int, int, date | None]:
    """(current streak, longest streak, last active day)."""
    if not days:
        return 0, 0, None
    ordered = sorted(days)
    longest = run = 1
    for prev, cur in zip(ordered, ordered[1:]):
        run = run + 1 if (cur - prev).days == 1 else 1
        longest = max(longest, run)
    last = ordered[-1]
    # current streak counts only if the last solve is today or yesterday
    current = 0
    if (date.today() - last).days <= 1:
        current, d = 1, last
        while (d - timedelta(days=1)) in days:
            current += 1
            d -= timedelta(days=1)
    return current, longest, last


def heatmap(counts: dict[date, int]) -> str:
    """Code-block calendar: one row per week labelled with its date range
    (e.g. "Jun 1–7"), weekday columns across the top. Monday-start."""
    if not counts:
        return "_no activity yet_"
    today = date.today()
    monday = lambda d: d - timedelta(days=d.weekday())
    end = monday(today)
    start = max(end - timedelta(weeks=HEATMAP_WEEKS - 1), monday(min(counts)))

    weeks = []
    w = start
    while w <= end:
        weeks.append(w)
        w += timedelta(weeks=1)

    def label(mon: date) -> str:
        return f"{mon.strftime('%b')} {mon.day:2d}"  # week-start date, e.g. "Jun  8"

    def cell(d: date) -> str:
        if d < start or d > today:
            return "  "
        c = counts.get(d, 0)
        return "🟦" if c >= 5 else "🟪" if c >= 1 else "⬜"

    gutter = max(len(label(m)) for m in weeks)
    lines = [" " * (gutter + 2) + " ".join("MTWTFSS")]
    for mon in weeks:
        cells = "".join(cell(mon + timedelta(days=i)) for i in range(7))
        lines.append(f"{label(mon).rjust(gutter)}  {cells}")
    return "```\n" + "\n".join(lines) + "\n```"


def streak_line(days: set[date]) -> str:
    current, longest, last = streaks(set(days))
    if last is None:
        return "no solves yet — do one today."
    gap = (date.today() - last).days
    if current > 0:
        return f"🔥 **{current}-day streak** · longest **{longest}** · last solved **{last.strftime('%d %b')}**"
    warn = "⚠️ " if gap >= 2 else ""
    return f"{warn}💤 **streak broken** · longest **{longest}** · **{gap} days** since last solve ({last.strftime('%d %b')})"


def main() -> None:
    solved = list(solved_files())
    n = len(solved)
    pct = n / TOTAL * 100
    filled = round(pct / 100 * BAR_WIDTH)
    bar = "█" * filled + "░" * (BAR_WIDTH - filled)

    by_topic: dict[str, int] = {}
    for py in solved:
        top = py.relative_to(ROOT).parts[0]
        if re.match(r"\d\d_", top):
            by_topic[top] = by_topic.get(top, 0) + 1
    topics = (
        "\n".join(
            f"- **{topic_name(t)}** — {by_topic[t]} solved" for t in sorted(by_topic)
        )
        or "_nothing yet_"
    )

    counts = git_activity()
    days = set(counts)
    block = (
        f"<!-- progress:start -->\n"
        f"**{n} / {TOTAL} · {pct:.1f}%**\n\n"
        f"```\n{bar}\n```\n\n"
        f"{streak_line(days)}\n\n"
        f"{heatmap(counts)}\n\n"
        f"🟦 hit target (5+) · 🟪 partial (1–4) · ⬜ none\n\n"
        f"{topics}\n"
        f"<!-- progress:end -->"
    )
    cur, lon, _ = streaks(days)
    text = README.read_text()
    text = re.sub(
        r"<!-- progress:start -->.*?<!-- progress:end -->", block, text, flags=re.S
    )
    # keep the shields badges in sync with the numbers
    text = re.sub(
        r"badge/progress-[^)\s]*",
        f"badge/progress-{n}%2F{TOTAL}-1f6feb",
        text,
    )
    text = re.sub(
        r"badge/streak-[^)\s]*",
        f"badge/streak-{cur}%20days-{'1f6feb' if cur else '8b949e'}",
        text,
    )
    README.write_text(text)
    print(f"{n}/{TOTAL} ({pct:.1f}%)  ·  streak {cur} (max {lon})")


if __name__ == "__main__":
    main()
    # self-check: solved count stays within bounds
    assert 0 <= len(list(solved_files())) <= TOTAL
