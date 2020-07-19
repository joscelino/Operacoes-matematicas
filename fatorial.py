
def fatorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        calc = n * fatorial(n-1)
        return calc


print(fatorial(6))
