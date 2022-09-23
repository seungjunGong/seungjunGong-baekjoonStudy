N = int(input())
nList = list(map(int, input().split(' ')))

M = int(input()) 
mList = list(map(int, input().split(' ')))

plusList = [0 for _ in range(10000001)]
minusList = [0 for _ in range(10000001)]

for n in nList:
    if n > 0:
        plusList[n] += 1
    else: minusList[n] += 1

for m in mList:
    if m > 0:
        print(plusList[m], end=' ')
    else: print(minusList[m], end=' ')