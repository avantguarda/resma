import locale

import pytest
from rich.text import Text

from hipertexto import __version__
from hipertexto.main import app


def test_start(temp_dir, monkeypatch, capsys: pytest.CaptureFixture):
    monkeypatch.chdir(temp_dir)
    result = app('start project')

    output = Text.from_ansi(capsys.readouterr().out).plain

    assert not result
    assert 'Project project created successfully' == output


def test_start_project_already_exists(
    temp_dir, monkeypatch, capsys: pytest.CaptureFixture
):
    monkeypatch.chdir(temp_dir)

    app('start project')
    with pytest.raises(SystemExit) as e:
        app('start project')

    assert e.value.code == 1
    assert 'File project already exists' in capsys.readouterr().err


def test_build_hipertexto_project_not_found(
    temp_dir, monkeypatch, capsys: pytest.CaptureFixture
):
    monkeypatch.chdir(temp_dir)

    with pytest.raises(SystemExit) as e:
        app('build')

    assert e.value.code == 1
    assert 'Not a hipertexto project' in capsys.readouterr().err


def test_build_empty_project(
    temp_dir, monkeypatch, capsys: pytest.CaptureFixture
):
    monkeypatch.chdir(temp_dir)

    app('start project')

    monkeypatch.chdir('project')
    with pytest.raises(SystemExit) as e:
        app('build')

    assert e.value.code == 1
    assert (
        'Content and Templates directories cannot be empty'
        in capsys.readouterr().err
    )


def test_build_hipertexto_table_not_found_in_config_toml(
    temp_dir, monkeypatch, capsys: pytest.CaptureFixture
):
    monkeypatch.chdir(temp_dir)
    app('start project')

    monkeypatch.chdir('project')

    # erasing hipertexto table from config.toml
    with open(
        'config.toml', 'w', encoding=locale.getpreferredencoding(False)
    ) as f:
        f.write('')

    with pytest.raises(SystemExit) as e:
        app('build')

    assert e.value.code == 1
    assert (
        'config.toml should have a hipertexto table' in capsys.readouterr().err
    )


@pytest.mark.parametrize(
    ('args', 'expected_output'),
    [
        ([], 'ht --help'),
        (
            ['--help'],
            'Usage',
        ),
        (['--version'], __version__),
    ],
    ids=['default', 'help', 'version'],
)
def test_main(args, expected_output, capsys: pytest.CaptureFixture):
    result = app(args)

    assert not result
    assert expected_output in capsys.readouterr().out


def test_build_full_hipertexto_project_ok(
    full_hipertexto_project, monkeypatch, capsys: pytest.CaptureFixture
):
    monkeypatch.chdir(full_hipertexto_project)
    result = app('build')

    assert not result
    assert 'Site built successfully' in capsys.readouterr().out
