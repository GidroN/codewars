def persistence(num: int, counter = 1) -> int:
    if len(str(num)) == 1:
        return 0
    
    result = 1
    for i in str(num):
        result *= int(i)
        
    if len(str(result)) > 1:
        return persistence(result, counter + 1)
        
    return counter

print(persistence(39))