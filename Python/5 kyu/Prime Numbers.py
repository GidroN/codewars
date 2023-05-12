from typing import List
import sympy

def isPrime(num: int) -> bool:
    return sympy.isprime(num)

def getPrimes(start: int, end: int) -> List[int]:
    return [i for i in range(start, end + 1) if sympy.isprime(i)]
