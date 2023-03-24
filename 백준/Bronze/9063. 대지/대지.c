#include <stdio.h>
#define MAX(a, b) a > b ? a : b
#define MIN(a, b) a < b ? a : b

int main(void){
    int n, x, y, max_x = -10000, min_x = 10000, max_y = -10000, min_y = 10000;
    scanf("%d", &n);
    
    while(n--){
        scanf("%d %d", &x, &y);

        max_x = MAX(max_x, x);
        min_x = MIN(min_x, x);
        max_y = MAX(max_y, y);
        min_y = MIN(min_y, y);
    }

    printf("%d", (max_x - min_x) * (max_y - min_y));

    return 0;
}