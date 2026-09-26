import pandas as pd
import sys
sys.path.insert(1, 'C:\Python_AgentesInteligentes\Fontes\Python')
from Geral import cls, parada

valores = []
indices = []

i = 1 # variável de controle
while True:
    cls()

    nome = input(f"{i}a. pessoa (FIM para encerrar):\n")
    if nome.upper() == "FIM":
        break

    print()
    idade = int(input("Idade: "))

    valores.append(idade)
    indices.append(nome)
    i += 1

    parada()

pessoas = pd.Series(valores, index=indices)
print(type(pessoas))
print()
print(pessoas)

pessoas.to_csv('Pessoas.csv', index=True, mode='a')
print("<<< FIM DO PROGRAMA >>>")