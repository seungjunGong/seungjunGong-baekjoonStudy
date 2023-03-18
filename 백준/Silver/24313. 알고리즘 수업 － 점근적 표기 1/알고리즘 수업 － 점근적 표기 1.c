#include <stdio.h>

int main(void)
{
    int a1, a0, c, n0;
    int n;
    scanf("%d %d %d %d", &a1, &a0, &c, &n0);

    printf("%d", (c - a1) < 0 ? 0 : ((double)a0 / (c - a1) <= n0 ? 1 : 0));
    return 0;
}