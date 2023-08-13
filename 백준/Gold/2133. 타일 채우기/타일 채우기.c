#include <stdio.h>
#define MAX_SIZE 31

int n, dp[MAX_SIZE], tile;

int main(void){
    scanf("%d", &n);

    dp[2] = 3;
    for(int i = 4; i <= n; i += 2){
        dp[i] = 3 * dp[i-2] + 2;
        for(int j = i-4; j > 0; j -= 2)
            dp[i] += 2 * dp[j];
    }

    printf("%d", dp[n]);

    return 0;
}