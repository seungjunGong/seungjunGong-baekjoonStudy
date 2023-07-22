#include <stdio.h>
#define DIFF(a, b) a > b ? a - b : b - a

int gcd(int a, int b)
{
    return b ? gcd(b, a % b) : a;
}

int main(void)
{
    long n, s, a, b;

    scanf("%ld %ld", &n, &s);
    scanf("%ld", &a);
    a = DIFF(a, s);
    while (--n)
    {
        scanf("%ld", &b);
        b = DIFF(b, s);
        a = gcd(a, b);
    }

    printf("%ld", a);

    return 0;
}