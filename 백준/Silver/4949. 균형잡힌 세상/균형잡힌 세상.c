#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_STACK_SIZE 101

typedef char element;

typedef struct
{
    element data[MAX_STACK_SIZE];
    int top;
} StackType;

void init_stack(StackType *s)
{
    s->top = -1;
}

int empty(StackType *s)
{
    return -1 == s->top;
}

void push(StackType *s, element item)
{
    s->data[++(s->top)] = item;
}

element pop(StackType *s)
{
    return s->data[(s->top)--];
}

int check_matching(const char *in)
{
    StackType s;
    char ch, open_ch;
    int i, n = strlen(in);
    init_stack(&s);

    for (i = 0; i < n; i++)
    {
        ch = in[i];
        switch (ch)
        {
        case '(':
        case '[':
            push(&s, ch);
            break;
        case ')':
        case ']':
            if (empty(&s))
                return 0;

            open_ch = pop(&s);
            if ((open_ch == '(' && ch != ')') || (open_ch == '[' && ch != ']'))
                return 0;

            break;
        default:
            break;
        }
    }
    if (!empty(&s))
        return 0;
    return 1;
}
int main(void)
{

    while (1)
    {
        element *p = malloc(sizeof(element) * MAX_STACK_SIZE);
        gets(p);
        if (p[0] == '.')
            break;

        if (check_matching(p) == 1)
            printf("yes\n");
        else
            printf("no\n");

        free(p);
    }

    return 0;
}