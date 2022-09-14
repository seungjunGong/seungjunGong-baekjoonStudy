import sys
N = int(sys.stdin.readline())
xy = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]
xy.sort()
yx = [(y,x) for x, y in xy]

for y, x in sorted(yx):
    print(f"{x} {y}")