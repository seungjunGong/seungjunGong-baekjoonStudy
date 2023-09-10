#include <stdio.h>
#define MAX_SIZE 12
#define DIS_SIZE 6

int k, arr[MAX_SIZE], s[DIS_SIZE];

void print()
{
    for (int i = 0; i < DIS_SIZE; i++)
        printf("%d ", arr[s[i]]);
    printf("\n");
}

void sol(int cnt)
{
    if (cnt == DIS_SIZE)
    {
        print();
        return;
    }

    if (cnt == 0)
    {
        for (int i = 0; i < k; i++)
        {
            s[cnt] = i;
            sol(cnt + 1);
        }
    }
    else
    { // 6자리가 되어야 출력
        for (int i = s[cnt - 1] + 1; i < k; i++)
        {
            s[cnt] = i;
            sol(cnt + 1);
        }
    }
}

int main(void)
{
    while (1)
    {
        scanf("%d", &k);
        if (k == 0)
            break;

        for (int i = 0; i < k; i++)
            scanf("%d", &arr[i]);

        sol(0);
        printf("\n");
    }

    return 0;
}