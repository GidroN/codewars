from typing import List

def find_all_dividers(number: int) -> List[int]:
    dividers = []
    for num in range(1, (number // 2) + 1):
        if number % num == 0:
            dividers.append(num)
    
    dividers.append(number)
    
    return dividers

def get_dividers(values: List[int], powers: List[int]) -> List[int]:
    product_result = 1
    for index in range(len(values)):
        product_result *= values[index] ** powers[index]
    
    return find_all_dividers(product_result)
    
print(get_dividers([11, 113], [1, 1]))  