#include <stdio.h>
#define MAX_SIZE 15

int L, C, s[MAX_SIZE];
char arr[MAX_SIZE];

void check_print()
{
    int con = 0, vow = 0;
    char c;
    for (int i = 0; i < L; i++)
    {
        c = arr[s[i]];
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
            con++;
        else
            vow++;
    }

    if (con && vow > 1)
    {
        for (int i = 0; i < L; i++)
            printf("%c", arr[s[i]]);
        printf("\n");
    }
}

void sol(int cnt)
{
    if (cnt == L)
    {
        check_print();
        return;
    }

    if (cnt == 0)
    {
        for (int i = 0; i < C; i++)
        {
            s[cnt] = i;
            sol(cnt + 1);
        }
    }
    else
    {
        for (int i = s[cnt - 1] + 1; i < C; i++)
        {
            s[cnt] = i;
            sol(cnt + 1);
        }
    }
}

void sort()
{
    for (int i = 0; i < C; i++)
        for (int j = i + 1; j < C; j++)
            if (arr[i] > arr[j])
            {
                char tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
            }
}

int main(void)
{
    scanf("%d %d", &L, &C);

    for (int i = 0; i < C; i++)
        scanf(" %c", &arr[i]);

    sort();
    sol(0);

    return 0;
}