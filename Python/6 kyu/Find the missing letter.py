from typing import List
from string import ascii_letters


def find_missing_letter(lst: List[str]) -> str:
    index = ascii_letters.find(lst[0])
    for letter in lst:
        if letter != ascii_letters[index]:
            return ascii_letters[index]
        index += 1