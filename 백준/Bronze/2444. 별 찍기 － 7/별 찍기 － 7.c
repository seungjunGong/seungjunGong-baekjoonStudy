#include <stdio.h>

int main(void){
    int n, star = 0;
    scanf("%d", &n);
    
    for (int i = 0; i < n; i++){
        
        for (int j = 1; j < n - i; j++){
            printf(" ");
        }

        for (int k = 0; k < 2 * i + 1; k++){
            printf("*");
        }
        printf("\n");

    }

    n--;
    
    for (int i = n - 1; i > -1; i--){

        for (int j = 0; j < n - i; j++){
            printf(" ");
        }

        for (int k = 0; k < 2 * i + 1; k++){
            printf("*");
        }
        printf("\n");

    }
    
    return 0;    
}