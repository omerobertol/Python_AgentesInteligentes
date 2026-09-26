import numpy as np

a = np.array([], dtype=int) # criando um array vazio

n = int(input("Digite o tamanho do array: "))
print()
for i in range(n):
    valor = int(input(f"Digite o {i+1}o. valor: "))

    # adicionando um valor ao array
    a = np.append(a, valor)

print()
print("{", end="")
for i in range(n):
    print(f"{a[i]}", end="")
    if (i != (n-1)): # não é o último
        print(", ", end="")
print("}")