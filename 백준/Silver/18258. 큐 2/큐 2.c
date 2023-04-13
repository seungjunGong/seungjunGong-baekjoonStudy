#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define MAX_SIZE 2000001

typedef int element;
typedef struct 
{
    element *data;
    int front, rear, size;
}QueueType;

void init_queue(QueueType *q){
    q->data = (element *)malloc(MAX_SIZE * sizeof(element));
    q->front = q->rear = q->size = 0;
}

int empty(QueueType *q){
    return q->front == q->rear;
}

void push(QueueType *q, element item){
    q->data[q->rear] = item;
    q->rear = (q->rear + 1) % MAX_SIZE;
    q->size++;
}

element pop(QueueType *q){
    if (empty(q)){
        return -1;
    }
    element val = q->data[q->front];
    q->front = (q->front + 1) % MAX_SIZE;
    q->size--;
    return val;
}

int size(QueueType *q){
    return q->size;
}

element front(QueueType *q){
    if(empty(q)){
        return -1;
    }
    return q->data[q->front];
}

element back(QueueType *q){
    if(empty(q)){
        return -1;
    }
    return q->data[(q->rear - 1 + MAX_SIZE) % MAX_SIZE];
}
int main(void){
    QueueType q;
    
    int n, item = 0;
    scanf("%d", &n);
    char command[15];
    
    init_queue(&q);

    while(n--){
        scanf("%s", command);
        if (!strcmp(command, "push")){
            scanf("%d", &item);
            push(&q, item);
        } else if(!strcmp(command, "pop")){
            printf("%d\n", pop(&q));
        } else if(!strcmp(command, "size")){
            printf("%d\n", size(&q));
        } else if(!strcmp(command, "empty")){
            printf("%d\n", empty(&q));
        } else if(!strcmp(command, "front")){
            printf("%d\n", front(&q));
        } else if(!strcmp(command, "back")){
            printf("%d\n", back(&q));
        }
    }

    free(q.data);
    return 0;
}