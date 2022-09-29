from typing import List

def tribonacci(numbers: List[int], num: int) -> List[int]:
    if num == 0:
        return []
    
    if num == 1:
        return numbers[0]
    
    if num == 2:
        return [numbers[0], numbers[1]]
    
    mass = [0] * num
    mass[0], mass[1], mass[2] = numbers[0], numbers[1], numbers[2] 
    
    for i in range(3, num):
        mass[i] = mass[i - 1] + mass[i - 2] + mass[i - 3]
    
    return mass