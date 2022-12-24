t = int(input())
max_value = 12

dp = [0] * max_value
dp[0] = 1
dp[1] = 2
dp[2] = 4

for i in range(3, 12):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for _ in range(t):
    n = int(input())

    print(dp[n - 1])