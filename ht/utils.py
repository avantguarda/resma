from pathlib import Path


def calculate_depth(md_file: Path, root_dir: Path) -> int:
    return len(md_file.relative_to(root_dir).parts) - 1
