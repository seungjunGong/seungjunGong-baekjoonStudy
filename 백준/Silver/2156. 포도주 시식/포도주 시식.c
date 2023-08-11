#include <stdio.h>
#define MAX_SIZE 10000
#define MAX(a, b, c) a > b ? a > c ? a : c : b > c ? b : c

int n, arr[MAX_SIZE], dp[MAX_SIZE];

int main(void)
{
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);

    for (int i = 0; i < n; i++)
        dp[i] = MAX(arr[i] + dp[i - 2], arr[i] + arr[i - 1] + dp[i - 3], dp[i-1]);

    printf("%d", dp[n-1]);

    return 0;
}