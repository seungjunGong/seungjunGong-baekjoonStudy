#include <stdio.h>

int main(void){
    int n;
    scanf("%d", &n);

    for (int i = 1; i <= (int)(n / 4); i++){
        printf("long ");
    }
    printf("int");
}