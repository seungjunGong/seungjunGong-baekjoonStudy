# 문제 풀이 실패
A = [' '] + list(input())
B = [' '] + list(input())
N, M = len(A), len(B)

dp = [[0] * M for _ in range(N)]
for i in range(1, N):
    for j in range(1, M):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[N-1][M-1])