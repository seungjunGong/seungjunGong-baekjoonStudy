#include <stdio.h>
#define MAX_SIZE 21
#define ABS(x) (x > 0 ? x : (-1) * x)
#define MIN(a, b) (a < b ? a : b)

int n, S[MAX_SIZE][MAX_SIZE];
int check[MAX_SIZE], min;

void cal()
{
    int status = 0;

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
        {
            if (check[i] && check[j])
                status += S[i][j];
            if (!check[i] && !check[j])
                status -= S[i][j];
        }
    min = MIN(min, ABS(status));
}

void dfs(int depth, int cnt)
{
    if (depth >= n)
        return;

    if (cnt > n / 2 + 1)
        return;

    if (cnt > 0)
        cal();

    check[depth] = 1;
    dfs(depth + 1, cnt + 1); // 처음에는 한쪽 팀으로 전부 이동
    check[depth] = 0;
    // 이후 반대쪽 팀으로 한명씩 이동, 이미 팀을 뽑았기 때문에 cnt X
    dfs(depth + 1, cnt);
}

int main(void)
{
    min = 40000;

    scanf("%d", &n);

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            scanf("%d", &S[i][j]);

    dfs(0, 0);

    printf("%d", min);

    return 0;
}