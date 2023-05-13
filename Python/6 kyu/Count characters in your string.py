from collections import Counter

def count(string: str) -> dict:
    return Counter(string)

print(count("aba"))