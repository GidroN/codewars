def create_phone_number(numbers: list) -> str:
    result = ''
    numbers = ''.join(map(str, numbers))
    result = f"({numbers[:3]}) {numbers[3:6]}-{numbers[6:]}"
            
    return result
