import numpy as np

a = np.zeros((2, 3))

print(type(a))
print(type(a[0][0]))
print(a)
#-----------------------------
print()

b = np.zeros((5, 5), dtype=int)

print(type(b))
print(type(b[0][0]))
print(b)