#include <stdio.h>

int main() {
    float inicial, taxa, montante;
    int anos;
    
    printf("Valor inicial (R$): ");
    scanf("%f", &inicial);
    printf("Taxa de juros anual (%%): ");
    scanf("%f", &taxa);
    printf("Numero de anos: ");
    scanf("%d", &anos);
    
    if (inicial <= 0 || anos <= 0 || taxa < 0) {
        printf("Valores invalidos.\n");
        return 1;
    }
    
    montante = inicial;
    taxa = taxa / 100;
    
    printf("\nEvolucao do investimento:\n");
    for (int i = 1; i <= anos; i++) {
        montante *= (1 + taxa);
        printf("Ano %2d: R$ %.2f\n", i, montante);
    }
    
    return 0;
}
