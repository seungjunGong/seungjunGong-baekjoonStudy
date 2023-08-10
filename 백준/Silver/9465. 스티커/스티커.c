#include <stdio.h>
#define MAX_SIZE 100001
#define CASE_SIZE 3
#define MAX(a, b) a > b ? a : b

int T, n;
int arr[CASE_SIZE][MAX_SIZE], dp[MAX_SIZE][CASE_SIZE];

int main(void)
{
    scanf("%d", &T);

    while (T--)
    {
        scanf("%d", &n);
        for (int i = 1; i < CASE_SIZE; i++)
            for (int j = 1; j <= n; j++)
                scanf("%d", &arr[i][j]);

        for (int i = 1; i <= n; i++)
        {
            dp[i][0] = MAX(dp[i - 1][1], dp[i - 1][2]);
            dp[i][1] = MAX(dp[i - 1][0] + arr[1][i], dp[i - 1][2] + arr[1][i]);
            dp[i][2] = MAX(dp[i - 1][0] + arr[2][i], dp[i - 1][1] + arr[2][i]);
        }

        printf("%d\n", MAX(dp[n][1], dp[n][2]));
    }

    return 0;
}