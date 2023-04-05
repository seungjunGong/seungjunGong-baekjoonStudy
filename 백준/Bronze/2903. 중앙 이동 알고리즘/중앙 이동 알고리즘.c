#include <stdio.h>

int main(void)
{
    int n;
    scanf("%d", &n);

    int res = 2;
    for (int i = 1; i <= n; i++){
        res = res + res - 1;
    }

    printf("%d", res * res);
    return 0;
}