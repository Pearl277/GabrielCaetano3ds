#include <stdio.h>

int main() {
    int num, continuar;
    
    do {
        printf("Qual numero deseja ver a tabuada? ");
        scanf("%d", &num);
        
        printf("\nTabuada do %d:\n", num);
        for (int i = 1; i <= 10; i++) {
            printf("%2d x %2d = %3d\n", num, i, num * i);
        }
        printf("\n");
        
        printf("Deseja ver outra tabuada? (1 = sim / 0 = nao): ");
        scanf("%d", &continuar);
        
    } while (continuar == 1);
    
    printf("Programa encerrado.\n");
    return 0;
}
