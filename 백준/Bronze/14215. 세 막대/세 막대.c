#include <stdio.h>

int main(void)
{
	int arr[3];
	scanf("%d %d %d", &arr[0], &arr[1], &arr[2]);

	for (int i = 0; i < 3; i++)
	{
		int tmp;

		for (int j = 0; j < 2; j++)
			if (arr[j] < arr[j + 1])
			{
				tmp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = tmp;
			}
	}

	int a = arr[0], b = arr[1], c = arr[2];

	if (a >= b + c)
		a = b + c - 1;

	printf("%d", a + b + c);

	return 0;
}
