try:
    inicial = float(input("Valor inicial (R$): "))
    taxa = float(input("Taxa de juros anual (%): "))
    anos = int(input("Número de anos: "))
    
    if inicial <= 0 or anos <= 0:
        print("Valores devem ser positivos.")
    else:
        montante = inicial
        taxa_decimal = taxa / 100
        
        print("\nEvolução do investimento:")
        for ano in range(1, anos + 1):
            montante *= (1 + taxa_decimal)
            print(f"Ano {ano:2}: R$ {montante:,.2f}")
            
except:
    print("Digite valores numéricos válidos.")
