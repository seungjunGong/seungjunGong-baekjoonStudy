#include <stdio.h>
#include <string.h>

int main(void) {
    
    int T;
    scanf("%d", &T);

    while (T--) {
        char S[1000];
        scanf("%s", S);

        printf("%c%c\n", S[0], S[strlen(S) - 1]);
    }
    
    return 0;
}