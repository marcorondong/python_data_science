#!/usr/bin/env python3
import ast
import sys
import importlib.util
import inspect
from pathlib import Path

EXCLUDED_DIRS = {"__pycache__", "tools", "tests"}

# def check_file(filepath):
#     """Return list of functions missing docstrings in a file."""
#     with open(filepath, "r", encoding="utf-8") as f:
#         tree = ast.parse(f.read(), filename=str(filepath))
# 
#     missing = []
# 
#     for node in ast.walk(tree):
#         if isinstance(node, ast.FunctionDef):
#             if ast.get_docstring(node) is None:
#                 missing.append(node.name)
# 
#     return missing

def check_file(filepath):
    """Return list of functions missing __doc__ in a file."""
    spec = importlib.util.spec_from_file_location("module.name", filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    missing = []

    for name, obj in inspect.getmembers(module, inspect.isfunction):
        if obj.__module__ == module.__name__:  # only functions defined in this file
            if obj.__doc__ is None:
                missing.append(name)

    return missing

def main():
    """Entry point of the docstring checker."""
    if len(sys.argv) != 2:
        print("Usage: python check_docstrings.py <directory>")
        sys.exit(1)

    root = Path(sys.argv[1])

    if not root.exists():
        print("Path does not exist.")
        sys.exit(1)

    failed = False

    for py_file in root.rglob("*.py"):
        if any(part in EXCLUDED_DIRS for part in py_file.parts):
            continue

        missing = check_file(py_file)
        if missing:
            failed = True
            print(f"\n{py_file}:")
            for name in missing:
                print(f"  - {name}")

    if failed:
        sys.exit(1)

    print("All functions in all files have docstrings ✔")
    sys.exit(0)


if __name__ == "__main__":
    main()
