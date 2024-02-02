N, K = map(int, input().split())

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    W, V = map(int, input().split())
    for j in range(1, K+1):
        if j < W:       # 무게가 작은 경우
            dp[i][j] = dp[i-1][j]
        else:           # 물건을 담을지 안 담을지 정해야 함
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-W] + V) 

print(dp[N][K])