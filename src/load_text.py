from pathlib import Path

def read_text_from_file(path):
    text = Path(path).read_text(encoding="utf-8")
    return text