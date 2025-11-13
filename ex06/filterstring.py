import sys as sys
from ft_filter import ft_filter

def main():
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        text = sys.argv[1]
        word_length = int(sys.argv[2])
        if not isinstance(text, str):
            raise TypeError("the arguments are bad")
        # word_list = text.split()
        words = [w for w in text.split()] # This is a list comprehension
        # Need to create lambda expression outside filter, because filter calls the predicate with one argument
        pred = lambda w: len(w) > word_length
        # print(list(ft_filter(extract_even, numbers)))
        # print(list(ft_filter(lambda n: n % 2 == 0, numbers)))
        # print(list(ft_filter(lambda n, word_length: len(n) > word_length == 0, word_list)))
        print(list(ft_filter(pred, words)))

    except AssertionError as error:
        print(F"AssertionError: {error}")
    except TypeError as error:
        print(F"AssertionError: {error}")
    except ValueError as error:
        print("AssertionError: the arguments are bad")
    except Exception as error:
        print(f"Error: {type(error).__name__}: {error}")

if __name__ == "__main__":
    main()
