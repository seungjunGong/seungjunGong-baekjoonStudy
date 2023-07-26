// DP 기초 가장 작은 부분으로 나누어 풀이(점화식)
// 2 * n 의 경우는 2 * (n - 1) + 1 X 2 + 2 * (n - 2) + 2 * 1 + 2 * (n - 2) + 2 * 2로 나타낼 수 있음
#include <stdio.h>
#define MAX_SIZE 1000

int main(void)
{
    int n;
    int tiling[MAX_SIZE] = {1, 3};

    for (int i = 2; i < MAX_SIZE; i++)
        tiling[i] = (2 * tiling[i - 2] + tiling[i - 1]) % 10007;

    scanf("%d", &n);

    printf("%d", tiling[n - 1] % 10007);

    return 0;
}