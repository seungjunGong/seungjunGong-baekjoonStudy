N, M = map(int, input().split(' '))

nList = [input() for _ in range(N)]
mList = [input() for _ in range(M)]

count = 0
for m in mList:
    if m in nList:
        count += 1
        continue
print(count)