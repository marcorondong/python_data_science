
def ft_filter(func, iterable):
    if func is None:
        func = bool
    return [x for x in iterable if func(x)]

    # except AssertionError as error:
    #     print(F"AssertionError: {error}")
    # except Exception as e:
    #     print(f"Error: {type(e).__name__}: {e}")

def extract_even(number):
    if number % 2 == 0:  # Filtering condition
        return True
    else:
        return False
    # def extract_even(numbers):
    #  even_numbers = []
    #  for number in numbers:
    #      if number % 2 == 0:  # Filtering condition
    #          even_numbers.append(number)
    #  return even_numbers

def main():
    numbers = [1, 3, 10, 45, 6, 50]
    # print(list(ft_filter(extract_even, numbers)))
    print(list(ft_filter(lambda n: n % 2 == 0, numbers)))

if __name__ == "__main__":
    main()