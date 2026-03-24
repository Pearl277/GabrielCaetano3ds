qtd = int(input("Quantos números você deseja digitar? "))

if qtd <= 0:
    print("Quantidade inválida.")
else:
    soma = 0
    maior = float('-inf')
    menor = float('inf')
    
    for i in range(1, qtd + 1):
        num = float(input(f"Digite o {i}º número: "))
        soma += num
        
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    
    media = soma / qtd
    
    print("\nResultados:")
    print(f"Soma total     = {soma}")
    print(f"Média          = {media:.2f}")
    print(f"Maior número   = {maior}")
    print(f"Menor número   = {menor}")
