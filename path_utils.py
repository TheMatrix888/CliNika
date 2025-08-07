from pathlib import Path
from typing import List


def recursive_directory_walk(directory_path: Path, ends_with: List[str] = None) -> List[Path]:
    if ends_with is None:
        return [file for file in directory_path.rglob('*') if file.is_file()]
    else:
        return [file for file in directory_path.rglob('*') if file.is_file() and file.suffix.lower() in ends_with]
