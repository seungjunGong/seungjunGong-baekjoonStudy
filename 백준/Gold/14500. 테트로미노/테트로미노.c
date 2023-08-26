#include <stdio.h>
#define MAX_SIZE 500
#define MAX(a, b) (a > b ? a : b)

int n, m, max;
int paper[MAX_SIZE][MAX_SIZE];
int visited[MAX_SIZE][MAX_SIZE];
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

// ㅗ 모양을 제외한 나머지모양
void case_abcd(int y, int x, int cnt, int sum)
{
    if (cnt == 4)
    {
        max = MAX(max, sum);
        return;
    }

    for (int i = 0; i < 4; i++)
    {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (nx < 0 || nx >= m || ny < 0 || ny >= n)
            continue;
        if (!visited[ny][nx])
        {
            visited[ny][nx] = 1;
            case_abcd(ny, nx, cnt + 1, sum + paper[ny][nx]);
            visited[ny][nx] = 0;
        }
    }
    return;
}

// ㅗ 모양
void case_e(int y, int x)
{
    for (int i = 0; i < 4; i++)
    {
        int rotate[3] = {i, (i + 1) % 4, (i + 2) % 4};
        int sum = paper[y][x], check = 1;
        for (int j = 0; j < 3; j++)
        {
            int ny = dy[rotate[j]] + y;
            int nx = dx[rotate[j]] + x;
            if (nx < 0 || nx >= m || ny < 0 || ny >= n)
                check = 0;
            sum += paper[ny][nx];
        }
        if (check)
            max = MAX(max, sum);
    }
}

int main(void)
{
    max = 0;
    scanf("%d %d", &n, &m);

    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            scanf("%d", &paper[i][j]);

    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
        {
            visited[i][j] = 1;
            case_abcd(i, j, 1, paper[i][j]);
            visited[i][j] = 0;
            case_e(i, j);
        }

    printf("%d", max);

    return 0;
}