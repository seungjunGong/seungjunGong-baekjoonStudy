#include <stdio.h>

/* 최대 공약수 구하기 => 유클리드 호제법 . 2개의 자연수(또는 정식) 
a, b에 대해서 a를 b로 나눈 나머지를 r이라 하면(단, a>b), a와 b의 최대공약수는 b와 r의 최대공약수와 같다 */
long long int gcd(long long int a, long long int b){
    if (b == 0){
        return a;
    } else return gcd(b, a % b);
}

int main(void){
    long long int a, b;
    scanf("%lld %lld", &a, &b);

    long long int tmp = a;
    a = (a > b) ? a : b;
    b = (tmp < b) ? tmp : b;
    printf("%lld", a * b / gcd(a, b)); // 두 수의 곱 = 최대 공약수 * 최소 공배수

    return 0;
}