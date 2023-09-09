#include <stdio.h>
#define MIN(a, b) (a < b ? a : b)
#define MAX_VALUE 10000000
#define SIZE 10

int n, W[SIZE][SIZE], min;
int s[SIZE], visited[SIZE];

int cal()
{
    int sum = 0;

    for (int i = 0; i < n - 1; i++)
    {
        if (!W[s[i]][s[i + 1]])
            sum = MAX_VALUE;
        sum += W[s[i]][s[i + 1]];
    }
    if (!W[s[n - 1]][s[0]])
        sum = MAX_VALUE;
    sum += W[s[n - 1]][s[0]];

    return sum;
}

void sol(int cnt)
{
    if (n == cnt)
    {
        min = MIN(min, cal());
        return;
    }
    for (int i = 0; i < n; i++)
    {
        if (!visited[i])
        {
            visited[i] = 1;
            s[cnt] = i;
            sol(cnt + 1);
            visited[i] = 0;
        }
    }
}

int main(void)
{
    min = MAX_VALUE;

    scanf("%d", &n);
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            scanf("%d", &W[i][j]);

    sol(0);

    printf("%d", min);
    return 0;
}