#include <stdio.h>
#define MOD 1000000000
#define MAX_SIZE 201

int n, k, dp[MAX_SIZE][MAX_SIZE];

int main(void)
{
    scanf("%d %d", &n, &k);

    for(int i = 1; i <= n; i++)
        dp[i][1] = 1;
    for(int i = 1; i <= k; i++)
        dp[0][i] = 1;

    for(int i = 1; i <= n; i++)
        for(int j = 2; j <= k; j++)
            dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % MOD;

    printf("%d", dp[n][k]);
    return 0;
}