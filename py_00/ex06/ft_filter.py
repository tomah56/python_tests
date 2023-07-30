def ft_filter_iter(filter_func, iterable):
    """
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """
    for item in iterable:
        if filter_func(item):
            yield item


def ft_filter(filter_func, iterable):
    """
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """
    return [item for item in iterable if filter_func(item)]


def is_even(num):
    return num % 2 == 0


def main():
    try:
        print(filter.__doc__)
        print("\n\n")
        print(ft_filter.__doc__)
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        filterd__ft = ft_filter(is_even, numbers)
        filterd_iter = ft_filter_iter(is_even, numbers)
        filterd_sys = filter(is_even, numbers)
        print("mine")
        print(list(filterd__ft))
        print("\nIter:")
        print(filterd_iter)
        print(list(filterd_iter))
        print("\noriginal")
        print(filterd_sys)
        print(list(filterd_sys))

    except RuntimeError as e:
        print(e)


if __name__ == "__main__":
    main()
