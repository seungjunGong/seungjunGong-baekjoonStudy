#include <stdio.h>
#define MAX_SIZE 8

int n, m, check[MAX_SIZE];

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

void generateSequence(int *sequence, int *arr, int index)
{
    if (index == m)
    {
        printSequence(sequence);
        return;
    }

    int tmp = 0;
    for (int i = 0; i < n; i++)
    {
        if (tmp != arr[i])
            if (!check[i])
            {
                check[i] = 1;
                sequence[index] = arr[i];
                tmp = sequence[index];
                generateSequence(sequence, arr, index + 1);
                check[i] = 0;
            }
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

    generateSequence(sequence, nArr, 0);

    return 0;
}