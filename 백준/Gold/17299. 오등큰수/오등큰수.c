#include <stdio.h>
#define MAX_SIZE 1000001

int arr[MAX_SIZE];
int cntArr[MAX_SIZE] = {0};

typedef struct
{
    int data[MAX_SIZE];
    int top;
} StackType;

StackType stack, res;

int is_empty(StackType *s)
{
    return s->top == -1;
}

void push(StackType *s, int item)
{
    s->data[++s->top] = item;
}

int pop(StackType *s)
{
    return s->data[s->top--];
}

int main(void)
{
    stack.top = -1, res.top = -1;

    int N, a;
    scanf("%d", &N);

    for (int i = 0; i < N; i++)
    {
        scanf("%d", &a);
        arr[i] = a;
        cntArr[a] += 1;
    }

    for (int i = N - 1; i > -1; i--)
    {
        if (cntArr[arr[i]] < cntArr[stack.data[stack.top]])
        {
            push(&res, stack.data[stack.top]);
            push(&stack, arr[i]);
        }
        else
        {
            if (is_empty(&stack))
            {
                push(&res, -1);
                push(&stack, arr[i]);
            }
            else
            {
                pop(&stack);
                i++;
            }
        }
    }

    while (N--)
    {
        printf("%d ", pop(&res));
    }

    return 0;
}