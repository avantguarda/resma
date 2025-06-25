from typing import Literal

from jinja2 import pass_context
from jinja2.runtime import Context


@pass_context
def rel_path(
    context: Context,
    file_path: str,
    resource_type: Literal['static', 'style'],
) -> str:
    levels_to_go_up = context['page']['depth']

    relative_path_to_root = '../' * levels_to_go_up

    match resource_type:
        case 'style':
            resource_path = f'{relative_path_to_root}public/styles/{file_path}'
        case 'static':
            resource_path = f'{relative_path_to_root}public/static/{file_path}'
        case _:
            raise ValueError('resource_type must be either static or style')

    return resource_path
