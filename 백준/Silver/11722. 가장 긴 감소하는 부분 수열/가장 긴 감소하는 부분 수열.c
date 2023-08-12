#include <stdio.h>
#define MAX_SIZE 1001
#define MAX(a, b) a > b ? a : b

int n, arr[MAX_SIZE], dp[MAX_SIZE], max;

int main(void)
{
    scanf("%d", &n);

    for (int i = 0; i < n; i++){
        scanf("%d", &arr[i]);
        dp[i] = 1;
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < i; j++)
            if (arr[i] < arr[j])
                dp[i] = MAX(dp[i], 1 + dp[j]);
        max = MAX(max, dp[i]);
    }

    printf("%d", max);
    return 0;
}