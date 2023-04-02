#include <stdio.h>
#include <stdlib.h>
#define MAX_SIZE 100000

typedef int element;
typedef struct
{
    element *data;
    int top;
} StackType;

void init_stack(StackType *s)
{
    s->data = (element *)malloc(MAX_SIZE * sizeof(element));
    s->top = -1;
}

int empty(StackType *s)
{
    return s->top == -1;
}

int is_full(StackType *s){
    return s->top -1 == MAX_SIZE;
}

void push(StackType *s, element item)
{
    if(is_full(s)){
        printf("NO");
        exit(1);
    }
    s->data[++(s->top)] = item;
}

void pop(StackType *s)
{
    s->top--;
}

int main(void)
{
    int n;
    scanf("%d", &n);
    int *number = (element *)malloc(n * sizeof(element));

    StackType stack;
    init_stack(&stack);

    for (int i = 0; i < n; i++)
        scanf("%d", number + i);

    char calculation[MAX_SIZE * 2];
    int push_num = 0;
    int num_i = 0, cal_i = 0; // number index
    int check_minus = 0, stack_pos = 0;

    while (++push_num <= n)
    {
        push(&stack, push_num);
        calculation[cal_i++] = '+';
        while (stack.data[stack.top] == number[num_i] && num_i < n)
        {
            pop(&stack);
            calculation[cal_i++] = '-';
            check_minus++;
            num_i++;
        }
    }

    if (check_minus == n)
    {
        for (int i = 0; i < cal_i; i++)
        {
            printf("%c\n", calculation[i]);
        }
    }
    else
        printf("NO");

    free(number);
    return 0;
}