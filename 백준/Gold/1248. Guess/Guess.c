/*
문제
규현이는 종이에 수를 N개 썼다.
(규현이가 아는 가장 큰 수는 10이기 때문에, 수를 10개까지만 쓸 수 있다.)
그 다음에, 가능한 모든 N*(N+1)/2개의 구간의 합을 구했다. 이 것을 해인이는 행렬로 표현했다.

규현이가 쓴 수를 A라고 하면, A[i]는 규현이가 i번째 쓴 수이다. 그리고, S[i][j]는 A[i]부터 A[j]까지
합이 0보다 크면 +, 0이면 0, 0보다 작으면 -이다. 여기서 i는 항상 j보다 작거나 같다.
이렇게 배열을 채우면 배열에는 총 N*(N+1)/2개의 문자가 있다.
(+, -, 0 중 하나) 이 S 배열이 주어졌을 때, 규현이가 쓴 N개의 수 A를 구해서 출력하면 된다.
규현이는 -10부터 10까지의 정수밖에 모르기 때문에,
A도 -10부터 10까지의 정수로만 이루어져 있어야 한다.
입력
첫째 줄에 수열의 크기 N이 주어진다. N은 10보다 작거나 같은 자연수이다.
둘째 줄에는 N(N+1)/2 길이의 문자열이 주어진다. 처음 N개의 문자는 부호 배열의
첫 번째 줄에 해당하고, 다음 N-1개의 문자는 두 번째 줄에 해당한다.
마찬가지로 마지막 문자는 N번째 줄에 해당하는 문자다.
출력
첫째 줄에 수열의 원소 N개를 빈 칸을 사이에 두고 출력한다.
답이 여러 가지 일 경우에는 아무거나 출력하면 된다.
*/
#include <stdio.h>
#include <stdlib.h>
#define MAX_SIZE 10

int n, A[MAX_SIZE];
char S[MAX_SIZE][MAX_SIZE];

int cal(int row)
{
    int sum = 0;
    for (int i = row; i >= 0; i--)
    {
        sum += A[i];
        if (S[i][row] == '+' && sum <= 0)
            return 0;
        if (S[i][row] == '-' && sum >= 0)
            return 0;
        if (S[i][row] == '0' && sum != 0)
            return 0;
    }
    return 1;
}

void dfs(int depth)
{
    if (depth == n)
    {
        for (int i = 0; i < n; i++)
            printf("%d ", A[i]);
        exit(0);
    }

    for (int i = -10; i <= 10; i++)
    {
        A[depth] = i;
        if (cal(depth)) // 해당 라인이 조건을 만족하는지 확인
            dfs(depth + 1);
    }
}

int main(void)
{
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
        for (int j = i; j < n; j++)
            scanf(" %c", &S[i][j]);

    dfs(0);

    return 0;
}