from typing import Iterable

def unique_in_order(sequence: Iterable) -> list:
    result = []
    item = None
    for i in sequence:
        if i != item:
            result.append(i)
            item = i

    return result

print(unique_in_order([1, 2, 2, 2, 3, 3, 4]))

