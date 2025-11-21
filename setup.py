"""
Setup configuration for AI-OSINT-Framework
"""

from setuptools import setup, find_packages
import os


def read_file(filename):
    """Read file contents."""
    with open(filename, encoding="utf-8") as f:
        return f.read()


# Read requirements
def read_requirements(filename):
    """Read requirements from file."""
    with open(filename, encoding="utf-8") as f:
        return [
            line.strip()
            for line in f
            if line.strip() and not line.startswith("#") and not line.startswith("-r")
        ]


setup(
    name="ai-osint-framework",
    version="1.0.0",
    author="Bartosz Gaca",
    author_email="gaca.bartosz@gmail.com",
    description="The world's most comprehensive, 100% legal OSINT framework for AI systems",
    long_description=read_file("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/gacabartosz/AI-OSINT-Framework",
    project_urls={
        "Bug Reports": "https://github.com/gacabartosz/AI-OSINT-Framework/issues",
        "Source": "https://github.com/gacabartosz/AI-OSINT-Framework",
        "Documentation": "https://github.com/gacabartosz/AI-OSINT-Framework/blob/main/README.md",
    },
    packages=find_packages(exclude=["tests", "examples"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Topic :: Security",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
    python_requires=">=3.9",
    install_requires=read_requirements("requirements.txt"),
    extras_require={
        "dev": read_requirements("requirements-dev.txt"),
    },
    entry_points={
        "console_scripts": [
            "osint=core.cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords=[
        "osint",
        "intelligence",
        "security",
        "ai",
        "claude",
        "openai",
        "investigation",
        "whois",
        "dns",
        "reconnaissance",
    ],
)
