#include <stdio.h>
#define MAX_SIZE 100001
#define D 1000000009

int T, n;
long dp[MAX_SIZE][4] = {{0}};

int main(void)
{
    scanf("%d", &T);

    for (int i = 1; i <= 3; i++) // dp[n][1]은 n이 끝에 1에 오는 경우의 수를 의미
        dp[i][i] = 1;

    for (int i = 3; i < MAX_SIZE; i++)
        for (int j = 1; j <= 3; j++)
            if (i - j > 0) // [현재 구하고자하는 수][끝에 오는수] = [현재구하고자하는 수 - j][구하는 수 제외한 수]
                dp[i][j] += (dp[i - j][j % 3 + 1] + dp[i - j][(j + 1) % 3 + 1]) % D;

    while (T--)
    {
        scanf("%d", &n);
        printf("%ld\n", (dp[n][1] + dp[n][2] + dp[n][3]) % D);
    }

    return 0;
}