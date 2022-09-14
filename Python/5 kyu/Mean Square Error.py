from typing import Union

def average(lst: Union[list, int]) -> int:
    result = sum(lst) / len(lst)
    return int(result) if str(result)[-2:] == '.0' else result


def mean_square_error(lst1:  Union[list, int], lst2: Union[list, int]) -> int:
    diff_mass = []
    for index, element in enumerate(lst1):
        diff_mass.append(abs(element - lst2[index]) ** 2)
    
    return average(diff_mass)