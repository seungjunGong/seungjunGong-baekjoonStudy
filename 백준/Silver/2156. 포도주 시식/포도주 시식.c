#include <stdio.h>
#define MAX_SIZE 10000
#define MAX(a, b) a > b ? a : b

int n, arr[MAX_SIZE], dp[MAX_SIZE], max;

int main(void)
{
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);

    max = 0;
    for (int i = 0; i < n; i++)
    {
        dp[i] = MAX(arr[i] + dp[i - 2], arr[i] + arr[i - 1] + dp[i - 3]);
        dp[i] = MAX(dp[i], dp[i - 1]);
        max = MAX(max, dp[i]);
    }

    printf("%d", max);

    return 0;
}