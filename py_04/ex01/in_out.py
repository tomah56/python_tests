def error_handler(number):
    """Error handeling function"""
    if not isinstance(number, (int, float)):
        raise TypeError("arguments Must be a number")


def square(x: int | float) -> int | float:
    try:
        error_handler(x)
        return x ** 2
    except TypeError as e:
        print(f"TypeError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")
    except SyntaxError as e:
        print(f"SyntaxError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def pow(x: int | float) -> int | float:
    try:
        error_handler(x)
        return x ** x
    except TypeError as e:
        print(f"TypeError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")
    except SyntaxError as e:
        print(f"SyntaxError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def outer(x: int | float, function) -> object:
    try:
        error_handler(x)
        count = 0
        result = x

        def inner() -> float:
            nonlocal count, result
            result = function(result)
            count += 1
            return result
        return inner
    except TypeError as e:
        print(f"TypeError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")
    except SyntaxError as e:
        print(f"SyntaxError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
