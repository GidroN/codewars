from typing import Union
def basic_op(operator: str, value1: Union[int, float], value2: Union[int, float]) -> Union[int, float]:
    return eval(f'{str(value1)} {operator} {str(value2)}')

print(basic_op("", 5, 5))

basic_op = lambda o, v1, v2: __import__("operator").__dict__[{"+":"add","-":"sub", "*":"mul", "/":"truediv"}[o]](v1,v2)