n = int(input("Quantos números você deseja digitar? "))

numeros = []
soma_total = 0

for _ in range(n):
    num = float(input("Digite um número: "))
    numeros.append(num)
    soma_total += num
print("*************************")
print("RESULTADOS")
print("Soma total:", soma_total)
print("Média dos números:", soma_total / n)
print("Maior número:", max(numeros))
print("Menor número:", min(numeros))
print("*************************")
