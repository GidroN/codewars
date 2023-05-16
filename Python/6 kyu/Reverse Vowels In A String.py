def reverse_vowels(string: str) -> str:
    left = 0
    right = len(string) - 1
    pre_result = list(string)
    vowels = 'aeiouAEIOU'
    while left < right:
        
        if pre_result[left] in vowels and pre_result[right] in vowels:
            pre_result[left], pre_result[right] = pre_result[right], pre_result[left]
            right -= 1
            left += 1
        
        elif pre_result[left] in vowels:
            right -= 1
        elif pre_result[right] in vowels:
            left += 1
        else:
            right -= 1
            left += 1
            
    return ''.join(pre_result)


print(reverse_vowels('Reverse Vowels In A String'))