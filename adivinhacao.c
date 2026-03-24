#include <stdio.h>

int main() {
    int secreto = 37;
    int palpite, tentativas = 0;
    
    printf("Tente adivinhar o numero secreto (1 a 100)\n");
    
    do {
        printf("Seu palpite: ");
        scanf("%d", &palpite);
        tentativas++;
        
        if (palpite == secreto) {
            printf("Parabens! Voce acertou em %d tentativas!\n", tentativas);
        }
        else if (palpite < secreto) {
            printf("Muito baixo!\n");
        }
        else {
            printf("Muito alto!\n");
        }
        
    } while (palpite != secreto);
    
    return 0;
}
