wordReps = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 
            'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
            'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14,
            'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 
            'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40,
            'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90,
            'hundred': 100, 'thousand': 1000, 'million': 1000000, 'zero': 0
}


# def parse_int(string: str) -> int:
#     if '-' in string and len(string.split('-')) == 2 and not ' ' in string:
#         return int(str(wordReps[string.split('-')[0]])[:-1] + str(wordReps[string.split('-')[-1]]))
#     if 'hundred' in string and len(string.split()) == 2 and not '-' in string:
#         return wordReps[string.split()[0]] * 100
#     if 'thousand' in string and 'hundred' in string and len(string.split()) == 3:
#         return wordReps[string.split()[0]] * 100000
#     if 'thousand' in string and not 'hundred' in string:
#         if not '-' in string:
#             return wordReps[string.split()[0]] * 1000
#         else:
#             temp = string.split()[0].split('-')
#             return int(str(wordReps[temp[0]])[:-1] + str(wordReps[temp[-1]])) * 1000
    
#     if 'million' in string:
#         return wordReps[string]
    
#     if ' ' not in string:
#         return wordReps[string]
    

#     hundred = False
#     if string.split()[-1] == 'hundred':
#         hundred = True    
    
#     result = ''
#     string = string.replace('-', ' ').replace(' and', '').replace('hundred', '').replace('thousand', '')
#     word_mass =  string.split()
    
#     for i in word_mass:
#         if wordReps[i] in range(20, 100) and word_mass[0] != wordReps[i]:
#             result += str(wordReps[i])[:-1]
#             continue
#         result += str(wordReps[i])
    
#     if hundred:
#         return int(result) * 100
    
#     return int(result)

def parseInt(string):
    string = string.replace(' and', '')
    if string == 'one million':
        return 1000000
    if string == 'zero' or string == '':
        return 0
    arr = string.split('thousand')
    if len(arr) == 2:
        return parseInt(arr[0]) * 1000 + parseInt(arr[1])
    arr = string.split('hundred')
    if len(arr) == 2:
        return parseInt(arr[0]) * 100 + parseInt(arr[1])
    arr = string.split('-')
    if len(arr) == 2:
        return parseInt(arr[0]) + parseInt(arr[1])

    return wordReps[string]
        

print(parseInt('one thousand'))