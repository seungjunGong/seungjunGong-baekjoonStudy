#include <stdio.h>

int main(void)
{
    long long int n;
    scanf("%d", &n);
    printf("%lld\n%d", (n-2) * (n-1) * n / 6, 3);

    return 0;
}