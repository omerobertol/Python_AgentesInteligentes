import numpy as np

m = np.array([[1, 2, 3],
              [4, 5, 6]])

print(type(m))
print(type(m[0][0])) # elemento da primeira linha e primeira coluna
print(m)
#--------------------------------------
print()

minha_matriz = [[1, 2],
                [3, 4],
                [5, 6],
                [7, 8]]
m2 = np.array(minha_matriz)

print(m2)
