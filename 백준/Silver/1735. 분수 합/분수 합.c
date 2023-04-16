#include <stdio.h>
#define MAX(a, b) a > b ? a : b
#define MIN(a, b) a < b ? a : b
typedef long long int element;

element gcd(element a, element b)
{
    if (b == 0)
    {
        return a;
    }
    return gcd(b, a % b);
}

int main(void)
{
    element a1, a2, b1, b2;
    scanf("%lld %lld %lld %lld", &a1, &b1, &a2, &b2);

    element lcm = b1 * b2 / gcd(MAX(b1, b2), MIN(b1, b2));

    element num = lcm / b1 * a1 + lcm / b2 * a2;
    element denum = lcm;
    element div = gcd(MAX(num, denum), MIN(num, denum));

    printf("%lld %lld", num / div, denum / div);

    return 0;
}