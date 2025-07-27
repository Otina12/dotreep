from setuptools import setup, find_packages

with open("README.md", encoding = "utf-8") as f:
    long_description = f.read()

setup(
    name = "dotreep",
    version = "1.0.0",
    packages = find_packages(),
    entry_points = {
        "console_scripts": [
            "dotreep=dotreep.cli:main",
        ]
    },
    python_requires = ">=3.7",
    install_requires = [],
    author = "Giorgi Otinashvili",
    description = "A simple command-line tool to display a directory tree with file sizes.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Otina12/dotreep",
)
