#include <stdio.h>
#include <math.h>
#define MAX_SIZE 1000001

int prime_arr[MAX_SIZE]; // 소수 1 아니면 0
int stack[MAX_SIZE];
int top;

int main(void)
{
    top = -1;
    for (int i = 0; i < MAX_SIZE; i++)
        prime_arr[i] = 1;

    for (int i = 2; i < (int)sqrt(MAX_SIZE); i++)
        if (prime_arr[i])
            for (int j = i * i; j < MAX_SIZE; j += i)
                prime_arr[j] = 0;

    for (int i = 3; i < MAX_SIZE; i += 2)
        if (prime_arr[i])
            stack[++top] = i;

    int n;
    scanf("%d", &n);
    while (n != 0)
    {
        for (int i = 0; i < MAX_SIZE; i++)
            if (prime_arr[n - stack[i]])
            {
                printf("%d = %d + %d\n", n, stack[i], n - stack[i]);
                break;
            }
        scanf("%d", &n);
    }

    return 0;
}