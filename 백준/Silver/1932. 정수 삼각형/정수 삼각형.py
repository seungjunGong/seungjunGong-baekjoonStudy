'''
2차원 배열안에 밑에서부터 더 큰값을 저장한다.
중복된 하위 문제 - 두 개 중에 더 큰 값을 선택한다.
최적 부분 구조 - 
'''

n = int(input())
dp = []

for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(n - 1):
    check = False
    for j in range(i+1):
        if not check:
            if j != 0:
                dp[i + 1][j] = max(dp[i][j] + dp[i + 1][j], dp[i][j - 1] + dp[i + 1][j])
                check = True        
            else: 
                dp[i + 1][j] = dp[i][j] + dp[i + 1][j]
        
        if j != i :
            dp[i + 1][j + 1] = max(dp[i][j] + dp[i + 1][j + 1], dp[i][j + 1] + dp[i + 1][j + 1])
            check = True
        else:  
            dp[i + 1][j + 1] = dp[i][j] + dp[i + 1][j + 1]

print(max(dp[n-1]))