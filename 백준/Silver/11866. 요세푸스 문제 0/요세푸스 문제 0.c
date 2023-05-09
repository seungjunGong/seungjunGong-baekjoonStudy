// 요세푸스 큐 이용
#include <stdio.h>
#define MAX_SIZE 1000

typedef int element;
typedef struct
{
    element data[MAX_SIZE];
    int front, rear;
    int cnt;
} QueueType;

void init_queue(QueueType *q)
{
    q->front = q->rear = 0;
    q->cnt = 0;
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

int main(void)
{
    int n, k;
    scanf("%d %d", &n, &k);

    QueueType queue;
    init_queue(&queue);

    for (int i = 1; i <= n; i++)
        enqueue(&queue, i);

    printf("<");
    while (queue.cnt < n)
    {
        for (int i = 0; i < k - 1; i++)
        {
            element add_item = dequeue(&queue);
            enqueue(&queue, add_item);
        }
        printf(++queue.cnt == n ? "%d>" : "%d, ", dequeue(&queue));
    }

    return 0;
}