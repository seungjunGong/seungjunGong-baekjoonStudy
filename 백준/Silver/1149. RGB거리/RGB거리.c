#include <stdio.h>
#define MAX_SIZE 1000
#define RGB_SIZE 3
#define MIN(a, b) a < b ? a : b

int n, dp[MAX_SIZE][RGB_SIZE], rgb[RGB_SIZE], next;

int main(void)
{
    scanf("%d", &n);
    scanf("%d %d %d", &dp[0][0], &dp[0][1], &dp[0][2]);

    for (int i = 1; i < n; i++)
        for (int j = 0; j < RGB_SIZE; j++)
            dp[i][j] = MAX_SIZE * MAX_SIZE;

    for (int i = 1; i < n; i++)
    {
        scanf("%d %d %d", &rgb[0], &rgb[1], &rgb[2]);
        for (int j = 0; j < RGB_SIZE; j++)
        {
            next = (j + 1) % RGB_SIZE;
            dp[i][next] = MIN(dp[i][next], dp[i - 1][j] + rgb[next]);
            next = (j + 2) % RGB_SIZE;
            dp[i][next] = MIN(dp[i][next], dp[i - 1][j] + rgb[next]);
        }
    }

    int min = dp[n - 1][0];
    min = MIN(min, dp[n - 1][1]);
    printf("%d", MIN(min, dp[n-1][2]));
    
    return 0;
}