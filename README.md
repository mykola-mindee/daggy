<br />
<div align="center">
  <a href="https://github.com/teamMindee/project-template">
    <img src="https://raw.githubusercontent.com/cookiecutter/cookiecutter/3ac078356adf5a1a72042dfe72ebfa4a9cd5ef38/logo/cookiecutter_medium.png" alt="Logo">
  </a>

<h3 align="center">project-template</h3>
  <p align="center">
    Template for R&D projects.
    <br />
    <br />
    <a href="https://github.com/teamMindee/project-template/issues">Report Bug</a>
    ·
    <a href="https://github.com/teamMindee/project-template/issues">Request Feature</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#options-details">Options details</a></li>
  </ol>
</details>

## About The Project

This repository is a `cookiecutter` template for R&D projects. It contains :

- Ready-to-use github workflow CI to check :
    - Style: Black, flake8, isort, mypy, pydocstring and darglint
    - Build: Package installation with flit
    - Main: Unit tests in tests folder
- Config files :
    - `.flake8`: config file for flake8
    - `pyproject.toml`: global project config file
    - `.pre-commit-config.yaml`: pre-commit config file to launch style checks before each commit.
- Templated markdown files :
    - `README.md`, `CONTRIBUTING.MD`
    - Issue templates at ./github/ISSUE_TEMPLATE : `bug_report.md` and `feature_request.md`

<p align="right">(<a href="#top">back to top</a>)</p>

## Getting Started

### Usage

Here are the instructions to use this repository as a template.

Create a new project:
1. Create a new **empty** repository in github.
2. Share the repository with the appropriate teams.
3. Clone that repository on your computer in your usual workspace.
4. Install the [recommended cookiecutter version](https://github.com/teamMindee/project-template/blob/main/requirements.txt#L8) in a dedicated virtual environment
5. Generate the project by running

`cookiecutter git+ssh://git@github.com/teamMindee/project-template.git --overwrite-if-exists`
  * You’ll be asked to enter values to set the project.
  * If you don’t know what to enter, stick with the defaults. [Details about the parameters can be found below](#options-details).
6. A new folder with your boilerplate code has been created. Copy **the content of that new folder** inside the empty github folder created at the step 1.

<p align="right">(<a href="#top">back to top</a>)</p>

### Options details

* `project_name`: The name of the project in natural language (can contain spaces and uppercases).
* `package_name`: The package name in lower case and words joined by dashes. Default is set to formatted `project_name`.
* `module_name`: The module name in lower case and words joined by underscores. Default is set to formatted `package_name`.
* `short_description`: The project short description.
* `long_description`: The project long description.
* `is_opensource`: Project is opensource, if so it should contain copyright header. Default is `no`.
* `use_docker`: If True, add a Dockerfile to run the Python code inside and a CI to check that the Dockerfile can be built. Default is `yes`.

<p align="right">(<a href="#top">back to top</a>)</p>

## Contribution to this repository

### Prerequisites

Python 3.8 and [pip](https://pip.pypa.io/en/stable/) are required. Be sure to do everything inside a dedicated virtual environment using (virtualenvwrapper, venv, pyenv, etc.).

### Installation

In order to contribute to this repository or install it from source, you will need to
install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

1. First clone the project repository
   ```sh
   git clone git@github.com:teamMindee/project-template.git
   ```
2. Install from source
   ```sh
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#top">back to top</a>)</p>
