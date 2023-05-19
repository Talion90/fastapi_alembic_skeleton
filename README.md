# FastApi_SQLModel_alembic_skeleton

This repository contains a skeleton project built with FastAPI, SQLModel, Alembic, Poetry, Black, Flake8, Isort, and Pytest. It also includes multiple Docker Compose configurations for different environments.

## Description

The skeleton project serves as a starting point for developing web applications using FastAPI and SQLModel. It incorporates essential tools and configurations commonly used in Python web development to ensure code quality, database migrations, package management, and testing.

## Features

- FastAPI: A modern, fast (high-performance), web framework for building APIs with Python 3.10+.
- SQLModel: A library for interacting with databases using SQLAlchemy Core for queries and Pydantic models for data validation.
- Alembic: A database migration tool that integrates with SQLAlchemy and provides a flexible way to manage database schema changes.
- Poetry: A dependency management and packaging tool for Python projects.
- Black: A Python code formatter that enforces a consistent style across the project.
- Flake8: A static analysis tool for checking Python code for style and quality issues.
- Isort: A Python utility to sort imports in an organized and standardized manner.
- Pytest: A testing framework that allows easy and scalable testing of Python code.

## Project Structure

```
.
├── alembic
├── database
│   ├── db
│   └── models
├── env
├── tests
├── utils
├── docker-compose.dev.yml
├── docker-compose.local.yml
├── docker-compose.prod.yml
└── README.md
```

- **alembic**: Contains database migration scripts managed by Alembic.
- **database**: Includes database-related code.
  - **db**: Stores database connection and configuration files.
  - **models**: Defines SQLAlchemy models.
- **env**: Stores environment-specific configurations and settings.
- **tests**: Contains test cases for the project.
- **utils**: Includes utility modules and helper functions.
- **docker-compose.dev.yml**: Docker Compose configuration for the development environment.
- **docker-compose.local.yml**: Docker Compose configuration for the local environment.
- **docker-compose.prod.yml**: Docker Compose configuration for the production environment.
- **README.md: This file.**

## Getting Started

### Prerequisites

- Python 3.10 or above
- Docker (for running with Docker Compose)

### Development Setup

1. Clone the repository:

```shell
git clone https://github.com/Talion90/fastapi_sqlmodel_alembic_skeleton.git
```

2. Change to the project directory:

```shell
cd fastapi_sqlmodel_alembic_skeleton
```

3. The easiest way to activate the virtual environment is to create a nested shell with poetry shell:

```shell
poetry shell
```

4. Install project dependencies using Poetry:

```shell
poetry install
```

5. Set up and start server in the development environment with Docker Compose:

```shell
docker-compose -f docker-compose.dev.yml up -d
```

6. Set up and start server in the production environment with Docker Compose:

```shell
docker-compose -f docker-compose.prod.yml up -d
```


7. Set up and start server in the local environment and test database postgres with Docker Compose:

```shell
docker-compose -f docker-compose.local.yml up -d
```
The API should now be accessible at [http://localhost:8000](http://localhost:8000).

Data migrations will be applying automatically.

### Testing

To run the tests, use the following command:

```shell
poetry run pytest
```

or with using linters:

```shell
poetry run bash run_cheks.sh
```