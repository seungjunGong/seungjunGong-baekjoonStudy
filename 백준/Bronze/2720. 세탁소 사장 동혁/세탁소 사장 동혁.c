#include <stdio.h>

int main(void)
{

    int t;
    scanf("%d", &t);

    while (t--)
    {
        int m;
        int q = 0, d = 0, n = 0, p = 0;

        scanf("%d", &m);

        while (m)
        {
            if ((int)m / 25)
            {
                q = (int)m / 25;
                m = m % 25;
            }
            else if ((int)m / 10)
            {
                d = (int)m / 10;
                m = m % 10;
            }
            else if ((int)m / 5)
            {
                n = (int)m / 5;
                m = m % 5;
            }
            else
            {
                p = m;
                m = 0;
            }
        }

        printf("%d %d %d %d\n", q, d, n, p);
    }

    return 0;
}