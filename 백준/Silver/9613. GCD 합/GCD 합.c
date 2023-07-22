#include <stdio.h>
#include <stdlib.h>

int t, n, num[100];
long long int sum; // 전체 합은 1억이 넘어갈 수 있음

int gcd(int a, int b) // 유클리드 호제법 a와 b의 최대 공약수는 b와 a % b의 최대 공약수와 같다.
{
    return b ? gcd(b, a % b) : a;
}

long long int sum_gcd()
{
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            sum += gcd(num[i], num[j]);
    return sum;
}

int main(void)
{

    scanf("%d", &t);
    while (t--)
    {
        sum = 0;
        scanf("%d", &n);
        for (int i = 0; i < n; i++)
            scanf("%d", &num[i]);
        printf("%lld\n", sum_gcd());
    }

    return 0;
}