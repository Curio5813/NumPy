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






