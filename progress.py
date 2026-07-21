#!/usr/bin/env python3
"""Count solved problems and rewrite the progress block in timeline.md.

Solved = a solution .py whose function body is real code (not just `pass`).
Run:  python progress.py
"""
import ast
import re
from pathlib import Path

ROOT = Path(__file__).parent
TOTAL = 474  # Striver's A2Z sheet
BAR_WIDTH = 25
TIMELINE = ROOT / "timeline.md"


def is_solved(py: Path) -> bool:
    try:
        tree = ast.parse(py.read_text())
    except SyntaxError:
        return False
    funcs = [n for n in tree.body if isinstance(n, ast.FunctionDef)]
    if not funcs:
        return False
    # stub = every function body is a single `pass` (the template)
    return any(not (len(f.body) == 1 and isinstance(f.body[0], ast.Pass)) for f in funcs)


def count_solved() -> int:
    n = 0
    for py in ROOT.rglob("*.py"):
        if py.name in {"_solution_template.py", "progress.py"} or "__pycache__" in py.parts:
            continue
        n += is_solved(py)
    return n


def main() -> None:
    solved = count_solved()
    pct = solved / TOTAL * 100
    filled = round(pct / 100 * BAR_WIDTH)
    bar = "█" * filled + "░" * (BAR_WIDTH - filled)
    block = (
        f"<!-- progress:start -->\n"
        f"**{solved} / {TOTAL} · {pct:.1f}%**\n\n"
        f"```\n{bar}\n```\n"
        f"<!-- progress:end -->"
    )
    text = TIMELINE.read_text()
    new = re.sub(r"<!-- progress:start -->.*?<!-- progress:end -->", block, text, flags=re.S)
    TIMELINE.write_text(new)
    print(f"{solved}/{TOTAL} ({pct:.1f}%)  {bar}")


if __name__ == "__main__":
    main()
    # self-check: solved count is within valid bounds
    assert 0 <= count_solved() <= TOTAL
