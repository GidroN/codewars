#My solve
def find_uniq(lst: list) -> int:
    if lst.count(lst[0]) > 1:
        for i in lst:
            if i != lst[0]:
                return i
    else:
        return lst[0]

#Not my
def find_uniq(lst):
    first, sec = set(lst)
    return first if lst.count(first) == 1 else sec
