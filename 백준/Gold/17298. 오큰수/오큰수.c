#include <stdio.h>
#define MAX_SIZE 1000000

typedef struct
{
    int stack[MAX_SIZE];
    int top;
} StackType;
int a[MAX_SIZE];
StackType s, res;

int is_empty(StackType *s)
{
    return s->top == -1;
}

void push(StackType *s, int item)
{
    s->stack[++s->top] = item;
}

int pop(StackType *s)
{
    return s->stack[s->top--];
}

int main(void) // stack area
{
    s.top = -1, res.top = -1;

    int n;
    scanf("%d", &n);

    for (int i = n - 1; i > -1; i--)
        scanf("%d", &a[i]);

    push(&res, -1);
    push(&s, a[0]);

    for (int i = 1; i < n; i++)
    {
        if (a[i] < s.stack[s.top])
        {
            push(&res, s.stack[s.top]);
        }
        else
        {
            if (!is_empty(&s))
            {
                pop(&s);
                i--;
                continue;
            }
            else
                push(&res, -1);
        }
        push(&s, a[i]);
    }

    for (int i = 0; i < n; i++)
        printf("%d ", pop(&res));
    return 0;
}