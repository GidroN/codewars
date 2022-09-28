def duplicate_encode(string: str):
    return ''.join("(" if string.lower().count(i) == 1 else ")" for i in string.lower())