#include <stdio.h>

long long int menOfPassion(int n){
    long long int cnt = 0;
    for (int i = 1; i < n; i++){
        cnt += n - i;        
    }
    return cnt;
}

int main(void)
{
    long long int n;
    scanf("%d", &n);
    printf("%lld\n%d", menOfPassion(n), 2);

    return 0;
}