A, B = list(map(int, input().split()))

aList = set(map(int, input().split()))
bList = set(map(int, input().split()))

print(len(aList - bList) + len(bList - aList))