# Hipertexto

**Hipertexto** is a static site generator (SSG) written in Python. Below you'll find information on how to set up the development environment, run the application, and run tests. 

## Installation

As of now, you can use `pipx` to install Hipertexto in your machine:

```sh
pipx install git+https://github.com/avantguarda/hipertexto
 ```

## Setting Up the Development Environment

To set up the development environment for Hipertexto, you'll need to have Python 3.12 installed. You can use [uv](https://docs.astral.sh/uv/) to manage dependencies and run commands.

1. **Clone the Repository:**

   ```sh
   git clone <repository-url>
   cd hipertexto
   ```

2. **Install uv:**

   If you don't have uv installed, you can install it by following the instructions on the [uv installation page](https://docs.astral.sh/uv/#installation).

3. **Install Dependencies:**

   ```sh
   uv sync
   ```

   This command will install all the necessary dependencies for both the application and development.

4. **Activate the Virtual Environment:**

   ```sh
   source .venv/bin/activate
   ```

## Running the Application

To run the application, use the following command:

```sh
ht
```

This command will start the Hipertexto application as defined in `hipertexto.main:app`.

## Development Commands

Hipertexto uses `taskipy` for task management. Here are some useful commands:

- **Linting:**

  ```sh
  task lint
  ```

  This command will run Ruff to check for code issues and display any differences.

- **Formatting:**

  ```sh
  task format
  ```

  This command will automatically format your code using Ruff.

- **Run Tests:**

  ```sh
  task test
  ```

  This will run the test suite using pytest and display coverage information.

- **Run Mypy:**

  ```sh
  task mypy
  ```

  This will run Mypy for type checking.

## Development Tools Configuration

- **Pytest:**

  Configuration for pytest is specified in `pyproject.toml` under `[tool.pytest.ini_options]`.

- **Mypy:**

  Configuration for Mypy is specified under `[tool.mypy]`.

- **Ruff:**

  Configuration for Ruff, including linting and formatting settings, is specified under `[tool.ruff]`.

## Contribution

If you would like to contribute to Hipertexto, please fork the repository and submit a pull request with your changes. Ensure that your changes pass the linting and testing requirements before submitting.

## Contact

For any questions or support, please contact:

- Thiago Campos: [commit@thigcampos.com](mailto:commit@thigcampos.com)
- Ivan Santiago: [ivansantiago.junior@gmail.com](mailto:ivansantiago.junior@gmail.com)

## License

Hipertexto is licensed under the [GNU General Public License v3.0](LICENSE).

Thank you for using Hipertexto!
