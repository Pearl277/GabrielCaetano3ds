
while True:
    try:
        alunos = int(input("Quantos alunos na turma? "))
        if alunos > 0:
            break
        print("Digite um número maior que zero.")
    except:
        print("Digite um número inteiro.")

aprovados = 0
recuperacao = 0
reprovados = 0
soma_notas = 0

for i in range(1, alunos + 1):
    while True:
        try:
            nota = float(input(f"Nota do aluno {i}: "))
            if 0 <= nota <= 10:
                break
            print("Nota deve estar entre 0 e 10.")
        except:
            print("Digite um número válido.")
    
    soma_notas += nota
    
    if nota >= 7:
        aprovados += 1
    elif nota >= 5:
        recuperacao += 1
    else:
        reprovados += 1

media = soma_notas / alunos

print("\nResultado da turma:")
print(f"Média da turma   : {media:.2f}")
print(f"Aprovados        : {aprovados}")
print(f"Recuperação      : {recuperacao}")
print(f"Reprovados       : {reprovados}")
