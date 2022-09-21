from typing import List

scores_table = {'5': 50, '1': 100, '222': 200, '111': 1000, '333': 300, '444': 400, '555': 500, '666': 600}

def score(lst: List[int]) -> int:
    result = 0
    lst_set = set(lst)
    for i in lst_set:
        try:
            count = lst.count(i)
            if i == 1 or i == 5:
                if count < 3:
                    for j in range(count):
                        result += scores_table[str(i)]
                    continue
                if count > 3:
                    while count >= 3:
                        result += scores_table[str(i)*3]
                        count -= 3
                    if count:
                        for j in range(count):
                            result += scores_table[str(i)]
                    continue
                else:
                    result += scores_table[str(i)*3]
                continue
            if lst.count(i) > 3:
                count = 3
            result += scores_table[count*str(i)]
        except KeyError:
            continue

    return result


print(score([1, 1]))