import sys as sys
from ft_filter import ft_filter


def main():
    """
    main function which recoded ft_filter function to return a list
    with the words of a text which length is greater than N
    1st arg: string (S). The text to analyse
    2nd arg: integer (N). The min length of each word (greater than N)
    """
    try:
        assert len(sys.argv) == 3, "the arguments are bad"
        text = sys.argv[1]
        word_length = int(sys.argv[2])
        # TODO: Maybe I don't need to check for type, but if it's empty
        if not isinstance(text, str):
            raise TypeError("the arguments are bad")
        # word_list = text.split() # This is NOT a list comprehension
        # Below is a list comprehension. It reads like this:
        # For each item named w in text.split(), put w into the resulting list.
        words = [w for w in text.split()]
        # Note: word_length is "passed" to lambda since it's in inner scope
        print(list(ft_filter(lambda w: len(w) > word_length, words)))

    except AssertionError as error:
        print(F"AssertionError: {error}")
    except TypeError as error:
        print(F"AssertionError: {error}")
    except ValueError:
        print("AssertionError: the arguments are bad")  # If length is not int
    except Exception as error:
        print(f"Error: {type(error).__name__}: {error}")


if __name__ == "__main__":
    main()
