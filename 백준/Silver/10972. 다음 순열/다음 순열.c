#include <stdio.h>
#define MAX_SIZE 10000

int n, check;
int s[MAX_SIZE];

int next_permutation()
{
    int idx = n - 1;
    while (idx > 0 && s[idx - 1] > s[idx])
        idx--;

    if (idx == 0)
        return 0;

    int idy = n - 1, tmp;
    while (s[idx - 1] > s[idy])
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

int main(void)
{
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
        scanf("%d", &s[i]);

    if (next_permutation(s))
        for (int i = 0; i < n; i++)
            printf("%d ", s[i]);
    else
        printf("-1");

    return 0;
}