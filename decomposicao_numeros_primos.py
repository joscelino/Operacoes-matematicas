try:
    n = input("Decompor o numero: ")
    n = int(n)
except TypeError:
    print(f'{n} invalido!')
except ValueError:
    print(f'{n} invalido!')

try:
    divisor = 2

    n_inicial = n
    if type(n_inicial) == int:
        print(n_inicial, "=", sep='', end='')

    while n > 1:
        while n % divisor == 0:
            n = n / divisor
            if n == 1:
                print(divisor)
            else:
                print(divisor, '*', sep='', end='')
        divisor += 1

    if n_inicial == divisor - 1:
        print(f'Numero digitado: {n} eh primo!!')
except ValueError:
    print(f'Como digitou {n} a decomposicao nao pode ser efetuada!')
except TypeError:
    print(f'Como digitou {n} a decomposicao nao pode ser efetuada!')
