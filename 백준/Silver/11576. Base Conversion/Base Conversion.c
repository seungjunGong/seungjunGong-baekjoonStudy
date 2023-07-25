#include <stdio.h>

int A, B, m, arr[25], top = 0;
long long base10 = 0, notation = 1, stack[26];

int main(void)
{
    scanf("%d %d", &A, &B);
    scanf("%d", &m);

    for (int i = 0; i < m; i++)
        scanf("%d", &arr[i]);

    for (int i = m - 1; i >= 0; i--)
    {
        base10 += arr[i] * notation;
        notation *= A;
    }

    while (base10 >= B)
    {
        stack[++top] = base10 % B;
        base10 /= B;
    }
    stack[++top] = base10;

    while (top)
        printf("%lld ", stack[top--]);

    return 0;
}