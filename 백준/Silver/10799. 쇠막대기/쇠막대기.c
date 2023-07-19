#include <stdio.h>
#define MAX_SIZE 100000

char str[MAX_SIZE];
char stack[MAX_SIZE];
int top = -1, cnt = 0;

void push(int x)
{
    stack[++top] = x;
}

char pop()
{
    return stack[top--];
}

int main(void)
{
    scanf("%s", str);

    for (int i = 0; str[i] != '\0'; i++)
    {
        if (str[i] == '(')
            push('(');
        else if (str[i] == ')')
        {
            pop();
            if (str[i - 1] == '(')
                cnt += top + 1;
            else
                cnt++;
        }
    }

    printf("%d", cnt);

    return 0;
}