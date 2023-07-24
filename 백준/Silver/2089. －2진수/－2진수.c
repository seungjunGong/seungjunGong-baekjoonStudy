#include <stdio.h>
#define MAX_SIZE 1000000

int stack[MAX_SIZE];
int top = 0;

int main(void)
{
    long long n;
    scanf("%lld", &n);

    if(!n) stack[++top] = n;
    
    while (n)
    {
        if (n % (-2) == -1)
        {
            n = n / (-2) + 1;
            stack[++top] = 1;
        }
        else
        {
            stack[++top] = n % (-2);
            n /= (-2);
        }
    }

    while (top)
        printf("%d", stack[top--]);

    return 0;
}