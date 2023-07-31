import sys


def is_even(num):
    return num % 2 == 0


def filterstring(thistring, numb):
    # isbigger = lambda num: num > numb
    return [item for item in thistring.split() if len(item) > numb]


def main():
    try:
        length = len(sys.argv)
        if length != 3:
            raise AssertionError("Wrong number of argument")
        if not sys.argv[2].isdigit():
            raise AssertionError("Second argument is not a number")
        numb = int(sys.argv[2])
        inthisstring = sys.argv[1]
        if type(inthisstring) is not str:
            raise AssertionError("First argument is not a string")
        # isbigger = lambda num: num > 5
        # print(isbigger(6))
        print(filterstring(inthisstring, numb))
    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
