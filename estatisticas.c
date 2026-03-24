#include <stdio.h>

int main() {
    float num, soma = 0;
    int cont = 0, pos = 0, neg = 0;
    
    printf("Digite numeros (0 para encerrar)\n");
    
    while (1) {
        printf("-> ");
        scanf("%f", &num);
        
        if (num == 0) break;
        
        cont++;
        soma += num;
        
        if (num > 0) pos++;
        else if (num < 0) neg++;
    }
    
    printf("\nEstatisticas:\n");
    printf("Quantidade de numeros digitados: %d\n", cont);
    if (cont > 0) {
        printf("Positivos                      : %d\n", pos);
        printf("Negativos                      : %d\n", neg);
        printf("Soma total                     : %.2f\n", soma);
        printf("Media                          : %.2f\n", soma / cont);
    } else {
        printf("Nenhum numero foi digitado.\n");
    }
    
    return 0;
}
