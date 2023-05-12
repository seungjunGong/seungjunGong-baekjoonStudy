#include <stdio.h>

int main(void)
{
    int n;
    int sum = 0;
    for (int i = 0; i < 5; i++)
    {
        scanf("%d", &n);
        sum += n * n;
    }
    int vertifyNum = sum % 10;
    printf("%d", vertifyNum);

    return 0;
}