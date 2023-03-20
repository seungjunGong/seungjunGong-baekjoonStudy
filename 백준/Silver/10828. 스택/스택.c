#include <stdio.h>
#include <stdlib.h>
#include <string.h>

long arr[100000];
int peek = -1;

int empty()
{
    return (peek != -1 ? 0 : 1);
}

int top()
{
    return (empty() == 1 ? -1 : arr[peek]);
}

int size()
{
    return (peek != -1 ? peek + 1 : 0);
}

void push(long x)
{
    arr[++peek] = x;
}

long pop()
{   
    return (empty() == 1 ? -1 : arr[peek--]);
}

int main(void)
{

    int n;
    scanf("%d", &n);
    while (getchar() != '\n') {}

    while (n--)
    {
        char str[6];
        long num;
        scanf("%s", &str);

        if (strcmp(str, "top") == 0)
        {
            printf("%d\n", top());
        }
        else if (strcmp(str, "empty") == 0)
        {
            printf("%d\n", empty());
        }
        else if (strcmp(str, "size") == 0)
        {
            printf("%d\n", size());
        }
        else if (strcmp(str, "push") == 0)
        {
            scanf("%ld", &num);
            push(num);
        }
        else if (strcmp(str, "pop") == 0)
        {
            printf("%ld\n", pop());
        }
    }
    return 0;
}