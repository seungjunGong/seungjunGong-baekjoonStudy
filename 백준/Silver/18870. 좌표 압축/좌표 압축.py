import sys
N = int(sys.stdin.readline())

xList = list(map(int, sys.stdin.readline().split(' ')))
xZipList = sorted(list(set(xList)))

for x in xList:
    start = 0
    end = len(xZipList)

    while start <= end:
        mid = (start + end) // 2        # 이진탐색 사용 

        if xZipList[mid] == x:
            sys.stdout.write(f"{mid} ")
            break
        elif xZipList[mid] < x:
            start = mid + 1
        else:
            end = mid - 1