#!/usr/bin/env python3
from __future__ import annotations
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = REPO_ROOT / "src"

def main() -> None:
    if not (SRC_DIR / "app.py").exists():
        print("[FAIL] Missing src/app.py")
        sys.exit(1)

    print("[OK] Layout looks good.")
    print("\nCanonical PyCharm mapping (ONE mapping only):")
    print(f"  Local : {SRC_DIR}")
    print("  Remote: /var/task")
    print("\nSAM packages deps from src/requirements.txt (CodeUri: src/).")

if __name__ == "__main__":
    main()
