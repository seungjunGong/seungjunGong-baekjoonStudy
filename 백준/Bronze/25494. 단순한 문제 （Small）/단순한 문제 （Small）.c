#include <stdio.h>

int T, a, b, c, cnt;

int main(void)
{
    scanf("%d", &T);

    while (T--)
    {
        scanf("%d %d %d", &a, &b, &c);

        cnt = 0;
        for (int x = 1; x <= a; x++)
            for (int y = 1; y <= b; y++)
                for (int z = 1; z <= c; z++)
                    if ((x % y == y % z) && (y % z == z % x))
                        cnt++;
        printf("%d\n", cnt);
    }

    return 0;
}