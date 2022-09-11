N = int(input())

xy = list()

for _ in range(N):
    xy.append(list(map(int, input().split(' '))))

xy.sort()

for xiyi in xy:
    print(f"{xiyi[0]} {xiyi[1]}")