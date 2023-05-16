#include <stdio.h>
#include <stdlib.h>
#define MAX_SIZE 500

typedef struct
{
    int value;
    int find;
} element;

typedef struct
{
    element data[MAX_SIZE];
    int front, rear;
} QueueType;

void init_queue(QueueType *q)
{
    q->front = q->rear = 0;
}

int is_empty(QueueType *q)
{
    return q->front == q->rear;
}

void enqueue(QueueType *q, element item)
{
    q->rear = (q->rear + 1) % MAX_SIZE;
    q->data[q->rear] = item;
}

element dequeue(QueueType *q)
{
    q->front = (q->front + 1) % MAX_SIZE;
    return q->data[q->front];
}

int check_front(QueueType *q)
{
    int front = (q->front + 1) % MAX_SIZE;
    for (int i = (front + 1) % MAX_SIZE; i <= q->rear; i = (i + 1) % MAX_SIZE)
    {
        if (q->data[front].value < q->data[i].value)
            return 0;
    }
    return 1;
}

int main(void)
{
    QueueType queue;

    int t, n, m, check, cnt;
    scanf("%d", &t);

    element item;
    while (t--)
    {
        init_queue(&queue);
        scanf("%d %d", &n, &m);
        for (int i = 0; i < n; i++)
        {
            item.find = m == i;
            scanf("%d", &item.value);
            enqueue(&queue, item);
        }

        check = 1;
        cnt = 0;

        while (check)
        {
            if (check_front(&queue))
            {
                cnt++;
                item = dequeue(&queue);
                check = !item.find;
            }
            else
            {
                item = dequeue(&queue);
                enqueue(&queue, item);
            }
        }

        while (!is_empty(&queue))
        {
            dequeue(&queue);
        }
        printf("%d\n", cnt);
    }

    return 0;
}