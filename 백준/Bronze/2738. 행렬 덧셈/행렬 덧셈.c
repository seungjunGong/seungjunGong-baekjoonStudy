#include <stdio.h>

int main(void) {

    int n, m, input;
    scanf("%d %d", &n, &m);

    int a[100][100] = { 0 };
    int b[100][100] = { 0 };

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%d", &input);
            a[i][j] = input;
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            scanf("%d", &input);
            b[i][j] = input;
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            printf("%d ", a[i][j] + b[i][j]);
        }
        printf("\n");
    }

    return 0;
}