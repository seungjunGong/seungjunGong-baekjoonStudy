#include <stdio.h>
#define MAX_SIZE 1001
#define MAX(a, b) a > b ? a : b

int n;
int p[MAX_SIZE], dp[MAX_SIZE] = {0};

int main(void)
{
    scanf("%d", &n);

    for(int i = 1; i <= n; i++)
        scanf("%d", &p[i]);

    for(int i = 1; i <= n; i++)
        for(int j = 1; j <= i; j++) // 카드수당 최대 dp 설정
            dp[i] = MAX(dp[i-j] + p[j], dp[i]);

    printf("%d", dp[n]);
    return 0;
}