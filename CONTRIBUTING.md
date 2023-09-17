# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

## Types of Contributions

### Report Bugs

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

### Write Documentation

You can never have enough documentation! Please feel free to contribute to any
part of the documentation, such as the official docs, docstrings, or even
on the web in blog posts, articles, and such.

### Submit Feedback

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

# Get Started!

Ready to contribute? Here's how to set up `clean_text_rhoni` for local development.

### Install the package for development

This package is developed by using `poetry` as package manager.
To install the package for development you will have to:

1. Download a copy of `clean_text_rhoni` locally.
2. Install `poetry` in your computer. Please check the last instalation instructions on their [website](https://python-poetry.org/).
3. Create a python environment and activate it.
4. Install `clean_text_rhoni` on editable-mode by using `poetry` in your environment:

    ```console
    $ poetry install
    ```

### Create a new git branch

1. Use `git` (or similar) to create a branch for local development and make your changes:

    ```console
    $ git checkout -b name-of-your-bugfix-or-feature
    ```

### Commiting changes

To commit your changes, please follow the [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) conventions.


### Contributions on code

1. Code is located in `src/clean_text_rhoni` folder.
You can add features, fix or refactor existing code.

2. When you're done making changes, check that your changes conform to any code formatting requirements and pass any tests.

If you add new features: 

* add the corresponding test in `test/` folder.
* modify or add documentation if necessary


### Testing the package

This package uses [`pytest`](https://docs.pytest.org/en/7.4.x/) for testing.
To run the package’s tests, you must be in the root of the package and run:

```
pytest tests/
```

**Testing the package on different python versions**

This package was developed on Ubuntu 22.04 and tested on python 3.8, 3.9, 3.10 and 3.11.
If you add new features, you have to test that the package is still working under the different versions.
The easiest way to do this, is by using [`Docker Compose`](https://docs.docker.com/compose/). The necessary `Dockerfiles` and the `docker-compose.yml` file are included in the package.
To run it, you'll have to:

1. Install [`docker`](https://docs.docker.com/engine/install/) in your computer.
2. Install [`docker compose`](https://docs.docker.com/compose/install/) in your computer.
3. Build the docker images defined in `docker-compose.yml`.
Open a terminal and go to the root of the package. Then run:

```bash
docker compose build
```
4. Start the services:

```bash
docker compose up
```

As result you will have to see that code coverage is calculated for each python version, and that every process is exited with code 0. This is, the processes were completed successfully without encountering any errors.

You will see something similar to:

```bash
clean_text_rhoni-py38-1 exited with code 0
```
for each python version that is being tested.

### Contributions on documentation

**Documenting functions and classes**

We use [`numpydoc style`](https://numpydoc.readthedocs.io/en/latest/format.html) to add docstrings. Please follow its conventions.

**Documenting README.md**

You can add examples or description of new features to the readme file if necessary.


## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include additional tests if appropriate.
2. If the pull request adds functionality, the docs should be updated.
3. The pull request should work for all currently supported operating systems and versions of Python.

## Code of Conduct

Please note that the `clean_text_rhoni` project is released with a
[Code of Conduct](CONDUCT.md). By contributing to this project you agree to abide by its terms.
