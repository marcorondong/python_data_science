def ft_filter(func:None, iterable=None):
    # Check if func is a function, and if it's callable
    if func is not None and not callable(func):
        raise TypeError(f"'{type(func).__name__}' object is not callable")
    # Check if iterable is actually an iterable (list, tuple, etc)
    try:
        _ = iter(iterable)  # Underscore is used for variables I won't use
    except TypeError:
        raise TypeError(f"'{type(iterable).__name__}' object is not iterable")
    # If function is None, then make it boolean
    if func is None:
        func = bool
    return [x for x in iterable if func(x)]  # This is a list comprehension
    # return (x for x in iterable if func(x)) # This is a generator expression
    # Filter function returns a iterable object. But the subject requires to
    # use a list comprehension, so I must return a list.


ft_filter.__doc__ = filter.__doc__  # match built-in docstring

# except AssertionError as error:
#     print(F"AssertionError: {error}")
# except Exception as e:
#     print(f"Error: {type(e).__name__}: {e}")

# def extract_even(number):
#     # if number % 2 == 0:  # Filtering condition
#     #     return True
#     # else:
#     #     return False
#     return number % 2 == 0

# def main():
#     numbers = [1, 3, 10, 45, 6, 50]
#     whatever = "424242"
#     # print(list(ft_filter(extract_even, numbers)))
#     # print(list(ft_filter(lambda n: n % 2 == 0, numbers)))
#     print(list(ft_filter(lambda n: n % 2 == 0, whatever)))

# if __name__ == "__main__":
#     main()

###############################################################################
# To check real filter function docsrtring, run `python3 -m pydoc filter`
# To check other docstrings, run `python3 -m pydoc folder_name.file_name`
