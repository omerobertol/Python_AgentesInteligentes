from random import choice
from Vetor import saida

while True:
    n = int(input("Quantidade de cartões (no máximo 10, -1 para encerrar) = "))
    if n == -1:
        break

    if (n < 1) or (n > 10):
        print(f"Erro: {n}, quantidade inválida de cartões!!!")
        print()
        continue

    print()
    escolha = [i for i in range(1, 61)] # cria uma lista com os números de 1 a 60
    for i in range(n):
        jogo = []
        for j in range(6): # sorteia 6 números para o jogo
            nro = choice(escolha) # sorteia um número para o jogo

            escolha.remove(nro)
            jogo.append(nro)
            
        print(saida(f"Cartão {(i + 1):2d}", sorted(jogo)))

    print()