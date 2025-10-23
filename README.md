# Project Name

A simple Python project managed with [uv](https://github.com/astral-sh/uv).

## Prerequisites

- Python 3.8 or higher
- [uv](https://github.com/astral-sh/uv) package manager

## Installation

### Install uv

If you don't have `uv` installed, install it with:

```bash
# On macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Alternative: using pip
pip install uv
```

### Setup Project

1. Clone or download this repository
2. Navigate to the project directory
3. Install dependencies:

```bash
uv sync
```

This will create a virtual environment and install all required packages from `pyproject.toml`.

## Running the Script

Run the main script with:

```bash
uv run script.py
```

This command automatically:
- Uses the project's virtual environment
- Ensures all dependencies are installed
- Executes the script

## Project Structure

```
.
├── script.py          # Main Python script
├── pyproject.toml     # Project configuration and dependencies
├── uv.lock           # Lock file (auto-generated)
└── README.md         # This file
```

## Adding Dependencies

To add a new package:

```bash
uv add package-name
```

To add a development dependency:

```bash
uv add --dev package-name
```

## Development

For development work, you can activate the virtual environment:

```bash
# On macOS/Linux
source .venv/bin/activate

# On Windows
.venv\Scripts\activate
```

Then run the script directly:

```bash
python script.py
```

## License

[Your License Here]