#include <stdio.h>
#include <string.h>
#define MAX_SIZE 1000000

char binary[MAX_SIZE];
int cnt = 1;
int sum = 0;
int stack[MAX_SIZE];
int top = 0;

int main(void)
{
    scanf("%s", &binary);

    for (int i = strlen(binary) - 1; i >= 0; i--)
    {
        sum += (binary[i] - 48) * cnt;
        cnt *= 2;
        if (i == 0 || cnt == 8)
        {
            stack[++top] = sum;
            cnt = 1;
            sum = 0;
        }
    }

    while (top)
        printf("%d", stack[top--]);

    return 0;
}