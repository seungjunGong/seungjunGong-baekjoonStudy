max_value = 41
dp = [0] * max_value
dp[0] = (1, 0)
dp[1] = (0, 1)

for i in range(2, 41):
    a = (dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1])
    dp[i] = a

for _ in range(int(input())):
    n = int(input())
    print(dp[n][0], dp[n][1])