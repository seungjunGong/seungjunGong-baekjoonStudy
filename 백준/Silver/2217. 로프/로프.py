import sys

N = int(sys.stdin.readline())
rope = [int(sys.stdin.readline()) for _ in range(N)]
rope.sort()
sum = [(N-i) * rope[i] for i in range(N)]

print(max(sum))