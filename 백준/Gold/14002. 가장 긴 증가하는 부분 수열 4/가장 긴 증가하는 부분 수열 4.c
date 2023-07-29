#include <stdio.h>
#define MAX_SIZE 1000

int N, A[MAX_SIZE], dp[MAX_SIZE];
int stack[MAX_SIZE], top = 0;

int main(void)
{
    scanf("%d", &N);

    for (int i = 0; i < N; i++)
        scanf("%d", &A[i]);

    for (int i = 0; i < N; i++)
        dp[i] = 1;

    int max = 0;
    for (int i = 1; i < N; i++)
    {
        for (int j = 0; j < i; j++)
            if (A[j] < A[i] && dp[j] >= dp[i])
                dp[i] = dp[j] + 1;
        max = dp[max] < dp[i] ? i : max;
    }

    printf("%d\n", dp[max]);

    stack[++top] = A[max];
    for (int i = max - 1; dp[max] > 1; i--)
        if (A[max] > A[i] && dp[max] - 1 == dp[i])
        {
            stack[++top] = A[i];
            max = i;
        }

    while (top)
        printf("%d ", stack[top--]);
    return 0;
}