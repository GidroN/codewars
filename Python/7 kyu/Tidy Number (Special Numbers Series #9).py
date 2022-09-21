def tidyNumber(num: int) -> bool:   
    num = str(num)
    for i in range(1, len(num)):
        if num[i] < num[i - 1]:
            return False
    return True
