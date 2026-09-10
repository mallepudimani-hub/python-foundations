# Python Foundations

A production-oriented Python foundation project built as part of my transition from Senior Frontend Engineer to AI Engineer.

## Purpose

The goal of this project is not to learn Python syntax in isolation.

It is to build strong Python engineering fundamentals that will support the development of production AI applications throughout the six-month AI engineering roadmap.

The project focuses on:

* Modern Python 3.13
* Clean project structure
* Type hints
* Error handling
* Testing
* Code quality
* Static type checking
* Dependency management
* Reproducible development environments

## Tech Stack

* Python 3.13
* uv
* pytest
* Ruff
* mypy

## Project Structure

```text
python-foundations/
├── src/
│   └── python_foundations/
│       ├── __init__.py
│       └── main.py
├── tests/
│   └── test_main.py
├── .python-version
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

## Development Setup

### Prerequisites

* Python 3.13
* uv

### Install dependencies

```bash
uv sync
```

### Run the application

```bash
uv run python -m python_foundations.main
```

### Run tests

```bash
uv run pytest
```

### Run linting

```bash
uv run ruff check .
```

### Format code

```bash
uv run ruff format .
```

### Check formatting

```bash
uv run ruff format --check .
```

### Run static type checking

```bash
uv run mypy src
```

## Engineering Quality Gate

Before committing changes, the project should pass:

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv run mypy src
```

All checks must pass before changes are committed.

## Learning Context

This repository is part of the broader [AI Engineering Roadmap](https://github.com/mallepudimani-hub/ai-engineering-roadmap).

The six-month roadmap progresses from Python and backend engineering through:

1. Python and backend engineering
2. LLM application development
3. Embeddings and semantic search
4. Retrieval-Augmented Generation
5. Agentic workflows and tool calling
6. MCP
7. Evaluation and observability
8. Docker, cloud and production deployment
9. AI system design
10. Production AI applications

## Status

**Phase:** Python Foundations

**Status:** In progress
