from typing import List, Callable

def takeWhile(numbers: List[int], pred_func: Callable):
    for index in range(len(numbers)):
        if not pred_func(numbers[index]):
            return numbers[:index]
    
    return numbers

# from itertools import takewhile
# takewhile(pred_func, array)