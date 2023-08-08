def solution(string: str) -> str:
    breaked_came_case = ''
    for letter in string:
        if letter.isupper():
            breaked_came_case += f' {letter}'
        else:
            breaked_came_case += letter

    return breaked_came_case

print(solution('camelCase'))