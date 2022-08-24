import json

class Converter:
    """
    Converts text/numbers to or from morse code.

    Examples:
        Converting from morse code
        >>> converter = Converter()
        >>> converter.convert("hello world")
        '.... . .-.. .-.. --- / .-- --- .-. .-.. -..'

        Converting to morse code
        >>> converter = Converter()
        >>> converter.convert(".... . .-.. .-.. --- / .-- --- .-. .-.. -..", to_morse=False)
        'hello world'

    Attributes:
        to_morse_alphabet (dict): All alphanumeric characters and their
            morse code counter-parts.
        from_morse_alphabet (dict): All morse code characters and their
        alphanumeric counter-parts.
    """

    def __init__(self):
        with open("morse_code_alphabet.json") as file:
            alphabet = json.load(file)
            self.to_morse_alphabet = alphabet["to_morse"]
            self.from_morse_alphabet = alphabet["to_normal"]

    def _convert(self, string, to_morse: bool = True) -> str:
        """
        Converts to or from morse code.

        When `to_morse` is `True`, iterates through each character of
        `string`, converting them to morse. Otherwise, `string` will be
        converted as a whole.

        Will not convert non-alphanumeric characters to morse, or any
        non-morse characters from morse. They will be skipped over.

        Args:
            string: alphanumeric word or morse code character to
                convert.
            to_morse: Set to `True` to convert to morse,`False` to
                convert from it.

        Returns:
            `string` converted either to or from morse code.
        """
        if to_morse:
            # Converting to morse
            morse_word = []
            try:
                for char in str(string).casefold():
                    morse_word.append(self.to_morse_alphabet[char])

            except KeyError:
                # An invalid type was given, so skip it and move on.
                pass

            return ' '.join(morse_word)
        else:
            # Converting from morse
            try:
                morse_word = self.from_morse_alphabet[string]
                return morse_word
            except KeyError:
                # A non-morse character was given
                return f"\nInvalid morse code letter: {string}\n"

    def convert(self, text_list, to_morse: bool = True) -> str:
        """Iterates through `text_list` converting all values to or from morse."""
        converted = [self._convert(item, to_morse) for item in text_list.split()]
        return ' / '.join(converted) if to_morse else ''.join(converted)


def get_choice():
    """Get user choice for choosing to convert to or from morse."""
    print("1. Translate to morse code")
    print("2. Translate from morse code")
    user_input = input("1 or 2: ")
    while user_input != "1" and user_input != "2":
        user_input = get_choice()

    return user_input


if __name__ == "__main__":
    converter = Converter()
    # Get user choice for conversion, and then text to convert
    choice = get_choice()
    text = input("Enter text: ")

    if choice == "1":
        # Converting to morse
        print(converter.convert(text))
    elif choice == "2":
        # Converting from morse
        print(converter.convert(text, to_morse=False))


