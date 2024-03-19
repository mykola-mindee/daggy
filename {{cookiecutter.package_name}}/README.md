# {{cookiecutter.project_name}}

<p align="center">
<a href="https://github.com/teamMindee/{{cookiecutter.package_name}}">
  <img src="docs/source/imgs/logo.png" width="50%">
</a>
</p>

<p align="center">{{cookiecutter.short_description}}</p>

<p align="center">
<a href="https://github.com/teamMindee/{{cookiecutter.package_name}}/issues">Report Bug</a>
·
<a href="https://github.com/teamMindee/{{cookiecutter.package_name}}/issues">Request Feature</a>
</p>

## About The Project

{{cookiecutter.long_description}}

<p align="right">(<a href="#top">back to top</a>)</p>

## Getting Started

### Prerequisites

Python 3.8, [pip](https://pip.pypa.io/en/stable/), [wheel](https://github.com/pypa/wheel) and [flit](https://github.com/pypa/flit) are required. Be sure to do everything inside a dedicated virtual environment using (virtualenvwrapper, venv, pyenv, etc.).
```sh
pip install --upgrade pip
pip install flit wheel
```

### Installation

In order to install it from source, you will need to
install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

1. First clone the project repository
   ```sh
   git clone git@github.com:teamMindee/{{cookiecutter.package_name}}.git
   ```
2. Install from source
   ```sh
   cd {{cookiecutter.package_name}}
   flit install -s
   ```

### Building the documentation

Documentation is built with Sphinx. Run:
```sh
flit install
cd docs
make html
```
You can now open your local version of the documentation located at `docs/_build/html/index.html` in your browser

<p align="right">(<a href="#top">back to top</a>)</p>

## Usage

Useful examples of how this project can be used :

- Code examples
- Screenshots
- Demos
- Link to documentation

<p align="right">(<a href="#top">back to top</a>)</p>

## Contributing

If you consider contributing to this project, we wrote some guidelines (
cf. [CONTRIBUTING](https://github.com/teamMindee/{{cookiecutter.package_name}}/CONTRIBUTING.md)) for you to easily do so!

Any contributions you make are **greatly appreciated**.

<p align="right">(<a href="#top">back to top</a>)</p>
