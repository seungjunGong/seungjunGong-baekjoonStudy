n, m = map(int, input().split())

array = list(map(int, input().split()))

start = 0
end = max(array)

while start <= end:
    mid = (start + end) // 2
    cnt = sum([max(0, i - mid) for i in array])

    if cnt >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)