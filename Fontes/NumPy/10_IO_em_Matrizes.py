import numpy as np

nl = int(input("Informe a quantidade de linha..: "))
nc = int(input("Informe a quantidade de colunas: "))

m = [] # criou uma lista vazia
print()
for i in range(nl):

    linha = [] # cria a lista 'linha' vazia
    print(f"{i+1}a. linha")
    for j in range(nc):
        item = int(input(f"m[{i}, {j}] = "))
        # adiciona o 'item' a lista 'linha'
        linha.append(item)       
    print("----------------------------")
    # adiciona a linha 'linha' a lista 'm'
    m.append(linha)


# cria a matriz a partir de uma lista
minhaMatriz = np.array(m)

print()
print("Matriz")
for i in range(nl):
    print("| ", end="")

    smLinha = 0
    for j in range(nc):
        print(minhaMatriz[i, j], end="")
        if (j != (nc-1)): # não é a última coluna
            print(", ", end="")
        smLinha += minhaMatriz[i, j]

    print(f" | soma = {smLinha}")

