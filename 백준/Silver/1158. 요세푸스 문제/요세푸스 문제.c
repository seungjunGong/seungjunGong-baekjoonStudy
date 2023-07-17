#include <stdio.h>

int main(void)
{
    int N, K;
    scanf("%d %d", &N, &K);

    int queue[N];
    for (int i = 0; i < N; i++)
        queue[i] = i + 1;
    int cnt = N, time = 0;

    printf("<");
    for (int i = 0; cnt != 0; i = (i + 1) % N)
    {
        if (queue[i])
            time++;
        if (time == K)
        {
            printf(cnt == 1 ? "%d>" : "%d, ", queue[i]);
            queue[i] = 0;
            time = 0;
            cnt--;
        }
    }

    return 0;
}