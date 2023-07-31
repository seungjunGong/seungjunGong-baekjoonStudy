#include <stdio.h>
#include <math.h>
#define MAX_SIZE 100000
#define MIN(a, b) a < b ? a : b

int n, dp[MAX_SIZE];

int main(void)
{
    scanf("%d", &n);

    for (int i = 1; i <= n; i++)
        dp[i] = i;

    for (int i = 2; i <= n; i++)
        for (int j = 1; j <= (int)sqrt(i); j++) // 제곱수 중 가장 작은 경우 저장
            dp[i] = MIN(dp[i], (dp[i - j * j] + 1));

    printf("%d", dp[n]);
    return 0;
}