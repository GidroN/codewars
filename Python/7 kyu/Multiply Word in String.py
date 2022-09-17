def modify_multiply(string: str, loc: int, num: int) -> str:
    return '-'.join([string.split()[loc] for i in range(num)])
