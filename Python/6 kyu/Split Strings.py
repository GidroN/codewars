from typing import List

def solution(s: str) -> List[str]:
    result = []
    if len(s) % 2 != 0:
        s += '_'
    
    for i in range(0, len(s), 2):
        result.append(s[i:i+2])
        
    return result