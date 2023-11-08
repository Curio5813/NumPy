import numpy as np

matriz = np.array([[1, 1, 2],
                  [3, 5, 8],
                  [13, 21, 34]])

# Encontre a diagonal principal (diagonal principal é a diagonal com deslocamento 0)
diagonal_principal = matriz.diagonal(offset=0)
print("Diagonal Principal:")
print(*diagonal_principal)

# Encontre as diagonais acima da diagonal principal
diagonais_acima = [matriz.diagonal(offset=i) for i in range(1, matriz.shape[0])]

print("Diagonais Acima:")
for i in range(0, len(diagonais_acima)):
    print(*diagonais_acima[i])

print("Diagonais Abaixo")
# Encontre as diagonais abaixo da diagonal principal
diagonais_abaixo = [matriz.diagonal(offset=-i) for i in range(1, matriz.shape[0])]

for i in range(0, len(diagonais_abaixo)):
    print(*diagonais_abaixo[i])

# Criar uma matriz de exemplo
matriz = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

# Encontrar a diagonal secundária
diagonal_secundaria = np.diag(np.fliplr(matriz))

# Encontrar a diagonal acima da diagonal secundária
diagonal_acima = np.diag(np.fliplr(matriz), k=1)

# Encontrar a diagonal abaixo da diagonal secundária
diagonal_abaixo = np.diag(np.fliplr(matriz), k=-1)

print("Diagonal Secundária:", diagonal_secundaria)
print("Diagonal Acima da Diagonal Secundária:", diagonal_acima)
print("Diagonal Abaixo da Diagonal Secundária:", diagonal_abaixo)

"""
Neste exemplo, np.fliplr(matriz) é usado para inverter a matriz ao
longo do eixo vertical, o que efetivamente troca as colunas da matriz, 
permitindo que você acesse a diagonal secundária e as diagonais acima e 
abaixo dela usando a função np.diag(). O argumento k da função np.diag() 
controla a posição da diagonal que você deseja acessar em relação à diagonal 
principal (k=0).
"""



