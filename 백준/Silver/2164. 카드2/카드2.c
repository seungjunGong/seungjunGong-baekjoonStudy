#include <stdio.h>
#define MAX_SIZE 500000

typedef int element;
typedef struct
{
    element data[MAX_SIZE];
    int front;
    int rear;
} QueueType;

void init_queue(QueueType *q)
{
    q->front = q->rear = 0;
}

int empty(QueueType *q)
{
    return q->front == q->rear;
}

void push(QueueType *q, element item)
{
    q->data[q->rear] = item;
    q->rear = (q->rear + 1) % MAX_SIZE;
}

element pop(QueueType *q)
{
    element tmp = q->data[q->front];
    q->front = (q->front + 1) % MAX_SIZE;
    return tmp;
}

int main(void)
{
    QueueType q;
    init_queue(&q);

    int n;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++)
    {
        push(&q, i);
    }
    while (--n)
    {
        pop(&q);
        push(&q, pop(&q));
    }

    printf("%d", q.data[q.front]);

    return 0;
}