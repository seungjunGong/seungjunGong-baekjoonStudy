#include <stdio.h>
#include <string.h>
#define MAX_SIZE 10001

typedef int element;

typedef struct
{
    element data[MAX_SIZE];
    int front;
    int back;
    int size;
} DequeType;

int empty(DequeType *q)
{
    return q->front == q->back;
}

int size(DequeType *q)
{
    return q->size;
}

void init_deque(DequeType *q)
{
    q->front = q->back = q->size = 0;
}

void push_front(DequeType *q, element item)
{
    q->data[q->front] = item;
    q->front = (q->front - 1 + MAX_SIZE) % MAX_SIZE;
    q->size++;
}

void push_back(DequeType *q, element item)
{
    q->back = (q->back + 1) % MAX_SIZE;
    q->data[q->back] = item;
    q->size++;
}

element pop_front(DequeType *q)
{
    if(empty(q)){
        return -1;
    }
    q->front = (q->front + 1) % MAX_SIZE;
    q->size--;
    return q->data[q->front];
}

element pop_back(DequeType *q)
{
    if(empty(q)){
        return -1;
    }
    int prev = q->back;
    q->back = (q->back - 1 + MAX_SIZE) % MAX_SIZE;
    q->size--;
    return q->data[prev];
}

element front(DequeType *q)
{
    if (empty(q))
    {
        return -1;
    }
    return q->data[(q->front + 1) % MAX_SIZE];
}

element back(DequeType *q)
{
    if (empty(q))
    {
        return -1;
    }
    return q->data[q->back];
}

int main(void)
{
    DequeType q;
    init_deque(&q);

    int n;
    scanf("%d", &n);
    while (n--)
    {
        char command[15];
        scanf(" %s", &command);
        int item;

        if (!strcmp(command, "push_front"))
        {
            scanf("%d", &item);
            push_front(&q, item);
        }
        else if (!strcmp(command, "push_back"))
        {
            scanf("%d", &item);
            push_back(&q, item);
        }
        else if (!strcmp(command, "pop_front"))
        {
            printf("%d\n", pop_front(&q));
        }
        else if (!strcmp(command, "pop_back"))
        {
            printf("%d\n", pop_back(&q));
        }
        else if (!strcmp(command, "size"))
        {
            printf("%d\n", size(&q));
        }
        else if (!strcmp(command, "empty"))
        {
            printf("%d\n", empty(&q));
        }
        else if (!strcmp(command, "front"))
        {
            printf("%d\n", front(&q));
        }
        else if (!strcmp(command, "back"))
        {
            printf("%d\n", back(&q));
        }
    }

    return 0;
}