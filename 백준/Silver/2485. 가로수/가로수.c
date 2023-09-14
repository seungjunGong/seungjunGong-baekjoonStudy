#include <stdio.h>
#define MAX_SIZE 100000
#define MIN(a, b) (a < b ? a : b)

int n, arr[MAX_SIZE], dist;

int get_min_number_tree()
{
    int min_dist = 1000000000;
    for (int i = 0; i < n - 1; i++)
    {
        dist = arr[i + 1] - arr[i];
        min_dist = MIN(min_dist, dist);
    }

    int check;
    for (int i = min_dist; i > 0; i--)
    {
        check = 1;
        for (int j = 0; j < n - 1; j++)
            if ((arr[j + 1] - arr[j]) % i != 0)
            {
                check = 0;
                break;
            }

        if (check)
        {
            dist = i;
            break;
        }
    }

    int ans = 0, cnt = 0;
    for (int i = arr[0]; i <= arr[n - 1]; i += dist)
    {
        if (arr[cnt] != i)
            ans++;
        else
            cnt++;
    }
    return ans;
}

int main(void)
{
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
        scanf("%d", &arr[i]);

    printf("%d", get_min_number_tree());
    return 0;
}