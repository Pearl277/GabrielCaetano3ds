#include <stdio.h>

int main() {
    float preco, total = 0, soma_precos = 0;
    int qtd, total_itens = 0, cont_prod = 0;
    
    printf("Registro de compra (preco 0 = finalizar)\n\n");
    
    while (1) {
        printf("Preco do produto (0 = finalizar): R$ ");
        scanf("%f", &preco);
        
        if (preco == 0) break;
        if (preco < 0) {
            printf("Preco invalido.\n");
            continue;
        }
        
        printf("Quantidade: ");
        scanf("%d", &qtd);
        
        if (qtd <= 0) {
            printf("Quantidade invalida.\n");
            continue;
        }
        
        float subtotal = preco * qtd;
        total += subtotal;
        total_itens += qtd;
        soma_precos += preco;
        cont_prod++;
        
        printf("  -> Adicionado: %d x %.2f = %.2f\n\n", qtd, preco, subtotal);
    }
    
    printf("\nResumo da compra:\n");
    printf("Valor total da compra     : R$ %.2f\n", total);
    printf("Quantidade total de itens : %d\n", total_itens);
    
    if (cont_prod > 0) {
        float preco_medio = soma_precos / cont_prod;
        printf("Preco medio dos produtos  : R$ %.2f\n", preco_medio);
    } else {
        printf("Nenhum produto registrado.\n");
    }
    
    return 0;
}
