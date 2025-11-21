# Contributing to AI-OSINT-Framework

Thank you for your interest in contributing to AI-OSINT-Framework! This document provides guidelines and best practices for contributing to this project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Standards](#coding-standards)
- [Legal Compliance Checklist](#legal-compliance-checklist)
- [Pull Request Process](#pull-request-process)
- [Adding New Modules](#adding-new-modules)
- [Testing Requirements](#testing-requirements)
- [Documentation Guidelines](#documentation-guidelines)

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive environment for all contributors, regardless of background, identity, or experience level.

### Our Standards

- ✅ Use welcoming and inclusive language
- ✅ Be respectful of differing viewpoints
- ✅ Accept constructive criticism gracefully
- ✅ Focus on what is best for the community
- ✅ Show empathy towards others

### Unacceptable Behavior

- ❌ Harassment or discriminatory language
- ❌ Trolling or insulting comments
- ❌ Publishing others' private information
- ❌ Contributing code for illegal purposes
- ❌ Any unethical OSINT practices

## How Can I Contribute?

### 🐛 Reporting Bugs

Before creating a bug report:
1. Check existing issues to avoid duplicates
2. Collect relevant information (OS, Python version, error logs)
3. Try to reproduce the issue

Create a bug report with:
- Clear, descriptive title
- Steps to reproduce
- Expected vs actual behavior
- Error messages and logs
- Your environment details

### 💡 Suggesting Features

Feature suggestions should:
- Align with project goals (ethical, legal OSINT)
- Include clear use cases
- Consider legal implications
- Provide implementation ideas (optional)

### 🔧 Code Contributions

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Write/update tests
5. Update documentation
6. Commit with clear messages
7. Push to your fork
8. Open a Pull Request

## Development Setup

### Prerequisites

- Python 3.9 or higher
- pip and virtualenv
- Git
- GitHub account

### Setup Steps

```bash
# Clone your fork
git clone https://github.com/YOUR-USERNAME/AI-OSINT-Framework.git
cd AI-OSINT-Framework

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install

# Run tests to verify setup
pytest tests/
```

## Coding Standards

### Python Style Guide

We follow **PEP 8** with some modifications:

- **Line length**: 88 characters (Black default)
- **Imports**: Organized with `isort`
- **Type hints**: Required for all functions
- **Docstrings**: Google style for all modules, classes, and functions

### Code Formatting

We use automated formatters:

```bash
# Format code with Black
black .

# Sort imports with isort
isort .

# Check code quality with flake8
flake8 .

# Type checking with mypy
mypy core/ modules/ ai_tools/
```

### Example Code Style

```python
from typing import Dict, List, Optional
import logging

logger = logging.getLogger(__name__)


class OSINTModule:
    """Base class for all OSINT modules.

    All OSINT modules must inherit from this class and implement
    the required methods. This ensures consistency and legal compliance.

    Attributes:
        name: The module name
        description: Brief description of module functionality
        legal_sources_only: Must always be True
    """

    def __init__(self, config: Optional[Dict] = None) -> None:
        """Initialize the OSINT module.

        Args:
            config: Optional configuration dictionary

        Raises:
            ValueError: If configuration is invalid
        """
        self.config = config or {}
        self.legal_sources_only = True
        logger.info(f"Initialized {self.__class__.__name__}")

    def validate_source(self, source: str) -> bool:
        """Validate that a data source is legal to use.

        Args:
            source: The source URL or identifier

        Returns:
            True if source is legal, False otherwise
        """
        # Implementation here
        pass
```

## Legal Compliance Checklist

**Every contribution MUST pass this checklist:**

### ✅ Data Source Validation

- [ ] All data sources are publicly accessible
- [ ] No unauthorized access or authentication bypass
- [ ] Respects robots.txt and similar restrictions
- [ ] Complies with Terms of Service
- [ ] No personal data collection without legal basis
- [ ] Rate limiting implemented to avoid abuse

### ✅ Privacy Protection

- [ ] No collection of sensitive personal data
- [ ] PII anonymization where applicable
- [ ] GDPR compliance (right to deletion, etc.)
- [ ] CCPA compliance
- [ ] Clear data retention policies
- [ ] Audit trail for data access

### ✅ Ethical Use

- [ ] Cannot be used for harassment
- [ ] Cannot facilitate illegal activity
- [ ] Transparent about data sources
- [ ] Respects individual privacy
- [ ] No circumvention of security measures

### ✅ Documentation

- [ ] Legal basis for data source documented
- [ ] Privacy implications disclosed
- [ ] Limitations and restrictions noted
- [ ] Example usage provided
- [ ] Error handling documented

## Pull Request Process

### Before Submitting

1. **Run all tests**: `pytest tests/`
2. **Check code quality**: `flake8 . && mypy .`
3. **Format code**: `black . && isort .`
4. **Update documentation**: README, docstrings, etc.
5. **Complete legal checklist**: See above
6. **Write meaningful commit messages**

### PR Title Format

Use conventional commits:

- `feat: Add WHOIS lookup module`
- `fix: Resolve rate limiting issue in Twitter module`
- `docs: Update API documentation`
- `test: Add tests for DNS module`
- `refactor: Improve error handling`
- `chore: Update dependencies`

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Legal Compliance Checklist
- [ ] All data sources are legal
- [ ] Privacy requirements met
- [ ] No ToS violations
- [ ] Ethical use ensured

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests pass
- [ ] Manual testing performed

## Documentation
- [ ] Code comments added
- [ ] Docstrings updated
- [ ] README updated (if needed)
- [ ] Examples provided

## Related Issues
Closes #123
```

### Review Process

1. **Automated checks**: CI/CD must pass
2. **Code review**: At least one maintainer approval
3. **Legal review**: For new data sources
4. **Testing**: All tests must pass
5. **Documentation**: Must be complete
6. **Merge**: Squash and merge to main

## Adding New Modules

### Module Structure

```
modules/
└── category/
    ├── __init__.py
    ├── module_name.py
    ├── validators.py
    └── tests/
        └── test_module_name.py
```

### Module Template

```python
"""
Module Name: Brief description
Category: people/business/technical/social_media/news
Legal Basis: Description of why this source is legal to use
Data Sources: List of public APIs or sources used
"""

from typing import Dict, Any, Optional
from core.validators import SourceValidator
from legal.compliance import ComplianceChecker


class ModuleName:
    """Brief description of module functionality.

    This module collects data from [source] using [method].
    All data is from publicly accessible sources and complies
    with applicable privacy laws.
    """

    def __init__(self) -> None:
        """Initialize the module."""
        self.validator = SourceValidator()
        self.compliance = ComplianceChecker()

    def search(self, query: str) -> Dict[str, Any]:
        """Perform OSINT search.

        Args:
            query: Search query

        Returns:
            Dictionary with results and metadata

        Raises:
            ValueError: If query is invalid
            ComplianceError: If operation violates legal requirements
        """
        # Validate compliance
        if not self.compliance.check(query):
            raise ComplianceError("Operation not compliant")

        # Perform search
        results = self._execute_search(query)

        # Return with metadata
        return {
            "results": results,
            "source": "public_api_name",
            "legal": True,
            "timestamp": "ISO-8601"
        }

    def _execute_search(self, query: str) -> Any:
        """Internal search implementation."""
        pass
```

### Module Requirements

1. **Inherit from base class** (if applicable)
2. **Implement required methods**
3. **Include legal validation**
4. **Provide comprehensive docstrings**
5. **Write unit tests** (>80% coverage)
6. **Document data sources**
7. **Handle errors gracefully**
8. **Implement rate limiting**

## Testing Requirements

### Test Coverage

- Minimum **80% code coverage**
- All new functions must have tests
- Edge cases must be covered
- Error conditions must be tested

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=core --cov=modules --cov=ai_tools

# Run specific test file
pytest tests/test_whois.py

# Run with verbose output
pytest -v
```

### Test Structure

```python
import pytest
from modules.technical.whois import WHOISModule


class TestWHOISModule:
    """Tests for WHOIS module."""

    def setup_method(self):
        """Setup for each test."""
        self.module = WHOISModule()

    def test_valid_domain_lookup(self):
        """Test lookup of valid domain."""
        result = self.module.lookup("example.com")
        assert result["domain"] == "example.com"
        assert result["legal"] is True

    def test_invalid_domain_raises_error(self):
        """Test that invalid domain raises appropriate error."""
        with pytest.raises(ValueError):
            self.module.lookup("invalid domain")

    def test_rate_limiting(self):
        """Test that rate limiting is enforced."""
        # Implementation
        pass
```

## Documentation Guidelines

### Code Documentation

- **Modules**: Docstring at top of file
- **Classes**: Describe purpose and usage
- **Methods**: Args, returns, raises
- **Complex logic**: Inline comments

### README Updates

Update README.md when:
- Adding new modules
- Changing API
- Adding dependencies
- Updating usage examples

### API Documentation

Generate API docs with:

```bash
# Generate documentation
pdoc --html --output-dir docs/ core/ modules/ ai_tools/
```

## Recognition

Contributors will be recognized in:
- README.md Contributors section
- Release notes
- Annual contributor awards
- Project website (when available)

## Questions?

- **GitHub Discussions**: For general questions
- **Discord**: Real-time chat with community
- **Email**: contributors@ai-osint-framework.org

## Thank You!

Your contributions make this project better for everyone. We appreciate your time and effort in helping build the world's best ethical OSINT framework for AI!

---

*Last updated: 2025-11-21*
