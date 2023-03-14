#include <stdio.h>
#include <stdlib.h>

int main(void){

    int n, m;
    scanf("%d %d", &n, &m);
    int arr[101] = {0};

    for (int i = 1; i <= n; i++)
        arr[i] = i;

    for(int t = 0; t < m; t++){
        int i, j, k;
        int tmp[101] = {0};

        scanf("%d %d %d", &i, &j, &k);

        for (int h = i; h <= j; h++)
            tmp[h] = arr[h];

    
        for (int h = i; h <= j; h++){
                
            if (k > j)
                k = i;

            arr[h] = tmp[k++];
        }   
    }

    for (int i = 1; i <= n; i++)
        printf("%d ", arr[i]);
    
}