'''
i - 1 만큼 뺐을 때
1 X 2 1개 배치 
i - 2 만큼 뺏을 때
1 X 2 2개 배치
2 X 1 2개 배치

i = i - 2 + i - 1
위 3가지 경우로 모든 경우 만들 수 있음
'''
n = int(input())
dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 2

for i in range(2, n):
    dp[i] = dp[i - 1] + dp[i -2]
print(dp[n-1] % 10007)