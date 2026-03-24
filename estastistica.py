positivos = 0
negativos = 0
soma = 0
contador = 0

print("Digite números (0 para encerrar)")

while True:
    try:
        num = float(input("→ "))
        if num == 0:
            break
            
        contador += 1
        soma += num
        
        if num > 0:
            positivos += 1
        elif num < 0:
            negativos += 1
            
    except:
        print("Valor inválido. Digite um número.")

print("\nEstatísticas:")
print(f"Quantidade de números digitados : {contador}")
if contador > 0:
    print(f"Quantidade de positivos         : {positivos}")
    print(f"Quantidade de negativos         : {negativos}")
    print(f"Soma total                      : {soma}")
    print(f"Média                           : {soma/contador:.2f}")
else:
    print("Nenhum número foi digitado.")
