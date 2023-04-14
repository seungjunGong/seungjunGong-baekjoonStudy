#include <stdio.h>
#include <string.h>
#define MAX_SIZE 101

typedef double element;
typedef struct
{
    element data[MAX_SIZE];
    int top;
} StackType;

void init_Stack(StackType *s)
{
    s->top = -1;
}

int empty(StackType *s)
{
    return s->top == -1;
}

void push(StackType *s, element item)
{
    s->data[++s->top] = item;
}

element pop(StackType *s)
{
    return s->data[s->top--];
}

element calc_posfix(char *exp, element *num)
{
    element op1, op2, value;
    int len = 0;

    for (int i = 0; exp[i]; i++)
    {
        len += 1;
    }

    char ch;
    StackType s;
    init_Stack(&s);

    for (int i = 0; i < len; i++)
    {
        ch = exp[i];
        if (ch != '+' && ch != '-' && ch != '*' && ch != '/')
        {
            value = num[(int)exp[i] - 65];
            push(&s, value);
        }
        else
        {
            op2 = pop(&s);
            op1 = pop(&s);
            switch (ch)
            {
            case '+':
                push(&s, op1 + op2);
                break;
            case '-':
                push(&s, op1 - op2);
                break;
            case '*':
                push(&s, op1 * op2);
                break;
            case '/':
                push(&s, op1 / op2);
                break;
            }
        }
    }
    return pop(&s);
}

int main(void)
{
    int n;
    scanf("%d", &n);

    char s[MAX_SIZE];
    scanf("%s", s);

    // 65 ~ 90 A ~ Z
    element num[26];
    int i = 0;
    while (n--)
    {
        scanf("%lf", &num[i++]);
    }

    printf("%.2lf", calc_posfix(s, num));

    return 0;
}