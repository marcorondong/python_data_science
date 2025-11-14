from .functions import count_in_list

__all__ = ["count_in_list"]

# Note that since this is a package, I need to prepend a dot before filename
# so it's ".functions" and not "functions"
# Inside a package, imports must specify whether they are (absolute/relative)
# Since __init__.py and functions.py are in the same package folder,
# the correct import is relative.