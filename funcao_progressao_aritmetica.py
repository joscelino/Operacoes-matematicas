

def rectangle(n: int) -> int:
    a1 = 1
    r_line = 1
    r_column = 2
    for i in range(1, n+1):
        a_line = a1 + (i - 1) * r_line
        a_column = a1 + (i - 1) * r_column
        perimeter = 2 * (a_line * 1 + a_column * 1)
    return perimeter


print(rectangle(100))
