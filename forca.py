import random

palavras = [
    "python", "programacao", "computador", "teclado", "monitor",
    "internet", "algoritmo", "variavel", "funcao", "classe",
    "objeto", "sistema", "arquivo", "memoria", "processador",
    "servidor", "banco", "dados", "rede", "codigo"
]

palavra = random.choice(palavras)
letras_descobertas = ["_" for _ in palavra]
tentativas = 10
letras_usadas = []

while tentativas > 0 and "_" in letras_descobertas:
    print("\nPalavra:", " ".join(letras_descobertas))
    print("Tentativas restantes:", tentativas)
    print("Letras usadas:", " ".join(letras_usadas))

    letra = input("Digite uma letra: ").lower()

    if letra in letras_usadas:
        print("Você já usou essa letra.")
        continue

    letras_usadas.append(letra)

    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                letras_descobertas[i] = letra
        print("Acertou!")
    else:
        tentativas -= 1
        print("Errou!")

if "_" not in letras_descobertas:
    print("\nParabéns, você ganhou! A palavra era:", palavra)
else:
    print("\nVocê perdeu! A palavra era:", palavra)