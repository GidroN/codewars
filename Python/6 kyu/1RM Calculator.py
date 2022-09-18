def calculate_1RM(w: int, r: int) -> int:
    if r == 0: return 0
    if r == 1: return w
    
    formula1 = round((w * (1 + r / 30)), 0)
    formula2 = round((100 * w / (101.3 - 2.67123 * r)), 0)
    formula3 = round((w * r ** 0.10), 0)

    return max(formula1, formula2, formula2)
