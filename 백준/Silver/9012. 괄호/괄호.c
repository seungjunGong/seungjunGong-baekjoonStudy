#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_STACK_SIZE 50

typedef char element;

typedef struct
{
	element data[MAX_STACK_SIZE];
	int top;
} StackType;

void init_stack(StackType *s)
{
	s->top = -1;
}

int empty(StackType *s)
{
	return -1 == s->top;
}

void push(StackType *s, element item)
{
	s->data[++(s->top)] = item;
}

element pop(StackType *s)
{
	return s->data[(s->top)--];
}

int check_matching(const char *in)
{
	StackType s;
	char ch, open_ch;
	int i, n = strlen(in);
	init_stack(&s);

	for (i = 0; i < n; i++)
	{
		ch = in[i];
		switch (ch)
		{
		case '(':
		case '[':
		case '{':
			push(&s, ch);
			break;
		default:
			if (empty(&s))
				return 0;

			open_ch = pop(&s);
			if ((open_ch == '(' && ch != ')') || (open_ch == '[' && ch != ']') || (open_ch == '{' && ch != '}'))
				return 0;

			break;
		}
	}
	if (!empty(&s))
		return 0;
	return 1;
}
int main(void)
{
	int t;
	scanf("%d", &t);

	while (t--)
	{
		element *p = malloc(sizeof(element) * MAX_STACK_SIZE);

		scanf(" %s", p);
		if (check_matching(p) == 1)
			printf("YES\n");
		else
			printf("NO\n");

		free(p);
	}

	return 0;
}