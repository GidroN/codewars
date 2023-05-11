def narcissistic(number: int) -> bool:
    pow_num = len(str(number))
    result = 0
    
    for i in str(number):
        result += int(i) ** pow_num
        
    return number == result


# -----------------

def narcissistic2(number: int) -> bool:
    return number == sum(int(i) ** len(str(number)) for i in str(number))