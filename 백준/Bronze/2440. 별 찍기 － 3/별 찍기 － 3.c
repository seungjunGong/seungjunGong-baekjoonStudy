#include <stdio.h>

void print_star(int n)
{
    if (n == 0)
        return;
    printf("*");
    print_star(n - 1);
}

void print_triangle(int n)
{
    if (n == 0)
        return;
    print_star(n);
    printf("\n");
    print_triangle(n - 1);
}

int main(void)
{
    int n;
    scanf("%d", &n);
    print_triangle(n);
    return 0;
}