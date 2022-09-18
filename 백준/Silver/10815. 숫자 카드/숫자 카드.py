N = int(input())
cards_N = list(map(int, input().split(' ')))
cards_N.sort()
M = int(input())
cards_M = list(map(int, input().split(' ')))

for card in cards_M:
    start = 0
    end = len(cards_N) - 1
    while 1:
        mid = int((start + end) // 2)
        if start > end:
            print(0, end=' ')
            break
        if cards_N[mid] == card:
            print(1, end=' ')
            break
        elif cards_N[mid] < card:
            start = mid + 1
        else:
            end = mid - 1