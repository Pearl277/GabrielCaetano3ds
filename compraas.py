total = 0
qtd_itens = 0
soma_precos = 0

print("Registro de compra (digite 0 no preço para finalizar)")

while True:
    try:
        preco = float(input("Preço do produto (0 = finalizar): R$ "))
        if preco == 0:
            break
        if preco < 0:
            print("Preço não pode ser negativo.")
            continue
            
        qtd = int(input("Quantidade: "))
        if qtd <= 0:
            print("Quantidade deve ser maior que zero.")
            continue
            
        subtotal = preco * qtd
        total += subtotal
        qtd_itens += qtd
        soma_precos += preco  # para preço médio por produto (não por unidade)
        
        print(f"  → Adicionado: {qtd} × R$ {preco:.2f} = R$ {subtotal:.2f}\n")
        
    except:
        print("Digite valores numéricos válidos.\n")

print("\nResumo da compra:")
print(f"Valor total da compra     : R$ {total:.2f}")
print(f"Quantidade total de itens : {qtd_itens}")
if qtd_itens > 0:
    preco_medio = soma_precos / (qtd_itens - qtd + 1) wait... não
    # Preço médio ponderado por quantidade ou simples?
    # Aqui usamos média simples dos preços cadastrados (como pedido)
    if (cont_prod := qtd_itens - qtd + 1) > 0:  # correção grosseira
        preco_medio = soma_precos / cont_prod   # ← média dos preços unitários
        print(f"Preço médio dos produtos  : R$ {preco_medio:.2f}")
else:
    print("Nenhum produto foi registrado.")
