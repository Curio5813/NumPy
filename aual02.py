import numpy as np


"""
Arrays de 1D - Transposta
"""

x = np.array([1, 2, 3, 4], dtype=np.int32)

print(x.shape)
print(type(x.dtype))
y = x.T  # Matriz Transposta

x = np.array([1, 2, 3, 4], dtype=np.int64)
print(x)

print(y)
print(y.shape)






