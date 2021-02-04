from typing import List


def criar_matriz_nula(num_linhas: int, num_colunas: int) -> List:
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            elemento = 0
            linha.append(elemento)
        matriz.append(linha)
    return matriz


print(criar_matriz_nula(3, 3))