/*
    이번문제에서의 실수
    1. 단순히 평균의 값으로 높이를 계산해서 가능한 높이를 구하면
    최소 시간이 되는 줄 알았음.
    반례를 테스트해 본 결과
    // 2 1
    1 3 68
    0 0 1
    의 경우 1 1 1 이 될때 최소값을 가짐
    따라서 가장 높은 수를 높이로 삼고 이후 높이를 줄여나가면서
    최소 시간을 구함.

    2. 동적 할당 segementation fault
    포인터를 잘못 만질 경우 생기는 오류이다.
    2차원 배열 동적 할당하는 방법을 숙지해두자.

    3. 최소시간
    최소 시간의 범위를 조건을 보고 판단할 수 있는 능력을 길러야함.
*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void mCopy(int **original, int **copy, int n, int m)
{
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            copy[i][j] = original[i][j];
}

int checking(int **arr, int height, int b, int n, int m, int *time)
{
    int count;
    for (int i = 0; i < n; i++) // 높이만큼 깍기
    {
        for (int j = 0; j < m; j++)
        {
            if (arr[i][j] > height)
            {
                count = arr[i][j] - height;
                *time += 2 * count;
                b += count;
                arr[i][j] = height;
            }
        }
    }

    for (int i = 0; i < n; i++) // 부족한 부분 채우기
    {
        for (int j = 0; j < m; j++)
        {
            if (arr[i][j] < height)
            {
                count = height - arr[i][j];
                *time += count;
                b -= count;
                if (b < 0)
                    return 0;
            }
        }
    }
    return 1;
}

int main(void)
{
    int n, m, b;
    scanf("%d %d %d", &n, &m, &b);

    int **original = (int **)malloc(sizeof(int *) * n);
    int **copy = (int **)malloc(sizeof(int *) * n);
    for (int i = 0; i < n; i++)
    {
        original[i] = (int *)malloc(sizeof(int) * m);
        copy[i] = (int *)malloc(sizeof(int) * m);
    }

    int item;
    int height = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            scanf("%d", &item);
            original[i][j] = item;
            if (item > height)
                height = item;
        }
    }

    int *time = (int *)malloc(sizeof(int));
    *time = 0;
    mCopy(original, copy, n, m);
    int short_time = 256 * 2 * n * m;
    int short_height = 0;

    while (height > -1) // 현재 높이에서 가능한지 확인
    {
        if (checking(copy, height, b, n, m, time))
        {
            if (short_time > *time)
            {
                short_time = *time;
                short_height = height;
            }
        }

        *time = 0;
        mCopy(original, copy, n, m);
        height -= 1;
    }

    printf("%d %d", short_time, short_height);

    for (int i = 0; i < n; i++)
    {
        free(original[i]);
        free(copy[i]);
    }
    free(original);
    free(copy);

    return 0;
}