import pandas as pd

nros = pd.Series([i for i in range(1, 21)])

print(type(nros))
print()
print(nros)

print()

# mostrando os 3 primeiros números
print(nros[:3])

# mostrando do 4o. ao 8o. números
print(nros[3:8])

# mostrando o primeiro e o último números
print(nros[0], nros[nros.size-1], nros.iloc[-1], sep=", ")

# mostrando os três ultimos números
print(nros[nros.size-3:])