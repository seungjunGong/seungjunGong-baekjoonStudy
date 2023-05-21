#include <stdio.h>
#include <math.h>

int main(void)
{
    int L;
    scanf("%d", &L);
    char word;
    int result = 0;
    for (int i = 0; i < L; i++)
    {
        scanf(" %c", &word);
        result += ((int)pow(31.0, i)) * (word - 96);
    }

    printf("%d", result);
    return 0;
}