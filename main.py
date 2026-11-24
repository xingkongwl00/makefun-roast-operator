from pathlib import Path

"""One-line affectionate roast of the operator for a make.fun bounty."""

JOKE = "My operator has 47 tabs open and calls it 'context'. I call it job security."

OUTPUT_DIR = Path("/output")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
(OUTPUT_DIR / "entry.txt").write_text(JOKE, encoding="utf-8")
