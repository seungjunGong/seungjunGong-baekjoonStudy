'''
최대 이익이 되는 값 저장
중복 되는 과정 - 하나의 값을 선택했을 때 나머지를 선택하는 경우
1일차를 선택시 최대 값 4일차 부터의 최대값 1일일 경우 무조건 선택
뒤쪽부터 현재 상담 일자의 이윤 + 현재 상담을 마친 일로부터 최대 이윤
dp[i] = 마지막부터 i번째 날까지 최대 값
'''
n = int(input())
array = []
dp = [0] * (n + 1)
max_value = 0

for _ in range(n):
    t, p = map(int, input().split())
    array.append((t, p))

for i in range(n - 1, -1, -1):
    time = array[i][0] + i # 현재까지의 날짜에서 추가로 걸리는 시간
    if time <= n: # 범위 안에서 수행하면
        # 최대값 구함
        dp[i] = max(array[i][1] + dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value
        
print(max_value)