#include <stdio.h>
#define MOD 1000000000
#define MAX_N 101
#define MAX_SIZE 10

int n;
int dp[MAX_N][MAX_SIZE];
int cnt = 0;

int main(void)
{
    scanf("%d", &n);

    for (int i = 1; i < MAX_SIZE; i++)
        dp[1][i] = 1; // [자리수][마지막수]

    for (int i = 2; i <= n; i++)
    {
        dp[i][0] = dp[i - 1][1];

        for (int j = 1; j < MAX_SIZE - 1; j++)
            dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % MOD;

        dp[i][9] = dp[i - 1][8] % MOD;
    }

    for (int i = 0; i < MAX_SIZE; i++)
        cnt = (cnt + dp[n][i]) % MOD;

    printf("%d", cnt);

    return 0;
}