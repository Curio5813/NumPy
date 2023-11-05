import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)

print(type(x))

print(x.shape)  # Estamos pegando um atributo do objeto não um método ou função. Não devemos utilizar parênteses.

n, m = x.shape  # Pega, respectivamente, o número de linhas e colunas de uma matriz

print(n, m)
