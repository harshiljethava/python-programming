"Test class for airtravel"


class Flight:

    def __init__(self, number):
        if not number[:2].isalpha():
            raise ValueError(f"No airline in code '{number}'")

        if not number[:2].isupper():
            raise ValueError(f"No airline in code '{number}'")

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"Invalid router number '{number}'")

        self._number = number

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]
