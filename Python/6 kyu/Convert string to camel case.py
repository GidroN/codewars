def to_camel_case(string: str) -> str:
    if not string:
        return ''
    
    check = False
    
    if string[0].islower():
        check = True
        
    string = string.replace('_', '-')
    result = ''.join(i.capitalize() for i in string.split('-'))
    
    if check:
        return result.replace(result[0], result[0].lower())
    else:
        return result