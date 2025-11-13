import sys as sys


def to_morse(txt):
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
    }
    result = ""
    for char in txt:
        upper_char = char.upper()
        if upper_char in NESTED_MORSE:
            result += NESTED_MORSE[upper_char]
        else:
            raise ValueError("the arguments are bad")
    return result.strip()  # remove last space


def main():
    try:
        assert len(sys.argv) == 2, "the arguments are bad"
        txt= sys.argv[1]
        assert txt != "", "the arguments are bad"
        print(to_morse(txt))

    except AssertionError as error:
        print(f"AssertionError: {error}")  # If arg count is wrong
    except ValueError as error:
        print(f"AssertionError: {error}")  # If txt has invalid chars


if __name__ == "__main__":
    main()