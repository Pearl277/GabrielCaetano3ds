#include <stdio.h>

int main() {
    int eleitores, voto;
    int cand1 = 0, cand2 = 0, cand3 = 0;
    
    printf("Quantas pessoas vao votar? ");
    scanf("%d", &eleitores);
    
    if (eleitores <= 0) {
        printf("Numero invalido de eleitores.\n");
        return 1;
    }
    
    for (int i = 1; i <= eleitores; i++) {
        while (1) {
            printf("Eleitor %d - Vote em (1, 2 ou 3): ", i);
            scanf("%d", &voto);
            
            if (voto == 1) { cand1++; break; }
            if (voto == 2) { cand2++; break; }
            if (voto == 3) { cand3++; break; }
            
            printf("Voto invalido! Tente novamente.\n");
        }
    }
    
    printf("\nResultado da votacao:\n");
    printf("Candidato 1: %d votos\n", cand1);
    printf("Candidato 2: %d votos\n", cand2);
    printf("Candidato 3: %d votos\n", cand3);
    
    if (cand1 > cand2 && cand1 > cand3)
        printf("Vencedor: Candidato 1 com %d votos!\n", cand1);
    else if (cand2 > cand1 && cand2 > cand3)
        printf("Vencedor: Candidato 2 com %d votos!\n", cand2);
    else if (cand3 > cand1 && cand3 > cand2)
        printf("Vencedor: Candidato 3 com %d votos!\n", cand3);
    else
        printf("Houve empate!\n");
    
    return 0;
}
