#include <stdio.h>
#define MAX 10
int main(void)
{
	int age, weight;
	char name[10];

	while (1)
	{
		scanf("%s %d %d", name, &age, &weight);

		if (name[0] == '#')
			break;
		if (age > 17 || weight >= 80)
			printf("%s Senior\n", name);
		else
			printf("%s Junior\n", name);
	}

	return 0;
}