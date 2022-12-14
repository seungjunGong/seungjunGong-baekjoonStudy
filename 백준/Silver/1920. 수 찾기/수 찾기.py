n = int(input())
nList = list(set(map(int, input().split())))
nList.sort()

m = int(input())
mList = list(map(int, input().split()))

def bineary_search(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == i:
            return 1
        elif array[mid] < i:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for i in mList:
    start = 0
    end = len(nList) - 1
    
    print(bineary_search(nList, start, end))