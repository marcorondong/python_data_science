from ft_filter import ft_filter

def run_test(description, func, iterable):
    print(f"\n--- {description} ---")

    # Test ft_filter
    try:
        ft_result = ft_filter(func, iterable)
        print("ft_filter result :", ft_result)
    except Exception as e:
        print("ft_filter error  :", repr(e))

    # Test original filter
    try:
        orig_result = list(filter(func, iterable))
        # orig_result = filter(func, iterable)
        print("filter result    :", orig_result)
    except Exception as e:
        print("filter error     :", repr(e))


if __name__ == "__main__":

    # Normal cases
    run_test("Basic lambda",
             lambda x: x > 2,
             [1, 2, 3, 4, 5])

    run_test("Even numbers",
             lambda x: x % 2 == 0,
             [1, 2, 3, 4, 5, 6])

    # func = None
    run_test("Function is None",
             None,
             [0, 1, "", "hello", [], [1]])

    # Empty iterable
    run_test("Empty list",
             lambda x: x > 0,
             [])

    # Non-callable func
    run_test("Non-callable function",
             42,
             [1, 2, 3])

    # Non-iterable iterable
    run_test("Non-iterable object",
             lambda x: x > 0,
             123)

    # Both None
    run_test("Both None",
             None,
             None)

    # String iterable
    run_test("String iterable",
             lambda x: x != "a",
             "banana")