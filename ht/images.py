import re
import shutil
from pathlib import Path


def copy_images_and_update_path(
    content_dir: Path,
    public_static_dir: Path,
    markdown_file: Path,
    root_dir: Path,
    no_frontmatter_content: str,
) -> str:
    img_path = re.compile(r'!\[.*\]\((.*)\)')

    images = re.findall(img_path, no_frontmatter_content)

    md_parent = markdown_file.parent
    for img_path in images:
        if 'http' in str(img_path):
            continue
        img_file = (
            content_dir / str(img_path)
            if md_parent == 'contents'
            else md_parent / str(img_path)
        )

        if img_file.exists():
            shutil.copy2(img_file, public_static_dir)

        folders_to_go_up = (
            len(markdown_file.relative_to(root_dir).parts[:-1]) - 1
        )

        relative_path_to_root = (
            ('../' * folders_to_go_up) if folders_to_go_up > 0 else './'
        )

        new_image_path = (
            f'{relative_path_to_root}{public_static_dir.name}/{img_file.name}'
        )
        no_frontmatter_content = no_frontmatter_content.replace(
            (str(img_path)), new_image_path
        )

    return no_frontmatter_content
