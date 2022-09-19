from string import ascii_lowercase
def alphabet_position(string: str) -> str:
    alphabet = {element: index for index, element in enumerate(ascii_lowercase, 1)}
    return ' '.join(str(alphabet[i]) for i in string.lower() if i.isalpha())
    
