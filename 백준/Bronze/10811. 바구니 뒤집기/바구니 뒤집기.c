#include <stdio.h>

int main(void) {
    int N = 0, M;
    scanf("%d %d", &N, &M);
    int arr[101];

    for (int i = 1; i < N + 1; i++) {
        arr[i] = i;
    }

    for (int k = 0; k < M; k++) {
        int i, j;
        scanf("%d %d", &i, &j);

        do {
            int tmp = arr[i];
            arr[i] = arr[j];
            arr[j] = tmp;
            i++, j--;
        } while (i < j);
    }

    for (int i = 1; i < N + 1; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}