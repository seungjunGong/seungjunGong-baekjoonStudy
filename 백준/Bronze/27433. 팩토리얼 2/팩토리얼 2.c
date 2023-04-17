#include <stdio.h>

long long int factiorial(int n)
{
    if (n == 0)
        return 1;
    if (n == 1)
        return 1;
    return n * factiorial(n - 1);
}
int main(void)
{
    int n;
    scanf("%d", &n);
    printf("%lld", factiorial(n));

    return 0;
}