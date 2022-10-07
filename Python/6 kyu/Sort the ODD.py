from typing import List

def sort_array(numbers: List[int]) -> List[int]:
    odd_numbers = [i for i in numbers if i % 2 != 0]
    position_odd_numbers = [i for i in range(len(numbers)) if numbers[i] % 2 != 0]
 
    odd_numbers.sort()
    
    for ind, el in enumerate(odd_numbers):
        numbers.pop(position_odd_numbers[ind])
        numbers.insert(position_odd_numbers[ind], el)
        
    return numbers
    
    