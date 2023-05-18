#dont work gor mass with size 10^6

from typing import List

def arrange(numbers: List[int]) -> List[int]:
    lst = numbers.copy()
    result = []
    while len(lst) > 0:
        if len(lst) != 1:
            result.append(lst.pop(0))
            result.append(lst.pop(-1))
        else:
            result.append(lst.pop(0))
            
        lst.reverse()
                
    return result


print(arrange([4, 3, 2]))