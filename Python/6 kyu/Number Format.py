def number_format(number: int) -> str:
    if len(str(number)) <= 3:
        return str(number)
    
    result = list(str(number))
    counter = 1
    for index in range(len(result) - 1, -1, -1):
        if counter == 3:
            result.insert(index, ',')
            counter = 0
        counter += 1
    
    if result[0] == ',':
        result = result[1:]
    
    return ''.join(result).replace('-,', '-')

    # return f'{number:,}'
