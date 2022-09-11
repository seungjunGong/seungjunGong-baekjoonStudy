import sys

N = int(sys.stdin.readline())

numList = [0 for _ in range(10001)]

for _ in range(N):
    num = int(sys.stdin.readline())
    numList[num] += 1

for i in range(1, 10001):
    if numList[i] != 0:
        for _ in range(numList[i]):
            print(i)