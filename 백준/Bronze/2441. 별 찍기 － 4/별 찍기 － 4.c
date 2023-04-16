#include <stdio.h>

void print_triangle(int n)
{
    int k = 0;
    for (n; n; n--)
    {
        for (int i = 0; i < k; i++)
            printf(" ");
        for (int i = 0; i < n; i++)
            printf("*");
        printf("\n");
        k++;
    }
}

int main(void)
{
    int n;
    scanf("%d", &n);
    print_triangle(n);
    return 0;
}