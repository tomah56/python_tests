import sys


def count_uppercase_characters(input_string):
    """
    This function return the sum of uppercase characters.
    """
    return sum(1 for char in input_string if char.isupper())


def count_lowercase_characters(input_string):
    """
    This function return the sum of lowercase characters.
    """
    return sum(1 for char in input_string if char.islower())


def count_digits_characters(input_string):
    """
    This function return the sum of digital characters.
    """
    return sum(1 for char in input_string if char.isdigit())


def count_spaces_characters(input_string):
    """
    This function return the sum of space characters.
    """
    return sum(1 for char in input_string if char.isspace())


def count_punctuation_characters(input_string):
    """
    This function return the sum of punctuation characters.
    """
    punctuation_chars = '''!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~'''
    count = 0
    for char in input_string:
        if char in punctuation_chars:
            count += 1
    return count


def main():
    try:
        length = len(sys.argv)
        if length > 2:
            raise AssertionError("AssertionError: Too many argument")
        userInput = ""
        if length < 2:
            userInput = input("Please we need a text:")
        else:
            userInput = sys.argv[1]
        length = len(userInput)
        print(f"The text contains {length} characters:")
        print(f"{count_uppercase_characters(userInput)} upper letters")
        print(f"{count_lowercase_characters(userInput)} lower letters")
        print(f"{count_punctuation_characters(userInput)} punctuation marks")
        print(f"{count_spaces_characters(userInput)} spaces")
        print(f"{count_digits_characters(userInput)} digits")

    except AssertionError as e:
        print("Caught an AssertionError:", e)


if __name__ == "__main__":
    main()
