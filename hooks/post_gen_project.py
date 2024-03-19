"""Applies after the project is generated"""
import os
import shutil


def remove_paths(paths_to_remove):
    """Remove a list of path from the final generated project.

    Args:
        paths_to_remove: A list of conditional paths (directories or files) to be removed
    """
    for path in paths_to_remove:
        path = path.strip()
        if path:
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.unlink(path)


# Remove file related if the genrated project is not for opensource.
opensource_paths = [
    '{% if cookiecutter.is_opensource == "no" %} tests/test_copyright_header.py {% endif %}'
]
remove_paths(opensource_paths)

docker_paths = [
    '{% if cookiecutter.use_docker == "no" %} start.sh {% endif %}',
    '{% if cookiecutter.use_docker == "no" %} run.sh {% endif %}',
    '{% if cookiecutter.use_docker == "no" %} Dockerfile {% endif %}',
    '{% if cookiecutter.use_docker == "no" %} .github/workflows/build-docker.yml {% endif %}',
]
remove_paths(docker_paths)
