#include <stdio.h>
#define MAX(a, b) a > b ? a : b

int main(void)
{
    int count, score[301] = {0}, dp[301] = {0};
    scanf("%d", &count);

    for (int i = 1; i <= count; i++)
        scanf("%d", &score[i]);

    if (count < 3)
    {
        int sum = 0;
        for (int i = 1; i <= count; i++)
            sum += score[i];
        printf("%d", sum);
    }
    else
    {
        dp[1] = score[1];
        dp[2] = score[1] + score[2];
        for (int i = 3; i <= count; i++)
            dp[i] = MAX(dp[i - 3] + score[i - 1] + score[i], dp[i - 2] + score[i]);
        printf("%d", dp[count]);
    }

    return 0;
}