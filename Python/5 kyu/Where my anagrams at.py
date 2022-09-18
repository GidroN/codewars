from typing import List
from collections import Counter

def anagrams(word: str, lst: List[str]) -> List[str]:
    return [i for i in lst if Counter(i) == Counter(word)]
