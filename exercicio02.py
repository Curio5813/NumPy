import numpy as np


x = np.array([[0, 1, 2, 3, 4],
              [1, 2, 3, 4, 5],
              [2, 3, 4, 5, 6],
              [3, 4, 5, 6, 7]])
m1 = x[2:, :2]
m2 = x[:2, 2:4]
m3 = x[:3, 3:]
print(m1)
print(m2)
print(m3)
