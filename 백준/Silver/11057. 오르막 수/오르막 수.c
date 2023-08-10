#include <stdio.h>
#define MAX_SIZE 1001
#define NUM_SIZE 10
#define MOD 10007

int n, dp[MAX_SIZE][NUM_SIZE];

int main(void)
{
    scanf("%d", &n);

    for (int i = 0; i < NUM_SIZE; i++)
        dp[1][i] = 1;

    for (int i = 2; i <= n; i++)
    {
        dp[i][0] = dp[i - 1][0];
        for (int j = 1; j < NUM_SIZE; j++)
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD;
    }

    int sum = 0;
    for (int i = 0; i < NUM_SIZE; i++)
        sum = (sum + dp[n][i]) % MOD;
    printf("%d", sum);

    return 0;
}