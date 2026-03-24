numero_secreto = 37
tentativas = 0

print("Tente adivinhar o número secreto (1 a 100)")

while True:
    try:
        palpite = int(input("Seu palpite: "))
        tentativas += 1
        
        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou em {tentativas} tentativas!")
            break
        elif palpite < numero_secreto:
            print("Muito baixo!")
        else:
            print("Muito alto!")
            
    except:
        print("Digite apenas números inteiros.")
