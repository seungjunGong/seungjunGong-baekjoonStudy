import sys
N = int(input())
numbers = [int(sys.stdin.readline()) for _ in range(N)]
numbers.sort()
for num in numbers:
    print(num)