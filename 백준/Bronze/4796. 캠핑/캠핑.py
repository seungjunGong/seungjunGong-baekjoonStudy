count = 0
while 1:
    count += 1
    L, P, V = map(int, input().split(' '))
    if L == 0 and P == 0 and V == 0:
        break
    result = V // P * L
    if V % P <= L:
        result += V % P
    else:
        result += L
    print(f"Case {count}: {result}")