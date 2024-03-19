# How to contribute to {{cookiecutter.project_name}}?

Everything you need to know to contribute efficiently to the project.

Everyone in the team is welcome to contribute !

## Codebase structure

- [{{cookiecutter.project_name}}](https://github.com/teamMindee/{{cookiecutter.package_name}}/blob/main/src) - The package codebase
- [test](https://github.com/teamMindee/{{cookiecutter.package_name}}/blob/main/tests) - Python unit tests

## Continuous Integration

This project uses the following integrations to ensure proper codebase maintenance:

- [Github Worklow](https://help.github.com/en/actions/configuring-and-managing-workflows/configuring-a-workflow) - run
  jobs for package build and coverage

As a contributor, you will only have to **ensure coverage of your code** by adding appropriate **unit testing** of your
code.

## Submitting a new issue or feature request

Use Github [issues](https://github.com/teamMindee/{{cookiecutter.package_name}}/issues) for feature requests, or bug reporting.

When doing so, use [issue templates](https://github.com/teamMindee/{{cookiecutter.package_name}}/blob/main/.github/ISSUE_TEMPLATE) whenever
possible and provide enough information for other contributors to jump in.

## Developing {{cookiecutter.project_name}}

### Commits

- **Code**: ensure to provide docstrings to your Python code. In doing so, please
  follow [Google-style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) so it can ease the
  process of documentation later.
- **Commit message**: please
  follow [Contribution guidelines](https://www.notion.so/Git-guidelines-168e3b4cf2d9430e8804f3e9c76c2bbb)

### Running CI verifications locally

#### Pre-commit

We check that your commits complies with the CI workflow using [`pre-commit`](https://pre-commit.com/). You can launch then locally in your terminal by installing the dev optional dependencies and running `pre-commit install` then `pre-commit run -a`. To run a single hook `pre-commit run -a hook-id`.

#### Unit tests

In order to run the same unit tests as the CI workflows, you can run unittests locally:

```sh
pytest
```

### Modifying the documentation

If you add a function/feature to the package, don't forget to add the entry in the documentation!
(Go to the file: `docs/source/modules/module.rst` and add `.. autoclass:: your added class` or `.. autofunction:: your added function` at the corresponding place).

In order to check locally your modifications to the documentation, go to /docs and run:

```sh
make html
```

You can now open your local version of the documentation located at `docs/_build/html/index.html` in your browser.

Additionally, you can check the coverage of your documentation by running:

```sh
make html SPHINXOPTS="-b coverage"
```

You can now open the coverage report at `docs/_build/html/python.txt`.
