def avg_3_best_of_4(a: int, b: int, c:int, d:int) -> int:
    total = a + b + c + d
    three_best = total - min(a, b, c, d)
    return int(three_best/3)

print(avg_3_best_of_4(50, 60, 70, 80))
