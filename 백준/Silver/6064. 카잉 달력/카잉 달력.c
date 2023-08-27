#include <stdio.h>

int t, m, n, x, y, year, max;

int gcd(int a, int b)
{
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

int main(void)
{
    scanf("%d", &t);

    while (t--)
    {
        scanf("%d %d %d %d", &m, &n, &x, &y);

        year = x;
        max = (m * n) / gcd(m, n);
        while (year <= max)
        {
            if ((year - y) % n == 0)
            {
                printf("%d\n", year);
                break;
            }
            year += m;
        }

        if (year > max)
            printf("-1\n");
    }
    return 0;
}