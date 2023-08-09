#include <stdio.h>
#define MAX_SIZE 100001
#define MOD 9901

int n, dp[MAX_SIZE];

int main(void)
{
    scanf("%d", &n);

    dp[1] = 3, dp[2] = 7;

    for (int i = 3; i <= n; i++)
        dp[i] = (2 * dp[i - 1] + dp[i - 2]) % MOD;

    printf("%d", dp[n]);

    return 0;
}