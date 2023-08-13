#include <stdio.h>
#define MAX_SIZE 1000
#define INF MAX_SIZE *MAX_SIZE
#define RGB_SIZE 3
#define MIN(a, b) a < b ? a : b
int n, arr[MAX_SIZE][RGB_SIZE], dp[MAX_SIZE][RGB_SIZE], min;

int main(void)
{
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
        scanf("%d %d %d", &arr[i][0], &arr[i][1], &arr[i][2]);

    min = INF;
    // red
    dp[0][0] = arr[0][0], dp[0][1] = INF, dp[0][2] = INF;
    for (int i = 1; i < n; i++)
    {
        dp[i][0] = (MIN(dp[i - 1][1], dp[i - 1][2])) + arr[i][0];
        dp[i][1] = (MIN(dp[i - 1][0], dp[i - 1][2])) + arr[i][1];
        dp[i][2] = (MIN(dp[i - 1][0], dp[i - 1][1])) + arr[i][2];
    }
    min = MIN(min, (MIN(dp[n - 1][1], dp[n - 1][2])));
    // green
    dp[0][0] = INF, dp[0][2] = INF, dp[0][1] = arr[0][1];
    for (int i = 1; i < n; i++)
    {
        dp[i][0] = (MIN(dp[i - 1][1], dp[i - 1][2])) + arr[i][0];
        dp[i][1] = (MIN(dp[i - 1][0], dp[i - 1][2])) + arr[i][1];
        dp[i][2] = (MIN(dp[i - 1][0], dp[i - 1][1])) + arr[i][2];
    }
    min = MIN(min, (MIN(dp[n - 1][0], dp[n - 1][2])));
    // blue
    dp[0][0] = INF, dp[0][1] = INF, dp[0][2] = arr[0][2];
    for (int i = 1; i < n; i++)
    {
        dp[i][0] = (MIN(dp[i - 1][1], dp[i - 1][2])) + arr[i][0];
        dp[i][1] = (MIN(dp[i - 1][0], dp[i - 1][2])) + arr[i][1];
        dp[i][2] = (MIN(dp[i - 1][0], dp[i - 1][1])) + arr[i][2];
    }
    min = MIN(min, (MIN(dp[n - 1][0], dp[n - 1][1])));

    printf("%d", min);
    return 0;
}