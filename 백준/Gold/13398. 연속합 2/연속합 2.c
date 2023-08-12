#include <stdio.h>
#define MAX_SIZE 100000
#define MAX(a, b) a > b ? a : b

int n, arr[MAX_SIZE], dp[MAX_SIZE][2], max, right;

int main(void)
{
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);

    max = -1000;
    for (int i = 0; i < n; i++)
    {
        right = n - i - 1;
        dp[i][0] = MAX(arr[i] + dp[i - 1][0], arr[i]);
        dp[right][1] = MAX(arr[right] + dp[right + 1][1], arr[right]);
        max = MAX(max, dp[i][0]);
    }

    for (int i = 1; i < n - 1; i++)
        max = MAX(max, dp[i - 1][0] + dp[i + 1][1]);

    printf("%d", max);

    return 0;
}