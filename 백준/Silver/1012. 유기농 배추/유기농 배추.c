/*
    이번문제에서의 실수
    1. 배열의 범위를 할당해서 포인터를 전달할 경우 오류가 생김
    정확한 이유를 모르겠음..
    -> 현재는 포인터를 사용해서 구현

    2. x, y의 가로 세로 위치를 헷갈림
    여기서는 y가 세로 배열로 구현
*/
#include <stdio.h>
#include <stdlib.h>

void init_map(int **map, int n, int m)
{
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            map[i][j] = 0;
}

void eat(int **map, int x, int y, int n, int m)
{
    if (y < 0 || y >= n || x < 0 || x >= m || map[y][x] == 0)
        return;
    map[y][x] = 0;
    eat(map, x + 1, y, n, m);
    eat(map, x, y + 1, n, m);
    eat(map, x - 1, y, n, m);
    eat(map, x, y - 1, n, m);
}

int main(void)
{
    int t, n, m, k, x, y, count;
    int **map;

    scanf("%d", &t);

    while (t--)
    {
        count = 0;
        scanf("%d %d %d", &m, &n, &k);
        map = (int **)malloc(sizeof(int *) * n);
        for (int i = 0; i < n; i++)
            map[i] = (int *)malloc(sizeof(int) * m);
        init_map(map, n, m);

        while (k--)
        {
            scanf("%d %d", &x, &y);
            map[y][x] = 1;
        }

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                if (map[i][j] == 1)
                {
                    count++;
                    eat(map, j, i, n, m);
                }
            }
        }
        printf("%d\n", count);

        for (int i = 0; i < n; i++)
            free(map[i]);
        free(map);
    }

    return 0;
}