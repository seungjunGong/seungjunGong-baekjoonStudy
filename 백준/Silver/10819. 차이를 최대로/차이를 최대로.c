#include <stdio.h>
#include <stdlib.h>
#define MAX(a, b) a > b ? a : b
#define MAX_SIZE 8

int n, max;
int s[MAX_SIZE];

int next_permutation()
{
    int idx = n - 1;
    while (idx > 0 && s[idx - 1] >= s[idx])
        idx--;

    if (idx == 0)
        return 0;

    int idy = n - 1, tmp;
    while (s[idx - 1] >= s[idy])
        idy--;

    tmp = s[idx - 1];
    s[idx - 1] = s[idy];
    s[idy] = tmp;

    idy = n - 1;
    while (idx < idy)
    {
        tmp = s[idx];
        s[idx] = s[idy];
        s[idy] = tmp;
        idx++;
        idy--;
    }

    return 1;
}

int cal()
{
    int sum = 0;
    for (int i = 0; i < n - 1; i++)
        sum += abs((s[i] - s[i + 1]));
    return sum;
}

void sort()
{
    int tmp;
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++)
            if (s[i] > s[j])
            {
                tmp = s[i];
                s[i] = s[j];
                s[j] = tmp;
            }
    return;
}

int main(void)
{
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
        scanf("%d", &s[i]);

    sort();
    while (next_permutation())
        max = MAX(max, cal());

    printf("%d", max);
    return 0;
}