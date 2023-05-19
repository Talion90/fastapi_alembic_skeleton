#!/bin/bash

black . && isort . && flake8 && pytest
