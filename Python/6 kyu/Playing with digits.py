def dig_pow(number: int, start: int) -> int:
    dig_pows = []
    digits = [int(j) for j in str(number)]
    
    for i in range(start, len(digits) + start):
        dig_pows.append(digits[i - start]**i)    
    
    return sum(dig_pows) // number if sum(dig_pows) % number == 0 else -1