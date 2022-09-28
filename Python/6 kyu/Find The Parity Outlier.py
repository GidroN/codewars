from typing import List

def find_outlier(numbers: List[int]) -> int:
    if len(list(filter(lambda x: x % 2 == 0, numbers))) == 1:
        return list(filter(lambda x: x % 2 == 0, numbers))[0]
    return list(filter(lambda x: x % 2 != 0, numbers))[0]