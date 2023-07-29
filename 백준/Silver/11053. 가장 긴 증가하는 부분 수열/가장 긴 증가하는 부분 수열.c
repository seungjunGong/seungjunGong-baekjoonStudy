#include <stdio.h>
#define MAX_SIZE 1000
#define MAX(a, b) a > b ? a : b

int N, A[MAX_SIZE], dp[MAX_SIZE];

int main(void)
{
    scanf("%d", &N);

    for (int i = 0; i < N; i++)
        scanf("%d", &A[i]);

    for (int i = 0; i < N; i++)
        dp[i] = 1;

    int max = 1;
    for (int i = 1; i < N; i++)
    {
        for (int j = 0; j < i; j++)
            if (A[j] < A[i] && dp[j] >= dp[i])
                dp[i] = dp[j] + 1;
        max = MAX(max, dp[i]);
    }

    printf("%d", max);
    return 0;
}