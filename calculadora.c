#include <stdio.h>

int main() {
    int qtd;
    float num, soma = 0, maior = -999999, menor = 999999;
    
    printf("Quantos numeros voce deseja digitar? ");
    scanf("%d", &qtd);
    
    if (qtd <= 0) {
        printf("Quantidade invalida.\n");
        return 1;
    }
    
    for (int i = 1; i <= qtd; i++) {
        printf("Digite o %d numero: ", i);
        scanf("%f", &num);
        
        soma += num;
        if (num > maior) maior = num;
        if (num < menor) menor = num;
    }
    
    float media = soma / qtd;
    
    printf("\nResultados:\n");
    printf("Soma total     = %.2f\n", soma);
    printf("Media          = %.2f\n", media);
    printf("Maior numero   = %.2f\n", maior);
    printf("Menor numero   = %.2f\n", menor);
    
    return 0;
}
