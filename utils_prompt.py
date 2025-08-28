# utils_prompt.py (skeleton)
from pathlib import Path

def load_prompt(name: str) -> str:
    private = Path("prompts_private") / f"{name}.md"
    public  = Path("prompts")         / f"{name}.md"
    src = private if private.exists() else public
    if not src.exists():
        raise FileNotFoundError(f"Prompt file not found: {private} or {public}")
    return src.read_text(encoding="utf-8")
