#include <stdio.h>

int main(void)
{
    int n;
    int check_num[100000] = {0};

    while (1)
    {
        scanf("%d", &n);
        if(n == -1) break;

        int sum = 0, cnt = 0;

        for (int i = 1; i < n; i++)
            check_num[cnt++] = (n % i == 0) ? i : 0;

        for (int i = 0; i < cnt; i++)
            sum += check_num[i];

        printf("%d ", n);
        if (sum == n)
        {
            printf("=");
            for (int i = 0; i < cnt; i++)
            {
                if (check_num[i] != 0)
                {
                    if (i == 0)
                        printf(" %d", check_num[i]);
                    else
                        printf(" + %d", check_num[i]);
                }
            }
        }
        else
            printf("is NOT perfect.");
        printf("\n");
    }

    return 0;
}