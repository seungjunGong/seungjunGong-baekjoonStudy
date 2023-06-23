#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define MAX_SIZE 31

int main(void)
{
    int n, k;
    scanf("%d", &n);
    int *arr = (int *)malloc(sizeof(int) * n);

    int counts[MAX_SIZE] = {0};
    for (int i = 0; i < n; i++) // 인덱스 번호 == 값
    {
        scanf("%d", &k);
        counts[k] += 1;
    }

    int a = 0;
    for (int i = 0; i < MAX_SIZE; i++)
        for (int j = 0; j < counts[i]; j++)
            arr[a++] = i; // 새 배열에 카운팅 정렬된 값을 얻을 수 있음

    int cut = round((double)n * 0.15); // 절사 할 부분

    long long res = 0;
    for (int i = cut; i < n - cut; i++)
        res += arr[i];
    res = n > 0 ? round(res / (long double)(n - 2 * cut)) : 0; // 절사평균 구하기

    printf("%lld", res);

    return 0;
}