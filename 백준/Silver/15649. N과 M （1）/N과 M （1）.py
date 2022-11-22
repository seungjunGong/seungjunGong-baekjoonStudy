from itertools import permutations

N, M = map(int, input().split())

nList = [i for i in range(1, N+1)]
result = list(permutations(nList, M))

for line in result:
    for j in line:
        print(j, end=" ")
    print()