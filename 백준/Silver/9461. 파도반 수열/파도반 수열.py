dp = [0 for _ in range(101)]
dp[1], dp[2], dp[3], dp[4] = 1, 1, 1, 2

for i in range(5, 101):
    dp[i] = dp[i-2] + dp[i-3]

T = int(input())

for _ in range(T):
    N = int(input())
    print(dp[N])