def string_incrementer(string: str) -> str:
    if not string:
        return '1'
    
    if not string[-1].isdigit():
        return string + "1"
    
    if string[-1] == '0':
        return string[:-1] + "1"
    
    beginning = string.rstrip('0123456789')
    end = string[len(beginning):]
    
    return beginning + str(int(end) + 1).zfill(len(end))


print(string_incrementer('foo0099'))