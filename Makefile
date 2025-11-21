# Makefile for AI-OSINT-Framework

.PHONY: help install install-dev test lint format security clean docs run-example

# Default target
help:
	@echo "AI-OSINT-Framework - Development Commands"
	@echo ""
	@echo "Setup:"
	@echo "  make install      Install production dependencies"
	@echo "  make install-dev  Install development dependencies"
	@echo ""
	@echo "Code Quality:"
	@echo "  make test         Run tests with pytest"
	@echo "  make lint         Run linters (flake8, mypy)"
	@echo "  make format       Format code (black, isort)"
	@echo "  make security     Run security scans (bandit, safety)"
	@echo ""
	@echo "Documentation:"
	@echo "  make docs         Generate documentation"
	@echo ""
	@echo "Examples:"
	@echo "  make run-example  Run basic WHOIS example"
	@echo ""
	@echo "Utilities:"
	@echo "  make clean        Remove build artifacts"

# Installation
install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

# Testing
test:
	pytest tests/ -v --cov=core --cov=modules --cov=ai_tools --cov-report=term --cov-report=html

# Code quality
lint:
	flake8 core/ modules/ ai_tools/ legal/ --max-line-length=88 --extend-ignore=E203
	mypy core/ modules/ ai_tools/ legal/ --ignore-missing-imports

format:
	black .
	isort .

# Security
security:
	bandit -r core/ modules/ ai_tools/ legal/ -f screen
	safety check
	pip-audit

# Documentation
docs:
	@echo "Generating documentation..."
	pdoc --html --output-dir docs/ core/ modules/ ai_tools/ legal/
	@echo "Documentation generated in docs/"

# Examples
run-example:
	python examples/basic_lookup.py

run-advanced:
	python examples/advanced_analysis.py

# Cleanup
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	rm -rf build/ dist/ .pytest_cache/ .coverage htmlcov/ .mypy_cache/
	@echo "Cleaned build artifacts"
