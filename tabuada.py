while True:
    try:
        n = int(input("Qual número deseja ver a tabuada? "))
        print(f"\nTabuada do {n}:")
        for i in range(1, 11):
            print(f"{n} × {i:2} = {n*i:3}")
        print()
        
        continuar = input("Deseja ver outra tabuada? (1 = sim / 0 = não): ")
        if continuar == "0":
            print("Programa encerrado.")
            break
        elif continuar != "1":
            print("Opção inválida. Encerrando...")
            break
            
    except:
        print("Digite um número inteiro válido.\n")
