#include <stdio.h>
#define MAX_SIZE 21
#define ABSDIF(a, b) (a > b ? (a - b) : (b - a))
#define MIN(a, b) (a < b ? a : b)

int n, S[MAX_SIZE][MAX_SIZE];
int check[MAX_SIZE], min, mid;

void cal()
{
    int start = 0, link = 0;

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
        {
            if (check[i] && check[j])
                start += S[i][j];
            if (!check[i] && !check[j])
                link += S[i][j];
        }

    min = MIN(min, ABSDIF(start, link));
}

void dfs(int depth, int cnt)
{
    if (cnt == mid)
    {
        cal();
        return;
    }

    for (int i = depth; i < n; i++)
    {
        check[i] = 1;
        dfs(i + 1, cnt + 1);
        check[i] = 0;
    }
}

int main(void)
{
    min = 40000;

    scanf("%d", &n);
    mid = n / 2;

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            scanf("%d", &S[i][j]);

    dfs(0, 0);

    printf("%d", min);

    return 0;
}