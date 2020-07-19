from typing import List


def criar_matriz(num_linhas: int, num_colunas: int) -> List:
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            elemento = int(input('Valor de: M['+str(i+1)+']['+str(j+1)+'] = '))
            linha.append(elemento)
        matriz.append(linha)
    return matriz


def print_matriz(matriz: List) -> None:
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])
    for i in range(num_linhas):
        for j in range(num_colunas):
            print('{0:3d} '.format(matriz[i][j]), end="")
        print()


M = criar_matriz(3, 3)

print_matriz(M)