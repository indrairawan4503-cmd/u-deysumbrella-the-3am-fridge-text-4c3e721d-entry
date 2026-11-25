"""make.fun entry runner: writes the entry text to the output directory.

The grader runs this script in a sandbox where the repository may be
mounted read-only, so the primary output target is ``MAKEFUN_OUTPUT_DIR``
(default ``/output``). A best-effort copy next to this script is kept for
local inspection only and must never fail the run.
"""

import os

ENTRY_TEXT = ("The microwave reheated your burrito three times tonight and told no one. I did. It's 3am and I keep receipts, not leftovers. — Fridge")


def output_dir():
    """Return the directory the grader collects the entry from."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(path):
    """Write the entry text to ``path`` (UTF-8, no trailing newline)."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


def write_local_copy():
    """Best-effort copy of the entry next to this script.

    Silently skipped when the repo is read-only (e.g. in the grader
    sandbox); the collected output in ``MAKEFUN_OUTPUT_DIR`` is the
    authoritative artifact, so a failure here is not an error.
    """
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        write_entry(os.path.join(here, "entry.txt"))
    except OSError:
        pass


def main():
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    write_entry(os.path.join(out_dir, "entry.txt"))
    write_local_copy()

if __name__ == "__main__":
    main()
