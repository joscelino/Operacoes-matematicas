import time

def fib_rec(n: int):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib_rec(n-2) + fib_rec(n-1)


start = time.time()
print(fib_rec(12))
end = time.time()
print('Tempo gasto com recurssao: ', end - start)