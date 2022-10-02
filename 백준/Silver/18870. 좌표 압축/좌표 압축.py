import sys
N = int(input())
xList = list(map(int, input().split(' ')))
xSort = sorted(list(set(xList)))

for x in xList:
    start = 0
    end = len(xSort)
    while 1:
        mid = (start + end)//2
        if x == xSort[mid]:
            sys.stdout.write(f"{mid} ")
            break
        if x > xSort[mid]:
            start = mid + 1
        else: end = mid - 1