#include <stdio.h>
#define MAX_SIZE 100000
#define MAX(a, b) a > b ? a : b

int n, arr[MAX_SIZE], dp[MAX_SIZE], max;

int main(void)
{
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);

    dp[0] = arr[0];
    max = dp[0];
    for (int i = 1; i < n; i++)
    {
        dp[i] = arr[i] + dp[i - 1] > arr[i] ? arr[i] + dp[i - 1] : arr[i];
        max = MAX(max, dp[i]);
    }

    printf("%d", max);
    
    return 0;
}