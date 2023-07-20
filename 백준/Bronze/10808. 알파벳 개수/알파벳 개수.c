#include <stdio.h>

int main(void)
{
    char S[100];
    int alp[26] = {0};
    scanf("%s", S);

    for (int i = 0; S[i] != '\0'; i++)
        alp[S[i] - 97] += 1;

    for (int i = 0; i < 26; i++)
        printf("%d ", alp[i]);

    return 0;
}