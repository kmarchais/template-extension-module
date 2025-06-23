# Template Extension Module

A modern template for creating Python extensions with C++, featuring a streamlined development experience and comprehensive CI pipeline.

## Features

- 🚀 Modern build system using [scikit-build-core](https://github.com/scikit-build/scikit-build-core) and CMake
- 🔧 C++ bindings with [pybind11](https://github.com/pybind/pybind11)
- 📦 Package management with [uv](https://github.com/astral-sh/uv)
- ✨ Code quality tools:
  - [Ruff](https://github.com/astral-sh/ruff) for linting and formatting
  - [mypy](https://github.com/python/mypy) for static type checking
  - [pre-commit](https://pre-commit.com/) for git hooks
- 🧪 Testing with [pytest](https://docs.pytest.org/)
- 🔄 Comprehensive CI/CD pipeline using GitHub Actions

## Getting Started

### Prerequisites

- Python 3.9 or later
- C++ compiler (e.g., GCC, Clang, MSVC)
- CMake

### Installation

1. Clone the repository:

```bash
git clone https://github.com/kmarchais/template-extension-module
cd template-extension-module
```

2. Install dependencies and build the package:

```bash
uv sync
```

If you've already built the package and want to rebuild it:

```bash
uv sync --reinstall
```

### Development Setup

1. Install pre-commit hooks:

```bash
pre-commit install
```

2. Run tests:

```bash
uv run pytest
```

3. Run the installed executable:

```bash
uv run template-extension-module
```

Note: No virtual environment activation is required when using `uv run` commands!

## Project Structure

```plaintext
template-extension-module/
├── src/                    # C++ source files
├── python/                 # Python source files
├── tests/                  # Test files
├── CMakeLists.txt          # CMake configuration
└── pyproject.toml          # Python project configuration
```

## Development Workflow

### Code Quality

The project uses several tools to maintain code quality:

- **Ruff**: For both linting and formatting Python code
- **mypy**: For static type checking
- **pre-commit**: Runs checks before each commit

Run checks manually:

```bash
uv run pre-commit run --all-files
```

### Testing

Run the test suite:

```bash
uv run pytest
```

### Building

The project uses scikit-build-core as the build backend, which automatically handles the CMake configuration and building process.

## Continuous Integration

The project includes several GitHub Actions workflows:

1. **Code Quality Checks**
   - Runs pre-commit hooks
   - Performs type checking
   - Ensures code formatting

2. **Build and Test**
   - Builds the package
   - Runs test suite
   - Tests installation

3. **Package Distribution**
   - Builds wheels for all supported platforms and Python versions
     - Using `manylinux` for Linux
     - Supporting `x86_64` and `arm64` architectures for MacOS
   - Creates source distribution
   - Publishes to PyPI or TestPyPI

## Contributing

Contributions are welcome! Do not hesitate to open an issue or a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This template is built with the following excellent tools:

- [scikit-build-core](https://github.com/scikit-build/scikit-build-core)
- [pybind11](https://github.com/pybind/pybind11)
- [uv](https://github.com/astral-sh/uv)
