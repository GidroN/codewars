# 7 KYU
def square_digits(num: int) -> int:
    result = ''
    for i in str(num):
         result += str(int(i) ** 2)
         
    return int(result)