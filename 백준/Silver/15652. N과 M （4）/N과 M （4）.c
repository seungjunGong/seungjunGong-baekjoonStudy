#include <stdio.h>

int n, m;

void printSequence(int *sequence)
{
    for (int i = 0; i < m; i++)
    {
        printf("%d ", sequence[i]);
    }
    printf("\n");
}

void generateSequence(int *sequence, int index, int start)
{
    if (index == m)
    {
        printSequence(sequence);
        return;
    }

    for (int i = start; i <= n; i++)
    {
        sequence[index] = i;
        generateSequence(sequence, index + 1, i);
    }
}

int main(void)
{
    scanf("%d %d", &n, &m);

    int sequence[m];

    generateSequence(sequence, 0, 1);

    return 0;
}