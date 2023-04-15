#include <stdio.h>

void hanoi(int cnt, int start, int mid, int end)
{
    if (cnt == 1)
    {
        printf("%d %d\n", start, end);
        return;
    }
    hanoi(cnt - 1, start, end, mid);
    printf("%d %d\n", start, end);
    hanoi(cnt - 1, mid, start, end);
}

// 참고: https://phaphaya.tistory.com/11
void print_power_of_two(int n)
{
    int i, j, k, num = 2, power = n;
    int next_sum = 0, temp_number, index = 0;
    int data[1000] = {0};
    data[0] = num;
    for (i = 1; i < power; i++)
    {
        temp_number = 0;
        next_sum = 0;
        for (j = index; j >= 0; j--)
        {
            temp_number = data[j] * num + next_sum;
            next_sum = 0;

            if (temp_number > 9)
            {
                data[j] = temp_number % 10;
                if (j == 0)
                {
                    for (k = index; k >= 0; k--)
                    {
                        data[k + 1] = data[k];
                    }
                    data[0] = temp_number / 10;
                    index++;
                }
                else
                {
                    next_sum = temp_number / 10;
                }
            }
            else
            {
                data[j] = temp_number;
            }
        }
    }

    data[index] -= 1;
    for (i = 0; i <= index; i++)
        printf("%d", data[i]);
    printf("\n");
}

int main(void)
{
    int n;
    scanf("%d", &n);

    print_power_of_two(n);
    if (n <= 20)
        hanoi(n, 1, 2, 3);
    return 0;
}