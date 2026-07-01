from pathlib import Path

def validate_path_file(path: str | Path) -> Path:
    path = Path(path)
    if not path.exists():
        return None, f"File not found: {path}"
    
    if not path.is_file():
        return None, f"Path not file: {path}"
    
    return path
