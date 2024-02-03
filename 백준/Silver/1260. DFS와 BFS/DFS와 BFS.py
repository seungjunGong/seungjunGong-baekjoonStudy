N, M, V = map(int, input().split())

graph = [[0]*(N+1) for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    graph[i][j] = 1
    graph[j][i] = 1

def dfs(v):
    print(v, end=" ")
    visited[v] = True

    for i in range(1, N+1):
        if not visited[i] and graph[v][i]:
            dfs(i)

from collections import deque

def bfs(v):
    queue = deque([v])
    visited[v] = True
    print(v, end=" ")
    
    while(queue):
        v = queue.popleft()
        for i in range(1, N+1):
            if not visited[i] and graph[v][i]:
                visited[i] = True
                print(i, end=" ")
                queue.append(i)
                   
dfs(V)
visited = [False for _ in range(N+1)]
print()
bfs(V)