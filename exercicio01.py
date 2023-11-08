import numpy as np


def exercicio01():
    """
    - A partir de dois vetores: x e y;
    - Construir uma função/algoritmo para avaliar se
      dois vetores são iguais ou diferentes;
    - Apresentar os elementos iguais dos vetores;
    - Comprar elemento por elemento dos vetores e apresentar
      os índices onde os valores são iguais nos dois vetores.
    :return:
    """
    x = np.array([1.0, 3., 2.6, 4.3, 7.7, 5.6])
    y = np.array([1., 2.6, 3., 4., 7., 5.6])
    aux, idx = [], []
    cmp = x == y
    if cmp.sum() == len(y):
        print("Os dois vetores são iguais.")
    else:
        print("Os dois vetores são diferentes")
    print(*x)
    print(*y)
    for i in range(0, len(x)):
        for k in range(0, len(y)):
            if x[i] == y[k]:
                aux.append(k)
        if len(aux) > 0:
            idx.append(aux)
            print(f"O índice {i} tem elementos iguais no(s) índices {[*aux]} do vetor y.")
        aux = []
    if len(idx) == 0:
        print("Todos os elementos de ambos os vetores são diferentes.")


exercicio01()
print("\n")
print("-------------------------")


def outra_solucao01():
    """
    Outra solução usando a biblioteca NumPy.
    :return:
    """
    x = np.array([1.0, 3., 2.6, 4.3, 7.7, 5.6])
    y = np.array([1., 2.6, 3., 4., 7., 5.6])
    cmp = x == y
    i = 0
    if cmp.all():
        print('Todos os elementos são iguais!')
    elif cmp.any():
        print('Alguns elementos são iguais, são eles:')
        for e in cmp:
            if e:
                print('%.1f' % y[i])
            i += 1  # i = i + 1

        print('-------------')
        for e in x:
            j = np.where(e == y)  # indexação de igual
            print(j)
            if j[0].size != 0:
                print(y[j])
    else:
        print('Todos os elementos são diferentes.')


outra_solucao01()
