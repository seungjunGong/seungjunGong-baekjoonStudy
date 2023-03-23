#include <stdio.h>
#include <string.h>
#define MAX_SIZE 10001
typedef int element;
typedef struct
{
    element data[MAX_SIZE];
    int front, rear, cnt;
} QueueType;

int is_empty(QueueType *q)
{
    return (q->front == q->rear);
}

int is_full(QueueType *q)
{
    return ((q->rear + 1) % MAX_SIZE == q->front);
}

void push(QueueType *q, element item)
{
    q->rear = (q->rear + 1) % MAX_SIZE;
    q->data[q->rear] = item;
    q->cnt += 1;
}

element pop(QueueType *q)
{
    if (is_empty(q))
        return -1;
    q->front = (q->front + 1) % MAX_SIZE;
    q->cnt -= 1;
    return q->data[q->front];
}

int front(QueueType *q)
{
    if (is_empty(q))
        return -1;
    return q->data[q->front + 1];
}

int back(QueueType *q)
{
    if (is_empty(q))
        return -1;
    return q->data[q->rear];
}

int main(void)
{
    int n;
    scanf("%d", &n);

    QueueType queue;
    queue.front = queue.rear = queue.cnt = 0;

    while (n--)
    {
        char str[6];
        int element;
        scanf(" %s", &str);

        if (!strcmp(str, "pop"))
            printf("%d\n", pop(&queue));
        else if (!strcmp(str, "size"))
            printf("%d\n", queue.cnt);
        else if (!strcmp(str, "empty"))
            printf("%d\n", is_empty(&queue));
        else if (!strcmp(str, "front"))
            printf("%d\n", front(&queue));
        else if (!strcmp(str, "back"))
            printf("%d\n", back(&queue));
        else
        {
            scanf("%d", &element);
            push(&queue, element);
        }
    }
    return 0;
}