chess = map(int, input().split())
perf_chess = [1,1,2,2,2,8]
result = [a-b for a,b in zip(perf_chess, chess)]
for i in result:
    print(i, end=" ") 