#include <stdio.h>

int main(void)
{

    int n;
    int b;
    scanf("%d", &n);
    scanf("%d", &b);

    char arithmetic[36] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};

    int res[100] = {0};
    int n_size = 0;
    int num;
    while (n >= b)
    {
        num = n % b;
        res[n_size++] = num;
    
        n = (int)n / b;
    }

    res[n_size] = n == b ? 1 : n;

    for (n_size; n_size > -1; n_size--)
    {
        printf("%c", arithmetic[res[n_size]]);
    }
}