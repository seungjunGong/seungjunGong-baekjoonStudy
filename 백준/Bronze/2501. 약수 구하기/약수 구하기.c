#include <stdio.h>

int main(void) {

	int N, K, res = 0;
	scanf("%d %d", &N, &K);

	int i = 1;
	while (K != 0) {
		if (N % i == 0) {
			res = i;
			K--;
		}
		if (N == i) break;
		i++;
	}

	printf("%d", K != 0 ? 0 : res);

	return 0;
}