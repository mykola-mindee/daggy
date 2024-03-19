"""Test cookiecutter.

This code is largely inspired from cookiecutter-pypackage repository :
    https://github.com/audreyfeldroy/cookiecutter-pypackage/
"""
import shlex
import subprocess

import pytest
from cookiecutter.utils import work_in


def run_inside_dir(command, dirpath):
    """Run a command from inside a given directory, returning the exit status.

    Args:
        command: Command that will be executed.
        dirpath: String, path of the directory the command is being run.
    """
    with work_in(dirpath):
        return subprocess.check_call(shlex.split(command))


def test_bake(cookies):
    """Bake the default template and test that we find expected folders."""
    result = cookies.bake()
    assert result.project_path.is_dir()
    assert result.exit_code == 0
    assert result.exception is None

    assert result.project_path.joinpath("src/github_project_name").exists()
    assert result.project_path.joinpath("tests").exists()


def test_bake_and_install_package(cookies):
    """Bake the default template and install package."""
    result = cookies.bake()
    assert run_inside_dir("flit install --deps production", result.project_path) == 0


@pytest.mark.parametrize("dependencies", ["dev,doc", "dev,test", "doc,test", "dev,doc,test", "all"])
def test_bake_and_install_package_with_extra_dependencies(cookies, dependencies):
    """Bake the default template, install package and extra dependencies."""
    result = cookies.bake()
    assert (
        run_inside_dir(
            f"flit install --deps production --extras {dependencies}", result.project_path
        )
        == 0
    )


def test_bake_and_run_precommmit(cookies):
    """Bake the default template and run pre-commit."""
    result = cookies.bake()
    assert run_inside_dir("flit install --deps production --extras dev", result.project_path) == 0
    assert run_inside_dir("git init", result.project_path) == 0
    assert run_inside_dir("pre-commit run -a", result.project_path) == 0


@pytest.mark.parametrize("is_opensource", ["no", "yes"])
def test_bake_and_test(cookies, is_opensource):
    """Bake the default template and test."""
    result = cookies.bake(extra_context={"is_opensource": is_opensource})
    assert run_inside_dir("flit install --deps production --extras test", result.project_path) == 0
    assert run_inside_dir("pytest", result.project_path) == 0
    if is_opensource == "yes":
        assert result.project_path.joinpath("tests/test_copyright_header.py").exists()
    else:
        assert not result.project_path.joinpath("tests/test_copyright_header.py").exists()


def test_bake_and_generate_shinx_doc(cookies):
    """Bake the default template and generate the doc."""
    result = cookies.bake()
    assert run_inside_dir("flit install --deps production --extras doc", result.project_path) == 0
    assert run_inside_dir("make html", result.project_path / "docs") == 0
    assert result.project_path.joinpath("docs/_build").exists()


@pytest.mark.parametrize("use_docker", ["no", "yes"])
def test_use_docker(cookies, use_docker):
    """Bake the default template and test."""
    result = cookies.bake(extra_context={"use_docker": use_docker})
    assert run_inside_dir("flit install --deps production --extras test", result.project_path) == 0
    assert run_inside_dir("pytest", result.project_path) == 0
    files = ["Dockerfile", "start.sh", "run.sh", ".github/workflows/build-docker.yml"]
    if use_docker == "yes":
        for f in files:
            assert result.project_path.joinpath(f).exists()
    else:
        for f in files:
            assert not result.project_path.joinpath(f).exists()
