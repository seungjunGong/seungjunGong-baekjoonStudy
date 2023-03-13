#include <stdio.h>

int main(void){
    int N, M;
    scanf("%d %d", &N, &M);
    int arr[N];

    for (int i = 0; i < N; i++){
        arr[i] = i + 1;
    }

    for (int i = 0; i < M; i++){
        int i, j, tmp;
        scanf("%d %d", &i, &j);
        tmp = arr[i - 1];
        arr[i - 1] = arr[j - 1];
        arr[j - 1] = tmp;
    }

    for (int i = 0; i < N; i++){
        printf("%d ", arr[i]);
    }

    return 0;
}