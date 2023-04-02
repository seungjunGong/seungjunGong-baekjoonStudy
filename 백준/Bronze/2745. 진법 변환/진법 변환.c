#include <stdio.h>
#include <math.h>

int main(void)
{
    char n[100] = {0};
    int b;
    scanf("%s", n);
    scanf("%d", &b);

    char arithmetic[36] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'};

    int i = 0, j = 0;
    for (j; n[j] != 0; j++){
    }

    int res = 0;
    for (--j; j > -1; j--)
        for (int z = 0; z < b; z++)
            if (arithmetic[z] == n[j])
                res += z * pow(b, i++);
    printf("%d", res);
    
    return 0;
}