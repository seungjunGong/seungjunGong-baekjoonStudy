'''
1 ~ 최대값 사이의 범위에서 원하는 총 예산에 근접 할 때까지 탐색 
'''
n = int(input())
array = list(map(int, input().split()))
m = int(input())

start = 1
end = max(array)

result = 0
while start <= end:
    mid = (start + end) // 2
    cnt = sum([mid if i > mid else i for i in array])

    if cnt > m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)