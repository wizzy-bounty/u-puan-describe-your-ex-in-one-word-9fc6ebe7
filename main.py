import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

WORD = "almost"


def resolve_out_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    out_dir = resolve_out_dir()
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
