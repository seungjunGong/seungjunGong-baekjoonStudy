#include <stdio.h>

int main(void)
{
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    long int res = a * b * c;

    int counts[10] = {0};
    while (res)
    {
        counts[res % 10] += 1;
        res /= 10;
    }

    for (int i = 0; i < 10; i++)
        printf("%d\n", counts[i]);

    return 0;
}