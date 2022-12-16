'''
필요한 랜선의 개수 1이상 백만 이하
'''
k, n = map(int, input().split())
array = [int(input()) for _ in range(k)]

start = 1
end = max(array)
while start <= end:
    mid = (start + end) // 2
    cnt = sum([i // mid for i in array])

    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)