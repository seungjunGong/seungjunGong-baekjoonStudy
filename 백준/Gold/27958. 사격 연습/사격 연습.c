#include <stdio.h>
#include <stdlib.h>

typedef struct
{
    int n, k;
    int **targets;
    int *bullets;
} ShootingType;

void init_shooting(ShootingType *s)
{
    // 메모리 할당
    s->targets = (int **)malloc(sizeof(int *) * s->n);
    for (int i = 0; i < s->n; i++)
    {
        s->targets[i] = (int *)malloc(sizeof(int) * s->n);
    }
    s->bullets = (int *)malloc(sizeof(int) * s->k);

    // 표적 및 총알 받기
    int target, bullet;
    for (int i = 0; i < s->n; i++)
    {
        for (int j = 0; j < s->n; j++)
        {
            scanf("%d", &target);
            s->targets[i][j] = target;
        }
    }
    for (int i = 0; i < s->k; i++)
    {
        scanf("%d", &bullet);
        s->bullets[i] = bullet;
    }
}

// 각 타겟을 제거했을 때, 그 타겟 주변에 있는 빈 칸에 새로운 타겟을 생성한다.
void new_target(int x, int y, int health, int n, int targets[][n])
{
    int dx[] = {0, 0, -1, 1};
    int dy[] = {-1, 1, 0, 0};

    for (int i = 0; i < 4; i++)
    {
        int nx = x + dx[i];
        int ny = y + dy[i];
        if (nx < 0 || nx >= n || ny < 0 || ny >= n)
            continue;
        if (targets[nx][ny] != 0)
            continue;
        int new_health = (int)health / 4;
        if (new_health == 0)
            continue;
        targets[nx][ny] = new_health;
    }
}

// 표적 및 총알 복사
int shooting(int pos[], ShootingType s)
{
    // map 복사
    int map[s.n][s.n];
    int targets[s.n][s.n];
    for (int i = 0; i < s.n; i++)
    {
        for (int j = 0; j < s.n; j++)
        {
            map[i][j] = s.targets[i][j];
            targets[i][j] = s.targets[i][j];
        }
    }

    int score = 0;
    for (int i = 0; i < s.k; i++)
    { // 총알 쏘기
        int x = pos[i];
        for (int y = 0; y < s.n; y++)
        { // 총알 타겟 맞으면 로직 실행
            if (targets[x][y] != 0)
            {
                if (targets[x][y] > 9)
                {
                    targets[x][y] = 0;

                    score += map[x][y];
                    map[x][y] = 0;
                }
                else
                {
                    targets[x][y] -= s.bullets[i];
                    if (targets[x][y] <= 0)
                    {
                        targets[x][y] = 0;
                        score += map[x][y];
                        new_target(x, y, map[x][y], s.n, targets);
                        // map 복사
                        for (int a = 0; a < s.n; a++)
                            for (int b = 0; b < s.n; b++)
                                map[a][b] = targets[a][b];
                    }
                }
                break;
            }
        }
    }

    return score;
}

void load(int arr[], int idx, ShootingType s, int *max)
{
    if (idx == s.k)
    { // 배열의 마지막 인덱스까지 값을 가졌으면 출력하고 리턴
        int score = shooting(arr, s);
        *max = *max < score ? score : *max;
        return;
    }
    for (int i = 0; i < s.n; i++)
    { // 0부터 M까지의 값을 가지는 원소에 대해서 재귀 호출
        arr[idx] = i;
        load(arr, idx + 1, s, max);
    }
}

int main(void)
{
    int n, k;
    scanf("%d %d", &n, &k);

    ShootingType s;
    s.n = n, s.k = k;
    init_shooting(&s);

    // 배열 복사
    int map[n][n];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            map[i][j] = s.targets[i][j];
        }
    }

    // 총알 장전
    int arr[k];
    int res = 0;
    load(arr, 0, s, &res);

    printf("%d", res);

    free(s.bullets);
    free(s.targets);
    return 0;
}