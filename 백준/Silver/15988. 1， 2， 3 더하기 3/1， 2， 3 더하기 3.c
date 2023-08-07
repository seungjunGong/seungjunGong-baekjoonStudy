#include <stdio.h>
#define MOD 1000000009
#define MAX_SIZE 1000001

int T, n;
long long int dp[MAX_SIZE];

int main(void)
{
    scanf("%d", &T);

    dp[1] = 1, dp[2] = 2, dp[3] = 4;
    for (int i = 4; i < MAX_SIZE; i++)
        dp[i] = (dp[i - 1] % MOD + dp[i - 2] % MOD + dp[i - 3] % MOD) % MOD;

    while (T--)
    {
        scanf("%d", &n);
        printf("%lld\n", dp[n]);
    }
    
    return 0;
}