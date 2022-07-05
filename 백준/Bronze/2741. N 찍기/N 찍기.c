#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
int main(void)
{
	int N = 0;

	scanf("%d", &N);	
	for (int i = 1; i < N + 1; i++) 
	{
		printf("%d\n", i);
	}
	return 0;
}