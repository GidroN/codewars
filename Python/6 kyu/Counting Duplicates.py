def duplicate_count(string: str) -> int:
    return sum(1 for i in set(string.lower()) if string.lower().count(i) >= 2)
