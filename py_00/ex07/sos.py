import sys


def check_space_and_alphanumeric(input_string):
    """
The function returns true if the string contain not
alphanumeric caracter and not space
The any() function returns True if at least one element
 in the iterable is True.
    """
    ha = any(not char.isalnum() and not char.isspace()
             for char in input_string)
    return ha


def text_to_morse(text):
    """
Returns morsecode from string passed as an argument.
    """
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
        "9": "----. "
    }
    morse_code = ""
    for char in text.upper():
        morse_code += NESTED_MORSE.get(char, " ")
        # Use " " for unknown characters (ignores punctuation
        #  and special characters) for safty
    return morse_code.strip()


def main():
    try:
        length = len(sys.argv)
        if length != 2:
            raise AssertionError("Wrong number of argument")
        inthisstring = sys.argv[1]
        if check_space_and_alphanumeric(inthisstring):
            raise AssertionError("the arguments are bad")
        if type(inthisstring) is not str:
            raise AssertionError("First argument is not a string")

        print(text_to_morse(inthisstring))

    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == "__main__":
    main()
