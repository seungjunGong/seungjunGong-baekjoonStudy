#include <stdio.h>

int cnt, virus = 0;
int computers[101][101] = { 0 };
int visited[101] = { 0 }; // c언어에서 {0}꼴 배열 초기화는 0 밖에 안된다.

void check(int n) // n: 현재 방문 노드
{
    for (int i = 1; i <= cnt; i++)
    {
        if (computers[n][i] && !visited[i]) // 방문 노드인지 확인
        {
            visited[i] = 1;
            virus++;
            check(i);
        }
    }
}

int main(void)
{
    int link;
    scanf("%d %d", &cnt, &link);

    int x, y;
    for (int i = 0; i < link; i++)
    {
        scanf("%d %d", &x, &y);
        computers[x][y] = computers[y][x] = 1;
    }

    visited[1] = 1;
    check(1);
    printf("%d", virus);

    return 0;
}