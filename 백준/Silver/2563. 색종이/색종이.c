#include <stdio.h>

int main(void) {

	int arr[100][100] = {0}, n, a, b, sum = 0;
	
	scanf("%d", &n);
	
	while (n--) {
		scanf("%d %d", &a, &b);

		for (int i = 90 - b; i < 100 - b; i++) {
			for (int j = a; j < a + 10; j++)
				arr[i][j] = 1;
		}
	}

	for (int i = 0; i < 100; i++) {
		for (int j = 0; j < 100; j++) {
			if (arr[i][j] == 1)
				sum += 1;
		}
	}
	
	printf("%d", sum);

	return 0;
}