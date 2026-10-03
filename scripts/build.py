"""Build the clean parks dataset from files in data/raw.

Right now this only checks the folders exist. Tasks will add fetching and cleaning.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
CLEAN = ROOT / "data" / "clean"


def main() -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    CLEAN.mkdir(parents=True, exist_ok=True)
    raw = [p for p in RAW.iterdir() if not p.name.startswith(".")]
    print(f"raw files: {len(raw)}")


if __name__ == "__main__":
    main()
