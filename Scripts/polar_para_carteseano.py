import cmath

""" Funcao -> z = x + yj"""
x = 7.07
y = 7.07
polar_coord = cmath.phase(complex(x, y))

cart_coord = polar_coord * 180 / cmath.pi

print(f' Polar : {round(polar_coord, 2)}')
print(f' Cartesiano : {round(cart_coord, 2)}º')
