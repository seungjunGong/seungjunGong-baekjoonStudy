#include <stdio.h>

int main(void){
    int N, M;
    scanf("%d %d", &N, &M);
    int arr[100] = {0};

    for (int i = 0; i < M; i++){
        int a, b, c;
        scanf("%d %d %d", &a, &b, &c);
        for (a; a <= b; a++){
            arr[a - 1] = c;
        }
    }

    for (int i = 0; i < N; i++){
        printf("%d ", arr[i]);
    }

    return 0;
}