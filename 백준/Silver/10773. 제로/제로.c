#include <stdio.h>
#include <stdlib.h>

typedef int element;
typedef struct
{
	element *list;
	int top;
	int size;
} stack;

void init_stack(stack *s)
{
	s->list = (element *)malloc(s->size * sizeof(element));
	s->size = 1;
	s->top = -1;
}

int is_empty(stack *s)
{
	return s->top == -1;
}

int is_full(stack *s)
{
	return s->size - 1 == s->top;
}

void push(stack *s, element item)
{
	if (is_full(s))
	{
		s->size *= 2;
		s->list = (element *)realloc(s->list, s->size * sizeof(element));
	}

	s->list[++(s->top)] = item;
}

void pop(stack *s)
{
	s->top--;
}

long long int stack_sum(stack *s)
{
	long long int sum = 0;
	while (s->top > -1)
	{
		sum += s->list[s->top--];
	}

	return sum;
}

int main(void)
{
	int k;
	scanf("%d", &k);
	stack account_book;

	init_stack(&account_book);

	while (k--)
	{
		int num;
		scanf("%d", &num);
		if (num)
			push(&account_book, num);
		else
			pop(&account_book);
	}

	printf("%lld", stack_sum(&account_book));
	return 0;
}