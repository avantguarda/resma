import locale
from pathlib import Path

import frontmatter
from jinja2 import Environment, TemplateNotFound
from markdown import markdown  # type: ignore

from ht.images import copy_images_and_update_path
from ht.utils import calculate_depth


def validate_frontmatter(page, file):
    if (
        not page.metadata
        or not page.metadata.get('template')
        or not page.metadata.get('title')
    ):
        raise ValueError(f'Frontmatter of {file} malformed')


def get_template(jinja_env, page):
    try:
        return jinja_env.get_template(page.metadata.get('template'))
    except TemplateNotFound:
        raise TemplateNotFound(
            f'Template {page.metadata.get("template")} not found'
        )


def process_markdown(
    file: Path,
    jinja_env: Environment,
    content_dir: Path,
    public_dir: Path,
    root_dir: Path,
    section_dir: Path | None = None,
    section_pages: list | None = None,
):
    page = frontmatter.load(file)
    validate_frontmatter(page, file)
    corrected_content = copy_images_and_update_path(
        content_dir, public_dir / 'static', file, root_dir, page.content
    )

    html = markdown(corrected_content)
    template = get_template(jinja_env, page)
    output_dir = section_dir or public_dir
    context = {
        **page.metadata,
        'content': html,
        'depth': calculate_depth(file, root_dir),
    }

    if file.stem == '_index':
        context['url'] = f'{output_dir}/'
        context['pages'] = section_pages
        html_filename = 'index.html'
    else:
        context['url'] = file.stem
        html_filename = f'{file.stem}.html'

    rendered_html = template.render(page=context)
    with open(
        output_dir / html_filename,
        'w',
        encoding=locale.getpreferredencoding(False),
    ) as f:
        f.write(rendered_html)

    return context
