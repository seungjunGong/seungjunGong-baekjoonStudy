#include <stdio.h>

int n, m;

void bubble_sort(int *arr)
{
    int temp;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n - 1; j++)
        {
            if (arr[j] > arr[j + 1])
            {
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

void printSequence(int *sequence)
{
    for (int i = 0; i < m; i++)
    {
        printf("%d ", sequence[i]);
    }
    printf("\n");
}

void generateSequence(int *sequence, int *arr, int index, int start)
{
    if (index == m)
    {
        printSequence(sequence);
        return;
    }

    for (int i = start; i < n; i++)
    {
        sequence[index] = arr[i];
        generateSequence(sequence, arr, index + 1, i);
    }
}

int main(void)
{
    scanf("%d %d", &n, &m);

    int nArr[n];
    int sequence[m];

    for (int i = 0; i < n; i++)
        scanf("%d", &nArr[i]);
    bubble_sort(nArr);

    generateSequence(sequence, nArr, 0, 0);

    return 0;
}