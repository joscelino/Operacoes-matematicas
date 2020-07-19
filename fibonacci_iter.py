import time


def fib_iter(n: int) -> int:
   ultimo = 1
   penultimo = 1
   if n == 1:
      return penultimo
   elif n == 2:
      return ultimo
   else:
      atual = 0
      for i in range(2, n):
         atual = ultimo + penultimo
         penultimo = ultimo
         ultimo = atual
      return atual


start = time.time()
print(fib_iter(120))
end = time.time()
print('Tempo gasto com recurssao: ', round(end - start, 5))