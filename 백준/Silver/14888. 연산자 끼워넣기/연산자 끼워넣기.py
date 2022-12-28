n = int(input())

array = list(map(int, input().split()))
oper = list(map(int, input().split()))

min_value = 1e9
max_value = -1e9

def dfs(i, now):
    global min_value, max_value
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if oper[0] > 0:
            oper[0] -= 1
            # 다음 인덱스, 현재 값 + 다음 값
            dfs(i + 1, now + array[i])
            # 해당 재귀가 끝나면 다시 복구
            oper[0] += 1
        if oper[1] > 0:
            oper[1] -= 1
            dfs(i + 1, now - array[i])
            oper[1] += 1
        if oper[2] > 0:
            oper[2] -= 1
            dfs(i + 1, now * array[i])
            oper[2] += 1
        if oper[3] > 0:
            oper[3] -= 1
            dfs(i + 1, int(now / array[i]))
            oper[3] += 1

dfs(1, array[0])

print(max_value)
print(min_value)