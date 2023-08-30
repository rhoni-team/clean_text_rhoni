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

### Contributions on code

1. Code is located in `src/clean_text_rhoni` folder.
You can add features, fix or refactor existing code.

2. When you're done making changes, check that your changes conform to any code formatting requirements and pass any tests.

If you add new features: 

* add the corresponding test in `test/` folder.
* modify or add documentation if necessary

This package uses [`pytest`](https://docs.pytest.org/en/7.4.x/) for testing.
To run the package’s tests, you must be in the root of the package and run:

```
pytest tests/
```

3. To commit your changes, please follow the [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/) conventions.


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
