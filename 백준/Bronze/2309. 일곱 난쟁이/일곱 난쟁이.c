#include <stdio.h>
#define MAX_SIZE 9

int dwarfs[MAX_SIZE], sum, sub[2];

void sort()
{
    int temp;
    for (int i = 0; i < MAX_SIZE - 1; i++)
        for (int j = i + 1; j < MAX_SIZE; j++)
            if (dwarfs[i] > dwarfs[j])
            {
                temp = dwarfs[i];
                dwarfs[i] = dwarfs[j];
                dwarfs[j] = temp;
            }
}

int main(void)
{
    sum = 0;
    for (int i = 0; i < MAX_SIZE; i++)
    {
        scanf("%d", &dwarfs[i]);
        sum += dwarfs[i];
    }

    sort();
    for (int i = 0; i < MAX_SIZE; i++)
        for (int j = i + 1; j < MAX_SIZE; j++)
            if (sum - dwarfs[i] - dwarfs[j] == 100)
            {
                sub[0] = i, sub[1] = j;
                break;
            }

    for (int i = 0; i < MAX_SIZE; i++)
        if (i != sub[0] && i != sub[1])
            printf("%d\n", dwarfs[i]);

    return 0;
}