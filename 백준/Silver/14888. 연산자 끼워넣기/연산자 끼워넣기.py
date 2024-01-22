n = int(input())
numbers = list(map(int, input().split()))
opers = list(map(int, input().split()))

max_v = -1000000000
min_v = 1000000000

def calc(v, num, oper):
    if oper == 0:
        v += num
    elif oper == 1:
        v -= num
    elif oper == 2:
        v *= num
    else:
        v = int(v / num)
    return v

def backtrack(idx, v):
    global max_v, min_v
    if idx == len(numbers):
        max_v = max(max_v, v)
        min_v = min(min_v, v)
        return

    for i in range(4):
        if opers[i] > 0:
            opers[i] -= 1
            backtrack(idx+1, calc(v, numbers[idx], i))
            opers[i] += 1

backtrack(1, numbers[0])
print(f"{max_v}\n{min_v}")