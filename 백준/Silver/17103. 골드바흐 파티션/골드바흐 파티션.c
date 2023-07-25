#include <stdio.h>
#include <math.h>
#define MAX_SIZE 1000001

int isPrime[MAX_SIZE] = {0};
int primeStack[MAX_SIZE];
int T, cnt, N = 0, top = -1;

int main(void)
{
    for (int i = 2; i < MAX_SIZE; i++)
        isPrime[i] = 1;

    for (int i = 2; i <= sqrt(MAX_SIZE); i++)
        if (isPrime[i])
            for (int j = i * i; j < MAX_SIZE; j += i)
                isPrime[j] = 0;

    for (int i = 0; i < MAX_SIZE; i++)
        if (isPrime[i])
            primeStack[++top] = i;

    scanf("%d", &T);
    while (T--)
    {
        cnt = 0;
        scanf("%d", &N);

        for (int i = 0; primeStack[i] <= N/2; i++)
            if (isPrime[N - primeStack[i]])
                cnt++;
        printf("%d\n", cnt);
    }

    return 0;
}