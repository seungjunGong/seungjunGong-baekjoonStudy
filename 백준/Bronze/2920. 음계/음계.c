#include <stdio.h>

int main(void)
{
    int n, arr[8];
    for (int i = 0; i < 8; i++)
    {
        scanf("%d", &n);
        arr[i] = n;
    }

    int check[2] = {1, 1};
    for (int i = 0; i < 8; i++)
    {
        if (arr[i] != i + 1)
            check[0] = 0;
        if (arr[i] != 8 - i)
            check[1] = 0;
    }

    if (check[0])
        printf("ascending");
    else if (check[1])
        printf("descending");
    else
        printf("mixed");
}