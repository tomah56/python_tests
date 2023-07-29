import sys

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

if len(sys.argv) > 2:
    print("AssertionError: more than one argument is provided")
if len(sys.argv) == 2:
    if is_integer(sys.argv[1]):
        number = int(sys.argv[1])
        if number % 2 == 0:
            print("I'm Even")
        else:
            print("I'm Odd")
    else:
        print("AssertionError: argument is not an integer")

    