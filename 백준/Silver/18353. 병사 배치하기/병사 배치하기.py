'''
i 번째까지의 최대가 되는 병사의 수
'''

n = int(input())

array = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if array[i] < array[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))