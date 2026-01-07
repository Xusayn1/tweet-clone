# Homework

# 1
def multiply(a :int | float, b :int | float) -> int | float:
    """
    multiply two numbers
    :param a: any integer or float
    :param b: any integer or float
    :return: result of multiply
    """
    return a * b


# 2
def repeat_string(s :str, times : int ) -> str :
    """
    repeat a string
    :param s: any string
    :param times: integer
    :return: how many times this string is repeated
    """
    return s * times


# 3
def get_even_numbers(numbers : list) -> list :
    """
    get even numbers
    :param numbers: list of numbers
    :return: only even numbers in list
    """
    return [n for n in numbers if n % 2 == 0]


# 4
def find_min_max(numbers : list) -> tuple:
    """
    find min and max of numbers
    :param numbers: list of numbers
    :return: only min and max of numbers in list
    """
    if not numbers:
        return None, None
    return min(numbers), max(numbers)


# 5
def concatenate_strings(strings : str) -> str:
    """
     to concatenate strings
    :param strings: only strings
    :return: as one string made of 2 strings
    """
    return " ".join(strings)


# 6
def square_dict(numbers : dict) -> dict:
    """
    square dictionary numbers
    :param numbers: int or float
    :return: square of numbers
    """
    return {k: v ** 2 for k, v in numbers.items()}


# 7
def reverse_list(items : list) -> list:
    """
    to reverse list.
    :param items: list of numbers or strings
    :return: reversed list
    """
    return items[::-1]


# 8
def count_occurrences(items :str, value :str ) -> int :
    """
    to count occurrences
    :param items: str,
    :param value: str
    :return: count of occurrences
    """
    return items.count(value)


# 9
def flatten_list_of_lists(lists: list) -> list:
    """
    flatten list of lists
    :param lists: LIST
    :return: flattened list
    """
    return [item for sublist in lists for item in sublist]


# 10
def divide(a : int | float, b : int | float) -> int | float:
    """
    divide two numbers
    :param a: int or float
    :param b: integer or float
    :return: result of division
    """
    if b == 0:
        return False
    return a / b
