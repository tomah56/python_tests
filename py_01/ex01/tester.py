from array2D import slice_me


def main():
    try:
        family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))

        print("\n\n------ My Test ------\n")
        newfamily = [1, 2, 1]
        print(slice_me(newfamily, 0, 2))
        print(slice_me([1, "b", 6], 0, 2))
    except (ValueError, TypeError) as e:
        print("Caught an exception:", e)
    except Exception as e:
        print("Caught a generic exception:", e)
    try:
        print(slice_me([[1.80, 78.4], [2.15, 102.7], [2.10, "f"],
                        [1.88, 75.2]], 1, 0))
    except (ValueError, TypeError) as e:
        print("Caught an exception:", e)
    except Exception as e:
        print("Caught a generic exception:", e)
    try:
        print(slice_me([[1.8, 78.4], [2.15, 12.7], [2.1, "f", [1.8, 75.2]]],
                       1, 0))
    except (ValueError, TypeError) as e:
        print("Caught an exception:", e)
    except Exception as e:
        print("Caught a generic exception:", e)


if __name__ == "__main__":
    main()
