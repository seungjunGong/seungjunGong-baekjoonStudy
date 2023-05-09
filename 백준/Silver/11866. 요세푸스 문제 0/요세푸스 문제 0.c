#include <stdio.h>
#include <string.h>

int main(void)
{
    int n, k;
    scanf("%d %d", &n, &k);

    int arr[1001] = {0};
    for (int i = 1; i <= n; i++)
        arr[i] = 1;

    int cnt = 0;   // k번까지 카운트
    int total = 0; // 현재 총 순열 개수
    int i = 0;     // 원형 이동 index
    printf("<");
    while (total < n)
    {
        if (arr[i] == 1)
            cnt++;
        if (cnt == k)
        {
            cnt = 0;
            total += 1;
            arr[i] = 0;
            printf(total == n ? "%d>" : "%d, ", i);
        }
        i = (i + 1) % (n + 1);
    }
    return 0;
}