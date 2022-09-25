xList = dict()
yList = dict()

for _ in range(3):
    a, b = map(int, input().split(' '))
    xList[a] = xList.get(a, 0) + 1
    yList[b] = yList.get(b, 0) + 1

for x, cnt in xList.items():
    if cnt < 2:
        print(x, end=' ')
for y, cnt in yList.items():
     if cnt < 2:
        print(y)