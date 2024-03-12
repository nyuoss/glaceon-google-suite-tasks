# Open Source Python Template

This is an advanced template for designing and developing Python projects with CI/CD. This template serves as a foundation and includes features for build management, unit testing, continuous integration, static analysis, code style adherence, and component specification.

The details of this template are listed below:

- The programming language: Python

- Testing Framework: Pytest

- Continuous Integration Solution: GitHub Actions, CircleCI

- Static Analysis Tools: Ruff, Flake8, MyPy

- Code Formatting Solution: Black

- Package/Dependency Manager: PDM (Python Dependency Management)

## Initial Setup

Install PDM as package and dependency manager:

    pip install pdm

Install initial dependencies:

    pdm install --dev

To update dependencies, run the following:

    pdm update

## Using Features

To use mypy, run the following:

    pdm run mypy <filename>

To use ruff, run the following:

    pdm run ruff <filename>

To use pytest, run the following:

    pdm run pytest tests/test_addition.py

To run the application, run the following:

    pdm run src/main.py
    
## Component Path

For now, we're focusing on two components: the test and the function itself.

To develop or maintain features, navigate to the /src directory.

    cd src

To add or modify test component, navigate to the /tests directory.

    cd tests

## Continuous Integration with GitHub Actions
This project is configured to use GitHub Actions for continuous integration. Every push to the repository triggers automated tests and checks to ensure code quality and functionality.

To see the status of your build, navigate to the main page of the repository. Go to Actions, and in the left sidebar, click the workflow you want to display. From the list of workflow runs, click the name of the run you want to see. There, you can view the logs that shows you how each of the steps was processed.

If you need to customize the build process, modify the `.github/workflows/github-actions.yml` file according to your needs. For detailed instructions, refer to the [GitHub Actions Documentation](https://docs.github.com/en/actions).

## Continuous Integration with CircleCI

As an alternative, this project is also configured to use CircleCI for continuous integration. 

To see the status of your build, visit the CircleCI dashboard. There, you can view the progress and results of the build tests, static analysis, and more for your latest commits.

If you need to customize the build process, modify the `.circleci/config.yml` file according to your needs. For detailed instructions, refer to the [CircleCI Configuration Reference](https://circleci.com/docs/2.0/configuration-reference/).

## Contributors - Team Glaceon 

- Yifei Zhuang
- Fan Yang
- Bowen Gong
- Yanglin Tao
- Winnie Zheng
- Kaining Mao
