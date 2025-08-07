from pathlib import Path
from typing import List
from filename_aliases import FILENAME_ALIASES
import re


def recursive_directory_walk(directory_path: Path, ends_with: List[str] = None) -> List[Path]:
    directory_path.mkdir(exist_ok=True)
    if ends_with is None:
        return [file for file in directory_path.rglob('*') if file.is_file()]
    else:
        return [file for file in directory_path.rglob('*') if file.is_file() and file.suffix.lower() in ends_with]


def normalize_name(name: str) -> str:
    # Leaving only Russian and English letters a-z, а-я, and ё
    letters_only = re.findall(r'[a-zа-яё]+', name.lower())
    return ''.join(letters_only)


def resolve_filename(filepath: Path) -> str | None:
    filename = normalize_name(filepath.stem)
    for key, aliases in FILENAME_ALIASES.items():
        for alias in aliases:
            if filename == normalize_name(alias):
                return key
    return None


def resolve_filedate(filepath: Path) -> str | None:
    pass
