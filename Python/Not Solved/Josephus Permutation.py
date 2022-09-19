from typing import List, Union

def josephus(lst: Union[List[int], List[str]], num: int) -> List[int]:
    if len(lst) == 0:
        return []

    result = []
    counter = 1
    
    while len(lst) > 0:
        elements_to_remove = []
        for element in lst:
            if counter == num:
                elements_to_remove.append(element)
                counter = 0
            counter += 1
    
        for i in elements_to_remove:
            lst.remove(i)
            result.append(i)
    
    return result