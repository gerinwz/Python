#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {

    float num1,num2,soma;
    
    printf("Digite o primeiro numero\n");
    scanf("%f", &num1);

    printf("Digite o segundo numero\n");
    scanf("%f", &num2);

    soma = num1 + num2;

    printf ("A soma de %f mais %f e igual %f" , num1, num2, soma );

    system("pause");
    return 0;
}
