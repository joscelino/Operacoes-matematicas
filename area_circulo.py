import math


def area_circulo(r: float) -> None:
    if type(r) is str:
        print('Raio invalido')
    elif r < 0:
        print('Raio invalido')
    else:
        area = math.pi * pow(r, 2)
        print(f'Area do circulo: {area}')


area_circulo(20)
