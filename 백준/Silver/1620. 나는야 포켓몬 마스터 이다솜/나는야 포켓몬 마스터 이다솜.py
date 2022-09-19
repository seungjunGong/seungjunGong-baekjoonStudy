import sys
N, M = map(int, sys.stdin.readline().split(' '))

nList = [sys.stdin.readline().rstrip() for _ in range(N)]
nsorted = list()
for i in range(N):
    nsorted.append((nList[i], (i+1)))
nsorted.sort()

for _ in range(M):
    m = sys.stdin.readline().rstrip()
    
    try:
        print(nList[int(m) - 1])
    except:
        start = 0
        end = N - 1 
        while start <= end:
            mid = (start + end) // 2
            if nsorted[mid][0] == m:
                print(nsorted[mid][1])
                break
            elif nsorted[mid][0] > m:
                end = mid - 1
            else:
                start = mid + 1