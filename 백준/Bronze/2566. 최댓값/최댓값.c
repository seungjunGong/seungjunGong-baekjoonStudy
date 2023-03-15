#include <stdio.h>

int main(void) {

	int arr[9][9] = { 0 };
	int num, x = 0, y = 0, max = 0;

	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			scanf("%d", &num);
			if (max < num) {
				max = num;
				x = i;
				y = j;
			}
		}
	}

	printf("%d\n%d %d", max, x + 1, y + 1);
	return 0;
}