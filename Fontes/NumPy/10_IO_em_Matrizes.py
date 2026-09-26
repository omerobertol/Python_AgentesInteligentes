import numpy as np

nl = int(input("Informe a quantidade de linha..: "))
nc = int(input("Informe a quantidade de colunas: "))

m = np.empty((0,nc), dtype=int) # criou uma matriz vazia 0x0

print()
for i in range(nl):
    linha = []
    print(f"{i+1}a. linha")
    for j in range(nc):
        item = int(input(f"m[{i}, {j}] = "))
        linha.append(item)
    print("----------------------------")
    m = np.append(m, [linha], axis=0)

print()
print("Matriz")
for i in range(nl):
    print("| ", end="")

    smLinha = 0
    for j in range(nc):
        print(m[i, j], end="")
        if (j != (nc-1)): # não é a última coluna
            print(", ", end="")
        smLinha += m[i, j]
    print(f" | soma = {smLinha}")

