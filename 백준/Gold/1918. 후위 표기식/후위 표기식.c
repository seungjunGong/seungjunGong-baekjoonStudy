#include <stdio.h>
#include <string.h>
#define MAX_SIZE 101

typedef char element;
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

element peek(StackType *s)
{
    return s->data[s->top];
}

int prec(element op)
{
    switch (op)
    {
    case '(':
    case ')':
        return 0;
    case '+':
    case '-':
        return 1;
    case '*':
    case '/':
        return 2;
    }
    return -1;
}

/* logic
1. 연산자 일 경우 스택이 비어있지 않으면 peek 우선순위가 작을 때까지 해당 값을 pop 출력, 이후 push
2. ( 는 push
3. ) 이면 ( 가 나올 때까지 pop 출력
4. 나머지 피연산자는 출력
5. 나머지 스택에 남아있는 값을 pop 출력
*/
void infix_to_postfix(char *exp)
{
    StackType s;
    init_Stack(&s);
    element ch, top_op;

    for (int i = 0; exp[i]; i++)
    {
        ch = exp[i];
        switch (ch)
        {
        case '-':
        case '+':
        case '*':
        case '/':
            while (!empty(&s) && (prec(peek(&s)) >= prec(ch)))
                printf("%c", pop(&s));
            push(&s, ch);
            break;
        case '(':
            push(&s, ch);
            break;
        case ')':
            top_op = pop(&s);
            while (top_op != '(')
            {
                printf("%c", top_op);
                top_op = pop(&s);
            }
            break;
        default:
            printf("%c", ch);
            break;
        }
    }
    while (!empty(&s))
    {
        printf("%c", pop(&s));
    }
}

int main(void)
{
    char s[MAX_SIZE];
    scanf("%s", s);

    infix_to_postfix(s);

    return 0;
}