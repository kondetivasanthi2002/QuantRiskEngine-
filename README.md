# Enterprise Financial Risk Analytics & Algorithmic Trading Platform (QuantRiskEngine)

A high-throughput, specialized domain platform for quantitative risk modeling, order book matching, SEC/MiFID compliance surveillance, and real-time portfolio analytics.

---

## Installation Guide

### How to install dependencies

To install all required dependencies for the project, run:

```bash
pip install -r requirements.txt
```

Alternatively, to install the package in editable development mode:

```bash
pip install -e .
```

---

## Build Instructions

### How to build the project

To build the package distribution artifacts (wheel and source distribution):

```bash
python -m build
```

Or using setuptools build target:

```bash
python setup.py build
```

---

## Running the Application

### How to run the application

To run the interactive system CLI demonstration and execute the 250 unit test suite:

```bash
python main.py
```

To start the live Institutional Web Terminal and REST API server on `http://localhost:8000`:

```bash
python server.py
```

To run the automated unit test suite directly:

```bash
python -m unittest discover -s tests
```

---

## Dependency Documentation

The project manages its dependencies using standard Python manifest files and lockfiles:
- **`requirements.txt`**: Production and development dependencies (pytest, fastapi, uvicorn, numpy, pandas, scipy).
- **`requirements.lock`**: Exact pinned dependency versions lockfile.
- **`Pipfile.lock`**: Locked dependencies specification file.
- **`setup.py`**: Package installation and setup manifest.
- **`pyproject.toml`**: Modern Python build system specification (PEP 517 / PEP 518).
