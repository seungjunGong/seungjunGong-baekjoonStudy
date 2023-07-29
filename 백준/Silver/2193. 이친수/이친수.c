#include <stdio.h>
#define MAX_SIZE 91

int N;
long long dp[MAX_SIZE][2];

int main(void){
    dp[1][1] = 1;

    for(int i = 2; i < MAX_SIZE; i++){
        dp[i][1] += dp[i - 1][0];
        dp[i][0] += dp[i - 1][0] + dp[i - 1][1];
    }

    scanf("%d", &N);
    printf("%lld", dp[N][0] + dp[N][1]);

    return 0;
}