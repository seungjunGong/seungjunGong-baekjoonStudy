N = int(input())
fileName = [input() for _ in range(N)]
findName = fileName[0]
for n in range(N):
    for i in range(len(findName)):
        if findName[i] != fileName[n][i]:
            findName = findName[:i] + '?' + findName[i+1:]
print(findName)