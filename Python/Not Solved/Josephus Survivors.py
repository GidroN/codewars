def josephus_survivors(num: int, every_num: int) -> int:
    mass = [*range(1, num + 1)]
    indexes_to_remove = []
    counter = 1

    while len(mass) != 1:
        for i in range(len(mass)):
            if counter == every_num:
                indexes_to_remove.append(i)
                counter = 1
                continue
                
            counter += 1
            
        dop = 0
        for i in indexes_to_remove:
            mass.pop(i - dop)   
            dop += 1
            
        indexes_to_remove.clear()
            
    return mass[0]
        

print(josephus_survivors(100, 1))