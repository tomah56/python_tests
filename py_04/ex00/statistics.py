def error_handler(args, kwargs):
    """Error handeling function"""
    if not args or not kwargs:
        raise ValueError("No arguments provided.")
    in_act = ['mean', 'median', 'quartile', 'std', 'var']
    for value in kwargs.values():
        if value not in in_act:
            raise ValueError(f"Invalid instruction: '{value}'")
    for arg in args:
        if not isinstance(arg, (int, float)):
            raise TypeError("arguments Must be a number")


def calculate_me(numbers):
    """calculates the mean"""
    total = sum(numbers)
    count = len(numbers)
    mean = total / count
    return mean


def calculate_mean(numbers):
    """prints the mean"""
    mean = calculate_me(numbers)
    print("mean :", mean)


def calculate_median(numbers):
    """calculates the median"""
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 1:
        median = sorted_numbers[n // 2]
    else:
        middle1 = sorted_numbers[n // 2 - 1]
        middle2 = sorted_numbers[n // 2]
        median = (middle1 + middle2) / 2.0
    print("median :", median)


def calculate_quartile(numbers):
    """calculates the quartiels"""
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    q1_index = n // 4
    q3_index = 3 * n // 4
    q1 = sorted_numbers[q1_index]
    q3 = sorted_numbers[q3_index]
    print(f"Quartile : [{q1}, {q3}]")


def calculate_standard_deviation(numbers):
    """calculates the std"""
    variance = calculate_variance(numbers)
    std_deviation = variance ** 0.5
    return std_deviation


def calculate_variance(numbers):
    """calculates the vairance"""
    mean = calculate_me(numbers)
    squared_diff_sum = sum((x - mean) ** 2 for x in numbers)
    variance = squared_diff_sum / len(numbers)
    return variance


def print_variance(numbers):
    """prints the vairance"""
    variance = calculate_variance(numbers)
    print("var :", variance)


def print_std(numbers):
    """prints the std"""
    std = calculate_standard_deviation(numbers)
    print("std :", std)


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Calculates many statistical staff"""
    try:
        error_handler(args, kwargs)
        actions = {
            'mean': calculate_mean,
            'median': calculate_median,
            'quartile': calculate_quartile,
            'std': print_std,
            'var': print_variance
        }
        for value in kwargs.values():
            if value in actions:
                action_func = actions[value]
                action_func(args)
    except TypeError as e:
        print(f"TypeError: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")
    except SyntaxError as e:
        print(f"SyntaxError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
