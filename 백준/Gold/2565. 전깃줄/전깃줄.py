N = int(input())

lineList = [tuple(map(int, input().split())) for _ in range(N)]
lineList.sort()

dp = [1 for _ in range(N)]

for i in range(len(lineList)):
    for j in range(i):
        if lineList[i][1] >= lineList[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)
print(N-max(dp))