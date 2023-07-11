#include <stdio.h>
#include <string.h>

int main(void)
{
    int m, x;
    scanf("%d", &m);
    char commend[7];
    int set[21] = {0};

    while (m--)
    {
        scanf("%s", commend);
        if (!strcmp("add", commend))
        {
            scanf("%d", &x);
            set[x] = 1;
        }
        else if (!strcmp("remove", commend))
        {
            scanf("%d", &x);
            set[x] = 0;
        }
        else if (!strcmp("check", commend))
        {
            scanf("%d", &x);
            printf("%d\n", set[x]);
        }
        else if (!strcmp("toggle", commend))
        {
            scanf("%d", &x);
            set[x] = !set[x];
        }
        else if (!strcmp("all", commend))
        {
            for (int i = 1; i <= 20; i++)
                set[i] = 1;
        }
        else if (!strcmp("empty", commend))
        {
            for (int i = 1; i <= 20; i++)
                set[i] = 0;
        }
    }

    return 0;
}