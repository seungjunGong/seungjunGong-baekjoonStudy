#include <stdio.h>

int cnt[4] = {0};

void init_count()
{
    for (int i = 0; i < 4; i++)
        cnt[i] = 0;
}

int main(void)
{
    char c;
    while ((c = getchar()) != EOF)
    {
        if (c > 96)
            cnt[0]++;
        else if (c > 64)
            cnt[1]++;
        else if (c == ' ')
            cnt[3]++;
        else if (c == '\n')
        {
            printf("%d %d %d %d\n", cnt[0], cnt[1], cnt[2], cnt[3]);
            init_count();
        }
        else
            cnt[2]++;
    }

    return 0;
}