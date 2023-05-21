#include <stdio.h>
#include <math.h>

int main(void)
{
    int L;
    scanf("%d", &L);
    char word;
    int result = 0;
    int r = 1;
    int M = 1234567891;
    for (int i = 0; i < L; i++)
    {
        scanf(" %c", &word);
        result += (r * (word - 96)) % M;
        r *= 31 % M;
    }

    printf("%d", result);
    return 0;
}