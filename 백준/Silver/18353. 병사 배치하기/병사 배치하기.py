'''
가장 긴 증가하는 부분 수열(LIS)
배열을 뒤집은 뒤에 LIS 를 구하고 이후 
전체 배열의 길이에서 최대값을 뺀다.
'''
n = int(input())

array = list(map(int, input().split()))
array.reverse()

# 처음 한개만 남길 때 최소 1개가 최대이다.
dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        # 값이 앞에 있는 것이 더 크면 앞에 있는 것에 1더한 값과 비교해 더 큰 값을 저장한다.
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))