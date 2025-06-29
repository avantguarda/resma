import shutil
from pathlib import Path

import pytest


@pytest.fixture
def temp_dir():
    temp_dir = Path('temp_test_dir')
    temp_dir.mkdir(exist_ok=True)
    yield temp_dir

    # removing the temp_dir
    shutil.rmtree(temp_dir)


@pytest.fixture
def full_hipertexto_project(temp_dir):
    # copy hipertexto project from assets to temp_dir
    shutil.copytree(
        'tests/assets/full_hipertexto_project', temp_dir, dirs_exist_ok=True
    )

    return temp_dir
