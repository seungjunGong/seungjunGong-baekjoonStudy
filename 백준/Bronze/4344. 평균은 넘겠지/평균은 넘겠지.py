import sys
C = int(sys.stdin.readline())

for _ in range(C):
    nList = list(map(int, sys.stdin.readline().split(' ')))
    del nList[0]
    average = sum(nList) / len(nList)
    result = 0
    for n in nList:
        if n > average:
            result += 100 / len(nList)
    print(f"{result:.3f}%")