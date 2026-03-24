while True:
    try:
        eleitores = int(input("Quantas pessoas vão votar? "))
        if eleitores > 0:
            break
        print("Digite um número maior que zero.")
    except:
        print("Digite um número inteiro válido.")

votos = [0, 0, 0]  # índice 0 = candidato 1, índice 1 = cand. 2, índice 2 = cand. 3

for i in range(1, eleitores + 1):
    while True:
        try:
            voto = int(input(f"Eleitor {i} - Vote em (1, 2 ou 3): "))
            if voto in [1, 2, 3]:
                votos[voto-1] += 1
                break
            else:
                print("Voto inválido! Digite 1, 2 ou 3.")
        except:
            print("Digite apenas 1, 2 ou 3.")

print("\nResultado da votação:")
print(f"Candidato 1: {votos[0]} votos")
print(f"Candidato 2: {votos[1]} votos")
print(f"Candidato 3: {votos[2]} votos")

maior_voto = max(votos)
if votos.count(maior_voto) > 1:
    print("Houve empate entre os candidatos com mais votos!")
else:
    vencedor = votos.index(maior_voto) + 1
    print(f"O vencedor é o Candidato {vencedor} com {maior_voto} votos!")
