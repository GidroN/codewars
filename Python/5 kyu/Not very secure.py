from string import whitespace, punctuation

def alphanumeric(password: str):
    if "_" in password or password == '':
        return False
    for i in whitespace:
        if i in password:
            return False
    for i in punctuation:
        if i in password:
            return False
    return True

# return password.isalnum()