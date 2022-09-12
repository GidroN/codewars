def first_non_repeating_letter(string: str) -> str:
    repeating_letter = []
    lower_string = string.lower()
    for index, letter in enumerate(lower_string):
        if lower_string.count(letter) >= 2 and letter not in repeating_letter:
            repeating_letter.append(letter)
        elif letter in repeating_letter:
            continue
        else:
            return string[index]
    return ''


print(first_non_repeating_letter('moonmen'))