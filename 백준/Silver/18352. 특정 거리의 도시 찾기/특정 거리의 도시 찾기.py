from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)

distance = [-1] * (n + 1)
distance[x] = 0

que = deque([x])
# 전부 탐색
while que:
    this = que.popleft()
    for next in graph[this]:
        if distance[next] == -1:
            distance[next] = distance[this] + 1
            que.append(next)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True
if not check:
    print(-1)