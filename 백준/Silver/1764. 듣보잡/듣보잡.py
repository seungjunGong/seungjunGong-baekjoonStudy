N, M = list(map(int, input().split(' ')))

n_mList = dict()
for _ in range(N):
    n = input()
    n_mList[n] = n_mList.get(n, 0) + 1

for _ in range(M):
    m = input()
    n_mList[m] = n_mList.get(m, 0) + 1

result = list()
for word, i in n_mList.items():
    if i > 1: 
        result.append(word)

print(len(result))
for word in sorted(result):
    print(word)