#include <stdio.h>
#define MAX_SIZE 20

int N, S, cnt;
int arr[MAX_SIZE], check[MAX_SIZE], visited[MAX_SIZE];

void dfs(int depth, int sum)
{
    if (depth == N)
    {
        if (sum == S)
            cnt++;
        return;
    }

    // 더하기
    dfs(depth + 1, sum + arr[depth]);

    // 안 더하고 건너 뛰기
    dfs(depth + 1, sum);
}

int main(void)
{
    scanf("%d %d", &N, &S);

    for (int i = 0; i < N; i++)
        scanf("%d", &arr[i]);

    cnt = 0;
    dfs(0, 0);

    if (!S)
        cnt--;
    printf("%d", cnt);

    return 0;
}