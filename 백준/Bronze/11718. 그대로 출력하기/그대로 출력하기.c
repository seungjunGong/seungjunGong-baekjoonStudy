#include <stdio.h>

int main(void) {
    
    char input;

    while (scanf("%c", &input) != EOF) {
        printf("%c", input);
    }
    
    return 0;
}