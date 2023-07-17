#include <stdio.h>

char str[100000];
char stack[100000];
int top = -1;

void push(int x)
{
    stack[++top] = x;
}

char pop()
{
    return stack[top--];
}

void output()
{
    for(; top > -1; top--)
        printf("%c", stack[top]);
}

int main(void)
{
    scanf("%[^\n]s", str);

    for (int i = 0; str[i] != '\0'; i++)
    {
        switch (str[i])
        {
        case '<':
            output();
            push('<');
            break;
        case '>':
            printf(">");
            pop();
            break;
        case ' ':
            if (stack[top] == '<')
                break;
            output();
            printf(" ");
            break;
        default:
            if (stack[top] == '<')
                break;
            push(str[i]);
            break;
        }
        if (stack[top] == '<')
            printf("%c", str[i]);
    }
    output();

    return 0;
}