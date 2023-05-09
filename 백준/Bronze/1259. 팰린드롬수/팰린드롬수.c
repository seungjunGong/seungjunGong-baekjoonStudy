#include <stdio.h>
#include <string.h>

int main(void)
{
    char n[5];

    while (scanf("%s", n) && n[0] != '0')
    {
        int start = 0;
        int end = strlen(n);
        int check = 1;
        for (int i = start; i < (start + end) / 2; i++)
        {
            if (n[i] != n[end - 1 - i])
            {
                check = 0;
            }
        }
        if (check)
            printf("yes\n");
        else
            printf("no\n");
    }
    return 0;
}