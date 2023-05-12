from typing import Sequence

def to_underscore(sequence: Sequence) -> str: 
    sequence = str(sequence)
    for letter in sequence:
        if letter.isupper() and letter != sequence[0]:
            sequence = sequence.replace(letter, f"_{letter}")
        else:
            continue
            
    return sequence.lower()

print(to_underscore('test_controller'))