#include <stdio.h>

int main() {
    int alunos, aprov = 0, recup = 0, reprov = 0;
    float nota, soma = 0;
    
    printf("Quantos alunos na turma? ");
    scanf("%d", &alunos);
    
    if (alunos <= 0) {
        printf("Quantidade invalida.\n");
        return 1;
    }
    
    for (int i = 1; i <= alunos; i++) {
        do {
            printf("Nota do aluno %d (0-10): ", i);
            scanf("%f", &nota);
            if (nota < 0 || nota > 10)
                printf("Nota invalida! Digite entre 0 e 10.\n");
        } while (nota < 0 || nota > 10);
        
        soma += nota;
        
        if (nota >= 7) aprov++;
        else if (nota >= 5) recup++;
        else reprov++;
    }
    
    float media = soma / alunos;
    
    printf("\nResultado da turma:\n");
    printf("Media da turma   : %.2f\n", media);
    printf("Aprovados        : %d\n", aprov);
    printf("Recuperacao      : %d\n", recup);
    printf("Reprovados       : %d\n", reprov);
    
    return 0;
}
